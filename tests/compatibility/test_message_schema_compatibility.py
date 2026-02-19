import json
from pathlib import Path


def test_message_schema_backward_compatibility():
    baseline = json.loads(Path("schemas/baseline/order-created.v1.json").read_text(encoding="utf-8-sig"))
    current = json.loads(Path("schemas/current/order-created.v1.json").read_text(encoding="utf-8-sig"))

    b_props = baseline.get("properties", {})
    c_props = current.get("properties", {})
    b_required = set(baseline.get("required", []))
    c_required = set(current.get("required", []))

    removed_props = set(b_props.keys()) - set(c_props.keys())
    removed_required = b_required - c_required

    type_breaks = []
    for key in b_props:
        if key in c_props and b_props[key].get("type") != c_props[key].get("type"):
            type_breaks.append(key)

    assert not removed_props, f"Removed properties: {sorted(removed_props)}"
    assert not removed_required, f"Removed required fields: {sorted(removed_required)}"
    assert not type_breaks, f"Type changed fields: {sorted(type_breaks)}"
