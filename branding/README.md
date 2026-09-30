# Core Design System — identity kit

**Selected direction: Negative Core.**

![Core Design System](assets/png/cds-banner.png)

The Human Maintainer selected the creative direction and accepted the displayed
visual implementation in conversation on 2026-09-30 ("ok, weiter"). A subsequent
corrective pass removed the organizational endorsement lettering from the logo,
banner and social preview, and set the social-preview claim on one line; the mark
geometry is unchanged. The corrected kit is integrated in the repository by the
Human-Maintainer commit `ccc7b2d421b13e35efe1fd311b03082cf024f9b0`. That integration
implies no release or tag; publication remains `Private Development`. This document
records no independent-review outcome for the corrected kit.

[Brand Guide](BRAND_GUIDE.md) · [Font provenance](FONT_PROVENANCE.md)

| Asset | SVG source | PNG export | Dimensions |
| --- | --- | --- | --- |
| Mark | [SVG](assets/svg/cds-mark.svg) | [PNG](assets/png/cds-mark.png) | 512 × 512 |
| Logo | [SVG](assets/svg/cds-logo.svg) | [PNG](assets/png/cds-logo.png) | 1200 × 320 |
| README banner | [SVG](assets/svg/cds-banner.svg) | [PNG](assets/png/cds-banner.png) | 1600 × 500 |
| Social preview | [SVG](assets/svg/cds-social-preview.svg) | [PNG](assets/png/cds-social-preview.png) | 1280 × 640 |
| Light monochrome mark | [SVG](assets/svg/cds-mark-mono-white.svg) | [PNG](assets/png/cds-mark-mono-white.png) | 512 × 512 |
| Dark monochrome mark | [SVG](assets/svg/cds-mark-mono-black.svg) | [PNG](assets/png/cds-mark-mono-black.png) | 512 × 512 |

SVG is the primary source. Lettering is outlined for portable rendering; the
accessible SVG title/description preserves its meaning. No fonts are embedded.
PNG derivatives are rendered directly from these SVGs at native dimensions.
Marks are transparent; logo, banner and social preview have an opaque dark ground.

The previous Core Grid draft is a superseded design iteration that was never
integrated. It is retained in the repository under `branding/archive/core-grid/`
for traceability and is not part of the portable kit.

## Portable kit

`CDS-Branding-Kit-Negative-Core.zip` is a derived artifact, never a source. It
holds byte-identical copies of this README, the Brand Guide, the font provenance
record, the two licence notices and the twelve SVG/PNG assets, plus a
`SHA256SUMS.txt` covering every other file in it. It excludes the Core Grid archive
and review records. Regenerate it after any change to those files; never edit it by
hand. From the repository root, with Python 3:

```python
import hashlib, zipfile
from pathlib import Path
root, name = Path("branding"), "CDS-Branding-Kit-Negative-Core"
files = ["README.md", "BRAND_GUIDE.md", "FONT_PROVENANCE.md"] + [
    f"assets/{kind}/cds-{a}.{kind}" for kind in ("png", "svg")
    for a in ("banner", "logo", "mark-mono-black", "mark-mono-white", "mark",
              "social-preview")] + [
    "licenses/Inter-OFL.txt", "licenses/SpaceGrotesk-OFL.txt"]
sums = "".join(f"{hashlib.sha256((root / f).read_bytes()).hexdigest()}  {f}\n"
               for f in files)
with zipfile.ZipFile(root / f"{name}.zip", "w", zipfile.ZIP_DEFLATED) as z:
    for f, data in [(f, (root / f).read_bytes()) for f in files] + [
            ("SHA256SUMS.txt", sums.encode())]:
        info = zipfile.ZipInfo(f"{name}/{f}", (2026, 9, 30, 0, 0, 0))
        info.compress_type, info.external_attr = zipfile.ZIP_DEFLATED, 0o644 << 16
        z.writestr(info, data)
```

The kit uses deterministic file content and fixed archive metadata.
`SHA256SUMS.txt` verifies the packaged file contents. Byte-identical ZIP rebuilds
have been verified with Windows, Python 3.13.15 and zlib 1.3.1; byte-identical
output across platforms or compression-library versions is not guaranteed.

Repository identity artwork is non-normative with respect to CDS Core visual token
values. This kit creates no Visual Source Set, Product Profile, evidence admission,
maturity promotion, release, licensing decision or work-package authorization. It
establishes no endorsement, parent-brand or product-family relationship.
