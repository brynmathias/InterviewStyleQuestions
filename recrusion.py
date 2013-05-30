#!/usr/bin/env python


def Factorial(n):
  if(n <=1): return 1
  else:
     return  Factorial(n-1) * n

def n_to_zero(n):
  print n
  if( n == 0 ):
    return 0
  n_to_zero(n-1)


def zero_to_n(n):
  if( n == 0 ) : return 0
  zero_to_n(n-1)
  print n

def reverse_string(input):
   if(len(input) < 1):return 0
   print input[len(input)-1]
   input = input[:len(input)-1]
   reverse_string(input)



def main():
   print Factorial(100)
   n_to_zero(100)
   zero_to_n(100)
   reverse_string("the end")
if __name__ == '__main__':
  main()
