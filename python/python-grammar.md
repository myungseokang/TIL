## Python 문법
> Python 3.x 버전 기준

#### 1. Number

```python
# 기본적인 사칙연산
print(5 + 6)  # 11
print(5 - 2)  # 3
print(3 * 8)  # 24
print(3 ** 3) # 27 제곱
print(8 / 2)  # 4.0 float형
print(8 // 2) # 4 int형
print(8 % 3)  # 2 나머지
```
들이 가능합니다.


#### 2. String

```python
test = "Hello World!"
print(test) # Hello World!

test = 'Hello!'
print(test) # Hello!

test = 'I don\'t need Coke!'
print(test) # I don't need Coke!

test = "I don't need Coke!"
print(test) # I don't need Coke!

```
"",'' 로 감싸진 문자열을 string으로 인식합니다.
싱글쿼터 혹은 더블쿼터를 문자열로 사용하려면 앞에 \ 가 들어가야 합니다.
다른 방법으로는 더블쿼터로 문자열을 감싸고 문자열 내에서 싱글쿼터를 사용하는 것입니다.

```python
test = r'C:\Nature'
print(test) # C:\Nature
```
r'' 로 문자열을 감싸주게 되면 raw라는 뜻으로 아무 의미없는 문자열이라는 것을 나타내줍니다.

```python
first = 'Myungseo'
last = 'Kang'

print(first + last) # Myungseo Kang
print(last * 5) # KangKangKangKangKang
```
+ 기호를 이용해서 문자열을 합치는 것이 가능합니다.
또한 * 기호를 이용해서 문자열을 반복하는 것이 가능합니다.


#### 3. Slicing String

```python
test_str = 'Leopold'

print(test_str[0])   # L
print(test_str[1])   # e
print(test_str[-1])  # d
print(test_str[-2])  # l
```
List의 인덱스 부분에 음수를 넣어서 오른쪽부터 가져올 수 있습니다.

주의할 점은 음수로 인덱싱할 경우에는 0부터 시작이 아니라 1부터 시작합니다.
```python
print(test_str[2:5]) # opo
print(test_str[3:6]) # pol
print(test_str[:5])  # Leopo
print(test_str[3:])  # pold
```
이렇게 범위를 인덱스로 지정해서 호출하는 것도 가능합니다.

주의할 점은 콜론 앞의 숫자는 포함되지만 뒤의 숫자는 포함되지 않습니다.

시작지점을 지정하지 않으면 처음부터 콜론 뒷 부분 숫자의 인덱스까지 출력하고,

끝지점을 지정하지 않으면 콜론 앞 부분 숫자부터 끝까지 출력합니다.


#### 4. if, elif, else

```python
name = 'Leopold'

if name is 'Myungseo':
    print('Hello Myungseo')
elif name is 'Kang':
    print('Hello Kang!')
else:
    print('Hello Everyone!')
```
python의 조건문은 이런식으로 구성되어 있습니다.
```python
if 조건문:
    코드
elif 조건문2:
    코드
else:
    코드
```
이런 식으로 구성되어 있습니다.

특이한 점이 있다면 C언어처럼 else if를 쓰는 것이 아니라,
elif를 쓴다는 것입니다.


#### 5. List
리스트는 배열이라고 생각하면 편합니다.

```python
a = [] # a = list()와 동일
b = [1, 3, 5]
c = ['Leopold', 'Myungseo', 'Kang', 'L3opold7']
d = [7, 9, ['Myungseo', 'L3opold7']]
```
리스트 안에는 여러가지 자료형을 담을 수 있습니다.

List에도 Slicing String에서 말한 것들을 적용할 수 있습니다.
```python
print(b[-1]) # 5
print(c[-2]) # Kang
print(d[-1][0]) # Myungseo
```
이중 리스트에서 인덱싱은 다음과 같이 할 수 있습니다.

```python
# 리스트 값 수정
test = [1, 2, 3, 4, 5]
test[3] = 6

print(test) # [1, 2, 3, 6, 5]
```
이렇게 인덱스를 지정해서 직접 값을 바꿔줄 수 있습니다.

```python
# 리스트 연속된 값으로 변경
test = [1, 2, 3, 4, 5]
test[2:3] = ['a', 'b', 'c']

print(test) # [1, 2, 'a', 'b', 'c', '4', '5']
```
2이상 3미만의 인덱스 부분에 a,b,c 리스트를 변경해주는 것입니다.

```python
# 리스트 요소 삭제
test = ['a', 'b', 'c', 'd', 'e']
test[2:4] = []

print(test) # ['a', 'b', 'e']
# del 함수 사용
test = ['a', 'b', 'c', 'd', 'e']
del test[2]

print(test) # ['a', 'b', 'd', 'e']
```
del 함수를 사용해서 삭제할 수도 있습니다.

