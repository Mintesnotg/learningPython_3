import string


def is_palindrome_for(input_string: str):

    input_string=input_string.replace(" ","")
    clean_text = input_string.translate(str.maketrans("", "", string.punctuation)).replace(" ", "").lower()

    bk=len(clean_text)-1
    fr=0
    while(fr<=bk and bk>=fr):
        if(not(clean_text[bk] == clean_text[fr])):
            return False
        bk-=1
        fr+=1
    return True
        
        # for tex in range(clean_text):



print(is_palindrome_for("race a car"))
