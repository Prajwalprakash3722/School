import csv 

def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell()==0:
            writer.writerow(["Name","Age","Email_ID","Contact"])
        
        writer.writerow(info_list)

if __name__ == '__main__':
    condition = True
    student_num = 1

while(condition):
    student_info = input("enter some student information for student #{}(Name,Age,Email_ID,Contact) ".format(student_num))
    
    print(student_info)
    
    student_info_list = student_info.split(' ')
    print("\nThe entered information of the student is - \nName: {}\nAge: {}\nEmail ID: {} \n Contact: {}"
          .format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))

    check_choice = input("is the input entered correct ? ")

    if check_choice=="yes":
        write_into_csv(student_info_list)
    
    condition_check = input("do u want to enter more information (yes/no)")
    if condition_check == "yes":
        condition = True
        student_num = student_num + 1
    elif condition_check =="no":
        condition = False
