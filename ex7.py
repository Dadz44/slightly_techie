student={}
def add_student():
    st_name= input("Enter Student Name:").strip().title()
    age= input("Enter Student Age:").strip()
    course= input("Enter Student Course:").strip().title()
    grade= (input("Enter Student Grades:").strip().split(","))
    igrade=list(map(int,grade))
    
    student[st_name]={"Name":st_name,"Age":age, "Course": course, "Grade":igrade}
    print(f"Student {st_name} Added ")
    print(student)

def update_std_details():
    name = input("Enter Name to Update:")
    if name in student:
        ab=student[name]
        print(ab)
        while True:
            print("\n1.Update Student Name")
            print("2.Update Student Age")
            print("3.Update Student Course")
            print("4.Update Student Grades")
            print("5.Exit")

            update = input("\nEnter Data to Update:")

            if update == "1":
                names= input("Enter New name:")
                ab[name]= names

                print(f"{names} updated")

            elif update == "2":
                ages= input("Enter New Age:")
                ab["Age"]=ages

                print(f"Age Updated for {name}")
            elif update == "3":
                courses= input("Enter New Courses:")
                ab["Course"]=courses

                print(f"Courses Updated for {name}")

            elif update == "4": 
                grades= (input("Enter New Scores:").strip().split(","))
                fgrades=list(map(int,grades))
                ab["Grade"]=fgrades

                print(f"Grades Updated for {name}")

            elif update == "5":
                break
            else:
                print("Enter a Valid Input(1-5):")
    else:
        print(f"{name} does not exist")
    
                      
def average_grade(student):
    score_list=[]
    if student:
        for key, value in student.items():
            score_list.append(value['Grade'])
           # print(score_list)
         
        count=0
        total=0
        for sublist in score_list:
            for item in sublist:
                count=count+1
                total=total+item
        
        average=total/count
        print("Universal Average is:",average)

def view_students():
    if not student:
        print("No Data Available")
        return
    
    print("\nStudent Records")
    for key,value in student.items():
        print(f"-{key}, Age:{value["Age"]}, Course:{value["Course"]}, Grade:{value["Grade"]}")

def main():
    while True:
        print("\nWelcome to The Student Management System")
        print("1.Add Student")
        print("2.Update Student Record")
        print("3.Compute Universal Average")
        print("4.View All Students")
        print("5.Exit")


        choice=input("\nChoose Menu(1-5):")
        
        if choice == "1":
            add_student()
        elif choice =="2":
            update_std_details()
        elif choice == "3":
            average_grade(student)
        elif choice == "4":
            view_students()
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid Input, Enter 1-5")

if __name__=="__main__":
    main()
    