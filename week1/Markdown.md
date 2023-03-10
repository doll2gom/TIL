# 마크다운 Markdown

## 개요

```bash
텍스트 기반의 마크업 언어 HTML에서 ML이 마크업을 뜻한다.
마크업의 핵심은 구조화이다!
마크다운은 텍스트를 HTML로 변환하는 도구다, 쉽게 읽고, 쓰는 plain text formet이다. 가장 단순한 문법적 기반을 가진다.
워드프로세서는 다양한 서식과 구조를 지원하지만 다양한 환경에서 호환이 안될 수 있다.
마크다운은 단순 텍스트로 되어 있기 때문에 다양한 환경에서 변환하여 보여짐
마크다운의 확장자명 : README.md
모든 페이지에 입력하면 호환되어 볼 수 있다.
마크다운 문서로 작성한 정적사이트생성기 기반 블로그 깃헙에 기록을 남기면서 공부할 수 있다. 웹에 대한 이해가 늘어나면서 더 많이 활용할 수 있게 된다.
노션이나 많은 SW에서 사용
```

# 마크다운 문법

```bash
1. Heading : 문서의 제목이나 소제목

   - #의 개수에 따라 h1~h6까지 표현 가능
   - 문서 구조를 위해 사용! 글자 크기를 조절하기 위해 사용해서는 안됨

2. List : 목록

   1. 하나
   2. 둘
   3. 셋

   - 하나
   - 둘
   - 셋
     (-) 이름 : 하이픈
     목록에서 대칭관계 만들기 가능
     tab으로 줄 바꿈
     shift + tab으로 입력란 앞으로 당김

3. Fenced Code block : 코드 블록
   백틱backtick 기호 3개를 활용하여 작성
   언어의 하이라이팅 기능 사용가능

4. Inline code block : 코드 블록
   특정 단어만 하이라이팅할 때 한번으로 가능

5. Link : 링크
   [문자열] (url)을 통해 링크 작성 가능
   예시)
   [구글] (https://google.com)
   [네이버] (https://naver.com)
   [a 파일](./a.md)
   [b 폴더](b/)
   [b 폴더 b.txt](b/b.txt)

6. image : 이미지
   ![1](1.png)
   ![2](b/2.png)

7. Blockquates : 인용문
   (>)로 사용한다

8. 테이블
   너무 어려운 문법

9. 텍스트 강조
   굵게 기울임 언더바

10. 수평선
    하이픈 3번

11. 취소선
    물결 2번
```

<!--- Heading --->

# Heading 1

## Heading 2

### Heading 3

#### Heading 4

##### Heading 5

###### Heading 6

Paragraph

<!-- Line -->

---

<!--- Text attributes -->

This is the **bold** text and this is the _italic_ text and let's do ~~strikethrough~~.

<!--Quote -->

> Don't forget to code your dream.

<!--Bullet list -->

Fruits:

- a
- b

<!--Bullet list -->

Other fruits:

- 1
- 2

<!--Numbered list -->

Numbers:

1. first
2. second
3. third

<!-- Link -->

Click [here](https://github.com/dream-ellie/markdown)

<!--Image -->

![image description](https://i.pinimg.com/564x/57/dd/81/57dd816dd0100ca1ec296c9ccabc4055.jpg)

<!--Table -->

| Header | Description |
| :----: | :---------: |
| Cell1  |    Cel12    |
| Cell1  |    Cell2    |
| Cell1  |    Cell2    |
| Cell1  |    Cell2    |

<!--Code-->

To print message in the console, use `console.log('your message')` and ..

```python
console. log ('your message')
```

<!--Task Lists-->

- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> supported
- [x] list syntax required (any unordered or ordered list supported)
- [x] this is a complete item
- [ ] this is an incomplete item
