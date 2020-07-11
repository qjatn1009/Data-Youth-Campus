def cust_print(information, current): #정보 출력
    print("이름 :",information[current].name,
            "성별 :", information[current].gender,
            "이메일 :", information[current].email,
            "출생년도 :", information[current].birthday)

def print_menu(): # 메뉴 출력
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