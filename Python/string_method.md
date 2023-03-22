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
