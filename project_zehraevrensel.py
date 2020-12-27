name_list = ["Korhan Özdemir", "Zehra Evrensel", "Ömer Cengiz"]
answer = 0
counter = 0

while answer == 0 and counter < 3:
    name_surname = input("Please enter your name and surname: ")
    if name_surname not in name_list:
        counter += 1
        if counter == 3:
            print('Please try again later')
    else:
        answer = 1
        print("Welcome")

if answer:  # answer == 1
    course_list = ["chemical reaction engineering", "thermodynamics", "stoichiometry", "mass transfer", "statistics"]
    print(course_list)
    selected_courses = []
    while True:  # karsilastirma while - ture false i==1
        selected_course = input("Please enter the course you selected from list: ")
        if selected_course not in course_list:
            print('You typed the course incorrect. Please type correctly.')
        else:
            selected_courses.append(selected_course)
            print("Your course is added successfully.")

        print(selected_courses)
        if len(selected_courses) < 5:
            check = input("If you want to continue to choose course please type 1 otherwise please type 0 ")
        elif len(selected_courses) == 5:  # iki esittir karsilastirma mantik operatoru
            print("You reached the limit.")
            break

        if check == "0":  # i use 0 in a string form because we take this from user and user's answer is a string as long as we don't change it.
            if len(selected_courses) < 3:
                print("You failed in class.")
            elif len(selected_courses) >= 3:
                print("Your selection is completed. Well Done.")
            break

    while True:
        exam_course = input("Please choose one of the course from the list to take an exam: ")
        if exam_course not in selected_courses:
            print('You typed the course incorrect. Please type correctly.')
        else:
            print("Operation is successful.")
            break

    midterm = int(input('midterm score: '))
    final = int(input('final score: '))
    project = int(input('project score: '))

    score = 0.3 * midterm + 0.5 * final + 0.2 * project

    d2 = {"midterm": midterm, "final": final, "project": project}
    print(d2)

    print("overall score is", (score))

    if score > 100 or score < 0:
        print('Invalid score')

    elif score >= 90:
        print('You got an AA')

    elif score >= 70 and score < 90:
        print('You got a BB')

    elif score >= 50 and score < 70:
        print('You got a CC')

    elif score >= 30 and score < 50:
        print('You got a DD')

    else:
        print('You got FF')



#zehra evrensel
#zehra.evrensel2017@gtu.edu.tr
#Son quizim internet bağlantımda sıkıntı yaşadığım için istediğim gibi gitmedi. Projem ve ödevlerim umarım yeterli olur.