> React 공식문서

# Installation(설치)

React(이하 리액트) 에 관심이 있는데 당장 개발환경을 구축하기 귀찮다면 **CodePen** 을 사용해보자. [헬로월드 예제 링크](http://codepen.io/gaearon/pen/rrpgNB?editors=0010)

하지만 Yarn이나 npm을 사용하는 것을 추천한다.
따라서 웬만하면 위의 도구를 사용해서 프로젝트 개발환경을 구축하자.

리액트에서는 ES6 문법과 JSX 문법 사용이 가능하다.

Ex)
```
import React from 'react';
import ReactDOM from 'react-dom';

ReactDOM.render(
  <h1>Hello, world!</h1>,
  document.getElementById('root')
);
```

만약에 진짜진짜 Yarn이나 npm이 사용하기 귀찮다면 CDN으로 사용하는 방법도 있다.
(하지만 겪어본 결과 이 경우에는 문법이 달라져서 그리 추천되지는 않는다.)

Ex)
```html
<script src="https://unpkg.com/react@15/dist/react.js"></script>
<script src="https://unpkg.com/react-dom@15/dist/react-dom.js"></script>
```