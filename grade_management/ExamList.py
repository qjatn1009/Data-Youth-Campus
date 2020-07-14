
class ExamList:
    def __init__(self, list=list(), current=-1):
        self.__list = list
        self.__current = current
    
    def add_list(self, exam):
        self.__list.append(exam)

    def pop_list(self, idx):
        del self.__list[idx]
    
    def get_list(self):
        return self.__list

    def set_current(self, current):
        self.__current = current
    
    def get_current(self):
        return self.__current
    
    def add(self, exam, current):
        self.__list.append(exam)
        self.set_current(self.get_current()+1)

    def get(self, i):
        return self.get_list()[i]