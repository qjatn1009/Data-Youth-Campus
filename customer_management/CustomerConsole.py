import customerList as cl
import Customer as cust
import os
import pickle
import sqlalchemy as db
from sqlalchemy.sql import text
import cx_Oracle



class CustomerConsole:
    def __init__(self):
        self.__list = cl.customerList()

    def cust_print(self): #정보 출력
        print("이름 :",self.__list.get_list()[self.__list.get_current()].get_name(),
                "성별 :", self.__list.get_list()[self.__list.get_current()].get_gender(),
                "이메일 :", self.__list.get_list()[self.__list.get_current()].get_email(),
                "출생년도 :", self.__list.get_list()[self.__list.get_current()].get_birthday())

    def print_menu(self): # 메뉴 출력
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
    
    def input_info(self): #정보 입력
        
        personal = self.all_modify()
        self.__list.add(personal, -1)     

    def modify_cust(self): #수정
        if 0<= self.__list.get_current() < len(self.__list.get_list()):
            self.cust_print()
            num = int(input("수정하고 번호를 입력하세요(1 : 이름 2: 성별 3: 이메일 4: 출생년도 5: 전체) :"))
            if num ==1:
                name = input("이름을 입력하세요 : ")
                self.__list.get_list()[self.__list.get_current()].set_name(name)
            elif num==2:
                while True:
                    gender = input("성별을(M/F) 입력하세요 : ").upper()
                    if gender=="M" or gender =="F":
                        break
                self.__list.get_list()[self.__list.get_current()].set_gender(gender)
            elif num==3:
                Email = input("이메일을 입력하세요 : ")
                self.__list.get_list()[self.__list.get_current()].set_email(Email)
            elif num==4:
                while True:
                    birthday = input("출생년도를 입력하세요 : ")
                    if birthday.isdigit():
                        break
                self.__list.get_list()[self.__list.get_current()].set_birthday(birthday)
            elif num==5:
                personal = self.all_modify()
                self.__list.insert(personal)
            self.cust_print()   
        else:
            print("현재 고객 정보가 없습니다.")

    def all_modify(self): #정보 전체 
        
        name = input("이름을 입력하세요 : ")
        while True:
            gender = input("성별을(M/F) 입력하세요 : ").upper()
            if gender=="M" or gender =="F":
                break
        Email = input("이메일을 입력하세요 : ")
        while True:
            birthday = input("출생년도를 입력하세요 : ")
            if birthday.isdigit():
                break
        customer = cust.Customer()
        customer.set_name(name)
        customer.set_gender(gender)
        customer.set_email(Email)
        customer.set_birthday(birthday)
        return customer

    def search_cust(self): #검색
        sname = input("검색할 이름을 입력하세요.")
        b=0
        for a in range(len(self.__list.get_list())):
            if sname in self.__list.get_list()[a].get_name():
                self.cust_print()
                b+=1
                current = a
                
        if b ==0:
            print("찾으시는 이름이 없습니다.")

        return current

    def current_cust(self): #현재 고객
        print("현재 고객 정보 출력")
        if self.__list.get_current() >=0 :
            self.cust_print()
        else:
            print("입력된 정보가 없습니다.")

    def previous_cust(self): #이전 고객
        print("이전 고객 정보 출력")
        if self.__list.get_current()>0:
            self.__list.set_current(self.__list.get_current()-1)
            self.cust_print()
        else:
            print("이전 정보가 없습니다.")
        
    def next_cust(self): #다음 고객
        if self.__list.get_current()<len(self.__list.get_list())-1:
            self.__list.set_current(self.__list.get_current()+1)
            self.cust_print()
        
        else:
            print("다음 정보가 없습니다.")

    def all_cust(self): #전체
        if len(self.__list.get_list())==0:
            print("정보가 존재하지않습니다")
        else:
            for i in range(len(self.__list.get_list())):
                self.__list.set_current(i)
                self.cust_print()
                 
    def delete_cust(self): #삭제
        print("정보를 삭제합니다.")
        self.__list.pop_list(self.__list.get_current())
        if self.__list.get_current()==0:
            self.__list.set_current(0)
        else:
            self.__list.set_current(self.__list.get_current()-1)
    
    def end(self):
        print("프로그램을 종료합니다.")
        
    def saveData(self):# 정보 저장
        with open('./data/cust_data.pkl', 'wb') as f:
            print(self.__list.get_list())
            pickle.dump(self.__list.get_list(), f)
            print("정상적으로 저장되었습니다.")

    def loadData(self): # 정보 불러오기
        engine = db.create_engine("oracle://hr:hr@oraxe11g/xe")
        with engine.connect() as connection:
            result = connection.execute("select * from cust")
            cust_list = [dic(row) for row in result]
            self.__list.set_list(cust_list)
    
    def saveData(self): # 정보 저장
        engine = db.create_engine("oracle://hr:hr@oraxe11g/xe")
        with engine.connect() as connection:
            