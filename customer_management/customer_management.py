from module.select_menu import input_info
from module.select_menu import modify_cust
from module.select_menu import search_cust
from module.select_menu import current_cust
from module.select_menu import previous_cust
from module.select_menu import next_cust
from module.select_menu import all_cust
from module.select_menu import delete_cust
from module.print_info import print_menu
from module.cust_data import saveData
from module.cust_data import loadData

def main():
    information = []
    current, information=loadData(information)
    while True:

        menu = print_menu()

        if menu == "I":
            
            current = input_info(information, current)
            
        elif menu == "S":

            current = search_cust(information, current)

        elif menu == "C":
            
            current_cust(information, current)

        elif menu == "P":
            
            current = previous_cust(information, current)

        elif menu == "N":
            
            current = next_cust(information, current)

        elif menu == "U":

            modify_cust(information, current)
            
        elif menu =="A":
            
            all_cust(information)

        elif menu == "D":

            current = delete_cust(information, current)

        elif menu == "Q":
            print("프로그램을 종료합니다.")
            saveData(information)
            break

if __name__ =="__main__":
    main()
