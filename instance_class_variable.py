class Employee:
    no_of_leave = 12
    pass
sabbir = Employee()
michael = Employee()

sabbir.name = "Sabbir Ahamed"
sabbir.salary = 1200
sabbir.role = "Dev"

michael.name = "Micahel Horton"
michael.salary = 1500
michael.role = "QA"

print(sabbir.name)
print(sabbir.no_of_leave)
print(michael.no_of_leave)
print(Employee.no_of_leave)
print(sabbir.__dict__)
sabbir.no_of_leave = 10
print(sabbir.no_of_leave)
print(sabbir.__dict__)
print(Employee.__dict__)
print(Employee.no_of_leave)