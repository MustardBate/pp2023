import random
studentList = []
courseList = []
def inputStudents():
    numStudents = int(input("Enter the number of students: "))
    for i in range(numStudents):
        studentID = input("Enter student's ID: ")
        studentName = input("Enter student's Name: ")
        studentDoB = input("Enter student's DoB: ")
        student = {"Name": studentName, "ID": studentID, "DoB": studentDoB}
        studentList.append(student)
        print("\n")
    return studentList

def inputCourses():
    global numCourses 
    numCourses = int(input("Enter the number of courses: "))
    for i in range(numCourses):
        courseID = input("Enter course's ID: ")
        global courseName
        courseName = input("Enter course's Name: ")
        course = {"Name": courseName, "ID": courseID}
        courseList.append(course)
        print("\n")
    return courseList

def courseMarks():
    courseNameToMark = input(("Select the course you want to mark: "))
    if(courseNameToMark == courseName):
        a = random.randint(0, 100)
        if(a > 0 & a < 50):
            print("Nobody went to this class, so everyone gets a 0.")
        elif(a > 51 & a < 75):
            print("Some gets 10, some gets 20. The specifics are a mystery.")
        elif(a > 76 & a <= 100):
            print("Everyone passses so it's all 20.")
    else:
        print("Invalid course.")

print(inputCourses())
print(courseMarks())
