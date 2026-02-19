import argparse
import json
import os
import re
import sys
from pathlib import Path


def check_release_tag(tag: str) -> tuple[bool, str]:
    if not tag:
        return False, "release tag is empty"
    if not re.match(r"^v\d+\.\d+\.\d+$", tag):
        return False, f"invalid tag format: {tag}"
    return True, "ok"


def check_release_note(path: str) -> tuple[bool, str]:
    p = Path(path)
    if not p.exists():
        return False, f"release note missing: {path}"
    text = p.read_text(encoding="utf-8")
    required = ["변경 요약", "브레이킹 여부", "롤백"]
    missing = [k for k in required if k not in text]
    if missing:
        return False, f"release note fields missing: {missing}"
    return True, "ok"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--quality-profile", default="pass", choices=["pass", "fail"])
    parser.add_argument("--release-tag", default=os.getenv("RELEASE_TAG", "v1.0.0"))
    parser.add_argument("--release-note", default="docs/release-note-draft.md")
    args = parser.parse_args()

    results = []
    ok, msg = check_release_tag(args.release_tag)
    results.append({"check": "tag", "ok": ok, "message": msg})

    ok2, msg2 = check_release_note(args.release_note)
    results.append({"check": "release_note", "ok": ok2, "message": msg2})

    if args.quality_profile == "fail":
        results.append({"check": "quality_profile", "ok": False, "message": "forced fail for block rehearsal"})

    os.makedirs("artifacts", exist_ok=True)
    Path("artifacts/release-governance-check.json").write_text(
        json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    failed = [r for r in results if not r["ok"]]
    if failed:
        print(json.dumps({"status": "blocked", "failed": failed}, ensure_ascii=False, indent=2))
        sys.exit(1)

    print(json.dumps({"status": "passed", "checks": results}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
