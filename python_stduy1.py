from math import *
from random import *

#String, int, float 예제
animal = "고양이" #String
name = "도베" #String
age = 4 #int
age_f = 4.5 #float
hobby = "낮잠" #String 


print("우리집 "+animal + "의 이름은 " + name + "입니다.\n"\
+ name + "는" + str(age) + "살이며 지금 3월이니 정확히 말하면, "\
+ str(age_f) + "살입니다. " + hobby + "을 아주 좋아합니다.")

#boolean 예제
print(age > 5) #false
print(age < 5) #true

#사칙연산
#number = number*3 == number*=3

#지수연산 **
#몫연산 //
#나머지 연산 %
#비교연산 ==, !=, >, <, >=, <=
#대입연산 =, +=, -=, *=, /=, %=
#논리연산 and, or, not

#탈출문자 \ #줄바꿈 \n #큰/작은따옴표 \" #여러줄쓰기 ""
print("""줄 바꿔서 여러줄을
쓰고 싶을 때는 이렇게 쓰면 될 것 같다\n줄바꿈은
\\n이다.""")

#숫자 처리 함수 abs, pow, sqrt, max, min, round, floor, ceil
print(abs(-7)) #마이너스 없앰
print(pow(4,3)) #4의 3승
print((4**3) == pow(4,3)) #true
print(sqrt(16)) #제곱근 #4
print(max(4,12)) #최댓값
print(min(4,12)) #최솟값
print(round(4.95)) #반올림
print(round(3.141592,2)) #소수점 둘째 자리까지 반올림
print(floor(4.89898)) #내림
print(ceil(5.11)) #올림

#숫자 랜덤 함수
print(random()) #0.0~1.0 미만의 임의값 생성
print(random()*10) #0.0~10.0 미만의 임의값 생성
print(int(random()*10)) #0~10 미만의 임의값 생성
print(randrange(1,45)) #1~46 미만의 임의값 생성

#시퀀스 타입 : 기본 타입(숫자, 문자열)을 여러개 모아서 하나의 자료형으로 관리하기 위한 방법
#튜플(tuple) : 불가변형 타입
#공통 연산자 : in, not in
tup1 = ("일", "이","삼","사","오","육")
print("일" in tup1) #ture
print("이" not in tup1) #false

#슬라이스 : 시퀀스 자료형에서 사용하는 기능. 시퀀스 객체의 일부를 잘라내는 역할이다. 
print(tup1[0:4]) #첫 인자부터 네번째 인덱스 전까지 가져온다
print(tup1[0:7]) #끝 인덱스는 가져오려는 범위에 포함되지 않기 때문에 실제로 가져오려는 인덱스보다 +1 해 주어야 한다
print(tup1[1:1]) #시작 인덱스와 끝 인덱스가 같으면 아무것도 가져오지 않는다
print(tup1[1:2]) #가져오는 인덱스와 잘라내는 인덱스가 차이 있어야 가져온다
print(tup1[3:-1]) #-1은 뒤에서 첫번째 요소를 가리키기 떄문에 실제로 뒤에서 두번째 인덱스(-2)요소인 "오" 까지만 가져온다
print(tup1[1 : 6 : 2]) #인덱스 1에서 5까지 중 증가폭 2로 출력
print(tup1[:: -1]) #reverse

#리스트 : 가장많이 사용하는 자료형이며, 선형 자료구조이다. append, extend, insert, pop, count, sort, revers, clear
subway = ["단대오거리","모란","야탑","서현","죽전"]
print(subway)
print(subway.index("서현")) #인덱스 값 출력

#append와 extend 차이
subway.append("망포")
print(subway)
subway.extend(["영통","수정구청","동탄"]) #한번에 여러객체 추가
print(subway)

subway.insert(3,"우리집") #(index,value)
subway.insert(7,"우리집") #(index,value)
subway.insert(8,"우리집") #(index,value)
print(subway)
print(subway.count("우리집")) #횟수 검색

subway.sort() #정렬
print(subway)
subway.reverse() #역정렬
print(subway)

#삭제 pop:뒤에서부터, del, remove, clear
subway.pop() #맨 뒤 객체 삭제
print(str(subway) + " : 죽전 삭제 - 맨 뒤 객체")
del subway[8] #해당 인덱스 삭제
print(str(subway) + " : 8번째 인자 모란 삭제")
subway.remove("우리집") #삭제하려는 값이 2개 이상 존재한다면 인덱스 순으로 앞쪽 객체가 삭제된다
print(str(subway) + " : 우리집 객체 삭제")
subway.clear() #비우기
print(str(subway) + " : 깔끔하게 클리어")

#list(리스트) : 가변형 타입(자료드르이 값을 바꿀 수 있다) 이는 가변형 타입에서만 사용할 수 있는 연산자가 따로 있기 떄문이다.
#range(레인지) : 범위 내에서 수열을 생성하는 시퀀스 타입. 정수만 가능하며 범위는 시작점~끝점+1이다. 
print(str(list(range(0,21,2)))+" : 0~20까지 index 2씩 증가하며 출력")

#set

#dictionary

#문자열(String)
#문자열 포맷
#방법1 
print("저는 %s살 입니다 " %30) # %s는 숫자, 글자 모두 가능. 콤파가 없다는것에 주의할 것
print("저는 %d살이며, %c씨입니다 " %(30, "우")) #%d는 숫자, %c는 한글자
print("저는 %s을(를) 좋아하며, 역시 %s도 좋아합니다" %("휴가","퇴근"))

#방법2
print("저는 {}를 좋아하며 {}도 좋아합니다".format("클라이밍","휴식"))
print("저는 {1}를 좋아하며 {0}도 좋아합니다".format("클라이밍","휴식")) #순서 바꾸기

#방법3
print("저는 {age}살이며, {artist}의 노래를 즐겨 듣습니다.".format(age=30, artist="Jada Facer"))
age=30
artist="Travis atreo"
print(f"저는 {age}살이며, {artist}의 노래를 즐겨 듣습니다.") #변수를 먼저 생성하고 print()함수 내의 ""앞에 f를 넣는다

#문자열 함수
python = "Python is Amazing"
print(python.upper()) #대문자 변환
print(python.lower()) #소문자 변환
print(python[1].upper()) #0번째 글자만 대문자 변환
print(python) #원본에는 변함이 없다
print(python[0].isupper()) #0번째 글자가 대문자가 맞는지 판단

print(len(python)) #글자 길이 확인
print(python.replace("Python", "Java")) #글자 바꾸기
print(python.replace("A","a"))

#index와 find의 차이 : 비슷하나 없는 값을 산출할 때 find는 -1이라 출력하지만 index는 error를 발생시킨다
index =python.index("n") #시작은 0부터
print(index)
index = python.index("n", index+1) #두번째로 등장하는 해당 글자 위치
print(index)
print(python.find("n")) 
print(python.find("Java"))
print(python.index("Java"))
print(python.count("n"))