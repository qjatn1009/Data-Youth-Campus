import grade as gra

class grade_management:
    def main(self):
        lists = list()
        while True:
            menu = self.print_menu()
            if menu == 1:
                self.input_exam(lists)
            elif menu == 2:
                self.print_exam(lists)
            elif menu == 3:
                print("프로그램을 종료합니다.~~~")
                break
            else:
                print("메뉴를 잘못입력하셨습니다.")

    def input_exam(self, lists):
        print("성적 입력")
        # for i in range(3):
        i = len(lists)
        while True:
            kor = int(input("국어 %d :" % (i +1)))
            if 0  > kor or kor > 100:
                print("성적은 0 ~ 100 사이의 범위로 입력 가능합니다.")
            else:
                break
        while True:
            eng = int(input("영어 %d :" % (i +1)))
            if 0  > eng or eng > 100:
                print("성적은 0 ~ 100 사이의 범위로 입력 가능합니다.")
            else:
                break
        while True:
            math = int(input("수학 %d :" % (i +1)))
            if 0  > math or math > 100:
                print("성적은 0 ~ 100 사이의 범위로 입력 가능합니다.")
            else:
                break

        exam = gra.grade()
        exam.kor = kor
        exam.eng = eng
        exam.math = math
        lists.append(exam)
        print(list)
        print("="*50)

    def print_exam(self, lists):
        print("성적 출력")
        total = 0
        for i in range(len(lists)):
            exam = lists[i]
            total = exam.kor + exam.eng + exam.math

            print("[국어 %d : %3d]" % (i+1, exam.kor), end=" ")
            print("[영어 %d : %3d]" % (i+1, exam.eng), end=" ")
            print("[수학 %d : %3d]" % (i+1, exam.math), end=" ")
        
            avg = total / 3.0
            print("\n총점 : %3d " % total)
            print("평균 : %6.2f " % avg)
            print("="*50)

    def print_menu(self):
        print("성적 관리")
        print("메인메뉴")
        print("1. 성적 입력")
        print("2. 성적 출력")
        print("3. 프로그램 종료")
        menu = int(input())
        return menu

if __name__ == "__main__":
    grade_management = grade_management()
    grade_management.main()