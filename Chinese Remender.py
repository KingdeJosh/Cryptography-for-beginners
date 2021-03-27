def inv(a, m):
    m0 = m
    x0 = 0
    x1 = 1

    if (m == 1):
        return 0

    # Apply extended Euclid Algorithm
    while (a > 1):
        # q is quotient
        q = a // m

        t = m

        # m is remainder now, process
        # same as euclid's algo
        m = a % m
        a = t

        t = x0

        x0 = x1 - q * x0

        x1 = t

        # Make x1 positive
    if (x1 < 0):
        x1 = x1 + m0

    return x1


# k is size of num[] and rem[].
# Returns the smallest
# number s such that:
# s % num[0] = rem[0],
# s % num[1] = rem[1],
# ..................
# s % num[k-2] = rem[k-1]
# Assumption: Numbers in num[]
# are pairwise coprime
# (gcd for every pair is 1)
def findMinX(num, rem, k):
    # Compute product of all numbers
    prod = 1
    print("1. To solve this we first get the product of all N values")
    for i in range(0, k):

        prod = prod * num[i]

    print("2. The product of all N: pN=",num, " = ", prod)
        # Initialize result
    result = 0

    print("3. We then have the CRT formular to be the following")

    # Apply above formula
    for i in range(0, k):
        if i == 0:
            print("s = (a%s"%(i) ," * ", "inv((pN","/","N%s"%(i),"),N%s"%(i),")", " * ",  "pN","/","N%s"%(i),") +")
        elif i==k-1:
            print("    (a%s"%(i) ," * ", "inv((pN","/","N%s"%(i),"),N%s"%(i),")", " * ",  "pN","/","N%s"%(i),")")
        else:
            print("    (a%s"%(i) ," * ", "inv((pN","/","N%s"%(i),"),N%s"%(i),")", " * ",  "pN","/","N%s"%(i),") +")

    print("4. We then have the apply the CRT formular to get the following")

    for i in range(0, k):
        pp = prod // num[i]
        if i == 0:
            print("s = (",rem[i] ," * ", "inv((",prod,"/",num[i],"),", num[i],")", " * ",  prod,"/",num[i],") +")
        elif i==k-1:
            print("    (",rem[i], " * ", "inv((",prod,"/",num[i],"),", num[i],")", " * ", prod, "/", num[i],")")
        else:
            print("    (", rem[i], " * ", "inv((",prod,"/",num[i],"),", num[i],")", " * ", prod, "/", num[i],") +")

        result = result + rem[i] * inv(pp, num[i]) * pp
    print("5. When we compute all this we can then get the s value",result)
    print("6. We then do ", result,"mod",prod)
    return result % prod


# Driver method
num = [7, 3, 5, 11]
rem = [2, 2, 3, 4]
k = len(num)
for n in range(0, k):
    print("s = ",rem[n]," mod ",num[n])
print("   s = ", findMinX(num, rem, k))