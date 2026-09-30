# Branding — Core Design System repository identity

This directory archives the **Core Grid** design of the Core Design System (CDS):
the mark, logo, README banner and GitHub social preview. This design was prepared as
a candidate public repository identity but was superseded before integration; it was
never the integrated public identity. The active identity is Negative Core (see
`../../README.md`).

> [!IMPORTANT]
> **Repository identity artwork is non-normative with respect to CDS Core visual
> token values.** The colours, shapes, dimensions and type used here are project
> artwork for the repository presentation. They are **not** CDS design tokens, not
> normative visual values, not Source Set content, not a Brand and Identity (Layer 2)
> decision, and not a conformance reference. `BRAND ART COLOUR ≠ CDS CORE TOKEN`.

## Concept — Core Grid

The mark is a three-by-three grid built around one solid **core**:

- the **core** sits in the centre and holds a smaller inner square, separated by a
  thin ring — the layered foundation at the centre of the system;
- four **modules** attach directly to the core through short connectors — reusable
  building blocks and the relationships between them;
- the four **corner** squares are outlines only — the grid continues, and the
  system composes outward.

The banner and social preview extend the same grid to a five-by-five field whose
squares fade from connected modules to faint outlines with distance from the core,
expressing modular composition from foundations outward.

Colour direction: a dark neutral ground, indigo/violet as the primary identity, a
restrained cyan accent for connections, and light neutral type.

## Assets

| Asset | SVG source | PNG derivative | Canvas (px) | Purpose |
| --- | --- | --- | --- | --- |
| Mark | [`cds-mark.svg`](assets/svg/cds-mark.svg) | [`cds-mark.png`](assets/png/cds-mark.png) | 512 × 512 | Square mark; icons, avatars, small sizes |
| Logo | [`cds-logo.svg`](assets/svg/cds-logo.svg) | [`cds-logo.png`](assets/png/cds-logo.png) | 1200 × 320 | Horizontal lock-up with name and tagline |
| Banner | [`cds-banner.svg`](assets/svg/cds-banner.svg) | [`cds-banner.png`](assets/png/cds-banner.png) | 1600 × 500 | Root README hero |
| Social preview | [`cds-social-preview.svg`](assets/svg/cds-social-preview.svg) | [`cds-social-preview.png`](assets/png/cds-social-preview.png) | 1280 × 640 | GitHub repository social preview |

The mark and logo PNGs carry transparent rounded corners; the banner and social
preview PNGs are opaque.

## Sources and derivatives

- **SVG is the design source.** Every file is standalone SVG with `<title>`,
  `<desc>` and `role="img"`, and contains no script, `foreignObject`, raster image,
  embedded font, or remote reference.
- **PNG files are derivatives.** Each PNG is rendered 1:1 from its SVG at the canvas
  size above. Change the SVG and re-render — never edit a PNG by hand.
- **No font is bundled.** Text uses a system font stack
  (`Segoe UI`, `Helvetica Neue`, Helvetica, Arial, `Liberation Sans`, sans-serif);
  the PNGs were rendered with Segoe UI, so SVG text may render with slightly
  different metrics on systems without it.

## Usage

- Use the mark and logo only to refer to the CDS repository and project.
- Keep the artwork unaltered; do not recolour, crop or rearrange it.
- Do not use the artwork, or colours sampled from it, as design tokens, as values
  for a consumer product, or as evidence of CDS maturity, adoption or conformance.

## What this artwork does not do

It creates no Brand Foundation, satisfies no CDS branding work package, defines no
consumer brand behaviour, selects no visual token value, creates no evidence, and
changes no maturity. Logo architecture for the Core ecosystem remains an open,
separately governed question.
