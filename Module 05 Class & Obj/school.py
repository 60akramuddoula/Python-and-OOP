
class Student:

    def __init__(self, name, id, crnt_class) -> None:
        self.name= name
        self.id= id
        self.crnt_class= crnt_class

    def __repr__(self) -> str:
        return f'student with name : {self.name}, id : {self.id}, class : {self.crnt_class}' 

class Teacher:
    def __init__(self, name, id , subject) -> None:
        self.name= name
        self.id= id 
        self.subject= subject

    def __repr__(self) -> str:
        return f'Teacher name: {self.name}, id: {self.id}, subject: {self.subject}'

class  school:
    def __init__(self,name) -> None:
        self.name= name
        self.teachers=[]
        self.students=[]

    def add_teacher(self, name, subject):
        id = len(self.teachers)+101
        teacher= Teacher(name,id, subject)
        self.teachers.append(teacher)

    def enroll(self, name, fee):
        if fee<6500:
            return 'sorry Not enough fee'
        else:
            id = len(self.students)+1
            student= Student(name, id, 'C')
            self.students.append(student)
            return f'{name} is enrolled with id :{id}, extra money :{fee-6500}'
        
    def __repr__(self):
        print('Wellcome to {self.name}')

        print('--------OUR TEACHERS-----')
        for teacher in self.teachers:
            print(teacher)

        print('------OUR STUDENTS-----')
        for student in self.students:
            print(student)

        return f' all has been done'
         
        

        







# alia = Student('alia torkari', 9, 12)
# print(alia)
# ranbir= Teacher('Ranbir',101, 'algorithm')
# print(ranbir)
    
obj1 = school('Adarsha school')
obj1.enroll('alia',6500)
obj1.enroll('rahim',600)
obj1.enroll('karim',66500)


obj1.add_teacher('akramuddoula','physics')
obj1.add_teacher('Mahi','chemistry')
obj1.add_teacher('Dhusor','Bangla')

# print(self.teachers())
# print(obj1.teachers)
# print()

print(obj1)