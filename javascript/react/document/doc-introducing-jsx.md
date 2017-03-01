> React 공식문서

# Introducing JSX
JSX 는 JavaScript의 확장성 문법이고 React에서 사용하는 걸 추천합니다.

JSX는 템플릿 문법 같이 보이지만 JavaScript 의 모든 기능을 제공합니다.

JSX로 React Elements 를 생성할 수 있습니다. 그리고 이것을 React DOM 에 렌더링합니다.

## Embedding Expressions in JSX

어떤 JavaScript 표현식이라도 중괄호(curly braces) 로 감싸서 사용할 수 있습니다.

Ex)
```
function formatName(user) {
  return user.firstName + ' ' + user.lastName;
}

const user = {
  firstName: 'Harper',
  lastName: 'Perez'
};

const element = (
  <h1>
    Hello, {formatName(user)}!
  </h1>
);

ReactDOM.render(
  element,
  document.getElementById('root')
);
```
[A Pen by  Dan Abramov](http://codepen.io/gaearon/pen/PGEjdG?editors=0010)

## JSX is an Expression Too
또한 JSX는 컴파일이 완료되면 일반 JavaScript가 됩니다.

즉, if 문과 for 문에서 JSX를 사용할 수 있고, 변수에 할당하고, 인수로 받아 함수에서 반환 할 수 있습니다.

```
function getGreeting(user) {
  if (user) {
    return <h1>Hello, {formatName(user)}!</h1>;
  }
  return <h1>Hello, Stranger.</h1>;
}
```

## Specifying Attributes with JSX
그리고 JSX를 이용해서 **특별한 속성** 을 지정해줄 수도 있습니다.

따옴표를 이용해서 문자열을 표현할 수 있습니다.
Ex)
```
const element = <div tabIndex="0"></div>;
```

중괄호를 이용해서 JavsScript 표현식을 나타낼 수도 있습니다.
Ex)
```
const element = <img src={user.avatarUrl}></img>;
```

중괄호를 사용하여 JavaScript 표현식을 사용할 때, 따옴표로 중괄호를 감싸면 안됩니다.
이렇게 될 경우 중괄호랑 그 표현식을 문자열로 인식하기 때문입니다.

## Specifying Children with JSX
JSX 태그 안에도 내용을 넣을 수 있습니다.
Ex)
```
const element = (
  <div>
    <h1>Hello!</h1>
    <h2>Good to see you here.</h2>
  </div>
);
```

> 다만 주의할 점은 JSX는 HTML보다 JavaScript에 더 가깝기 때문에 속성 이름을 적을 때 camelCase로 적어야 합니다.
> Ex) className, tabIndex 등등

## JSX Prevents Injection Attacks
사용자에게 입력받은 값을 JSX에 포함시켜서 렌더링해도 안전합니다.
기본적으로 React DOM은 렌더링하기 전에 JSX에 삽입된 모든 값을 이스케이프 처리합니다.
따라서 응용 프로그램에 명시적으로 작성되지 않은 것을 삽입할 수 없습니다.
모든 것은 렌더링되기 전에 문자열로 변환됩니다.
이렇게 하면 XSS(Cross Site Scripting) 공격을 방지 할 수 있습니다.

Ex)
```
const title = response.potentiallyMaliciousInput;
// This is safe:
const element = <h1>{title}</h1>;
```

## JSX Represents Objects
Babel은 아래의 JSX를 React.createElement () 호출로 컴파일 합니다.
아래의 두 개의 코드는 동일합니다
Ex)
```
const element = (
  <h1 className="greeting">
    Hello, world!
  </h1>
);
```

```
const element = React.createElement(
  'h1',
  {className: 'greeting'},
  'Hello, world!'
);
```

React.createElement ()는 버그없는 코드를 작성하는 데 도움이 되는 몇 가지 검사를 수행하지만 기본적으로 다음과 같은 객체를 만듭니다.

```
// Note: this structure is simplified
const element = {
  type: 'h1',
  props: {
    className: 'greeting',
    children: 'Hello, world'
  }
};
```

이러한 객체를 “React Elements” 라고 합니다.
React는 이러한 객체를 읽고, 이를 사용하여 DOM을 구성하고 최신 상태로 유지합니다.