```python
test = ['a', 'b', 'c', 'd', 'e']
del test[2:4]

print(test) # ['a', 'b', 'e']
```
마찬가지로 인덱스를 범위로 지정하는 것 또한 가능합니다.


**List 내장 함수들!**

```python
test = [1, 2]
test.append(3) # 맨 뒤에 값 추가
print(test) # [1, 2, 3]
```
append(x) 함수는 인자를 1개밖에 받지 않기 때문에 여러개의 인자를 넘겨줄 경우 에러가 납니다.

```python
test = [3, 1, 2, 5, 4]
test.sort()
print(test) # [1, 2, 3, 4, 5]

test.sort(reverse=True)
print(test) # [5, 4, 3, 2, 1]
```
sort() 함수는 리스트를 자동으로 정렬해줍니다.
역순으로 정렬하기 위해서는 sort 함수에 reverse 옵션을 True로 설정해주면 됩니다.

```python
test = [3, 1, 2]
test.reverse()
print(test) # [2, 1, 3]
```
reverse() 함수는 현재의 리스트를 역순으로 뒤집어 줍니다.
정렬은 하지 않고 현재의 리스트를 역순으로 뒤집어 줍니다.

```python
test = [1, 2, 3, 4, 5]
print(test.index(3)) # 2
print(test.index(5)) # 4
```
index(x) 함수는 x 라는 값이 있는 경우 , x 의 인덱스를 반환해주는 함수입니다.

```python
test = [1, 2, 3, 4, 5]
test.insert(0, 6)
print(test) # [6, 1, 2, 3, 4, 5]
```
insert(x, y) 함수는 x 위치에 y 라는 값을 삽입해주는 함수입니다.

```python
test = [1, 2, 3, 4, 3]
test.remove(3)
print(test) # [1, 2, 4, 3]
```
remove(x) 함수는 첫 번째로 나오는 x 라는 값을 리스트에서 삭제해주는 함수입니다.
보시다시피 뒷부분에 있는 3은 삭제되지 않았습니다.

```python
test = [1, 2, 3]
print(test.pop()) # 3
print(test) # [1, 2]
```
pop() 함수는 리스트의 가장 마지막 인덱스의 값을 반환해주고 그 값을 삭제해주는 함수입니다.
위의 예제에서 굳이 3이라는 값이 필요없을 경우에는 print() 함수를 빼도 상관없습니다.

```python
test = [1, 2, 3, 1, 1]
print(test.count(1)) # 3
```
count(x) 함수는 x 라는 값이 리스트 안에 몇 개나 있는지 반환해주는 함수입니다.

```python
test = [1, 2, 3]
test.extend([4, 5, 6])
print(test) # [1, 2, 3, 4, 5, 6]
```
extend(x) 함수는 x 부분에 리스트를 받아서 원래의 리스트와 병합시켜주는 함수입니다.

리스트에서는 위와 같은 내장 함수들을 사용할 수 있습니다.


#### 6. Tuple
튜플은 조금 특이한 리스트라고 해도 무방할 정도로 리스트와 성격이 비슷합니다.

리스트에 대한 설명은 위에서 자세하게 했으므로 튜플과의 차이점을 간단하게 언급하고자 합니다.

리스트는 [] 대괄호로 묶이지만 튜플은 () 소괄호로 묶입니다.
```python
tp1 = ()
tp2 = (1,)
tp3 = (1, 2, 3, 4, 5)
tp4 = (1, 2, (3, 4, 5))
tp5 = 1, 2, 3
```
튜플의 선언은 다음과 같이 할 수 있습니다.
리스트와 거의 비슷하지만 다른 점이 조금 있습니다.
1개의 요소만을 가질때 튜플은 tp2 와 같이 뒤에 반드시 콤마(,) 가 와야합니다.
또한 tp5 처럼 괄호를 생략해도 된다는 점입니다.

튜플과 리스트의 차이점은 이뿐만이 아닙니다.
튜플과 리스트의 가장 큰 차이점은 **튜플은 값을 변경할 수 없다** 입니다.
리스트는 항시 값의 변화가 가능하지만 튜플은 불가능합니다.
그래서 **값의 변화를 원하지 않는 리스트의 경우에는 튜플로 선언하는 것이 바람직** 합니다.

간단하게 리스트와 비슷한 점도 짚고 넘어가겠습니다.

튜플은 인덱싱, 슬라이싱, 병합, 반복 모두 가능합니다.
```python
tp1 = (1, 2, 3)
tp2 = (4, 5, 6)

print(tp1[2]) # 3
print(tp1[1:]) # (2, 3)
print(tp1 + tp2) # (1, 2, 3, 4, 5, 6)
print(tp2 * 2) # (4, 5, 6, 4, 5, 6)
```


#### 7. Dictionary



#### 8. for, for in, while
```python

```


#### 9. Function



#### 10. Lambda



#### 11. File I/O
