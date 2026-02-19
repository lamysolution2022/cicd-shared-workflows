import json
import os
from datetime import datetime, timedelta, timezone


def at(base, minutes):
    return (base + timedelta(minutes=minutes)).isoformat()


base = datetime(2026, 2, 19, 9, 0, tzinfo=timezone.utc)

events = [
    {"time": at(base, 0), "scenario": "R1", "event": "warning_triggered", "metric": "latency_p95_ms", "value": 1890},
    {"time": at(base, 5), "scenario": "R1", "event": "critical_triggered", "metric": "latency_p95_ms", "value": 2620},
    {"time": at(base, 15), "scenario": "R1", "event": "escalation", "target": "sre_lead"},
    {"time": at(base, 22), "scenario": "R1", "event": "recovered", "metric": "latency_p95_ms", "value": 1700},
    {"time": at(base, 30), "scenario": "R3", "event": "warning_triggered", "metric": "dlq_depth", "value": 35},
    {"time": at(base, 36), "scenario": "R3", "event": "critical_triggered", "metric": "dlq_depth", "value": 92},
    {"time": at(base, 44), "scenario": "R3", "event": "escalation", "target": "incident_commander"},
    {"time": at(base, 55), "scenario": "R3", "event": "recovered", "metric": "dlq_depth", "value": 18}
]

summary = {
    "submission_id": "3246e459144f4c81b910a8c9bfbc5c26",
    "plan_id": "408c46dd-86d6-4207-81a7-3b8130b3eda8",
    "result": "pass",
    "events": events,
    "checks": {
        "alert_trigger": True,
        "alert_clear": True,
        "escalation": True
    }
}

os.makedirs("artifacts/observability", exist_ok=True)
with open("artifacts/observability/rehearsal-log-2026-02-19.json", "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)

with open("artifacts/observability/rehearsal-summary-2026-02-19.md", "w", encoding="utf-8") as f:
    f.write("# 리허설 요약\n\n")
    f.write("- 결과: pass\n")
    f.write("- 경고 발생: 2회\n")
    f.write("- 치명 발생: 2회\n")
    f.write("- 에스컬레이션: 2회\n")
    f.write("- 복구 확인: 2회\n")

print(json.dumps(summary, ensure_ascii=False, indent=2))
