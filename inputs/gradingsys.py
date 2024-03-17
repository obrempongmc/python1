
def gradeME(score):
    if score >=70:
        print("you have Grade A ")
    elif score<=70 and score >=60:
        print("you have Grade B ")
    elif score<=60 and score>=50 :
        print("you have Grade C ")
    elif score <=50 and score >=40:
        print("you have Grade D ")
    elif score <=40:
        print ("prepare for resit You have fail")


score = int(input(" Enter your score "))

gradeME(score)


