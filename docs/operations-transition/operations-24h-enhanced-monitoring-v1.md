# 24시간 강화 모니터링 기준 v1

- SubmissionId: `6b70ea428f9248d28b92d97b77527ead`
- PlanId: `fdec7f53-2374-4857-806e-5408fe2548f0`
- 모니터링 윈도우: 전환 시점 기준 24시간

## 1) SLI/지표 및 임계치

| 영역 | 지표 | 경고(Warning) | 치명(Critical) | 데이터 소스 |
|---|---|---|---|---|
| 성능 | Throughput(msg/s) | < 2700 5분 지속 | < 2500 5분 지속 | `artifacts/performance/messaging-load-test-results.json` |
| 성능 | p95 지연(ms) | > 70 | > 80 | `artifacts/performance/perf-gate-report.json` |
| 성능 | p99 지연(ms) | > 120 | > 140 | `artifacts/performance/perf-gate-report.json` |
| 오류율 | Error rate(%) | > 0.5 | > 1.0 | `artifacts/performance/perf-gate-report.json` |
| DLQ | DLQ depth | > 5 | > 10 | `artifacts/observability/wave2-alert-events-2026-02-19.json` |
| 관측성 | retryCount 누락률(%) | > 0 | > 0 | `artifacts/observability/wave2-retrycount-validation-2026-02-19.json` |
| 스키마 | schema drift 건수 | > 0 | > 0 | contract/compat 테스트 결과 |

## 2) 운영 절차(24시간)
1. 5분 주기 상태 점검(자동)
2. 30분 주기 수동 점검(운영 담당)
3. Critical 발생 시 즉시 배포 동결 + 복구 절차 진입
4. 24시간 종료 시 누적 이벤트/복구 시간 리포트 작성

## 3) 복구 절차
1. Critical 트리거 확인 후 최근 성공 릴리스 태그 기준 롤백
2. `rehearsal_mode=recover` 시나리오로 복구 경로 재검증
3. 복구 후 15분 안정화 모니터링(지표 모두 Warning 이하 확인)
4. 원인/재발방지 항목을 Coordination 채널에 보고

## 4) 증적 경로
- 통합 인덱스: `docs/operations-transition/operations-transition-evidence-index-v1.md`
- recover 증빙: `artifacts/runner/api-self-runner-recover-evidence-2026-02-20.json`
- fallback 증빙: `artifacts/runner/api-self-runner-fallback-rehearsal-2026-02-19.json`
- 운영 로그: `docs/logs/api-self-runner-deploy-rollback-rehearsal.log`
