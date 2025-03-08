




def get_positive_float(prompt):
       
    while True:
        try : 
               value =  float( input( (prompt)))
               if(value>0 ):
                   return value
               print("⚠️ Please enter a positive number.")
        except (ValueError) as e:
                print(F"⚠️ Invalid input! Enter a valid number.{e}")
               

               



weight= get_positive_float("Enter your weight (kg): ")
height = get_positive_float("Enter your height (m): ")




try:
    
    Bmivalue= round( (weight )/ (height * height),2)

    if(Bmivalue< 18.5):
        print(F"Your BMI is {Bmivalue} You are  Underweight ")
    elif (Bmivalue >= 18.5  and Bmivalue <=24.9):
        print(F"Your BMI is {Bmivalue} You have a Normal weight")
    elif (Bmivalue >= 25.0  and Bmivalue <=29.9):
        print(F"Your BMI is {Bmivalue} You are  Overweight ")

except ( Exception) as ex :

    print("exeption is {ex}")





