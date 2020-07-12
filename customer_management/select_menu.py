from print_info import cust_print
from modify_info import all_modify

def input_info(information, current): #정보 입력
    
    personal = all_modify()
    information.append(personal)
    current= len(information)-1
    return current

def modify_cust(information, current): #수정
    if 0<= current < len(information):
        cust_print(information, current)
        num = int(input("수정하고 번호를 입력하세요(1 : 이름 2: 성별 3: 이메일 4: 출생년도 5: 전체) :"))
        if num ==1:
            name = input("이름을 입력하세요 : ")
            information[current].name = name
        elif num==2:
            while True:
                gender = input("성별을(M/F) 입력하세요 : ").upper()
                if gender=="M" or gender =="F":
                    break
            information[current].gender = gender
        elif num==3:
            Email = input("이메일을 입력하세요 : ")
            information[current].email = Email
        elif num==4:
            birthday = int(input("출생년도를 입력하세요 : "))
            information[current].birthday = birthday
        elif num==5:
            personal = all_modify()
            information.insert(current,personal)
        cust_print(information, current)   
    else:
        print("현재 고객 정보가 없습니다.")

def search_cust(information, current): #검색
    sname = input("검색할 이름을 입력하세요.")
    b=0
    for a in range(len(information)):
        if sname in information[a].name:
            cust_print(information, a)
            b+=1
            current = a
            
    if b ==0:
        print("찾으시는 이름이 없습니다.")

    return current

def current_cust(information, current): #현재 고객
    print("현재 고객 정보 출력")
    if current >=0 :
        cust_print(information, current)
    else:
        print("입력된 정보가 없습니다.")

def previous_cust(information, current): #이전 고객
    print("이전 고객 정보 출력")
    if current>0:
        current-=1
        cust_print(information, current)
    else:
        print("이전 정보가 없습니다.")
    return current

def next_cust(information, current): #다음 고객
    if current<len(information)-1:
        current +=1
        cust_print(information, current)
    
    else:
        print("다음 정보가 없습니다.")
    
    return current   

def all_cust(information): #전체
    if len(information)==0:
        print("정보가 존재하지않습니다")
    else:
        for i in range(len(information)):
            cust_print(information, i)

def delete_cust(information, current): #삭제
    print("정보를 삭제합니다.")
    del information[current]
    if current==0:
        current=0
    else:
        current-=1
    return current

