Q1="""1= what will the output of a = "hi, ali!"
print(a[1])?
A= e  B= h   C= e   D= r 
"""
Q2="""2= what will the output of txt = "The best answers of the question!"
print("free" in txt)?
A= true B= false C= A and B
"""
Q3=""" 3=  what will the outpot of  txt = "The best things in life are free!"
print("expensive" not in txt)?
A= true  B=false  C= A and B
"""
Q4="""4= what will the output of this operator system(100 + 5 * 3)
A= 115 B= 110 C= 210
"""
Q5= """5= which one is correct   mylist=[“Cabdulaahi”, “muhuddin”, “omar”]
Print(mylist)
A= [‘sumayya’, ‘mohammed’, ‘Dhaqane’]   B= [‘summaya mohamed’]  C= [‘mohammed Dhaqane’]
"""
Q6= """ 6=what is the output of  this list letterr=[1,5,7,9,3]
Print(Number)
A= [1,5,7,9,3]  B= [5,7,9,1] C=[7,9,1,5]
"""
Q7=""" 7= which one is the correct answer  dic={“dal” :1, “year”:25}
Print(dic)
A= {'afyare': 1, 'year': 25}  B= {'sumaiah': 1, 'year': 55}  C={'sumaiah': 1, 'year':}
"""
Q8= """ 8= which one is the correct student={“ Rollnum”:77, “studentname”: “sumaiah Dhaqane”, “age”: 19, “marks” :96}
Print(teacher)
A= key error B= index error C= syntax error 
"""
Q9="""9= what will the output of this list Number=[2,3,4,5,6] 
Print(Number)
Print(Number[5]
A= index error B= value error C= key error
"""
Q10= """ 10=  what is the correct anwer of:
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
A= b is not greater than a   B= a is not greater than  C= b is greater than d
"""
DicAns= {Q1: "d", Q2:"d", Q3:"a", Q4:"a", Q5:"a", Q6:"a",Q7:"a", Q8:"a",Q9:"a", Q10:"a" }
count=0
for x in  DicAns:
  print(x)
  Ans= input("choose the best answer").lower()
  if Ans== DicAns[x]:
    print("correct answer")
    print("you got 1 mark")
    count= count+1;
else:
    print("Incorrect answer")
    print("Crrect answer is:",DicAns[x]);

Score=(count/len(DicAns))*100
print("Your Score is",round(Score,1),"%")








