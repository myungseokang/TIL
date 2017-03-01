> React 공식문서

# Components and Props
컴포넌트를 사용하여 UI를 독립적이고 재사용 가능한 부분으로 분할하고 각 부분을 개별적으로 생각할 수 있습니다.

개념 상 컴포넌트는 JavaScript 함수와 같습니다.
그들은 임의의 입력 ("props"라고 함)을 받아들이고 무엇이 화면에 나타나야 하는지를 설명하는 React Element를 반환합니다.

## Functional and Class Components
Component 를 정의하는 가장 간단한 방법은 JavaScript 함수를 작성하는 것입니다.
Ex)
```
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}
```

이 함수는 하나의 props 객체 인수를 데이터와 함께 받아들이고 React Element 를 반환하기 때문에 유효한 React Component 입니다.
이러한 컴포넌트는 말 그대로 JavaScript 함수이기 때문에 “**기능적**”이라고 부릅니다.

ES6 클래스를 사용하여 Component 를 정의할 수도 있습니다
Ex)
```
class Welcome extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}</h1>;
  }
}
```

위의 두 Component 는 React의 관점에서 동일합니다.

## Rendering a Component
이전에는 DOM 태그를 나타내는 React Element 만 있었습니다.
Ex)
```
const element = <div />;
```

그러나 Element 는 사용자 정의 Component 를 나타낼 수도 있습니다.
Ex)
```
const element = <Welcome name="Sara" />;
```

React가 사용자 정의 Component 를 나타내는 Element 를 볼 때 JSX 속성을 이 Component 에 단일 객체로 전달합니다.
우리는 이 객체를 “**Props**” 이라고 부릅니다.

예를 들어, 이 코드는 페이지에 "Hello, Sara"를 렌더링합니다.
Ex)
```
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}

const element = <Welcome name="Sara" />;
ReactDOM.render(
  element,
  document.getElementById('root')
);
```
[Try it on CodePen](http://codepen.io/gaearon/pen/YGYmEG?editors=0010)

- 우리는 `ReactDOM.render ()` 를 `<Welcome name = "Sara"/>` Element 와 함께 호출합니다.
- React는 `{name : 'Sara’}` 가 있는 `Welcome Component` 를 Props으로 호출합니다.
- `Welcome Component` 는 결과로 `<h1> Hello, Sara </ h1>`  Element 를 반환합니다.
- React DOM은 `<h1> Hello, Sara </ h1>` 와 일치하도록 DOM을 효율적으로 업데이트합니다.

> 주의할 점은 항상 대문자로 Component 이름을 시작해야 합니다.
> 예를 들어, <div />는 DOM 태그를 나타내지 만 <Welcome />는 Componet 를 나타내며 이 범위에 있어야합니다.

## Composing Components
Component 는 출력에서 다른 Component 를 참조할 수 있습니다.
이를 통해 모든 세부 수준에서 동일한 Component 추상화를 사용할 수 있습니다. Button,  Form, Dialog, Screen : React 앱에서 모든 것은 일반적으로 Component 로 표현됩니다.

예를 들어 Welcome를 여러 번 렌더링하는 App Component 를 만들 수 있습니다.
Ex)
```
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}

function App() {
  return (
    <div>
      <Welcome name="Sara" />
      <Welcome name="Cahal" />
      <Welcome name="Edite" />
    </div>
  );
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
);
```
[Try it on CodePen](http://codepen.io/gaearon/pen/KgQKPr?editors=0010)

일반적으로 새로운 React 앱에는 맨 위에 단일 App Component 가 있습니다.
그러나 React를 기존 앱에 통합하는 경우 Button과 같은 작은 Component 를 사용하여 상향식으로 시작하고 점차적으로 보기 계층의 맨 위로 올라갈 수 있습니다.

> Component 는 단일 루트 Element 를 반환해야 합니다.
> 이것이 <Welcome /> Element 를 모두 포함하도록 <div>를 추가 한 이유입니다.

## Extracting Components
Component 를 더 작은 Component 로 분할하는 것을 두려워하지 마십시오.

예를 들어,이 Comment Component 를 고려하십시오.
Ex)
```
function Comment(props) {
  return (
    <div className="Comment">
      <div className="UserInfo">
        <img className="Avatar"
          src={props.author.avatarUrl}
          alt={props.author.name}
        />
        <div className="UserInfo-name">
          {props.author.name}
        </div>
      </div>
      <div className="Comment-text">
        {props.text}
      </div>
      <div className="Comment-date">
        {formatDate(props.date)}
      </div>
    </div>
  );
}
```
[Hello World in React](http://codepen.io/gaearon/pen/VKQwEo?editors=0010)

저자, 텍스트 및 날짜를 **Props** 으로 받아들이고 소셜 미디어 웹 사이트에 대한 설명을 설명합니다.

이 Component 는 모든 중첩으로 인해 변경하기가 까다로울 수 있으며 개별 부분을 재사용하기도 어렵습니다.
여기에서 몇 가지 Component 를 추출해 봅시다.

먼저, 아바타를 추출합니다.
Ex)
```
function Avatar(props) {
  return (
    <img className="Avatar"
      src={props.user.avatarUrl}
      alt={props.user.name}
    />
  );
}
```

