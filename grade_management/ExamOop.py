import ExamConsole as ec

class ExamOop:
    def main(self):
        lists = ec.ExamConsole()
        while True:
            menu = lists.print_menu()
            if (menu == 1):
                lists.input_exam()
            elif (menu == 2):
                lists.print_exam()
            elif (menu == 3):
                lists.bey()
                break
            else:
                lists.getMsg()



if __name__ == "__main__":
    exam = ExamOop()
    exam.main()
