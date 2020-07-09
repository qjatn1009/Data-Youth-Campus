
def main():
    kors = list()
    while True:
        menu = print_menu()
        if menu == 1:
            input_exam(kors)
        elif menu == 2:
            print_exam(kors)
        elif menu == 3:
            print("프로그램을 종료합니다.~~~")
            break
        else:
            print("메뉴를 잘못입력하셨습니다.")

def input_exam(kors):
    print("성적 입력")
    for i in range(3):
        while True:
            kor = int(input("국어 %d :" % (i +1)))
            if 0  > kor or kor > 100:
                print("성적은 0 ~ 100 사이의 범위로 입력 가능합니다.")
            else:
                # kors.append(kor)
                kors.insert(i,kor)
                break
    print("="*50)

def print_exam(kors):
    print("성적 출력")
    total = 0
    for i in range(3):
        print("[국어 %d : %3d]" % (i+1, kors[i]), end=" ")
        total = total + kors[i]
    avg = total / 3.0
    print("\n총점 : %3d " % total)
    print("평균 : %6.2f " % avg)
    print("="*50)

def print_menu():
    print("성적 관리")
    print("메인메뉴")
    print("1. 성적 입력")
    print("2. 성적 출력")
    print("3. 프로그램 종료")
    menu = int(input())
    return menu


if __name__ == "__main__":
    main()