def palendrom (inputstring):
        inputstring = inputstring.lower().replace(" ", "").replace(",", "").replace(":", "").replace(".", "")
        left=0
        right = len(inputstring) - 1
        while left < right:
                if inputstring[left]!=inputstring[right]:
                        return False
                
                left+=1
                right-=1
        
        return True
word="radar"
print ( f"{palendrom(word)}" )
