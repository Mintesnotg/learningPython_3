def countwords(sentence):
    sentence= sentence.replace(" ","")
    counter=0

    for sent in sentence:
        counter+=1
    
    return counter

print(f" number  of words in the{countwords('mintesnot girma')}")