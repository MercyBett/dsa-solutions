def compareTriplets(a, b):
  """
    The function is expected to return an INTEGER_ARRAY.
    The function accepts following parameters:
    1. INTEGER_ARRAY a
    2. INTEGER_ARRAY b
  """
  alice = bob = 0
  for i in range(3):
    if a[i]>b[i]:
      alice +=1
    elif a[i]<b[i]:
      bob +=1
  return alice,bob