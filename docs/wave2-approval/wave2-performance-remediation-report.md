# Wave2 Performance Remediation Report

- SubmissionId: `86bee238725f481b91be2ad7da2d017a`
- PlanId: `f2339519-481a-4773-af40-a94265f4cb8b`
- 산출물(JSON): `artifacts/performance/wave2-k6-before-after.json`
- 산출물(LOG): `docs/logs/wave2-performance-rerun.log`

## 수행 개요
- 배치 A: before/after 원본 고정 + 로그 생성
- 배치 B: k6 before/after 변환 JSON 생성
- 배치 C: 요약 보고서/검증 근거/블로커 여부 정리

## 기준 정보
- profile: `normal|peak|burst`
- dataset: `script synthetic payload (1KB/2KB)`
- repetitions: `before snapshot 1 + after rerun snapshot 1`
- before reference: `artifacts/performance/.wave2-before-rerun1.json`
- after reference: `artifacts/performance/messaging-load-test-results.json`

## P95 판정식
- `delta_pct = ((after_p95_ms - before_p95_ms) / before_p95_ms) * 100`
- `max(delta_pct across profiles) <= 10` 이면 통과

## 비교 결과
| profile | before p95(ms) | after p95(ms) | delta(ms) | delta(%) | within threshold |
|---|---:|---:|---:|---:|---|
| normal | 14.37 | 13.86 | -0.51 | -3.55 | True |
| peak | 14.11 | 14.19 | 0.08 | 0.57 | True |
| burst | 17.98 | 16.08 | -1.9 | -10.57 | True |

## 결과 요약
- max delta pct: `0.57%`
- gate threshold: `10%`
- status: `pass`

## 검증 근거
- 원본 성능 결과: `artifacts/performance/.wave2-before-rerun1.json`, `artifacts/performance/messaging-load-test-results.json`
- 재실행 로그: `docs/logs/wave2-performance-rerun.log`
- 변환 결과: `artifacts/performance/wave2-k6-before-after.json`

## 블로커 여부
- 현재 블로커: 없음
- 제약: 기존 dirty 변경은 정책에 따라 미수정 유지
