#Problem7.py
#Project Euler problem 7

#This program finds the 10001st prime number by checking every odd number and adding 
#to a count every time one is found. until the count equalls 10001. Then it
#prints that prime number.

from NumberTests import isPrime


def main():
    target = 10001
  
    count = 1
    num = 1

    while count < target:
        num = num + 2

        if isPrime(num):
         count = count + 1
    print(num)


  

if __name__ == '__main__':
  main()