# DTL(Django Template Language)

django가 제공하는 특별한 HTML문법이 있다.\
template을 사용해 변수지정, 조건문, 반복문 등 기본적인 연산을 HTML 상에서 가능하도록 한다.

```django
## 변수 ##
{{ variable }}

## 필터 ##
{{ variable|filter }}

## 태그 ##
<!-- 태그를 활용해 연산을 할 수 있다. -->
{{% if var == 'name' %}} {{% endif %}}

## 주석 ##
{# comments #}
{{% comments %}}
```

# Template inheritance 템플릿 상속

## 1. 폴더의 최상단 root 위치에 base템플릿 생성

템플릿명은 `base.html`로 지정\
`{% Tags %}`를 활용하여 적용시킬 설정값을 지정해준다.

```django
<! -- articles/base.html -->

<!DOCTYPE html>
<html lang="en">
<head>
...
{% comment %} bootstrap CDN 생략 {% endcomment %}
</head>
<body>
  {% block content %}
  {% endblock content %}
  {% comment %} bootstrap CDN {% endcomment %}
</body>
</html>
```

## 2. 프로젝트 urls.py 설정

- 프로젝트<sub>firstpjt</sub> 폴더의 urls.py파일을 열어\
  `from django.urls import path`뒤에 `, include`를 넣어준다.
  &rArr; `from django.urls import path, include`

- `urlpatterns = []`안에 `path('', include('articles.urls)),`작성
  ```django
  urlpatterns = [
      path('', include('articles.urls)),
  ]
  ```

## 2. 앱 urls.py 생성 및 설정

- 앱<sub>articles</sub>폴더 안에 프로젝트<sub>firstpjt</sub>의 urls.py와 동일한 urls.py파일을 하나더 생성한다.

- 상단 code

  - ```django
    <!-- 현재경로 . 에서 views모듈을 가져옴 -->
    from django.urls import path
    from . import views
    ```

- 하단 code

`name`을 지정하는 이유는 html문서에서 서로 다른 앱 속의 같은 이름의 하위 템플릿명이 겹치는 경우 발생할 수 있는 경로의 오류를 방지하기 위함이다.

- ```django
  <!-- 앱이름을 문자열로 작성 -->
  app_name = 'articles'
  <!-- 첫 번째 요소는 앱이름 -->
  <!-- 두 번째 요소는 '모듈.함수명' -->
  <!-- 세 번째 요소는 해당 앱의 별명을 지정 -->
  urlpatterns = [
      path('articles', views.index, name='articles'),
    ]
  ```
