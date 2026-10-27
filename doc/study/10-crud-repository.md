# 10. CRUD와 Repository

## CRUD
- Create: 거래 추가
- Read: 거래 목록/검색
- Update: 거래 수정
- Delete: 거래 삭제

## Repository 역할
파일 저장 방식과 읽기/쓰기 작업을 한곳에 모아, CLI가 JSONL의 세부 사항을 직접 다루지 않도록 한다.

## 미션 적용
- add는 고유 ID를 만들고 검증된 거래를 저장한다.
- list는 최신순과 limit를 적용한다.
- update는 ID를 찾아 지정된 필드만 변경한다.
- delete는 해당 ID를 제거한다.
- 없는 ID는 조용히 무시하지 않고 명확히 알린다.

## 확인 과제
같은 거래를 추가→조회→수정→조회→삭제→조회하고 각 단계의 저장 파일을 확인한다.
