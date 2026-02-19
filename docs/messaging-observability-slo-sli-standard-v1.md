# 메시징 SLO/SLI 표준 v1

- SubmissionId: `3246e459144f4c81b910a8c9bfbc5c26`
- PlanId: `408c46dd-86d6-4207-81a7-3b8130b3eda8`
- 작성일: 2026-02-19
- 작성자: Platform Engineer (CI/CD Owner)

## 1) SLI 정의식
### SLI-01 지연시간(Latency)
- 정의: 메시지 생성 시각부터 소비 완료 시각까지 경과시간
- 수식: `p95(consume_completed_at - produced_at)`
- 집계 단위: 5분, 1시간

### SLI-02 실패율(Failure Rate)
- 정의: 전체 처리 대비 실패 처리 비율
- 수식: `failed_messages / total_processed_messages * 100`
- 집계 단위: 5분, 1시간

### SLI-03 DLQ 적체(DLQ Backlog)
- 정의: DLQ 큐의 미처리 메시지 수
- 수식: `dlq_queue_depth`
- 집계 단위: 실시간(1분)

### SLI-04 재시도율(Retry Rate)
- 정의: 전체 처리 대비 재시도 발생 비율
- 수식: `retried_messages / total_processed_messages * 100`
- 집계 단위: 5분, 1시간

## 2) 서비스 등급별 SLO/임계값
| 등급 | SLO 목표 | 경고(Warning) | 치명(Critical) |
|---|---|---|---|
| Tier-1 핵심 결제/주문 | p95 지연 <= 2.0s, 실패율 <= 0.5%, DLQ <= 50, 재시도율 <= 3% | 지연 > 1.8s 또는 실패율 > 0.3% 또는 DLQ > 30 또는 재시도율 > 2% | 지연 > 2.5s 또는 실패율 > 0.8% 또는 DLQ > 80 또는 재시도율 > 4% |
| Tier-2 일반 업무 | p95 지연 <= 5.0s, 실패율 <= 1.0%, DLQ <= 150, 재시도율 <= 5% | 지연 > 4.5s 또는 실패율 > 0.7% 또는 DLQ > 100 또는 재시도율 > 4% | 지연 > 6.0s 또는 실패율 > 1.5% 또는 DLQ > 200 또는 재시도율 > 7% |
| Tier-3 배치/비핵심 | p95 지연 <= 12.0s, 실패율 <= 2.0%, DLQ <= 500, 재시도율 <= 10% | 지연 > 10.0s 또는 실패율 > 1.5% 또는 DLQ > 350 또는 재시도율 > 8% | 지연 > 15.0s 또는 실패율 > 2.5% 또는 DLQ > 700 또는 재시도율 > 12% |

## 3) 공통 판정 원칙
- 2개 이상 지표가 경고 이상이면 Incident 후보로 분류
- 1개라도 치명 임계값 초과 시 즉시 치명 이벤트 생성
- SLO 위반이 10분 이상 지속되면 에스컬레이션 필수

## 4) 운영 원칙
- Coordination 단일 채널
- Owner 직접 소통 금지
