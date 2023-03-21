# callback 함수

## callback 함수 이해하기

### 1단계

- 함수도 변수에 저장하고, 저장한 변수에 괄호를 붙여 그대로 함수처럼 사용할 수 있다

```python
def function():
  return
a = function
# a() == function()
```

### 2단계

함수에 들어가는 매개변수를 함수로 넣어줄 수 있다.\
함수의 매개변수로 전달된 함수를 콜백함수라고 한다.

아래의 예시에서 function은 f2와 같고, function()을 호출하는 것은 f2()를 호출하는 것과 동일하다.\
또한, 함수의 매개변수로 전달된 function은 함수이므로, 콜백함수가 된다.

```python
# 첫 번째 함수
def f1(function):
  ## function = f2
  ## function() = f2()
  function()

# 두 번째 함수
def f2():
  print("second")

# 첫 번째 함수를 호출하면서 매개변수로 두 번째 함수를 넣어줌
f1(f2)

# 출력 >> second
```

### 3단계

콜백함수에도 매개변수를 넣어줄 수 있다.

```python
# 콜백함수
def f1(function):
  ## function() = f2()
  function("3rd")

def f2(third):
  print("second", third)

f1(f2)

# 출력 >> second, 3rd
```
