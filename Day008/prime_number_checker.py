def prime_checker(number):
    for num in range(2, number // 2 + 1):
        if (number % num == 0):
            print('Not prime')
            return
    print('Is Prime')
    return

        
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)