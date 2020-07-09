information = []
current=-1
while True:
    max=3
    if len(information)>=max:
        for i in range(max):
            print("이름 :",information[i]["name"],
                "성별 :", information[i]["gender"],
                "이메일 :", information[i]["Email"],
                "출생년도 :", information[i]["birthday"])
    elif len(information)==0:
        print("현재 데이터가 없습니다.")
    else:
        for i in range(len(information)):
            print("이름 :",information[i]["name"],
                "성별 :", information[i]["gender"],
                "이메일 :", information[i]["Email"],
                "출생년도 :", information[i]["birthday"])

    menu = input("""다음 중 작업하실 메뉴를 입력하세요.
                    I - 고객 정보 입력
                    S - 고객 정보 검색
                    C - 현제 고객 정보 출력
                    P - 이전 고객 정보 출력
                    N - 다음 고객 정보 출력
                    U - 고객 정보 수정
                    D - 고객 정보 삭제
                    A - 전체 고객 정보
                    Q - 프로그램 종료
                    """).upper()
    if menu == "I":
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
        information.append(personal)
        current= len(information)-1
    elif menu == "S":
        sname = input("검색할 이름을 입력하세요.")
        b=0
        for a in range(len(information)):
            if sname in information[a]["name"]:
                print(information[a])
                b+=1
                current = a
                
        if b ==0:
            print("찾으시는 이름이 없습니다.")
    elif menu == "C":
        print("현재 고객 정보 출력")
        if i >=0 :
            print("이름 :",information[i]["name"],
                "성별 :", information[i]["gender"],
                "이메일 :", information[i]["Email"],
                "출생년도 :", information[i]["birthday"])
        else:
            print("입력된 정보가 없습니다.")
    elif menu == "P":
        print("이전 고객 정보 출력")
        if current>0:
            current-=1
            print("이름 :",information[current]["name"],
            "성별 :", information[current]["gender"],
            "이메일 :", information[current]["Email"],
            "출생년도 :", information[current]["birthday"])
        else:
            print("이전 정보가 없습니다.")
        
    elif menu == "N":
        if current<len(information)-1:
            print("이름 :",information[current]["name"],
              "성별 :", information[current]["gender"],
              "이메일 :", information[current]["Email"],
              "출생년도 :", information[current]["birthday"])
        else:
            print("다음 정보가 없습니다.")
    elif menu == "U":
        if 0< current < len(information):
            print(information[current])
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
                information[current]=personal
            print(information[current])   
        else:
            print("현재 고객 정보가 없습니다.")
    elif menu =="A":
        if len(information)==0:
            print("정보가 존재하지않습니다")
        for i in range(len(information)):
            print(information[i])

    elif menu == "D":
        print("정보를 삭제합니다.")
        del information[current]
        if current==0:
            current=0
        else:
            current-=1
    elif menu == "Q":
        print("프로그램을 종료합니다.")
        break