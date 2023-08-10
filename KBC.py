#kbc 

Questions = [
    ["What is your name?","ram","sham","laxmn","None",3],
    ["What is your name?","ram","sham","laxmn","None",3],
    ["What is your name?","ram","sham","laxmn","None",3],
    ["What is your name?","ram","sham","laxmn","None",3],
    ["What is your name?","ram","sham","laxmn","None",3],
    ["What is your name?","ram","sham","laxmn","None",3],
    ["What is your name?","ram","sham","laxmn","None",3],
    ["What is your name?","ram","sham","laxmn","None",3],
    ["What is your name?","ram","sham","laxmn","None",3],
    ["What is your name?","ram","sham","laxmn","None",3],
    ["What is your name?","ram","sham","laxmn","None",3],
    ["What is your name?","ram","sham","laxmn","None",3],
    ["What is your name?","ram","sham","laxmn","None",3],
    ["What is your name?","ram","sham","laxmn","None",3],
    ["What is your name?","ram","sham","laxmn","None",3],
    ["What is your name?","ram","sham","laxmn","None",3],
    ["What is your name?","ram","sham","laxmn","None",3],
    ["What is your name?","ram","sham","laxmn","None",3]
]

levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,1000000]

i=0
money=0
for i in range(0,len(Questions)):
    question=Questions[i]
    print(f"Question for Rs. {levels[i]}")
    print(f"1. {question[1]}           2. {question[2]}")
    print(f"3. {question[3]}         4. {question[4]}")
    
    reply=int(input("Enter your answer: "))
    if(reply==question[-1]):
        print(f"Correct answer,you have won {levels[i]}")
        if(i==4):
            money=10000
        elif(i==9):
            money=320000
        elif(i==14):
            money=1000000
        
    else:
        print("Wrong answer!")
        break

print(f"Your final prize money: {money}")