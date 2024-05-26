import json
ques = { }
s = 0

num=1

n = open("questions.txt",'r')
ques = json.load(n)
n.close()


name = input("Enter your name: ")

for i in ques:
    
    print("Question",num , ": ", i)
    answer = input("The answer is ")
    
    if answer == ques[i]:
     s =   s + 1
     
    num = num + 1


final={name:s}
a = open("score.txt",'w')
final = json.dump(final,a)
a.close()