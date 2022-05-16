import random as r

print("Welcome to the Expert System!".center(60,'-')+"\n\n")

questions = [
    "The employee acts on all the feedback/inputs received from Managers",
    "The employee is willing to take on additional responsibilities",
    "The employee is able to attain work-life balance",
    "The employee is cognizant of the organizational goals and works towards them",
    "When working on a team project, the employee values everyone's contribution",
    "When attending team meetings, the employee is always on time",
    "The employee contributes suggestions to new initiatives or existing issues",
    "The employee is willing to contribute to proceedings for team meals or outings",
    "The employee is not averse to management and work-related changes",
]


def get_result(score):
    if score<=  1*MAX_QUESTIONS:
        print("You seem Happy with your work ! 🌝\nKeep it up!")
    elif score <= 2*MAX_QUESTIONS:
        print("You're liking your work 🌚🌝")
    elif score <= 3*MAX_QUESTIONS:
        print("It looks like you're not happy with your job 😔")
    elif score <= 4*MAX_QUESTIONS:
        print("It looks like you hate your job 😢")
    else:
        print("It looks like you're about to quit. ")
        print("Try searching for new job on linkedin.com 😬")

l = []

MAX_QUESTIONS = len(questions)
for i in range(MAX_QUESTIONS):
    l.append(0)


while 0 in l:
    qno = r.randint(0,MAX_QUESTIONS-1)
    if l[qno] == 0:
        print(questions[qno])
        exit = False
        while not exit:
            l[qno] = int(input('1.Always\t2.Sometimes\t3.yes\t4.Rarely\t5.Not at all\n Enter Your choice:'))
            exit = True
            if l[qno] > 5 and l[qno] < 0:
                print("please Enter Valid Choice.")
                exit = False
    
get_result(sum(l))