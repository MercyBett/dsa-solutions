# https://www.hackerrank.com/challenges/simple-array-sum/problem

def simpleArraySum(ar):
  """
  It takes an array of integers as input, and returns the sum of all the integers in the array

  :param ar: an array of integers
  :return: The sum of the array
  """
  total =0
  for i in ar:
    total +=i
  return total