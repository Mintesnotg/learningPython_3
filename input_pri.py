import datetime

useryear = int(input("Enter your birth year.."))

currentyer = datetime.datetime.now().year

print('your age is', currentyer-useryear)