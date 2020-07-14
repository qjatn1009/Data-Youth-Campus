class Subject:

    def __init__(self, kor=0, eng=0, math=0):
        self.__kor = kor
        self.__eng = eng
        self.__math = math

    def set_kor(self, kor):
        if 0 < kor <= 100 :
            self.__kor = kor

    def get_kor(self):
        return self.__kor

    def set_eng(self, eng):
        if 0 < eng <= 100 :
            self.__eng = eng

    def get_eng(self):
        return self.__eng

    def set_math(self, math):
        if 0 < math <= 100 :
            self.__math = math
            
    def get_math(self):
        return self.__math