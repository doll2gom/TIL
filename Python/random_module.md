# Random 모듈

가장먼저 `import random`으로 모듈을 불러온다.

## random.choice()

괄호 안에 들어가는 시퀀스<sub>문자열, 리스트, 튜플</sub>에서 무작위로 **하나의 원소**를 뽑아준다.

- Django 실습 예시

  - ```python
    def today_dinner(request):
        foods = ['김밥', '짜장면', '대패삼겹살',]
        context = {
            'foods': random.choice(foods),
        }
        return render(request, 'articles/today_dinner.html', context)
    ```

## random.sample()

괄호 안에 **배열**과, 랜덤으로 **출력할 요소의 개수**를 넣어준다.

- Django 실습 예시

  - ```python
    def lotto(request):
    data = request.GET.get('message')
    output = []
    for i in range(int(data)):
        output.append(random.sample(range(1, 46), 6))
    context = {
        'data': output
    }
    return render(request, 'articles/lotto.html', context)
    ```
