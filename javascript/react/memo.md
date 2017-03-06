> 간단하게 이것저것 메모하는 곳

1. Refs 가 안티패턴인가?
> 관련 페이스북 [게시물 링크](https://www.facebook.com/groups/react.ko/permalink/1809224009337763/)

- Refs 의 경우 [이러한 경우](https://facebook.github.io/react/docs/refs-and-the-dom.html#when-to-use-refs) 를 제외하고는 쓰지 말자.

- string ref가 legacy api라 callback기반 api를 사용하라는 eslint [룰](https://github.com/.../master/docs/rules/no-string-refs.md) 이 있다.

- string ref 기준으론 정적 분석하기 어렵다는 점과 callback 형태의 api가 string ref의 사용예를 모두 커버한다는 점에서 안바꿀 이유가 없다!! 라고 한다.

- 기본적으로 리액트는 스테이트가 바뀌면서 내부적인 diffing을 통해 실제 바뀐 부분만 DOM에 렌더링이 되는데, ref를 통해 DOM에 직접 접근해서 수정하게 되면 의도하지 않은 결과가 나올 수도 있습니다. 기존 코드베이스에서 마이그레이션 하거나 Dimension 구하는 경우가 아니면 사실 쓸 일이 거의 없다.