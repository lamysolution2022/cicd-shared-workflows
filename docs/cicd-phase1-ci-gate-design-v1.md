# 1차 CI 게이트 통합 설계안 v1

- 제출 ID: `61a07b6bb340414abed25716e638f5d3`
- 요청 ID: `61a07b6bb340414abed25716e638f5d3`
- 작성일: 2026-02-19
- 작성자: Platform Engineer (CI/CD Owner)
- 범위: 아키텍처 역의존 금지 + 메시지 호환성 테스트 게이트 설계(워크플로 반영 제외)

## 1) 게이트 목표
- PR/Push 단계에서 구조 위반과 메시지 스키마 비호환 변경 사전 차단
- 위반 시 즉시 실패 + 재현 가능한 로그/가이드 제공

## 2) 필수 게이트 항목
### G1. 아키텍처 역의존 금지 테스트
- 검증 대상: 모듈 레이어 간 import/참조 방향
- 금지 규칙 예시:
  - domain -> application/infrastructure 참조 금지
  - application -> infrastructure 참조 금지(인터페이스는 허용)
- 실패 조건: 금지 방향 1건 이상 발견

### G2. 메시지 호환성 테스트
- 검증 대상: 이벤트 스키마(JSON/Avro/Proto)
- 검증 규칙:
  - 기존 필수 필드 삭제 금지
  - 기존 필드 타입 변경 금지
  - 의미 변경(semantics change) 시 버전 상승 필수
- 실패 조건: backward compatibility 위반 1건 이상

## 3) 파이프라인 통합 설계
- 트리거: `pull_request`, `push(main)`
- 순서:
  1. 정적 분석/유닛 테스트
  2. G1 아키텍처 테스트
  3. G2 메시지 호환성 테스트
- 병합 규칙: 모든 필수 게이트 success일 때만 merge 허용

## 4) 실패 처리 및 재현 절차
### 공통 실패 처리
- PR 상태: failed
- 로그 위치: CI job log + artifact(`gate-failure-report`)
- 통보: Coordination 채널 실패 이벤트 공유

### 재현 절차
1. 동일 브랜치 checkout
2. 로컬 테스트 명령 실행
3. 실패 케이스 파일/라인 확인
4. 수정 후 재실행 및 증적 첨부

## 5) 로그 기반 보고 항목
- 실패 게이트 ID(G1/G2)
- 위반 파일/규칙/샘플 diff
- 재현 명령/환경 정보
- 수정 커밋/재실행 결과

## 6) 2차 구현 시 반영 범위
- `.github/workflows/ci-quality-gates.yml` 신설
- `tests/architecture/*`, `tests/compatibility/*` 반영
- branch protection required checks 등록

## 7) 운영 원칙
- Coordination 단일 채널
- Owner 직접 소통 금지
