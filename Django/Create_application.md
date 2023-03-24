# Create application

## 6. 앱 생성

- `$ python3 manage.py startapp articles`

![프로젝트와 앱](/Django/%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%EC%99%80%20%EC%95%B1.png)

`articles`라는 이름의 앱을 생성한다. 앱의 이름은 '복수형'으로 지정한다.

생성된 앱을 보면 프로젝트 폴더 안에 들어가 있지 않고 프로젝트 폴더와 같은 위치에 만들어져 있다.
이것은 장기적 관점에서 프로젝트 폴더 안에 앱이 많이 생기면 복잡해지는 것을 방지하기 위함이다.

이미지처럼 생각하지 않고, 생성되는 앱들을 프로젝트에 등록한다고 이해해야 한다.

---

## 7. 앱 등록\_settings.py

> ⚠️ 반드시 앱을 먼저 생성하고 등록해야한다.

앱이 생성된 것을 확인하면, 프로젝트 폴더 `settings.py`파일에 있는 `INSTALLED_APPS = []` 리스트를 찾는다.\
먼저 기본적으로 설치된 앱 리스트 중 가장 상단 위치에 방금 생성한 앱의 이름을 저장한다.

이 때, 앱 등록에 권장되는 순서가 있다.

```python
# Application definition

INSTALLED_APPS = [
    # 앱 등록 권장 순서
    # 1. local app
    'articles',

    # 2. 3rd party app(설치를 통해 추가하는 앱)

    # 3. 기본 django app
    '...',
]
```

---

## 8. url설정\_urls.py

프로젝트의 `urls.py` 입장에서는 특정 패키지에서 views 모듈을 가져오는 것이고, 이 모듈은 지정된 특정 함수를 불러와 실행시키는 것이다.

`http://123.0.0.1:8000/articles/` 에서 `articles`로 요청이 왔을 때 `views` 모듈의 `index` 뷰 함수를 호출한다는 뜻이다.

`articles/`를 비워두면 url의 첫 부분이 비워진채로 views.py에서 설정한 문자로 시작한다.

`views`뒤에 나오는 `index` 항목은 views.py에서 작성할 함수명을 미리 적는 것이다.

```js
// ...
from articles import views

urlpatterns = [
    // ...
    path('articles/', views.index)
]
```

## 9. 함수 생성\_views.py

render함수의 결과 값을 리턴하는 페이지\
가장 많은 정보를 받아 처리하고, 리턴하는 중요한 위치의 파일이다.\
render함수에 들어가는 요소는 최대 3가지이다.

- render함수\
   두번째로 주어진 **템플릿**을 세번째에 주어진 `context`데이터와 결합하고 첫 번째로 주어진 `HttpResponse`(응답)객체를 반환하는 함수

1. request
   응답을 생성하는 데 사용되는 요청 객체
2. template_name
   템플릿 이름의 경로
   > 일반적인 템플릿 모양 &rArr; `articles/index.html`\
   > `articles`는 경로폴더 이름이고, `index.html`은 실제적인 템플릿이다.
3. context
   템플릿에서 사용할 데이터 (딕셔너리 타입으로 작성)

```js
from django.shortcuts import render

def index(request):
      context = {
         'name': name,
      }
   return render(request, 'articles/index.html', context)
```

---

## 약속 2가지

1. 모든 `view`함수는 첫 번째 인자로 요청객체`request`를 필수적으로 받는다.
2. `templates`폴더는 앱폴더 안에/ 템플릿은 `templates`폴더 안에 위치한다.

> templates / &rArr; 여기까지 경로가 django와의 약속이다.
>
> > articles /
> >
> > > index.html / &rArr; 필수적으로 작성해야할 기초 템플릿이다.\
> > > 하지만 상위 경로가 있는 경우 반드시 함께 적어야 한다.
