from __future__ import annotations

import hashlib
import json
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def main() -> int:
    skill = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
    assert skill.startswith("---\nname: content-led-interactive-web\n")
    assert "references/visual-assets.md" in skill
    assert "references/technology-audition.md" in skill
    assert "references/visual-range-contract.md" in skill
    assert "references/public-web-copy.md" in skill
    assert "Universal Direction, Not A House Style" in skill
    assert "not a preset aesthetic" in skill
    assert "cannot establish the next task's style" in skill
    assert "examples/slow-reading-lab/design-dossier.md" not in skill

    for reference in (
        "decision-frontier.md",
        "design-dossier.md",
        "evaluation-cases.md",
        "interaction-and-brand.md",
        "review-rubric.md",
        "technology-audition.md",
        "visual-assets.md",
        "visual-range-contract.md",
        "public-web-copy.md",
    ):
        assert (SKILL_DIR / "references" / reference).is_file(), reference

    technology_audition = (SKILL_DIR / "references" / "technology-audition.md").read_text(encoding="utf-8")
    assert "Technology Audition For A Distinctive Experience" in skill
    assert "three genuinely different **visual-engine combinations**" in skill
    assert "Current-Fact Rule" in technology_audition
    assert "Compose, Do Not Stack" in technology_audition
    assert "Rejection Ledger" in technology_audition

    visual_range = (SKILL_DIR / "references" / "visual-range-contract.md").read_text(encoding="utf-8")
    public_copy = (SKILL_DIR / "references" / "public-web-copy.md").read_text(encoding="utf-8")
    assert "Visual Range Contract" in skill
    assert "Stable Anchors" in visual_range
    assert "Intentional Rupture" in visual_range
    assert "Write Public Copy That Carries Its Own Weight" in skill
    assert "Substitution Test" in public_copy
    assert "Contrast-Proof Test" in public_copy
    review_rubric = (SKILL_DIR / "references" / "review-rubric.md").read_text(encoding="utf-8")
    evaluation_cases = (SKILL_DIR / "references" / "evaluation-cases.md").read_text(encoding="utf-8")
    assert "Close The Visual Acceptance Loop" in skill
    assert "two focused correction cycles" in skill
    assert "Acceptance Remediation Loop" in review_rubric
    assert "visual acceptance unverified" in review_rubric
    assert "Visual Defect Cannot Ship As Ready" in evaluation_cases
    design_dossier = (SKILL_DIR / "references" / "design-dossier.md").read_text(encoding="utf-8")
    assert "Set A Visual Acceptance Matrix" in skill
    assert "uniformly scaling it down" in skill
    assert "Visual Acceptance Matrix" in design_dossier
    assert "Narrow-view recomposition" in design_dossier
    assert "Visual Collision And Proportion" in review_rubric
    assert "widest required view" in review_rubric
    assert "Diagram Collision Across Viewports" in evaluation_cases
    design_dossier = (SKILL_DIR / "references" / "design-dossier.md").read_text(encoding="utf-8")
    visual_assets = (SKILL_DIR / "references" / "visual-assets.md").read_text(encoding="utf-8")
    assert "Section Asset Coverage Map" in skill
    assert "not a numeric quota or a cap on creative range" in skill
    assert "Asset coverage map" in design_dossier
    assert "Hero-Only Raster Is Not A Default" in visual_assets
    assert "Hero-Only Raster Assumption" in evaluation_cases

    example_root = SKILL_DIR / "examples" / "slow-reading-lab"
    assert (example_root / "index.html").is_file()
    assert (example_root / "design-dossier.md").is_file()
    manifest = json.loads((example_root / "assets" / "asset-manifest.json").read_text(encoding="utf-8"))
    assert len(manifest["assets"]) == 3
    for asset in manifest["assets"]:
        path = example_root / asset["file"]
        assert path.is_file(), asset["file"]
        assert sha256(path) == asset["sha256"], asset["file"]

    print("content-led-interactive-web package: passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())



