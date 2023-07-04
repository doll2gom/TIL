# String_mrthod 문자열 메서드

## join()

괄호 안에 입력한 문자들을 앞에 있는 문자열로 연결하는 함수이다.

리스트 안의 요소들을 문자열로 출력할 때 유용하다.

문자열 뒤에 점 찍고 괄호 안에는 연결하고 싶은 문자열을 입력한다.

```python
"".join('a', 'b', 'c')
# abc
```

```python
A = [1, 2, 3, 4, 5]
for a in A:
  a = [str(요소) for 요소 in a]
  print(", ".join(a))

# 1, 2, 3, 4, 5
```

- BOJ 12605

  ```python
  import sys
  N = int(sys.stdin.readline())
  for case in range(1, N+1):
    n = reversed(list(map(str, sys.stdin.readline().split())))
    print(f'Case #{case}: {" ".join(n)}')
  ```

## insert()

내가 원하는 위치에 원하는 값을 끼워 넣을 때 사용한다.

문자열 혹은 배열에서 요소들을 삭제하거나 변경하지 않고 옆으로 한칸씩 밀어내서, 최종적으로는 배열의 크기가 커지게 된다.

- BOJ 2605 줄세우기 예제

  ```python
   import sys
   num = int(sys.stdin.readline())
   random = list(map(int,sys.stdin.readline().split()))
   lst = []
   for i in range(1, num+1):
       lst.insert(random[i-1],i)
   lst = reversed(lst)
   print(*lst)
  ```

## len()

문자열을 셀 때 사용함 1부터 시작한다.

## .strip()

점(.)과 함께 사용하며 문자열 앞 뒤에 들어가는 공백이 사라지게 한다.

#### .lstrip(), .rstrip()

- .lstrip() : 문자열의 왼쪽 공백만을 제거
- .rstrip() : 문자열의 오른쪽 공백만을 제거

## find()

원하는 문자열을 왼쪽부터 시작하여 오른쪽으로 탐색하고, 가장 먼저 일치하는 문자열의 위치를 인덱스 값으로 반환하는 함수

#### rfind()

문자열을 오른쪽(뒤)에서 시작하여 왼쪽(앞)으로 탐색하고, 가장 먼저 일치하는 문자열의 위치를 인덱스 값으로 반환

## .format()

- 뒷쪽 소괄호 속에 들어가는 내용이 앞의 따옴표("") 안에 있는 문자열 속에 들어간다.
- format 함수는 자동적으로 소괄호 안의 내용을 문자열로 변환한 뒤에 틀 안에 집어넣기 때문에 따로 문자열로 변환하는 처리를 하지 않아도 된다.
  - 예시
    ```python
    "{}".format(10)
    >> 10
    ```

- 여러개를 입력하는 경우 앞에서부터 순서대로 들어간다
  - 예시
    ```python
    "{} {}".format(10, 20)
    >> 10 20
    "{}년 {}월 {}일".format(2023, 6, 30)
    >> 2023년 6월 30일
    ```

### format 함수 응용
  ```python
  a = 10
  b = 20
  "{} + {} = {}".format(a, b, a+b)
  >> 10 + 20 = 30
  ```

## split
