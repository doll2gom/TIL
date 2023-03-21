# ♨️ TIL 220210

### 🕘 오전 알고리즘 수다

- 오후 알고리즘 모의고사를 전 아이스브레이킹
- 잡담 앞으로의 각오 다지기
- 자유시간
  - 알고리즘 스터디 오늘의 문제 풀이
  - BOJ 2231 분해합

### 🕜 오후 3회차 알고리즘 모의고사

#### SWEA

- 11856 반반
- 7465 창용 마을 무리의 개수
- 4406 모음이 보이지 않는 사람
- 3499 퍼펙트 셔플
- 1949 [모의 SW 역량테스트] 등산로 조성
- 1208 [SN 문제해결 기본] 1일차 - Flatten

오늘은 이상하게 손으로 수도코드를 적지 않고 무작정 달려들었다.\
알고리즘 실습이 끝나고 너무 많이 주어진 자유시간이 아직도 어리둥절하고 군기가 덜 빠진 느낌이다.\
뭔가 엄청나게 압박감과 자괴감 조급함? 그런 것들이 조여오다가 나사가 풀려버린 것도 같고,,
한 이틀정도 SQL 맛보기로 보고 다시 문제를 풀려고 하니 기억도 가물가물하고,, 파이썬 라이브러리도 이상하게 낮설어진 기분이다. 어제 분명히 들어갔는데,

### 🕔 스터디 코드리뷰

- BOJ 2231 분해합

비교하는건 아니지만, 조원들의 코드 보면서 혼자 고립되어 생각하지 말자 또 다짐하게 되었다.\
너무 깊게 생각하면 안된다.\
그리고 문제들을 보자마자 풀지 않고 적지 않고 가만히 생각해보는 시간을 무조건 가져야겠다.

<details markdown="1">
  <summary>내 코드</summary>

```python
for n in range(1,length*9+1):
number = N - n
lst.append(number)

while True:
a = divmod(number, 10)
lst.append(a[1])
number = a[0]

if a[0] == 0:
break

```

</details>

<details markdown="1">
  <summary>조원 코드</summary>

```python
for i in range(1, n): # 1부터 시험해보기
total = i
temp = i

while temp:       # i의 각 자리수 더하기
total += (temp % 10)
temp = temp // 10

if total == n:    # i의 각 자리수와 i를 더한 값이 n과 같으면
print(i)       # i를 출력하고 루프에서 나온다.
break

```

</details>

### 🐾 개인공부

- Git\
  오늘도 깃이랑 싸웠다.\
  어제의 커밋은 영원히 되돌릴 수 없나보다. 하위폴더에서 커밋해서 안보이는 건줄 알았는데, 문제는 진짜 이메일이었다. 진짜 공백 하나가 문제였다,, \
  $ git config -global 에서 이메일을 변경한 기억은 없지만, 아무튼 잔디는 정상적으로 다시 심기고 있다. 중간에 생긴 구멍을 보니 더 아쉬운 마음에 깃허브에 신경이 바짝쓰인다