from Employee import Employee

########## code to complete and comment ################

def display_menu(date):
    print("\nMenu (Year:"+str(date)+")");
    print("================");
    print("1-List Employees\t2-General Information\t3-Employee Information");
    print("4-Filter per job\t5-Filter per #years\t6-Remove Employee")
    print("7-Add Employee\t\t8-Change Date\t\t0-Exit");

######## All other functions listed below

### Employee list
employees=[]

employees.append(Employee("E04","Andrea",37,8,"Sales","yes"))
employees.append(Employee("E11","Bob",28,4,"Engineer","no"))
employees.append(Employee("E09","Brooke",34,5,"Engineer","yes"))
employees.append(Employee("E12","Connor",27,4,"Engineer","yes"))
employees.append(Employee("E16","James",25,3,"Accountant","no"))
employees.append(Employee("E24","Jenna",24,1,"Engineer","no"))
employees.append(Employee("E02","John",45,17,"Manager","yes"))
employees.append(Employee("E03","Julie",37,10,"Engineer","yes"))
employees.append(Employee("E01","Kate",48,24,"Manager","no"))
employees.append(Employee("E08","Keith",28,6,"Engineer","no"))
employees.append(Employee("E23","Kelly",25,1,"Engineer","no"))
employees.append(Employee("E17","Luke",33,3,"Sales","no"))
employees.append(Employee("E18","Mark",34,3,"Sales","yes"))
employees.append(Employee("E22","Pat",26,2,"Engineer","yes"))
employees.append(Employee("E15","Taylor",32,4,"Accountant","yes"))
employees.append(Employee("E05","Tony",34,8,"Sales","no"))


###Jobs list
jobs=[]
jobs.append("Manager")
jobs.append("Sales")
jobs.append("Accountant")
jobs.append("Engineer")

####Sorted ID Numbers
ID=[]
for e in employees:
    ID.append(e.ID)
ID=sorted(ID[:])

####Sorted Experience in Descending order
years=[]
for e in employees:
    years.append(e.exp)
xyears=sorted(years[:], reverse=True)

###initializing

def initialize():
    print("\nID\tName\t#years\tjob");
    print("---------------------------");
    for e in employees:
        print(e.ID+"\t"+e.name+"\t"+str(e.exp)+"\t"+e.job)

###information function
def info():
    print("\nNumber of Employees: "+str(len(employees)))
    managers=0
    sales=0
    accountants=0
    engineers=0
    for e in employees:
        if e.job =="Manager":
            managers=managers+1
        elif e.job =="Sales":
            sales=sales+1
        elif e.job =="Accountant":
            accountants=accountants+1
        elif e.job =="Engineer":
            engineers=engineers+1
    print("Manager: "+str((int(managers)/len(employees))*100)+"%")
    print("Sales: "+str((int(sales)/len(employees))*100)+"%")
    print("Accountant: "+str((int(accountants)/len(employees))*100)+"%")
    print("Engineer: "+str((int(engineers)/len(employees))*100)+"%")
    t=sum(e.age for e in employees)
    print("Age Mean: "+str(t/len(employees)))
    d=sum(e.exp for e in employees)
    print("#Years Mean: "+str(d/len(employees)))

###search employee list by ID number
def search_employee(ID):
    if any(e for e in employees if e.ID==str(ID)):
        display_employee(ID)
    else:
        print("Employee not found.")

###display ID information
def display_employee(ID):
    for e in employees:
        if str(ID)==e.ID:
            print(e.name+" is "+str(e.age)+" years old and has a "+e.job+" position.")
    for e in employees:
        if str(ID)==e.ID:
            if e.is_from_MA=="yes":
                print(e.name+" is from Massachusetts.")
            if e.is_from_MA=="no":
                print(e.name+" is not from Massachusetts.")

####filter employees by job
def job_filter():
    print("\nID\tName\t#years\tjob");
    print("---------------------------");
    for j in jobs:
        for e in employees:
            if j==e.job:
                print(e.ID+"\t"+e.name+"\t"+str(e.exp)+"\t"+e.job)
                
####filter employees by ID
def ID_filter():
    print("\nID\tName\t#years\tjob");
    print("---------------------------");
    for y in ID:
        for e in employees:
            if y==e.ID:
                print(e.ID+"\t"+e.name+"\t"+str(e.exp)+"\t"+e.job)

##### remove employee
def remove_employee(ID):
    for e in employees:
        if str(ID)!=e.ID:
            print("Employee not found!")
            break
        elif str(ID)==e.ID:
            x=employees.index(e)
            del employees[x]
            print("Employee %s successfully deleted."%(str(ID)))
            break

#####filter employees by experience
def years_filter():
    print("\nID\tName\t#years\tjob");
    print("---------------------------");
    x=0
    for y in xyears:
        for e in employees:
            if x>=len(xyears):
                break
            elif e.exp==xyears[x]:
                print(e.ID+"\t"+e.name+"\t"+str(e.exp)+"\t"+e.job)
                x=(x+1)

###add employee to employees list
def create_employee(ID):
    for e in employees:
        if any(e for e in employees if e.ID==str(ID)):
            print("Employee exists already!")
            break
        else:
            name=input("Enter Name: ")
            age=input("Enter Age: ")
            x=int(input("Job Select: 1-Manager, 2-Sales, 3-Accountant, 4-Engineer: "))
            job=jobs[x-1]
            employees.append(Employee(str(ID),name,age,0,job,"N/A"))
            break

###BONUS- Change Date
def change_date(year):
    if year >= 2020:
        z=int(year)-int(2020)
        [x+z for x in xyears]
        for e in employees:
            e.age=e.age+z
            e.exp=e.exp+z
        



