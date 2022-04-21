"""
===== 문자열 자료형 =====
"""

print("=" * 50)
print("Training_2. StringType")

# 파이썬 문자열 표현방식
s1 = "Hello"
s2 = 'Hello'
s3 = """
    H
    e
    l
    l
    o
    """
s4 = '''
    H
    e
    l
    l
    o
    '''

print(s1)
print(s2)
print(s3)
print(s4)

# s1은 작은따옴표(')를 문자열로 넣을 수 있음.
# s2는 큰따옴표(")를 문자열로 넣을 수 있음.
# s3는 s1과 똑같지만 여러줄을 한번에 문자열로 넣을 수 있음.
# s4는 s2와 똑같지만 여러줄을 한번에 문자열로 넣을 수 있음.
# 이스케이프(\) 문자를 사용해서 따옴표를 표시가능함.

# 파이썬 문자열 연산
a1 = "python"
a2 = " is fun!"

# 문자열을 더하면 python is fun이 나옴
print(a1 + a2)
# 문자열을 3번 곱하면 똑같은 문자열 3번이 나옴
print(a1 * 3)


# 문자열 길이 구하는 함수 len
print(len(a1))

# 문자열 인덱싱, c++의 문자열 배열처럼 첨자연산자([])로 인덱싱 가능, 파이썬도 숫자를 0부터 센다.
print(a1[4])
# 인덱스 번호에 -가 붙으면 뒤에서부터 인덱싱을 하게 된다. 즉, 원래 배열의 마지막 요소가 -1이 된다.
print(a1[-1])

# 문자열 슬라이싱, (:)을 기준으로 왼쪽이 시작인덱스, 오른쪽이 끝인덱스이며 이 인덱스에 포함된 문자열을 잘라 값을 리턴한다.
# 이 구문의 경우에는 0 <= index < 3 에 포함된 인덱스들만 출력한다.
print(a1[0:3])
# 끝 인덱스를 비워놓으면 시작 인덱스를 기준으로 끝 요소까지 자른다.
print(a1[1:])
# 시작 인덱스를 비워놓으면 처음요소부터 끝 인덱스까지 자른다.
print(a1[:4])
# 마찬가지로 슬라이싱에서도 -를 쓸수 있다.
print(a1[3:-1])

# 문자열 formatting, c++이랑 똑같은 구분자 사용
# 하나만 대입
fs1 = "I Learning %s." % a1
# 여러 개 대입
fs2 = "%s%s" % (a1, a2)

print(fs1)
print(fs2)

# 문자열 정렬
# 전체 길이가 16인 문자열에서 오른쪽 정렬, 나머지는 공백으로 채움
fs3 = "%16s" % a1
# 전체 길이가 16인 문자열에서 왼쪽 정렬, 나머지는 공백으로 채움
fs4 = "%-16s %s" % (a1, a2) 

print(fs3)
print(fs4)

print("=" * 50)