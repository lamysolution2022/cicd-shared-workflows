# 메시징 대시보드/알림 정책 설계 v1

- SubmissionId: `3246e459144f4c81b910a8c9bfbc5c26`
- PlanId: `408c46dd-86d6-4207-81a7-3b8130b3eda8`
- 작성일: 2026-02-19
- 작성자: Platform Engineer (CI/CD Owner)

## 1) 대시보드 패널 정의
1. End-to-End Latency(p50/p95/p99)
2. Success/Failure 처리량
3. Retry Rate 추이
4. DLQ Queue Depth 추이
5. Consumer Lag(파티션/큐별)
6. Alert State Timeline(Warning/Critical)

## 2) 데이터소스/필터 기준
- 데이터소스: Prometheus(실시간 지표), Elasticsearch(에러 로그), RabbitMQ Exporter(큐 깊이)
- 필터:
  - 환경: prod/staging
  - 서비스: producer/consumer/outbox-relay
  - 토픽/라우팅키
  - 테넌트(멀티테넌트 서비스 한정)

## 3) 알림 규칙
### 경고(Warning)
- 조건: 임계값 초과 5분 지속
- 채널: Slack `#ops-warning`
- 조치: on-call 확인, 15분 내 1차 판단

### 치명(Critical)
- 조건: 치명 임계값 즉시 초과 또는 경고 15분 지속
- 채널: PagerDuty + Slack `#ops-critical`
- 조치: 즉시 장애 채널 오픈, 런북 실행

### 에스컬레이션
- Critical 10분 지속: SRE Lead 호출
- Critical 20분 지속: Incident Commander 호출

## 4) 무음(Silence) 조건
- 계획 점검 윈도우(사전 승인)
- 릴리스 롤아웃 윈도우(최대 30분)
- 무음 시에도 Critical 로그는 저장/감사 대상 유지

## 5) 채널 정책
- 경고/치명/에스컬레이션 모든 이벤트는 Coordination 요약 보고 필수
- Owner 직접 태그/DM 금지

## 6) 운영 원칙
- Coordination 단일 채널
- Owner 직접 소통 금지
