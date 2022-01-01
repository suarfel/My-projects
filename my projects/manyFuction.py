import random
randomnumber=random.randint(0,100)
for i in range(7) :
    guess=int(input('enter a number :'))
    if guess==randomnumber :
        print('you win the game')
        break
    elif guess > randomnumber :
        print('your guess number is graeter than random number')
    elif i==19:
        print('GAME OVER')
    else :
         print('your guess number is less than the ramdom number')

 #1 to show the required index of a number
def find(list1,value):
    for i in list1:
        if value == i:
            return list1.index(i)
    return -1
find([2,3,4],7)

#2 existence check
def check(sentence,check_word): 
    for word in sentence.split() :
        if word == check_word:
            return 0
    return -1
check("my name is surafel","mi")


#3 counting the repetition of a word in a list 
def countWord(list3):
    dic ={}
    for word in list3:
        if word not in dic:
            dic[word] = 1
        else :
            dic[word] = dic[word] + 1
    return dic
countWord(['the','the','clown','ran','ran','the'])



#4 reversing an integer number
def moving(number):
    if number == 0 :
        return ""
    else:
        return str(number%10) + str(moving(number//10))
moving(234345)


#5 taking unlimited number of parameter
def addition(*para):
    total = 0
    for number in para:
        total = total + number
    return total
addition(1,2,3,4)


#6 finding factorial 
def findfactorial(number) :
    if number==1 :
        return 1
    return number*findfactorial(number-1)
findfactorial(5)


#7 reversing the order of then list entries
def arrange(list_1):
    if len(list_1)==1 :
        return list_1[0:]
    elif len(list_1)==2 :
        return list_1[-1:] + list_1[0:1]
    else :
        return arrange(list_1[1:]) + list_1[0:1]
arrange([4,45,6,78,89,0])


#8 2048 merging one row to the left
def merge(row):
    if len(row)==1:
        return row[0:]
    else :
        if row[0]==0:
            return merge(row[1:]) + [0]
        elif row[0]!=0 and row[0]==row[1]:
            row[0]=row[0]*2
            row[1]=0
            return row[0:1] + merge(row[1:])
        elif row[0]!=0 and row[1]==0:
            row.pop(1)
            return merge(row) + [0]
        else :
            return row[0:1] + merge(row[1:])
merge([0,0,0,8])


#9 finding gcd
def gcd(a,b):
    b=b%a
    if b==0:
        return a
    else:
        return gcd(b,a)
gcd(33,88)


# to find the sum of digits 
def sum_digit(number):
    if number//10 ==0:
        return number
    else :
        return number%10 + sum_digit(number//10)
sum_digit(235)


#checks wheather a number is prime or not 
def isprime(x):
    for i in range(2, (x//2)+1):
        if x%i==0:
            i+=1
            return "it is not prime"   
    return "it is prime"
isprime(21)


# Only checks for factors up to the square root of x
def isPrime1(x):
    i=2
    while i*i < x:          
        if x%i==0:
            return False
        i+=1
    return True
print(isPrime1(19*19))


def paleindromcheck(str1):
    str2=str1
    last=len(str1)-1
    start=0
    while start <= last :
        if str1[start]==str2[last] :
            if start>=last:
                print("str1 is a paleindrom") 
                break
        else :
            print("str1 is not a paliendrom")
            break
        start = start + 1
        last = last -1
paleindromcheck("abba")

#binary search algorithm
def locate(cards,query):
    min=0
    max=len(cards)
    while min <= max:
        mid=(min+max)//2
        mid_number=cards[mid]
        if mid_number == query:
            return "the number's position is " + str(mid)
        elif mid_number < query:
            max= mid
        elif mid_number > query:
            min= mid
    return -1
print(locate([75,67,65,45,33,31,29,12,9],9))

