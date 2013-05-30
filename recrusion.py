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



def main():
   print Factorial(100)
   n_to_zero(100)
   zero_to_n(100)

if __name__ == '__main__':
  main()
