# 02 Web - Box model

## CSS Box Model

모든 HTML 요소를 (사각형) 박스로 표현
박스에 대한 크기 여백, 테두리 등의 스타일을 지정하는 디자인 개념

## Box의 구성

> Margin : 박스와 다른 요소 사이의 공백 가장 `바깥쪽 영역`
>
> > Border : 콘텐츠와 패딩을 감싸는 `테두리 영역`
> >
> > > Padding : `콘텐츠 주위`에 위치하는 공백 영역
> > >
> > > > Content : `콘텐츠`가 표시되는 `영역`

## Box 구성의 방향별 명칭

![Box 구성의 방향별 명칭](/week9/02.23/box.png)

## box-sizing 속성

## block 타입 특징

- 항상 새로운 행으로 나뉨
- width와 height 속성을 사용하여 너비와 높이를 지정할 수 있음
- 기본적으로 width 속성을 지정하지 않으면 박스는 inline 방향으로 사용 가능한 공간을 모두 차지함 (너비를 사용가능한 공간의 100%로 채우는 것)
- 대표적인 block 타입 태그
- h1~6, p, div

## inline 타입 특징

- 새로운 행으로 나뉘지 않음
- width와 height 속성을 사용할 수 없음
- 수직 방향 : padding margins, borders가 적용되지만 다른 요소를 밀어낼 수는 `없음`
- 수평 방향 : padding margins, borders가 적용되어 다른 요소를 밀어낼 수 ` 있음`
- 대표적인 inline 타입 태그\
  : a, img, span

## 기타 속성

### shorthand 속성 - border

border-width, border-style, border-color를 한번에 설정하기 위한 속성

````
/* 순서는 영향을 주지 않음 #/
border: 1px solid black;```
````

### shorthand 속성 - margin & padding

4방향의 속성을 각각지정하지 않고 한번에 지정할 수 있는 속성

/ 4개 - 상우하좌 /\
margin: 10px 20px 30px 40px; \
padding: 10px 20px 30px 40px;

/ 3개 - 상 /좌우/하 /\
margin: 10px 20px 30px; \
padding: 10px 20px 30pX;

/ 2개 - 상하/좌우 /\
margin: 10px 20px;\
padding: 10px 20px;

/ 1개 - 공통 /\
margin: 10px;\
padding: 10px;

## Margin collapsing (마진 상쇄)

- 두 block 타입 요소의 martin top 과 bottom이 만나 큰 margin으로 결합되는 현상
- 웹 개발자가 레이아웃을 더욱 쉽게 관리할 수 있도록 함
  - 각 요소에 대한 상/하 margin을 각각 설정하지 않고 한 요소에 대해서만 설정할 수 있음
