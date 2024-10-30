## Exercise: `for` with `if`<br>`for` 와 `if` 문

**Please edit and submit exercise.py file.**<br>**exercise.py 파일을 수정하여 제출하세요.**

### Objective<br>목표

* Practice using conditional statements within loops.<br>반복문 내에서 조건문 사용 연습

### Function description<br>함수 설명
The `for_with_if` function in `exercise.py` is supposed to calculate the sum of either odd or even numbers within a given range. Your task is to fix it according to these requirements:

`exercies.py` 파일의 `for_with_if` 함수는 주어진 범위 내에서 홀수 또는 짝수의 합을 계산하는 것이 목적입니다. 다음 요구 사항에 따라 완성 바랍니다.

* The function should take three arguments:<br>해당 함수는 세 개의 인수를 받아야 합니다.

| Argument | Type | Description |
|:---|:---|:---|
| `a` | `int` | The starting value of the range (inclusive).<br>범위의 시작값(포함) |
| `b` | `int` | The ending value of the range (exclusive).<br>범위의 끝값(미포함) |
| `c` | `bool` | A boolean flag; `1` if the sum of odd numbers is requested, `0` for even numbers.<br>참이면 홀수의 합, 거짓이면 짝수의 합을 계산 |

* The function should return the calculated sum based on the `c` flag.<br>`c` 값에 따라 계산된 합을 반환해야 합니다.
* Please do not use `input()`, `map()`, or `sum()` functions in the `exercise.py` file.<br>`exercise.py` 파일 안에서 `input()`, `map()`, 또는 `sum()` 함수를 사용하지 마세요.

## How to run .py file on a shell 쉘에서 실행해 보는 방법

1. Complete the function of the file.<br>해당 파일의 해당 함수를 완성합니다.
1. On a shell, run `python sample.py` file.<br>터미널에서 `python sample.py` 명령을 실행하여 결과를 확인합니다.

## How to run the function on Google Colab<br>함수를 구글 코랩에서 실행해보는 방법 예
1. Make sure you've completed the `product()` function in `exercise.py` before running this.<br>실행 전 `exercise.py` 의 `product()` 함수를 완성.
1. Open Google Colab: Go to https://colab.research.google.com/ and create a new notebook.<br>구글 코랩을 연다 : https://colab.research.google.com/ 로 가서 새로운 노트북을 생성
1. Upload the .py files:<br>.py 파일을 업로드
    1. Click on the "Files" icon on the left sidebar.<br>왼쪽 테두리 위의 Files 아이콘 선택
    1. Click on the "Upload" button and select your `exercise.py` and `sample.py` files.<br>업로드 버튼을 선택하고 `exercise.py`, `sample.py` 파일 선택
1. Run the code<br>코드 실행:
    1. In a new code cell, type `!python sample.py` and press <kbd>Shift</kbd>+<kbd>Enter</kbd> to execute it.<br>새 코드 셀에서 `!python sample.py`을 입력하고 <kbd>Shift</kbd>+<kbd>Enter</kbd> 를 눌러 실행

## Grading Criteria<br>채점 기준

| Criteria<br>기준 | Points<br>배점 |
|:-----:|:-----:|
| Is the code written according to Python syntax?<br>Python 문법대로 작성되었는가? | 1 |
| Does code respect style guidelines?<br>코드 스타일 권고사항을 준수하는가? | 1 |
| Is the code implemented as required?<br>코드가 요구사항을 만족하는가? | 3 |

## Github 온라인 편집기 필요한 경우 사용법
* <kbd>.</kbd> 키를 누르면 MS VS Code 의 Web version 이 시작됨
* 수정 사항을 commit 등록 하려면 왼쪽에서 줄 셋 아래 (확대경 다음) 세번째 가지치기 아이콘 선택
* 파일 이름의 오른쪽 + 기호 선택 (staging)
* 위 빈칸에 변경 사항 설명 입력
* [커밋 및 푸시] 선택
* 줄 셋 의 [리포지토리로 이동] 선택하여 저장소로 복귀

## NOTICE REGARDING STUDENT SUBMISSIONS<br>제출 결과물에 대한 알림

* Your submissions for this assignment may be used for various educational purposes. These purposes may include developing and improving educational tools, research, creating test cases, and training datasets.<br>제출 결과물은 다양한 교육 목적으로 사용될 수 있을 밝혀둡니다. (교육 도구 개발 및 개선, 연구, 테스트 케이스 및 교육용 데이터셋 생성 등).

* The submissions will be anonymized and used solely for educational or research purposes. No personally identifiable information will be shared.<br>제출된 결과물은 익명화되어 교육 및 연구 목적으로만 사용되며, 개인 식별 정보는 공유되지 않을 것입니다.

* If you do not wish to have your submission used for any of these purposes, please inform the instructor before the assignment deadline.<br>위와 같은 목적으로 사용되기 원하지 않는 경우, 과제 마감일 전에 강사에게 알려주기 바랍니다.
