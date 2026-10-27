# 04. 터미널 CLI와 argparse

## CLI란?
터미널에 명령어와 옵션을 입력해 프로그램을 조작하는 방식이다.

## 공부할 개념
- 명령어와 옵션의 차이
- `argparse.ArgumentParser`
- `add_subparsers()`로 하위 명령 만들기
- 필수 옵션, 기본값, 선택지(`choices`)
- `--help` 자동 생성
- 인수 검증과 사용 예시
- `python -m budget_app <command> [options]`

## 미션 적용 예시
- `list --limit 10`
- `search --category food --type expense`
- `summary --month 2026-10 --top 5`
- `delete --id TX-000001`
- `budget set --month 2026-10 --amount 300000`

## 확인 과제
각 명령에서 옵션이 누락되거나 잘못된 값이 주어졌을 때 argparse가 어떻게 반응하는지 실행한다.
