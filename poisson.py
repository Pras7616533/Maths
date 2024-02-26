def fact(n):
  if n==0:
    return 1
  else:
    return n*fact(n-1)

def powm(m):
  e = 2.718
  return e**-m

def mpr(m,r):
  return m**r

def main():
  try:
    m = float(input("enter for m "))
    r = int(input("enter for r "))
    print ("here is the positional distribution")
    em = powm(m)
    mr = mpr(m,r)
    rf = fact(r)
    p = (em*mr)/rf
    print (f"e to the power of negative m is {em}")
    print (f"m to the power of r is {mr}")
    print (f"r factorial is {rf}")
    print (f"total Poisson distribution {p}")
  except value_error:
    print ("invalid input")

if __name__=='__main__':
  main()
