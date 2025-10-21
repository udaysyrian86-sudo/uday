lo=[1,2,3,4,5,6,7]
for i in lo:
    if i%2==0:
        print(i)
    else:
        print("odd number")

import random
given_password=input("Enter your password: ")
alpaswoe=["122345","asdasd123","asdasd!@#","ASDasd123!@#"]
paswoed=random.choices(alpaswoe)
while given_password not in paswoed:
    print("wrong password")
    given_password=input("Enter your password: ")
print("welcome to uday")

total=0
count=0
grades=[]
num=int(input("entwe the nummber of students: "))

for i in range(1, num+1):
    grade=float(input(f"enter the grade of student {i}:"))
    if grade <0 or grade > 100:
        print("invalid grade, please enter a grade between 0 and 100.")
        continue
    if grade == 0:
        print("finsching input")
        break
    

    total += grade
    count += 1
    grades.append(grade)

    if count > 0:
        average = total / count
        print(" عدد الطلاب: المقبولين", count)
        print("المعدل:", average)
        print("أعلى درجة:", max(grades))
        print("أدنى درجة:", min(grades))
    else:
        print("لا توجد درجات صالحة لإجراء الحسابات.")

lists=[-1.,2,3,-4,5,-6,7]


for i in lists:
    if i<0:
        continue
    print(i)
def my_live(number):
   for i in range(0,11):
        print(f"{number}x{i}={number*i}")

my_live(7)    

def my_livel1(name):
    print(f"hello {name}, welcome to the program!")
my_livel1("uday")
import string
def decrypt(message, shift):
    letterts=string.ascii_lowercase
    decrypted_message=""
    for char in message:
        if char.lower() in letterts:
            original_index=letterts.index(char.lower())
            new_index=(original_index - shift)%26
            new_char=letterts[new_index]
            if char.isupper():
                new_char=new_char.upper()
                decrypted_message+=new_char
            else:
                decrypted_message+=char
        print(decrypted_message)

user_message=input("enter your message: ")
shift_value=int(input("enter the shift value: "))
decrypt(user_message, shift_value)

# student managment system

my_students=[]
def show_menu():
    print("1. add student")
    print("2.view students")
    print("3. delete student")
    print("4. exit")
    print("-----------------------------")

def add_student():
    name=input("enter student name: ")
    age=int(input("enter student age: "))
    grade=input("enter student grade: ")
    
    students={
        "name":name,
        "age":age,
        "grade":grade
    }
    my_students.append(students)
    print(f"student{name}add successfully")


def show_students():
    if not my_students :
        print("no students found.")
        return
    for student in my_students:
        print(f"name:{student["name"]} age:{student["age"]}grade:{student["grade"]}")
    

def edit_student():
    if len(my_students)==0:
        print("no students found.")
        return
    name_of_edit=input("enter the name of the student to edit: ")
    for student in my_students:
        if student["name"]==name_of_edit:
            new_name=input(f"enter new name: ({student["name"]}) ")
            new_age=int(input(f"enter new age: ({student["age"]}) "))
            new_grade=input(f"enter new grade:({student["grade"]}) ")
            if new_name!="":
                student["name"]=new_name
            if new_age !="":
                student["age"]=new_age
            if new_grade !="":
                student["grade"]=new_grade
            print(f"student {name_of_edit} updated successfully.")
            return
    print(f"student {name_of_edit} not found.")

    def delete_student():
        if len(my_students)==0:
            print("no students found.")
            return
        name_of_delete=input("enter the name of the student to delete: ")
        for student in my_students:
            if student["name"]==name_of_delete:
                my_students.remove(student)
                print(f"student {name_of_delete} deleted successfully.")
                return
        print(f"student {name_of_delete} not found.")



while True:
    show_menu()
    choice=input("enter your choice (1-4): ")
    if choice=="1":
        add_student()
    elif choice=="2":
        show_students()
    elif choice=="3":
        edit_student()
    elif choice=="4":
        print("exiting the program. goodbye!")
        break
    else:
        print("invalid choice. please try again.")


class Prodect:
    def __init__(self, name, price, quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def display_info(self):
        print(f"prodect name:{self.name}")
        print(f"prodect price:{self.price}")
        print(f"prodect quantity:{self.quantity}")

    def total_price(self):
        self.price=1500

amazon=Prodect("LAPTOP",750,"sehr gut")
hermes=Prodect("phone",500,"gut")
dpd=Prodect("tablet",300,"mittel")
dpd.display_info()
dpd.total_price()
dpd.display_info()

class car:
    def __init__(self,color,model,year):
        self.color=color
        self.model=model
        self.year=year

    def display_info(self,new_color):
        self.color=new_color
        print(f"car color:{self.color}")
        print(f"car model:{self.model}")
        print(f"car year:{self.year}")

bmw=car("red","X5",2020)
bmw.display_info("blue")

bmw.display_info("green")

