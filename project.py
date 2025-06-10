class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age, salary)
        self.emp_id = emp_id
        self.salary = salary
    def show(self):
        super().show()
        print(f"Employee ID: {self.emp_id}, Salary: {self.salary}")
class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age, emp_id, salary)
        self.department = department
    def show(self):
        super().show()
        print(f"Department: {self.department}")

persons = []
employees = []
managers = []

while True:
    print("\n--Python OOP Project: Employee Management System --")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Compare Salaries")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        salary = int(input("enter salary:"))
        p = Person(name, age, salary)
        persons.append(p)
        print("Person created.")

    elif choice == 2:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        emp_id = input("Enter employee ID: ")
        salary = float(input("Enter salary: "))
        e = Employee(name, age, emp_id, salary)
        employees.append(e)
        print("Employee created.")

    elif choice == 3:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        emp_id = input("Enter employee ID: ")
        salary = float(input("Enter salary: "))
        dept = input("Enter department: ")
        m = Manager(name, age, emp_id, salary, dept)
        managers.append(m)
        print("Manager created.")

    elif choice == 4:
        print("1. to show  details")
        print("2. to show employee details")
        print("3. to show manager details")
        choice2 = int(input("enter youe choice"))
        if choice2 == 1:
             print(" Persons ")
             for p in persons:
               print(p)
        elif choice2 == 2:
            print("Employees ")
            for e in employees:
               print(e)
        elif choice2 == 3:
            print("Managers")
            for m in managers:
               print(m)
        
    elif choice == 5:
     pass
       
       


    elif choice == 6:
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Try again.")
        chi