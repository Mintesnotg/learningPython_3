
grads= list (input("input your grade"))
def compute_gpa(grads, points):
    count_points=0
    numb_courses=0
    for g in grads:
        if(g in points):
            numb_courses+=1
            count_points+=points[g]
    
    
    
    return  round(count_points/numb_courses,2)






points = {'A+': 4.0, 'A': 4.0, 'A-': 3.67, 'B+': 3.33,
          'B': 3.0, 'B-': 2.67, 'C+': 2.33, 'C': 2.0,
          'C-': 1.67, 'D+': 1.33, 'D': 1.0, 'F': 0.0}

print(f' your grade is -- {compute_gpa(grads,points)}')

