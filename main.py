class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f'Employee {self.name} has age {self.age} and salary {self.salary}'

    def __repr__(self):
        return f'Employee {self.name} has age {self.age} and salary {self.salary}'

def validate_input(msg, type=str):
    while True:
        inp = input(msg)
        if type == int:
            try:
                return int(inp)
            except ValueError:
                print('Invalid input. Please enter a valid integer.')
        elif type == float:
            try:
                return float(inp)
            except ValueError:
                print('Invalid input. Please enter a valid float.')
        else:
            return inp

class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_new_employee(self):
        print('\nEnter employee data')
        name = input('Enter the name: ')
        age = validate_input('Enter the age: ', type=int)
        salary = validate_input('Enter the salary: ', type=float)
        self.employees.append(Employee(name, age, salary))

    def print_all_employees(self):
        if len(self.employees) == 0:
            print('No employees at the moment to print!')
            return
        print(':::Employees List:::')
        for emp in self.employees:
            print(f'Employee: {emp}')

    def delete_employees_by_age(self):
        if len(self.employees) == 0:
            print('No employees at the moment to delete!')
            return
        age_from = validate_input('Enter age from: ', type=int)
        age_to = validate_input('Enter age to: ', type=int)
        for idx in range(len(self.employees) - 1, -1, -1):
            emp = self.employees[idx]
            if age_from <= emp.age <= age_to:
                print('\tDeleting', emp.name)
                self.employees.pop(idx)

    def find_employee_by_name(self, name):
        if len(self.employees) == 0:
            print('No employees at the moment!')
            return
        for emp in self.employees:
            if emp.name == name:
                return emp
        return None

    def update_salary_by_name(self):
        if len(self.employees) == 0:
            print('No employees at the moment!')
            return
        up_name = input('Enter up name: ')
        new_salary = validate_input('Enter new salary: ', type=float)
        employee = self.find_employee_by_name(up_name)
        if employee is None:
            print('No employee with such a name')
        else:
            employee.salary = new_salary

class FrontendManager:
    def __init__(self):
        self.employees_manager = EmployeeManager()

    def print_menu(self):
        print('\nProgram Options:')
        messages = [
            '1) Add a new employee',
            '2) List all employees',
            '3) Delete by age range',
            '4) Update salary given a name',
            '5) End the program'
        ]
        print('\n'.join(messages))
        msg = F'Enter your choice (from 1 to {len(messages)}): '
        return validate_input(msg, type=int)

    def run(self):
        while True:
            choice = self.print_menu()

            if choice == 1:
                self.employees_manager.add_new_employee()
            elif choice == 2:
                self.employees_manager.print_all_employees()
            elif choice == 3:
                self.employees_manager.delete_employees_by_age()
            elif choice == 4:
                self.employees_manager.update_salary_by_name()
            elif choice == 5:
                break

if __name__ == '__main__':
    app = FrontendManager()
    app.run()