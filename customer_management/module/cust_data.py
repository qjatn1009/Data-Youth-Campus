import os
import pickle

def saveData(information):# 정보 저장
    with open('./data/cust_data.pkl', 'wb') as f:
        pickle.dump(information, f)
        print("정상적으로 저장되었습니다.")

def loadData(information):# 정보 불러오기
    if os.path.exists("./data/cust_data.pkl") :
        with open('./data/cust_data.pkl', 'rb') as f:
            information = pickle.load(f)
            if len(information)!=0:
                page = len(information)-1
            else:
                page=-1
    else:
        page = -1
    return page, information
print("1")