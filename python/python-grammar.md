## Python 문법
> Python 3.x 버전 기준

#### 1. Number
```python
# 기본적인 사칙연산
print(5+6)  # 11
print(5-2)  # 3
print(3*8)  # 24
print(3**3) # 27 제곱
print(8/2)  # 4.0 float형
print(8//2) # 4 int형
print(8%3)  # 2 나머지
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
print(test)
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

#### 5, for, for in, while

#### 6. List

#### 7. Dictionary

#### 8. Function

#### 9. Lambda

#### 10. File I/O
