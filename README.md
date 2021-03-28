# Cryptography-for-beginners
This repo was created for students to better understand basic crypto, with code style.\ 
Run with python3\
Each code when ran shows' a step by step solution for a certain topic.\ 
For example finding two prime numbers p and q when toitient of N and N is known. The code should show something like the below.
```
      When we have n = 221 and toitent = 192
    1. We know that n = p * q and toitent = (p-1)(q-1)
    2. We then susbsitute to get
       toitent =p.q-(p+q)+1 = n-(p+q)+1
    3. To get p and q we have that 
       p+q = n + 1 - toitent
    4. Subsituting in the values we have that
       S = p+q = 221+1-192
       = 30
    5. To get p and q from S value we use the following fomular
       p = ( s+ sqrt(s^2 - 4 * n))/2 
       q = (s - sqrt(s^2 - 4 * n))/2 
    6. Applying the formular we get
       p = (30+sqrt(30^2 - 4 * 221))/2 
       q = (30-sqrt(30^2 - 4 * 221))/2
    7. We have that p = 17.0  and q = 13.0
 ```