아바타는 코멘트 내에 렌더링되고 있음을 알 필요가 없습니다.
이것이 우리가 그 소품에 더 일반적인 이름을 부여한 이유입니다.

Component 자체의 관점에서 사용되는 컨텍스트가 아닌 Component 의 이름을 지정하는 것이 좋습니다.

우리는 이제 간단한 설명을 단순화 할 수 있습니다
Ex)
```
function Comment(props) {
  return (
    <div className="Comment">
      <div className="UserInfo">
        <Avatar user={props.author} />
        <div className="UserInfo-name">
          {props.author.name}
        </div>
      </div>
      <div className="Comment-text">
        {props.text}
      </div>
      <div className="Comment-date">
        {formatDate(props.date)}
      </div>
    </div>
  );
}
```

다음으로 사용자 이름 옆에 아바타를 렌더링하는 UserInfo Component 를 추출합니다.
Ex)
```
function UserInfo(props) {
  return (
    <div className="UserInfo">
      <Avatar user={props.user} />
      <div className="UserInfo-name">
        {props.user.name}
      </div>
    </div>
  );
}
```

이를 통해 우리는 Comment를 더욱 단순화 할 수 있습니다
Ex)
```
function Comment(props) {
  return (
    <div className="Comment">
      <UserInfo user={props.author} />
      <div className="Comment-text">
        {props.text}
      </div>
      <div className="Comment-date">
        {formatDate(props.date)}
      </div>
    </div>
  );
}
```
[Hello World in React](http://codepen.io/gaearon/pen/rrJNJY?editors=0010)

Component 를 추출하는 것은 처음에는 쓸데없는 일처럼 보일 수 있지만 재사용 가능한 Component  팔레트를 사용하면 더 큰 응용 프로그램에서 비용을 지불하게 됩니다.
엄지 손가락의 좋은 규칙은 UI의 일부가 여러 번 (버튼, 패널, 아바타) 사용되거나 자체적으로 (App, FeedStory, Comment) 충분히 복잡하면 재사용 가능한 Component 가 될 수있는 좋은 후보자입니다.

## Props are Read-Only
Component 를 함수로 선언하든 클래스로 선언하든 관계없이 자체 소품을 수정해서는 안됩니다.
이 합계 함수를 고려하십시오.
Ex)
```
function sum(a, b) {
  return a + b;
}
```

이러한 함수는 입력을 변경하려고 시도하지 않고 항상 동일한 입력에 대해 동일한 결과를 반환하기 때문에 "순수"라고합니다.

대조적으로,이 함수는 자신의 입력을 변경하기 때문에 불순합니다.
Ex)
```
function withdraw(account, amount) {
  account.total -= amount;
}
```

React은 매우 유연하지만 단일 엄격한 규칙이 있습니다.

**모든 React Component 는 Props과 관련하여 순수한 기능처럼 작동해야 합니다.**

물론 응용 프로그램 UI는 동적이며 시간이 지남에 따라 변경됩니다.