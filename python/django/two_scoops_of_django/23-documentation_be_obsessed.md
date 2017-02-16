23장. 문서화에 집착하자
=====

# Index
- [파이썬 문서에 rst 이용하기](#파이썬-문서에-rst-이용하기)
- [rst로부터 스핑크스를 이용하여 문서 생성하기](#rst로부터-스핑크스를-이용하여-문서-생성하기)
- [어떤 문서들을 작성해야 하는가](#어떤-문서들을-작성해야-하는가)
- [문서화에 대한 자료](#문서화에-대한-자료)
- [Markdown](#markdown)
- [위키와 다른 문서화 방법들](#위키와-다른-문서화-방법들)

## 파이썬 문서에 rst 이용하기

최근 경향을 보면 reStructuredText를 이용해서 문서 작성을 많이 하는 것 같다라고 말하고 있다(~~나는 이 글을 작성할 때 Markdown을 사용했...~~)
핵심 명령을 간추려보겠다.

```rst
각 섹션의 헤더
============

**강조(Bold)**

*이탤릭(italic)*

기본 링크: https://djangoproject.com
구문에 링크 달기: 'Django DOCUMENTATION'_

.. _Django DOCUMENTATION: https://djangoproject.com

서브 섹션의 헤더
-------------

#) 번호를 가진 리스트 아이템

#) 두 번째 아이템

* 첫 번째 목록 기호

* 두 번째 목록 기호

  * 들여 쓴 목록 기호

  * 들여 쓴 상태에서 줄 바꾸기


코드 블록::
    def like():
        print('I like it!')

    def i in range(10):
        like()

파이썬 코드 블록(highlighting을 위해서는 pygments가 필요):

code-block:: python
    # pip install pygments

    for i in range(10):
        print(i)

자바스크립트 코드 블록(highlighting):

code-block:: javascript
    console.log("Don't use alert().");
```

## rst로부터 스핑크스를 이용하여 문서 생성하기

**Sphinx**는 .rst 파일을 보기 좋게 꾸며진 문서로 변환해 주는 도구다.
**주기적**으로 스핑크스 문서를 빌드하는 것이 좋다.

## 어떤 문서들을 작성해야 하는가

개발 문서: 프로젝트를 셋업하고 관리하는 데 필요한 설명과 가이드라인
개발 문서에 들어가는 것들
- 설치
- 개발
- 아키텍쳐 노트
- 테스트 케이스를 실행하는 방법
- 코드의 PR 요청 방법 등등

**꼭 필요하다고 생각되는 문서들**
- README.rst
- docs/
- docs/deployment.rst
- docs/installation.rst
- docs/architecture.rst

## 문서화에 대한 자료

- [독스트링에 대한 공식 스펙 문서](http://www.python.org/dev/peps/pep-0257)
- [스핑크스 문서를 무료로 호스팅해 주는 서비스](https://readthedocs.org/)
- [문서를 호스팅해 주는 또 다른 무료 서비스](https://pythonhosted.org/)

## Markdown

**마크다운(Markdown)** 은 reStructuredText 와 크게 다르지 않은 텍스트 포맷 문법이다.
reStructuredText와 같은 내장 기능은 없지만 배우기 쉽다는 장점이 있다.
Python Package Index는 rst를 제외한 다른 포맷의 문서에선 `long_description`을 지원하지 않는다.

**Pandoc(팬독)**은 한 마크업 언어를 다른 마크업 언어로 변환해주는 도구이다.

## 위키와 다른 문서화 방법들

어떤 이유에서 문서를 프로젝트 안에 위치시킬 수 없을 경우에는 다른 방법을 써서라도 문서를 제공해야 한다.
위키나 온라인에 문서를 저장하는 방식 또는 VCS를 이용할 수 없는 워드 프로세스 문서 형식이라도 문서가 없는 것 보다는 낫다.


여기까지가 책의 내용인데 개인적으로도 이 책의 내용과 생각이 비슷하다.
한 가지 다른 점을 꼽자면 나는 rst를 사용하지 않고 md를 사용하는 것 정도를 꼽을 수 있다.
이제부터는 rst도 써봐야겠다.(물론 저자가 md를 까는건 별로 좋지 않다고 생각한다.)

감사합니다 :D
