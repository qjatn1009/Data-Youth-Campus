
def cust_print(information, current):
    print("이름 :",information[current]["name"],
            "성별 :", information[current]["gender"],
            "이메일 :", information[current]["Email"],
            "출생년도 :", information[current]["birthday"])

def print_menu():
    menu = input("""다음 중 작업하실 메뉴를 입력하세요.
                I - 고객 정보 입력
                S - 고객 정보 검색
                C - 현재 고객 정보 출력
                P - 이전 고객 정보 출력
                N - 다음 고객 정보 출력
                U - 고객 정보 수정
                D - 고객 정보 삭제
                A - 전체 고객 정보
                Q - 프로그램 종료
                """).upper()
    return menu

def I_I_menu(information, current):
    personal = {"name":"" , "gender":"" , "Email":"" , "birthday":0}
    name = input("이름을 입력하세요 : ")
    while True:
        gender = input("성별을(M/F) 입력하세요 : ").upper()
        if gender=="M" or gender =="F":
            break
    Email = input("이메일을 입력하세요 : ")
    birthday = int(input("출생년도를 입력하세요 : "))
    personal["name"]=name
    personal["gender"]=gender
    personal["Email"]=Email
    personal["birthday"]=birthday
    return personal

def I_menu(information, current): #정보 입력
    personal = I_I_menu(information, current)
    information.append(personal)
    current= len(information)-1
    return current

def u_menu(information, current): #수정
    if 0<= current < len(information):
        cust_print(information, current)
        num = int(input("수정하고 번호를 입력하세요(1 : 이름 2: 성별 3: 이메일 4: 출생년도 5: 전체) :"))
        if num ==1:
            name = input("이름을 입력하세요 : ")
            information[current]["name"] = name
        elif num==2:
            while True:
                gender = input("성별을(M/F) 입력하세요 : ").upper()
                if gender=="M" or gender =="F":
                    break
            information[current]["gender"] = gender
        elif num==3:
            Email = input("이메일을 입력하세요 : ")
            information[current]["Email"] = Email
        elif num==4:
            birthday = int(input("출생년도를 입력하세요 : "))
            information[current]["birthday"] = birthday
        elif num==5:
            personal = I_I_menu(information, current)
            information.insert(current,personal)
        cust_print(information, current)   
    else:
        print("현재 고객 정보가 없습니다.")

def s_menu(information, current): #검색
    sname = input("검색할 이름을 입력하세요.")
    b=0
    for a in range(len(information)):
        if sname in information[a]["name"]:
            cust_print(information, a)
            b+=1
            current = a
            
    if b ==0:
        print("찾으시는 이름이 없습니다.")

    return current

def c_menu(information, current): #현재 고객
    print("현재 고객 정보 출력")
    if current >=0 :
        cust_print(information, current)
    else:
        print("입력된 정보가 없습니다.")

def p_menu(information, current): #이전 고객
    print("이전 고객 정보 출력")
    if current>0:
        current-=1
        cust_print(information, current)
    else:
        print("이전 정보가 없습니다.")
    return current

def n_menu(information, current): #다음 고객
    if current<len(information)-1:
        current +=1
        cust_print(information, current)
    
    else:
        print("다음 정보가 없습니다.")
    
    return current   

def a_menu(information): #전체
    if len(information)==0:
        print("정보가 존재하지않습니다")
    for i in range(len(information)):
        cust_print(information, i)

def d_menu(information, current): #삭제
    print("정보를 삭제합니다.")
    del information[current]
    if current==0:
        current=0
    else:
        current-=1
    return current

def main():
    information = []
    current=-1
    
    while True:

        menu = print_menu()

        if menu == "I":
            
            current = I_menu(information, current)
            
        elif menu == "S":

            current = s_menu(information, current)

        elif menu == "C":
            
            c_menu(information, current)

        elif menu == "P":
            
            current = p_menu(information, current)

        elif menu == "N":
            
            current = n_menu(information, current)

        elif menu == "U":

            u_menu(information, current)
            
        elif menu =="A":
            
            a_menu(information)

        elif menu == "D":

            current = d_menu(information, current)

        elif menu == "Q":
            print("프로그램을 종료합니다.")
            break

if __name__ =="__main__":
    main()