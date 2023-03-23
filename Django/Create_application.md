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

urls.py 입장에서는 articles 패키지에서 views 모듈을 가져오는 것이다.

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

## 10. templates
