# Wave2 Performance Remediation Report

- SubmissionId: 86bee238725f481b91be2ad7da2d017a
- PlanId: f2339519-481a-4773-af40-a94265f4cb8b
- 측정 방식: tools/perf/messaging_load_test.py 2회 재실행 후 before/after 비교 스키마 변환
- 로그: docs/logs/wave2-performance-rerun.log
- 결과 JSON: artifacts/performance/wave2-k6-before-after.json

## 실행 명령
1. python tools/perf/messaging_load_test.py (rerun#1, before)
2. python tools/perf/messaging_load_test.py (rerun#2, after)

## 가정값
- profile: normal, peak, burst
- dataset: 스크립트 내 synthetic payload(1KB/2KB)
- 반복 횟수: 2회(동일 조건)

## P95 전/후 비교
| profile | before p95(ms) | after p95(ms) | delta(ms) | delta(%) | 기준(+10%) 충족 |
|---|---:|---:|---:|---:|---|
| normal | 14.37 | 13.86 | -0.51 | -3.55 | True |
| peak | 14.11 | 14.19 | 0.08 | 0.57 | True |
| burst | 17.98 | 16.08 | -1.90 | -10.57 | True |

## 판정
- 최대 P95 변화율: 0.57% (peak)
- 게이트 기준: +10% 이내
- 최종 상태: pass

## 참고
- 본 판정은 동일 조건 재실행 2회(before/after) 비교값 기준
- 메시지 계약 필드/버전 의미 변경 없음(성능 측정 단계에서 계약 변경 미수행)
