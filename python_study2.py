a = "Life is"
b = 42
print(a + str(b) + " ! ")
print(a,b," ! ") #콤마로 구분 시 형변환이 불필요하다.

#매핑형 타입
#해시 자료구조라고 함
#Key값으로 불러오는 dict가 대표적
#tuple, list는 시퀀스 타입. 순서가 존재. 자료를 삽입/삭제/수정하는 방식으로 동작

#Dictionary
#형태 {key:value,key:value,key:value...}
#튜플이나 리스트와는 다르게 key를 직접 정의할 수 있다.(인덱스가 자동으로 생성되지 않음)
cabinet = {"A-3":"유재석","B-3":"박명수"} 
print(cabinet)
print(cabinet.get("A-3"))
print("A-3" in cabinet)
print(cabinet.get("A-1")) #없는 값 호출 시 none
print(cabinet.get("A-1","없는 값")) #없는 값 호출 시 none이 아닌 대체 안내 설정

cabinet["A-3"] = "정준하" #이미 존재하는 키면 수정 가능. 키 값은 중복될 수 없다
cabinet["A-4"] = "정준하" #이미 존재하는 value값은 중복될 수 있다
cabinet["B-4"] = "정형돈" #없는 키면 추가한다
print(cabinet)
del cabinet["B-3"] #del과 함께 삭제하고자 하는 키를 적으면 해당 키와 value가 삭제된다
print(cabinet)
print(cabinet.keys())
print(cabinet.values())
print(cabinet.items()) #튜플로 표현된다

#Set(집합){value}
#순서가 없는 자료형이다. 자동정렬된다
#중복이 안된다는 특징을 가지고 있다.
my_set = {3,1,2,5,4}
print(my_set)
frontier = {"유재석", "박명수", "정준하", "정형돈"}
tvshow = set(["유재석","하동훈"])
print(frontier & tvshow) #교집합
print(frontier.intersection(tvshow)) #교집합

print(frontier | tvshow) #합집합
print(frontier.union(tvshow)) #합집합

print(frontier - tvshow) #차집합
print(frontier.difference(tvshow)) #차집합

frontier.add("하동훈")
print(frontier)
frontier.remove("유재석")
print(frontier)

tvshow.add("노홍철")
print(tvshow)
tvshow.remove("하동훈")
print(tvshow)