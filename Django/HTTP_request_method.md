# HTTP request method

## GET 메서드

가져올 때만 사용; 정확히는 **조회**할 때만 사용한다.\
_SQL 쿼리문의 SELECT와 같은 기능_

- 예시
  view에서 사용자의 입력을 받아서 활용할 때 사용한다.

- 데이터를 조회할 때 사용
- 해당 주소를 보여줄 때
- 주소에 표현이 됨

> a태그는 get의 속성을 가진다.

## POST

변경할 때 사용; **수정**할 때 사용

a태그 단순 페이지 이동, 조회
submit은 form을 제출할 때
button 이벤트 실행
input
input의 submit/ button의 submit 둘 다 동일하게 작동한다.
버튼태그의 사용의 예시는 광범위하다.

delete 삭제하는 작엄은 수정의 영역이기 때문에, a태그 사용을 적절하지 않다.
POST:생성Create,수정Update,삭제Delete

- 제이터를 생성/수정/삭제할 때 사용
- 길이제한 없음
- Django에서 발행하는 [csrf](/Django/CSRF.md)토큰을 사용해야 한다.

> 생성을 할때는 form태그속 label,input태그를 사용해 입력을 받는다.
