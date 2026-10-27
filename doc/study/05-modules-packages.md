# 05. 모듈과 패키지

## 공부할 개념
- 모듈은 Python 파일 하나
- 패키지는 관련 모듈을 묶은 디렉터리
- `import`와 순환 import의 위험
- `__init__.py`, `__main__.py`
- `if __name__ == "__main__":`
- 책임에 따른 파일 분리
- `python -m budget_app` 실행 방식

## 권장 역할 예시
- `models.py`: Transaction 데이터 구조
- `storage.py`: JSONL 파일 읽기/쓰기
- `services.py`: 검증·검색·요약 같은 업무 규칙
- `cli.py`: argparse와 사용자 출력
- `__main__.py`: 실행 진입점

## 확인 과제
명령 실행 시 어떤 파일에서 시작하고, 각 모듈이 어떤 책임을 맡는지 화살표로 설명한다.
