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



view_cases()       
add_case()