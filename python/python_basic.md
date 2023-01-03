# Python 기초 개념

> 코드는 결국 도구일 뿐이다.
> 그 도구를 잘 사용하기 위해 연습이 필요하다.

# 컴퓨터 프로그래밍 언어

## 컴퓨터(Computer)

    Caculatiom : 조작
    Remember : 기억

## 프로그래밍(programming)

    멍령어의 모음(집합)
    언어 : 자신의 생각을 나타내고 전달하기 위해 사용하는 체계/ 문법적으로 맞는 말의 집합

## 컴퓨터에게 명령하기 위한 약속

    선언적 지식 declarative knowledge)
    : 사실에 대한 내용
    "이것도 모르냐"

    명령적 지식 (imperative knowledge)
    : How-to
    "내가 더 쪼개서 명령해야겠구나"

# Python이란?

문법이 간단, 표현이 간결, 쉽고 빨리 배움
간결하게 작성 가능, 다양한 운영체제에서 실행 가능

# 객체와 변수

## 객체?

    객체(Object)
    : 물건, 대상, 사물, 등등
    파이썬에서 A를 B에 담는 개념에서 B에 담기는 모든 A들을 '객체'라고 정의한다.
    '~ 것'

## 변수?

변수(Variable)
:객체를 참조하기 위해 사용되는 이름

동일한 이름에 다른 객체를 얼마든지 담을 수 있기에 '뱐수'라고 부른다.

-> 파이썬은 객체지향 언어로 모든 것이 객체로 구현되어 있다.

변수는 할당 연산자를 통해 값을 할당(assignment)

변수 할당

- 같은 값을 통시에 할당할 수 있음

```python
x = y =123
```

- 다른 값을 동시에 할당할 수 있음

```python
x, y = 1,2
```

수학적으로 말이 안되는 수식이라도  
**(=) 기호를 중심으로** 오른족의 문자를 왼쪽의 문자에 할당하는 것이라고 생각한다.

=> 오른쪽을 먼저 계산하고 왼쪽에 할당한다!

### 실습문제

- x=10, y=20 일때,
  각각 값을 바꿔서 저장하는 코드를 작성하시오.

```python
x, y = 10,20
```

> 풀이
> 임시 = x
> x = y
> y = 임시

```python
방법1 임시 변수 활용

tmp = x
X = y
y = tmp
print(x, y)
```

```python
방법2 Pythonic!

y, X = X, y
print (x, y)
```

## 식별자(Identifiers)

규칙 :
• 식별자의 이름은 영문 알파벳, 언더스코어(\_), 숫자로 구성

• 첫 글자에 숫자가 올 수 없음

• 길이제한이 없고, 대소문자를 구별

• 다음의 키워드(keywords)는 예약어(reserved words)로 사용할 수 없음

```
False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
```

내장함수나 모듈 등의 이름으로도 만들면 안됨
• 기존의 이름에 다른 값을 할당하게 되므로 더 이상 동작하지 않음

이름규칙 : 영어, (\_), 숫자

파이썬 : snake*case (단어와 단어 사이를 언더바(*)로 연결하기 때문에 뱀처럼 생겼다고 해서 snake_case)

다른언어 : CamelCase (단어와 단어 사이 첫 문자를 대문자로 쓰기 때문에 낙타 등처럼 튀어나와 았다고 CamelCase)

# 자료형 (Data Type)

변수, type이 이해되거나 와닿지 않으면 연습부족

객체(Object)의 종류
~ Type

## 1. 자료형 (Data Type)

# 자료형 (Data Type)

변수, type이 이해되거나 와닿지 않으면 연습부족

객체(Object)의 종류
~ Type

## 숫자

```
- 수치형(Numeric Type)

- int (정수, integer)
    • 모든 정수의 타입은 int
    • 오버플로우가 발생하지 않음

 float (부동소수점, 실수, floating point numbe

- complex (복소수, complex number)

- 불린형(Boolean Type)
```

## 시퀀스(Sequence)

```
- 문자열(String)

- 튜플(Tuple)

- 리스트(List)

- 레인지(Range)
```

## 컬렉션(Collection)

```
- 집합(Set)
- 딕셔너리(Dictionary)
```

## None
