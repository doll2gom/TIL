# list method

> 원래의 a의 값이 변경되는 연산 혹은 함수를 비파괴적 연산 또는 비파괴적 함수라고 한다.

## 파괴적 연산
피연산자를 바꾸는 연산
```python 
a = 10

a = a + 10
a = 20
a = 30
print(a)
```
ex) 

## 비파괴적 연산
피연산자를 바꾸지 않는 연산
```python 
a = 10

a + 10
a + 20
a + 30
a + a
print(a)
```
### 예시
ex) .lstrip()





