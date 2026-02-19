# 메시징 장애 런북/리허설 기록 v1

- SubmissionId: `3246e459144f4c81b910a8c9bfbc5c26`
- PlanId: `408c46dd-86d6-4207-81a7-3b8130b3eda8`
- 작성일: 2026-02-19
- 작성자: Platform Engineer (CI/CD Owner)

## 1) 장애 시나리오별 런북
### R1. 지연 급증
- 탐지: p95 latency 경고 임계 초과
- 판단: 브로커 지연 vs 소비자 처리 병목 구분
- 조치: 소비자 스케일아웃, 느린 파티션 재분배
- 복구: 10분 연속 정상 구간 확인 후 경보 해제

### R2. 실패율 증가
- 탐지: failure rate 경고/치명 초과
- 판단: 직렬화 오류/다운스트림 오류 분기
- 조치: 문제 릴리스 롤백, 재시도 백오프 상향
- 복구: 실패율 목표치 이하 15분 유지

### R3. DLQ 적체 증가
- 탐지: DLQ depth 경고/치명 초과
- 판단: poison message 비율/유형 분석
- 조치: DLQ 분류 재처리, 무효 메시지 격리
- 복구: DLQ depth 기준치 이하 + 재유입 없음 확인

### R4. 재시도율 급증
- 탐지: retry rate 임계 초과
- 판단: 일시 장애 vs 구조적 결함 구분
- 조치: 재시도 간격 조정, 회로차단기 활성화
- 복구: 재시도율 정상화 + 지연/실패율 동반 안정화

## 2) 리허설 증적
- 로그: `artifacts/observability/rehearsal-log-2026-02-19.json`
- 요약: `artifacts/observability/rehearsal-summary-2026-02-19.md`
- 스크린샷:
  - `artifacts/observability/screenshots/panel-latency.svg`
  - `artifacts/observability/screenshots/panel-dlq.svg`
  - `artifacts/observability/screenshots/alert-timeline.svg`

## 3) 판정
- 알림 발생/해제/에스컬레이션 이벤트 전 구간 생성 확인
- 경고 -> 치명 -> 에스컬레이션 -> 복구 순서 일관성 확인

## 4) 잔여 리스크
- 실제 프로덕션 데이터소스 연결 전 임계값 미세조정 필요
- 야간 트래픽 패턴 반영한 무음 정책 추가 보정 필요

## 5) 차기 액션
1. 실제 모니터링 스택(Prometheus/Grafana/Alertmanager) 반영
2. 월간 게임데이로 임계값 재검증
3. 자동 티켓 발행/런북 링크 자동 첨부 연계

## 6) 운영 원칙
- Coordination 단일 채널
- Owner 직접 소통 금지
