# GCD algorithm 유클리드 호제법

최대공약수를 구하는 알고리즘이다.

**호제법**: 두 수가 서로 상대방의 수로 나눈다는 뜻

- 호(互) : 서로
- 제(除) : 나누다

알고리즘의 순서

- a, b를 입력 받는다. (a > b인 경우)

1. a, b 둘 중 작은 수 b가 0이라면, 더 큰 수 a를 출력한다.
2. 둘 중 더 큰 수 a가 b로 나누어 떨어지면, b를 출력한다.
3. a를 b로 나눈 나머지(a%b)를 a에 대입하고, a와 b를 바꾼다.(반복)

- 예시

```python
# 반복문
def gcd(a, b):
  while b != 0:
    a, b = b, a%b
  return a

# 재귀문
def GCD(a, b):
    r = b % a
    if r == 0:
        return a
    return GCD(r, a)
```
