> React 공식문서

# State and Lifecycle
전 챕터에서 다뤘던 내용은 tick 자체를 계속해서 렌더링하는 것이었지만 이번 챕터에서는 그 부분을 State 라는 것을 사용하게끔 해볼 것입니다.

State 는 Props 와 비슷하지만, State는 **Private** 하고 **Component에 의해 완전히 제어됩니다.**
Class 로 정의된 Component 에는 몇 가지 추가 기능이 있습니다.
State는 클래스에 사용할 수 있는 기능입니다.

## Converting a Function to a Class
그렇다면 먼저 함수 로 정의되어 있던 Component 를 Class 로 바꿔줘야 합니다.

다음 5단계로 함수에서 클래스로 변환할 수 있습니다.

- React.Component 를 Extends 하는 동일한 이름의 ES6 Class 를 만듭니다.
- render () 라는 빈 메서드를 추가하십시오.
- 함수 본문을 render () 메서드로 옮깁니다.
- props를 render () 본문의 this.props 로 바꿉니다.
- 나머지 빈 함수 선언을 삭제하십시오.

```
class Clock extends React.Component {
  render() {
    return (
      <div>
        <h1>Hello, world!</h1>
        <h2>It is {this.props.date.toLocaleTimeString()}.</h2>
      </div>
    );
  }
}
```
[Hello World in React](http://codepen.io/gaearon/pen/zKRGpo?editors=0010)

이를 통해 State 및 Lifecycle 와 같은 추가 기능을 사용할 수 있습니다.

## Adding Local State to a Class


## Adding Lifecycle Methods to a Class


## Using State Correctly

### Do Not Modify State Directly

### State Updates May Be Asynchronous

### State Updates are Merged


## The Data Flows Down
