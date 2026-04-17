# TM Backlog Dashboard
# Author: Aleksandra Tomczak
# Date: April 2026
# Description: A CLI tool to manage and track Transaction Monitoring backlog cases

import csv

def view_cases():
    with open("backlog.csv", "r") as file:
        reader = csv.DictReader(file)
        cases = list(reader)


    print( 8*"=", "TM BACKLOG DASHBOARD", 8*"=")

    for case in cases:
        print(case["id"],case["transaction_id"],case["company name"],case["status"],case["owner"], case["priority"])


def add_case():

    with open("backlog.csv","r") as file:
        reader = csv.DictReader(file)
        cases = list(reader)

    transaction_id = input("Enter transaction id: ")
    company_name = input("Enter company name: ")
    root_cause = input("Enter company root cause: ")
    status = input("Enter status: ")
    owner = input("Enter owner: ")
    priority = input("Enter priority: ")
    comment = input("Enter comment: ")
    new_id = str(int(cases[-1]["id"]) + 1).zfill(3)

    new_case = {"id": new_id, "transaction_id": transaction_id, "company name": company_name, "root_cause": root_cause, "status": status, "owner": owner,"priority":priority, "comment":comment}

    with open("backlog.csv","a", newline = "") as file:
        writer = csv.DictWriter(file, fieldnames =  cases[0].keys())
        writer.writerow(new_case)

def update_status():
    with open ("backlog.csv", "r") as file:
        reader = csv.DictReader(file)
        cases = list(reader)
    
    item_to_update = input ("Enter ID: ")

    found= False
    for case in cases:
        if case["id"] == item_to_update:
            case["status"] = input("Enter new status: ")
            found =  True
    
    if not found:
        print ("ID not found")
    
    with open ("backlog.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames = cases[0].keys())
        writer.writeheader()
        writer.writerows(cases)

def delete_case():
    with open ("backlog.csv", "r") as file:
        reader = csv.DictReader(file)
        cases = list(reader)
    
    

    item_to_remove = input("Enter ID to be removed: ")
    
    found = any(case["id"] == item_to_remove for case in cases)
    
    #checking if id exists
    if not found:
        print("ID not found")
    else:
        new_cases = [case for case in cases if case["id"] !=item_to_remove]
        with open("backlog.csv","w") as file:
            writer = csv.DictWriter(file,fieldnames = cases[0].keys())
            writer.writeheader()
            writer.writerows(new_cases)
        print(f"Id {item_to_remove} has been removed")    
    
    
def filter_cases():
    with open ("backlog.csv", "r") as file: 
        reader = csv.DictReader(file)
        cases = list(reader)
    print("FILTER BY: ")
    print("1.Status")
    print("2.Owner")
    print("3.Priority")

    option = int (input("Select option: "))

    if option == 1:
        select_status= input("Enter status: ")
        filter_result =[]

        #checking matching items
        for case in cases:
            if case["status"] ==select_status:
                filter_result.append(case)

        #displaying matched items
        for result in filter_result:
            print(result["id"],result["transaction_id"],result["company name"],result["status"],result["owner"], result["priority"])
      
       
    elif option == 2:
        select_owner= input("Enter owner name: ")
        filter_result =[]

        #checking matching items
        for case in cases:
            if case["owner"] == select_owner:
                filter_result.append(case)

        #displaying matched items
        for result in filter_result:
            print(result["id"],result["transaction_id"],result["company name"],result["status"],result["owner"], result["priority"])
    elif option == 3:

        select_priority= input("Enter priority: ")
        filter_result =[]

        #checking matching items
        for case in cases:
            if case["priority"] == select_priority:
                filter_result.append(case)

        #displaying matched items
        for result in filter_result:
            print(result["id"],result["transaction_id"],result["company name"],result["status"],result["owner"], result["priority"])
    else:
        print ("Invalid option")

def show_summary():
    with open("backlog.csv", "r") as file:
         reader = csv.DictReader(file)
         cases = list(reader)

    status_count={}
    owner_count={}
    priority_count={}

    for case in cases:
        #status
        status = case["status"]
        if status in status_count:
            status_count[status] +=1
        else:
            status_count[status] =1
        #owner
        owner = case["owner"]
        if owner in owner_count:
            owner_count[owner] +=1
        else:
            owner_count[owner] =1
        #priority
        priority = case["priority"]
        if priority in priority_count:
            priority_count[priority] +=1
        else:
            priority_count[priority] =1
    
    print("BY STATUS:")
    print()
    for key,value in status_count.items():
        print(key,value)
    print()
    print("BY OWNER:")
    print()
    for key,value in owner_count.items():
        print(key,value)
    print()
    print("BY PRIORITY:")
    print()
    for key,value in priority_count.items():
        print(key,value)

       

#view_cases()       
#add_case()
#update_status()
#delete_case()
#filter_cases()
show_summary()