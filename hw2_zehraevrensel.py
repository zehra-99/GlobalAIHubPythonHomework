name = input("Please enter your name: ")
last_name = input("Please enter your last name: ")
age = input("Please enter your age: ")
date_of_birth = input("Please enter your date of birth (just year): ")

if age.isdigit():  #age kısmına yanlışlıkla string yazığımda kodumun hata verdiğini gördüm. internetten bu çözümü buldum.
    if int(age) <= 18:
        print("you cant go out because it is too dangerous")
    else:
        print("you can go out to the street")
else:
    print("please enter a proper integer")

#zehra evrensel
#zehra.evrensel2017@gtu.edu.tr