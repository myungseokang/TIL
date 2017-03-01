> React 공식문서

# Rendering Elements
Element 는 React의 가장 작은 단위입니다.
Element 는 화면에 표시 할 내용을 설명합니다.

```
const element = <h1>Hello, world</h1>;
```

브라우저 Element 인 DOM Element 와는 달리 React Element 는 일반 객체이므로 보다 쉽게 만들 수 있습니다. React DOM은 React Element 와 일치하도록 DOM을 업데이트합니다.

## Rendering an Element into the DOM

```
<div id="root"></div>
```

이 div를 루트 DOM 이라고 칭합니다.
그 내부의 모든 것이 React DOM에 의해 관리되기 때문입니다.

React로 구축 된 애플리케이션은 대개 단일 루트 DOM 노드를 사용합니다.
React 요소를 루트 DOM 노드로 렌더링하려면 ReactDOM.render () 에 전달합니다.
```
const element = <h1>Hello, world</h1>;
ReactDOM.render(
  element,
  document.getElementById('root')
);
```
[Hello World in React](http://codepen.io/gaearon/pen/rrpgNB?editors=1010)

## Updating the Rendered Element
React Element 는 **불변** 이다.
일단 Element 를 만들고 나면 Element 의 내용 또는 특성을 변경할 수 없습니다.
Element 는 특정 시점의 UI를 나타냅니다.

```
function tick() {
  const element = (
    <div>
      <h1>Hello, world!</h1>
      <h2>It is {new Date().toLocaleTimeString()}.</h2>
    </div>
  );
  ReactDOM.render(
    element,
    document.getElementById('root')
  );
}

setInterval(tick, 1000);
```
[Hello World in React](http://codepen.io/gaearon/pen/gwoJZk?editors=0010)

매 초마다 setInterval () 콜백에서 ReactDOM.render () 를 호출합니다.
실제로 대부분의 React 앱은 ReactDOM.render () 를 한 번만 호출합니다.

## React Only Updates What’s Necessary
React DOM은 요소와 그 자식을 이전 요소와 비교하여 DOM을 원하는 상태로 만드는 데 필요한 DOM 업데이트 만 적용합니다.

매 tick 마다 UI 트리 전체를 설명하는 요소를 만들었지 만 내용이 변경된 텍스트 노드 만 React DOM에 의해 업데이트됩니다.

우리의 경험에서 시간이 지남에 따라 UI를 변경하는 것이 아니라 주어진 순간을 UI가 어떻게보아야하는지 생각하면 버그 전체가 제거됩니다.
