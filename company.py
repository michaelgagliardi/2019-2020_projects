### Import Modules\
import database
from database import employees

'''------------------------------------------------------
                Main program starts here 
---------------------------------------------------------'''
###Menu

print("Employee Management Tool\n========================")
database.display_menu(2020)
com=int(input("Enter Command:"))
while True: ##while loop to keep printing and ask a new command
    if com!=0:
        if com==1:
            database.initialize()
            database.display_menu(2020)
            com=int(input("Enter Command:"))
        elif com==2:
            database.info()
            database.display_menu(2020)
            com=int(input("Enter Command:"))
        elif com==3:
            database.search_employee(str(input("\nEnter Employee ID: ")))
            database.display_menu(2020)
            com=int(input("Enter Command:"))
        elif com==4:
            database.job_filter()
            database.display_menu(2020)
            com=int(input("Enter Command:"))
        elif com==5:
            database.years_filter()
            database.display_menu(2020)
            com=int(input("Enter Command:"))
        elif com==6:
            database.remove_employee(input("\nEnter Employee ID:"))
            database.display_menu(2020)
            com=int(input("Enter Command:"))
        elif com==7:
            database.create_employee(input("\nEnter Employee ID:"))
            database.display_menu(2020)
            com=int(input("Enter Command:"))
        elif com==8:
            database.change_date(int(input("\nProjection Date (>=2020): ")))
            database.display_menu(2020)
            com=int(input("Enter Command:"))
    else:
        print("Goodbye.")

        break
