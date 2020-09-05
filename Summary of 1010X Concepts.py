## Breadth First Search (?)

#finding number of paths
## idea is to remove to have a naive while-loop that loops through all
## elements to create all possible permutations and combinations to find
## whatever you are searching for

def function(lst):
    to_check = [x for x in lst]
    solutions = []
    while to_check:
        current=lst.pop()

        #further question-specific conditions to be laid here, where if/else
        #branches will determine if something is to be added back to the
        #to_check list for further evaluation later or to be added to solutions

    return solutions


## Memoization
##idea is to reduce time complexity by storing values that have already been
##calculated before and retrieving it when a function calls it again. this
##is especially powerful for recursion

memo = {}
def coin_change(amount,denominations):
    if (amount,denominations) in memo:
        return memo[(amount,denominations)]
    elif amount==0 and len(denominations)!=0:
        return 1
    elif amount<0 or len(denominations)==0:
        return 0
    else:
        memo[(amount,denominations)] = coin_change(amount-denominations[0],denominations) + coin_change(amount,denominations[1:])
        return memo[(amount,denominations)]


##Time and Space Complexity
##important to deduce the time and space required for a piece of code to ensure that it does not use up too much resources
#below is the Finals Exam question, which I think it would be helpful if there's required some thinking and math knowledge


def fun(n, m):
    if n==0:
        return 0
    elif n%m==0:
        return n + fun((n-1)//m, m)
    else:
        return n + fun(n-1, m)

'''
Time complexity when m = 1: O(n).
Time complexity when 1 < m < n: O(mlogm n).
Time complexity when m ≥ n: O(n). (When m = n, it is O(1) to be precise.)

Justification (for each case):
When m = 1, the elif branch of the condition is executed always, and it is of the same
behavior as the else branch to reduce n by 1 each time. So, it needs O(n) time.

When m > n, the else branch is executed and it reduces n by 1 each time. So, it needs
also O(n) time. When m = n, the elif is executed with n = 0 passed into the function, so
O(1) which is also O(n).

When 1 < m < n, we have the following argument. The else branch of the condition is
executed for at most (m−1) time then it must reach the elif branch. The elif branch
is to keep only a fraction of n to continue (you are familiar with m = 2 that is halving
the n). So, there are only at most logm n times possible to take an m-fraction till n is 0,
and each time we do at most (m−1) reduction of n at the else branch to reach another
time of the elif branch. So the time is mlogm n.

'''

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

def fun2(n):
    result = 0
    for i in range(1, n):
        fact_i = fact(i)
        for j in range(1, i):
            result += fact_i + fact(j)
    return result

'''
Time complexity: O(n^3)

Justification:
The calling of fact(k) happens (n − k) times for k from 1 to n − 1. That is, fact(1) is
done just (n−1) times (when i = 1, and when j = 1 for each of i = 2,...,n−1), fact(2)
is done (n − 2) times (when i = 2, and when j = 2 for each of i = 3,...,n − 1), etc. till
fact(n-1) is done just once when i = n−1. So, the justification for the time complexity
is: 1(n−1) +2(n−2) +3(n−3) +...(n−1)1, and we know (from the web) that this sum
is (n−1)×n×(n+1)/6.

See https://www.youtube.com/watch?v=dUs5-Ak4WSw if you are interested in the derivation.
Alternatively, you can do an approximation to see that the sum is no larger than (n − 1) × (n − 1)^2 because each of the (n − 1) term
is smaller than (n − 1)^2. So, the sum is bounded above by O(n^3). What about bounded below? We can take those terms starting from
first quarter to the middle. Each one is ≥ n/4×(n−n/2) = n/4×n/2, and we have n/4 of them here. So, the sum is bounded below
by O(n^3) (as we ignore the constant 1/32).
'''













