# Wave2 게이트 차단 규칙 보정안

- SubmissionId: `86bee238725f481b91be2ad7da2d017a`
- PlanId: `f2339519-481a-4773-af40-a94265f4cb8b`
- 작성일: 2026-02-19
- 작성자: Platform Engineer (CI/CD Owner)

## 1) 보정 배경
- Architect 판정에서 관측성 조건부 Fail 확인: `retryCount` 누락률 1.8%
- 기존 게이트는 이벤트 상태 흐름 중심이며 필수 필드 누락 차단 규칙이 약함
- 따라서 필수 필드 강제 주입 + 누락 탐지 규칙을 게이트에 결합

## 2) 보정 규칙(안)
### R1. 필수 게이트 결합 차단
- 조건: 아래 중 1개 실패 시 즉시 차단
  1. 아키텍처 역의존 테스트 실패
  2. 메시지 호환성 테스트 실패
  3. 릴리스 노트 필수 항목 누락

### R2. 관측성 연동 차단
- 조건: 최근 30분 창에서 critical 이벤트 1회 이상 + recovered 미확인 시 차단
- 데이터 소스: `artifacts/observability/wave2-gate-validation-events-2026-02-19.json`

### R2-1. retryCount 필수 필드 강제 규칙
- 조건: 관측성 이벤트(`warning/critical/recovered`)의 `retryCount` 필드 누락률 > 0%면 차단
- 산출 근거: `artifacts/observability/wave2-retrycount-validation-2026-02-19.json`
- 판정 식:
  - `missing_rate_pct = (missing / total) * 100`
  - 기준: `missing_rate_pct == 0.0`

### R3. 무음 정책 보호 규칙
- 조건: 무음 윈도우가 승인 메타데이터 없이 적용된 경우 차단

### R4. 에스컬레이션 미이행 차단
- 조건: critical 10분 지속 시 escalation 이벤트 누락 시 차단

### R5. 로그 파이프라인 누락 탐지 규칙
- 조건: 수집 파이프라인에서 필수 필드 누락 감지 시 `MSG_RETRYCOUNT_MISSING` 이벤트 생성
- 동작:
  1. 누락 탐지 시 경고 이벤트 즉시 발행
  2. 5분 내 미복구 시 치명 이벤트 승격
  3. 필드 정상화 시 복구 이벤트 발행
- 검증 데이터: `warning -> critical -> recovered` 1사이클 이상 존재해야 함

## 3) 릴리스 보고 형식 강화
- 필수 포함:
  - 성공/차단 run URL 각 1개
  - 차단 step 링크
  - warning/critical/recovered 이벤트 경로
  - retryCount 누락률 산출 근거(보정 전/후)
  - 무음/에스컬레이션 적용 근거

## 4) 적용 순서
1. Wave2 파일럿에서 룰 경고 모드 적용(1주)
2. 오탐 점검 후 강제 차단 모드 전환
3. 월간 리허설로 룰 유효성 점검

## 5) 잔여 리스크
- 다중 서비스 동시 배포 시 이벤트 상관관계 오판 가능
- 임계값 고정값 사용 시 트래픽 계절성 반영 한계

## 6) 차기 액션
1. 이벤트 상관분석 키(배포ID/서비스ID) 추가
2. 임계값을 시간대/트래픽 구간별 동적화
3. 게이트 차단 사유 자동 티켓 발행
4. retryCount 외 필수 필드(`tenantId`, `traceId`) 동일 규칙 확장

## 7) 운영 원칙
- Coordination 단일 채널
- Owner 직접 소통 금지
