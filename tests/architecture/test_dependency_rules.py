import ast
from pathlib import Path

import yaml


def infer_layer(path: Path):
    parts = [p.lower() for p in path.parts]
    for layer in ["domain", "application", "infrastructure"]:
        if layer in parts:
            return layer
    return None


def test_no_reverse_dependency():
    rules = yaml.safe_load(Path("config/architecture-rules.yml").read_text(encoding="utf-8"))
    allowed = rules["layers"]
    violations = []

    py_files = list(Path("src").rglob("*.py")) if Path("src").exists() else []
    for file in py_files:
        layer = infer_layer(file)
        if not layer:
            continue
        tree = ast.parse(file.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            mod = None
            if isinstance(node, ast.Import):
                for n in node.names:
                    mod = n.name
            elif isinstance(node, ast.ImportFrom) and node.module:
                mod = node.module
            if not mod:
                continue
            target = None
            for candidate in ["domain", "application", "infrastructure"]:
                if candidate in mod.lower().split("."):
                    target = candidate
                    break
            if target and target != layer and target not in allowed[layer]:
                violations.append(f"{file}: {layer} -> {target}")

    assert not violations, "Reverse dependency violations:\n" + "\n".join(violations)
