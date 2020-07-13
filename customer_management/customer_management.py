import CustomerConsole as cc
import customerList as cl

class customer_mangement:
       

    def main(self):
        lists = cc.CustomerConsole()
        lists.loadData()
        while True:

            menu = lists.print_menu()

            if menu == "I":
                
                lists.input_info()
                
            elif menu == "S":

                lists.search_cust()

            elif menu == "C":
                
                lists.current_cust()

            elif menu == "P":
                
                lists.previous_cust()

            elif menu == "N":
                
                lists.next_cust()

            elif menu == "U":

                lists.modify_cust()
                
            elif menu =="A":
                
                lists.all_cust()

            elif menu == "D":

                lists.delete_cust()

            elif menu == "Q":
                lists.end()
                lists.saveData()
                break

if __name__ =="__main__":
    customer = customer_mangement()
    customer.main()