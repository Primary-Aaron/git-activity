# Python implementation of Naive method
# to print all divisors

# method to print the divisors
def printDivisors(n) :
    i = 1
    while i <= n :
        if (n % i==0) :
            print i,
        i = i + 1

# Driver method
print "The divisors of 100 are: "
printDivisors(100)

#This code is contributed by Nikita Tiwari.
#this code was taken from https://www.geeksforgeeks.org/find-divisors-natural-number-set-1/
