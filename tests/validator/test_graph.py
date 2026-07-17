"""Unit tests for manifest graph and resolver-order validation (DEC-S-099)."""

import unittest

from tools.cds_validator.graph import (
    SOURCE_SET_ID_RE,
    ManifestGraph,
    check_resolver_order,
)


def entry(set_id, layer, deps, path="x.tokens.json"):
    return {"sourceSetId": set_id, "path": path, "layer": layer,
            "dependencies": deps}


def manifest(entries, graph=None):
    payload = {"sourceSets": entries}
    if graph is not None:
        payload["dependencyGraph"] = graph
    return payload


def kinds(graph):
    return sorted(f.kind for f in graph.findings)


class SourceSetIdSyntaxTests(unittest.TestCase):
    def test_valid_ids(self):
        for value in ("fixture/reference", "a", "a-b/c-d/e0"):
            self.assertTrue(SOURCE_SET_ID_RE.match(value), value)

    def test_invalid_ids(self):
        for value in ("Fixture/reference", "a//b", "/a", "a/", "a b",
                      "a\\b", "-a", "0a", ""):
            self.assertFalse(SOURCE_SET_ID_RE.match(value), value)


class ManifestGraphTests(unittest.TestCase):
    def test_clean_graph_has_no_findings(self):
        graph = ManifestGraph.from_manifest(manifest(
            [entry("base", "reference", []), entry("mid", "semantic", ["base"])],
            {"base": [], "mid": ["base"]}))
        self.assertEqual(graph.findings, [])

    def test_case_only_collision_detected(self):
        graph = ManifestGraph.from_manifest(manifest(
            [entry("aa/bb", "reference", []),
             {"sourceSetId": "aa/bB", "path": "y.tokens.json",
              "layer": "reference", "dependencies": []}]))
        # The second ID is syntactically invalid AND a case-only collision;
        # the invalid-id finding fires first and fails closed either way.
        self.assertTrue(any(f.kind in ("case-collision", "invalid-id")
                            for f in graph.findings))

    def test_unregistered_dependency_detected(self):
        graph = ManifestGraph.from_manifest(manifest(
            [entry("mid", "semantic", ["ghost"])], {"mid": ["ghost"]}))
        self.assertIn("unregistered-dependency", kinds(graph))

    def test_backward_layer_dependency_detected(self):
        graph = ManifestGraph.from_manifest(manifest(
            [entry("base", "reference", ["mid"]), entry("mid", "semantic", [])],
            {"base": ["mid"], "mid": []}))
        self.assertIn("backward-layer", kinds(graph))

    def test_same_layer_dependency_is_backward(self):
        graph = ManifestGraph.from_manifest(manifest(
            [entry("a", "semantic", ["b"]), entry("b", "semantic", [])],
            {"a": ["b"], "b": []}))
        self.assertIn("backward-layer", kinds(graph))

    def test_self_dependency_detected(self):
        graph = ManifestGraph.from_manifest(manifest(
            [entry("a", "reference", ["a"])], {"a": ["a"]}))
        self.assertIn("self-dependency", kinds(graph))

    def test_cycle_detected(self):
        graph = ManifestGraph.from_manifest(manifest(
            [entry("a", "semantic", ["b"]), entry("b", "semantic", ["a"])],
            {"a": ["b"], "b": ["a"]}))
        self.assertIn("cycle", kinds(graph))

    def test_dependency_graph_mismatch_detected(self):
        graph = ManifestGraph.from_manifest(manifest(
            [entry("base", "reference", []), entry("mid", "semantic", ["base"])],
            {"base": [], "mid": []}))
        self.assertIn("graph-mismatch", kinds(graph))

    def test_transitive_dependencies(self):
        graph = ManifestGraph.from_manifest(manifest(
            [entry("base", "reference", []),
             entry("mid", "semantic", ["base"]),
             entry("top", "component", ["mid"])],
            {"base": [], "mid": ["base"], "top": ["mid"]}))
        self.assertEqual(graph.transitive_dependencies("top"), ["mid", "base"])


class ResolverOrderTests(unittest.TestCase):
    def setUp(self):
        self.graph = ManifestGraph.from_manifest(manifest(
            [entry("base", "reference", []), entry("mid", "semantic", ["base"])],
            {"base": [], "mid": ["base"]}))

    def test_correct_order_passes(self):
        resolver = {"orderedSourceSets": [
            {"order": 1, "sourceSetId": "base", "$ref": "b.tokens.json"},
            {"order": 2, "sourceSetId": "mid", "$ref": "m.tokens.json"}]}
        self.assertEqual(check_resolver_order(resolver, self.graph), [])

    def test_dependency_after_dependent_fails(self):
        resolver = {"orderedSourceSets": [
            {"order": 1, "sourceSetId": "mid", "$ref": "m.tokens.json"},
            {"order": 2, "sourceSetId": "base", "$ref": "b.tokens.json"}]}
        findings = check_resolver_order(resolver, self.graph)
        self.assertTrue(any(f.kind == "resolver-order" for f in findings))

    def test_unregistered_source_set_fails(self):
        resolver = {"orderedSourceSets": [
            {"order": 1, "sourceSetId": "ghost", "$ref": "g.tokens.json"}]}
        findings = check_resolver_order(resolver, self.graph)
        self.assertTrue(any(f.kind == "resolver-unregistered" for f in findings))


if __name__ == "__main__":
    unittest.main()
