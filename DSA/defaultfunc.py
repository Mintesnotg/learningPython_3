

def defaultfunc(a,b=10,c=15):
   
    return a+b+c

# print( f" results {defaultfunc(10,5)}")

points={ 'A+':4.0, 'A':4.0,' A-' :3.67, 'B+' :3.33,
'B' :3.0, 'B-' :2.67, 'C+' :2.33, 'C' :2.0,
'C' :1.67, 'D+' :1.33, 'D' :1.0, 'F' :0.0}
data = [1, 2, 4, 8]
i= iter("sort of strings")

val=points.values()

for value in val:
    print(f'{value}')

for tr in i:
    print(F"{tr}")

def compute_gpa(grades):
    try:
        num_courses = 0
        total_points = 0
        your_grades = str()
        
        for g in grades:
            if g in points:
                num_courses += 1
                total_points += points[g]
        
        for grade in grades:
            your_grades += grade + ', '

        return f"Your grade is {your_grades} and GPA {total_points / num_courses}"

    except ValueError as e:
        return e 
    #raise

print(f"{compute_gpa(['A-','A+','A','A-'])} {chr(90) } " )






