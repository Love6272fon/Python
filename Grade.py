name=input("What is your name?")
score=int(input("What is your score?"))

if score >= 90 and score <= 100:
    print(f"{name} Got Grade A+")
elif score >=80 and score <= 90:
    print(f"{name} Got Grade A")
elif score >=70 and score <=80:
    print(f"{name} Got Grade B")
elif score >=60 and score <=70:
    print(f"{name} Got Grade C")
elif score >=50 and score <=60:
    print(f"{name} Got Grade D")
elif score <50:
    print(f"{name} Got Grade F")
else:
    print("You shall not pass!")
