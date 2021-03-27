import random
import math
d = 8773
n = 38407
e = 13
K = (d * e) - 1
g = random.randint(2, n-1)
p=0
q=0
t=K
print(f"We have that d = {d} , e = {e} , n = {n}")
print("1. To factorise and get p and q get t as follows\n"
      "   t = (d * e) - 1")
print(f"2. Using that formular we have t = ({d}*{e})-1= {K}")

def isDivisible(number,divisor):
    if number % divisor == 0:
        return True
    else:
        return False

print(f"3. We then check to see if t is divisible by 2 which is \n"
      f"   {isDivisible(t,2)}")
print(f"4. Next we choose a random number(g) from 2 to n-1\n"
      f"   g = {g}")
print("5. We then check s=g^t mod n.\n"
      "   If it is equal to 1 we do t = t/2 and go to step 3 again\n"
      "   until we get a value greater than 1 ")
while p == 0 and q == 0:

    if isDivisible(t, 2) == True:
        x=pow(g, round(t), n)
        print(f"    s={g}^{round(t)} mod {n} = {x}")
        t = t/2
        #print(t)
        if x > 1:
           y = math.gcd(x - 1, n)
           print("6. We then check that gcd(s-1,n) is greater than 1\n"
                 f"    gcd({x-1},{n}) = {y}")
           if y > 1:

               p = y
               q = n/p
               print(f"7. So we can now say that p = {y}\n "
                     f"   We can now easily compute q = n/p ={n}/{p}={q} ")
               print("8.  Factors of N is ",p,q)





