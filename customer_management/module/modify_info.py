import module.Customer as cust

def all_modify(): #정보 전체 수정
    # personal = {"name":"" , "gender":"" , "Email":"" , "birthday":0}
    customer = cust.Customer()
    name = input("이름을 입력하세요 : ")
    while True:
        gender = input("성별을(M/F) 입력하세요 : ").upper()
        if gender=="M" or gender =="F":
            break
    Email = input("이메일을 입력하세요 : ")
    birthday = int(input("출생년도를 입력하세요 : "))
    customer.name = name
    customer.gender = gender
    customer.email = Email
    customer.birthday = birthday
    
    # personal["name"]=name
    # personal["gender"]=gender
    # personal["Email"]=Email
    # personal["birthday"]=birthday
    return customer
print("1")