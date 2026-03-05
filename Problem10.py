#Problem10.py
#Project Euler problem 10

#This program loops through odd numbers, checks if each number is prime and adds 
#each prime number to a running total. After every number under 2,000,000 has been 
#checked it prints the total.

from NumberTests import isPrime


def main():
    limit = 2000000
  
    total = 2
    num = 1

    while num < limit:
        num = num + 2

        if num >= limit:
           break
        if isPrime(num):
           total = total + num
    print(total)
        
  

if __name__ == '__main__':
  main()