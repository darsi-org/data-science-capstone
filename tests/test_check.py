"""The check script itself: it loads, runs on this folder and writes a file Darsi can read."""
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


def test_check_writes_darsi_check_json():
    subprocess.run([sys.executable, str(ROOT / "check.py")], check=True, cwd=ROOT, capture_output=True)
    out = json.loads((ROOT / "darsi-check.json").read_text(encoding="utf-8"))
    assert out["darsi"] == 1
    assert set(out["milestones"]) == {"m1", "m2", "m3", "m4", "m5"}
    for m in out["milestones"].values():
        assert all({"id", "ok", "en", "ar"} <= set(c) for c in m["checks"])


def test_m3_needs_the_paired_difference_interval(tmp_path):
    """Two separate intervals can overlap even when one model is reliably better, so m3 asks for diff_ci95 too."""
    (tmp_path / "check.py").write_bytes((ROOT / "check.py").read_bytes())
    (tmp_path / "results").mkdir()
    test_json = tmp_path / "results" / "test.json"

    def m3_ok(result):
        test_json.write_text(json.dumps(result), encoding="utf-8")
        subprocess.run([sys.executable, "check.py", "--milestone", "m3"], check=True, cwd=tmp_path, capture_output=True)
        return json.loads((tmp_path / "darsi-check.json").read_text(encoding="utf-8"))["milestones"]["m3"]["ok"]

    both = {"ci95": [1.9, 2.5], "baseline_ci95": [2.1, 2.8]}
    assert not m3_ok(both)
    assert m3_ok({**both, "diff_ci95": [0.1, 0.5]})


def test_workflows_are_valid_yaml():
    """A workflow with a YAML mistake never runs, and Darsi then reads a failed Actions run. Catch it before you push."""
    yaml = pytest.importorskip("yaml")
    for f in sorted((ROOT / ".github" / "workflows").glob("*.yml")):
        doc = yaml.safe_load(f.read_text(encoding="utf-8"))
        assert isinstance(doc, dict) and doc.get("jobs"), f"{f.name} has no jobs"
