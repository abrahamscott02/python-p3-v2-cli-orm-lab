from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab
def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(f"<Employee {employee.id}: {employee.name}, {employee.job_title}, Department ID: {employee.department_id}>")
    
    input("\nPress Enter to return to the menu...")



def find_employee_by_name():
    name = input("Enter the employee's name: ")
    employee = Employee.find_by_name(name)
    
    if employee:
        print(f"<Employee {employee.id}: {employee.name}, {employee.job_title}, Department ID: {employee.department_id}>")
    else:
        print(f"Employee {name} not found")
    
    input("\nPress Enter to return to the menu...")  # Pause for user input



def find_employee_by_id():
    id_ = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id_)
    if employee:
        print(f"<Employee {employee.id}: {employee.name}, {employee.job_title}, Department ID: {employee.department_id}>")
    else:
        print(f"Employee {id_} not found")

    input("\nPress Enter to return to the menu...")  # Pause for user input


def create_employee():
    name = input("Enter the employee's name: ")
    print(f"Debug: Name entered - {name}")  # Debugging line
    
    job_title = input("Enter the employee's job title: ")
    print(f"Debug: Job title entered - {job_title}")  # Debugging line
    
    department_id = input("Enter the employee's department id: ")
    print(f"Debug: Department ID entered - {department_id}")  # Debugging line

    try:
        employee = Employee.create(name, job_title, int(department_id))
        print(f"Success: <Employee {employee.id}: {employee.name}, {employee.job_title}, Department ID: {employee.department_id}>")
    except Exception as e:
        print(f"Error creating employee: {e}")
        print("Debug: Exception occurred during employee creation")  # Debugging line


def update_employee():
    id_ = input("Enter the employee's id: ")
    print(f"Debug: Employee ID entered - {id_}")  # Debugging line

    employee = Employee.find_by_id(id_)
    if not employee:
        print(f"Employee {id_} not found")
        input("\nPress Enter to return to the menu...")  # Pause for user input
        return

    try:
        # Update name
        name = input("Enter the employee's new name: ")
        print(f"Debug: New name entered - {name}")  # Debugging line
        employee.name = name

        # Update job title
        job_title = input("Enter the employee's new job title: ")
        print(f"Debug: New job title entered - {job_title}")  # Debugging line
        employee.job_title = job_title

        # Update department ID
        department_id = input("Enter the employee's new department id: ")
        print(f"Debug: New department ID entered - {department_id}")  # Debugging line
        employee.department_id = int(department_id)

        # Update in the database
        employee.update()
        print(f"Success: <Employee {employee.id}: {employee.name}, {employee.job_title}, Department ID: {employee.department_id}>")
    except Exception as e:
        print(f"Error updating employee: {e}")
        print("Debug: Exception occurred during employee update")  # Debugging line
    
    input("\nPress Enter to return to the menu...")  # Pause for user input



def delete_employee():
    id_ = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id_)
    
    if not employee:
        print(f"Employee {id_} not found")
        return

    employee.delete()
    print(f"Employee {id_} deleted")


def list_department_employees():
    department_id = input("Enter the department's id: ")
    department = Department.find_by_id(department_id)
    
    if not department:
        print(f"Department {department_id} not found")
        return

    employees = department.employees()
    for employee in employees:
        print(f"<Employee {employee.id}: {employee.name}, {employee.job_title}, Department ID: {employee.department_id}>")

    input("\nPress Enter to return to the menu...")  # Pause for user input