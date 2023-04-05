# ORM Read 조회

C**R**UD

## all() 전체 데이터 조회

- all()\
  `Article.objects.all()`

## get() 단일 데이터 조회

- get()\
  `Article.objects.get(pk=1)`
  - 유일한 값을 통해 찾을 때 즉, pk값을 통해 찾을 때 사용
  - pk 와 같은 고유성을 보장하는 조회에서 사용
  - 데이터가 없거나 2개 이상일 때 모두 에러가 발생

## 특정 조건에 대한 데이터 조회

- filter()\
  `Article.objects.get(pk=1)`
  - pk가 아닌 데이터를 통해 조회한다.
  - 만일 값이 없거나 2개 이상일 때 빈 퀴리셋을 반환

\> [다양한 쿼리셋 문법 참고-django](https://docs.djangoproject.com/en/4.1/ref/models/querysets/#methods-that-return-new-querysets)
