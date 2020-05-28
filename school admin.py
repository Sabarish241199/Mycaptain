# -*- coding: utf-8 -*-
"""
Created on Wed May 27 21:57:43 2020

@author: sabu
"""
import csv
def write_into_csv(info_list):
    with open('student_info.csv','a') as csv_file:
        writer=csv.writer(csv_file)
        writer.writerow(info_list)

if __name__ =="__main__":
    condition=True
    
    while(condition):
        student_info=input("Enter the student information in the following format(Name  Age Cantact_number E-mail_id):")
        student_info_list=student_info.split(' ')
        print("\n the entered information is-\nName: {})\nAge: {}\nContact number: {}\nE-mail: {}"
            .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        choice_check=input("if the information is correct enter yes else no:")
        if choice_check=="yes":
            
            write_into_csv(student_info_list)
            condition_check=input("Enter (yes/no) do you want to enter information of another student?")
            if condition_check=="yes":
                condition=True
            else:
                condition=False
        else:
            print("\nenter the values again:")