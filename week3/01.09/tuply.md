# Tuple

불변한 값들의 나열

|       변경       |      반복       |        생성방법         |
| :--------------: | :-------------: | :---------------------: |
| 변경 X immutable | 반복 O iterable | 소괄호(()) 혹은 tuple() |

- 사용자가 활용하기 보다 주로 파이썬에 내장되어 활용된다.
  - 예를들어 어떤 결과값의 타입이 튜플로 표현되어 보임
- 값에 대한 접근은 인덱스로 접근
  ![index](/TIL/week3/Day11/index.jpg)

```Python
dict = {'name':'더글로리', 'cast':'송혜교'}
print(dict.keys()
print(dict.items()) # dict_items('name':'더글로리', 'cast':'송혜교')
print(type(dict.items()))# tuple
```
