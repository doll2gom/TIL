# Django shell

django 환경 안에서 실행되는 python shell
(입력하는 Query Set API 구문이 django 프로젝트에 영향을 미침)

django 쿼리문을 사용하기 위해 python shell을 좀 더 편하게 만들어주는 ipython을 설치한다.
```
pip install ipython django-extensions
```

```py
# settings.py파일에 입력
INSTALLED_APPS = [
  ...,
  'django_extensions',
  ...,
]
```
```
터미널에서 실행
python manage.py shell_plus
```

### python shell

python을 설치하면 기본적으로 내장되어 있는 shell이 있다.\
한 줄씩 입력에 대한 기본 응답을 줌