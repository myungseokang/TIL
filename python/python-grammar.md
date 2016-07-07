## Python 문법

#### 1. Number

#### 2. String

#### 3. Slicing String

```
test_str = 'Leopold'
print(test_str[0])   # L
print(test_str[1])   # e
print(test_str[-1])  # d
print(test_str[-2])  # l
```
List의 인덱스 부분에 음수를 넣어서 오른쪽부터 가져올 수 있습니다.

주의할 점은 음수로 인덱싱할 경우에는 0부터 시작이 아니라 1부터 시작합니다.
```
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
