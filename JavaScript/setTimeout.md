# setTimeout()

`setTimeout()`함수는 괄호안에 들어가는 매개함수 혹은 매개변수가 수행되는 시간을 지연시킨다.

`javascript`에서는 기본적으로 모든 코드의 실행이 위에서 아래로 내려오면서 순차적으로 일어난다.

그런데 특수한 경우에 해당 위치에 있어야하는 연산이 있고, 실행의 순서가 바뀌어야할 때 `setTimeout()`을 사용한다.

- 협업 사이드 프로젝트 carousel 구현 예시

  아래 상황에서 버튼을 클릭할 때 실행되어야할 무한루프는 효과는 지키면서 인덱스 값의 변환이 특정 위치에서 일어나야 한다.

  - ```js
     <!-- 0(3) [1 2 3] 4(1) -->
    // 클릭을 한 순간 오른쪽으로 idx 위치가 이동한다.
    buttonAfter.addEventListener("click", () => {
    	 <!-- idx가 4보다 작을 때 아래 if문이 실행 -->
    	if (index < total - 1) {
    		index += 1;
    		carousel.style.transform = `translate(-${imgWidth * index}px)`;
    	}

    	 <!-- idx 4가 되면 1로 이동한다. 무한루프 구현 -->
    	if (index === total - 1) {
    		// 4 --> 1 위치가 이동하는 과정에서 transition은 멈추고 인덱스의 변화만 실행시켜야 한다.
    		setTimeout(() => {
    			index = 1;
    			carousel.style.transition = "transform 0s ease-out";
    			carousel.style.transform = `translate(-${imgWidth * index}px)`;
    		}, 400); // <-- 클릭하는 순간 idx가 4라면, 설정된 시간(0.4초) 뒤에 해당 동작을 실행한다.
    	 <!-- idx 4가 아니라면 계속해서 클릭할 때마다 무한루프에 맞춰서 실행 -->
    	} else {
    		carousel.style.transition = "transform 0.4s ease-out";
    	}
    });
    ```

[html, css, javascript를 사용한 carousel 구현하기 | 완성본 click](https://github.com/SunFlower-project01/SunFlower-site/blob/main/carousel/carousel.html)
