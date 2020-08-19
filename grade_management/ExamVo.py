import Subject as sb
class ExamVo:    
    def __init__(self, kor=0, eng=0, math=0):
        self.seq = 0
        self.tittle = ""
        self.reg_date = ""
        self.subject = sb.Subject(kor, eng, math)
    
    def set_kor(self, kor):
        if 0 < kor <= 100 :
            self.subject.set_kor(kor)
    
    def get_kor(self):
        return self.subject.get_kor()
    
    def set_eng(self, eng):
        if 0 < eng <= 100 :
            self.subject.set_eng(eng)
    
    def get_eng(self):
        return self.subject.get_eng()
    
    def set_math(self, math):
        if 0 < math <= 100 :
            self.subject.set_math(math)
    
    def get_math(self):
        return self.subject.get_math()