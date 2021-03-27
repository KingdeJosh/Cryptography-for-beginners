import math
n= 221
toitent = 192
print(f"When we have n = {n} and toitent = {toitent}")
print("1. We know that n = p * q and toitent = (p-1)(q-1)\n"
      "2. We then susbsitute to get\n"
      "   toitent =p.q-(p+q)+1 = n-(p+q)+1\n"
      "3. To get p and q we have that \n"
      "   p+q = n + 1 - toitent")
s=n+1-toitent
print("4. Subsituting in the values we have that\n"
      f"   S = p+q = {n}+1-{toitent}\n"
      f"   = {s}")
print("5. To get p and q from S value we use the following fomular\n"
      "   p = ( s+ sqrt(s^2 - 4 * n))/2 \n"
      "   q = (s - sqrt(s^2 - 4 * n))/2 ")
p = (s + math.sqrt((s**2) - 4 * n)) / 2
q = (s - math.sqrt((s**2) - 4 * n)) / 2
print("6. Applying the formular we get\n"
      f"   p = ({s}+sqrt({s}^2 - 4 * {n}))/2 \n"
      f"   q = ({s}-sqrt({s}^2 - 4 * {n}))/2")
print(f"7. We have that p = {p}  and q = {q}")