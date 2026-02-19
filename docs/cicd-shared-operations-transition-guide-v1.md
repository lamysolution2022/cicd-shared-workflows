# CI/CD 공용 워크플로우 운영 전환 가이드 v1

- PlanId: `24cc616d-c05e-476b-863d-b18c79d083da`
- SubmissionId: `7268e615cec1408ab121db5a3306ef9a`
- 작성일: 2026-02-19
- 작성자: Platform Engineer (CI/CD Owner)

## 1) 사용 가이드
1. 소비 리포의 workflow에서 공용 템플릿을 `uses`로 호출
2. 필수 입력 파라미터(build/test/deploy/security command) 설정
3. 환경별 시크릿은 GitHub Environments 또는 Org Secret 사용
4. 메이저 태그(`@v1`) 고정 후 변경은 릴리즈 노트 기준으로 반영

## 2) 변경관리 절차
1. 변경 요청 등록: Coordination 채널 RFC
2. 영향도 분석: 호환성/보안/SLA 점검
3. PR 생성 및 2인 승인
4. 소비 리포 스모크 검증
5. 릴리즈 태그 발행 및 공지
6. 7일 안정화 모니터링

## 3) 초기 안정화 모니터링 지표
- 배포 성공률(일/주): 목표 >= 98%
- 파이프라인 평균 소요시간 P50/P95
- 롤백 발생률: 목표 <= 5%
- 보안 스캔 실패율(High 이상): 목표 0건
- 템플릿 호출 실패율: 목표 <= 2%
- MTTR(배포 실패 복구 시간): 목표 <= 30분

## 4) 에스컬레이션 기준
- High 취약점 검출: 즉시 배포 중지 및 Security/Coordination 동시 통보
- 2회 연속 배포 실패: 롤백 후 원인분석 회의 소집
- MTTR 초과: DevOps Lead에 즉시 에스컬레이션

## 5) 제출 체크리스트
- [x] 아키텍처 정의서 제출
- [x] 워크플로우 템플릿 구현
- [x] 연동/롤백 검증 결과서 제출
- [x] 운영 가이드/지표 문서 제출

## 6) 운영 원칙
- Coordination 단일 채널
- Owner 직접 소통 금지
