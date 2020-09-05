#
# CS1010X --- Programming Methodology
#
# Mission 11a
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

# Collaborator: <Me> <Myself :foreveralone:>

###############
# Mission 11a #
###############

##########
# Task 1 #
##########

# With these operations, compound generic operations can be defined, such as
# def square(x):
#   return mul(x, x)

# (a) What are the types of the input and output of the generic square operation?
# Answer: Generic-Num -> (Generic-Num, Generic-Num) -> Generic-Num

# (b) Why would we prefer to define square in the above way, rather than:
# def square(x):
#    return apply_generic("square", x)
# Answer: the method in (b) means that more functions have to be created to specifically cater to the process,
# a process to which the method in (a), using pre-exisiting functions already defined, can achieve with equal result.
# for standardisation, (a) takes in a (type, number) tuple and depending on the type, the returned result will have the same type
# (b)'s method means that in the dictionary, there must be a further ('square',) key where within it, there must be more dictionaries for each type of number.
# and to extrapolate beyond (b), it means other secondary operators must also be included (eg cube) which in turn means more work to put more keys into the dictionary
# eg { ('square',): {('ordinary','ordinary'): lambda fucntion, ('rational','rational'): lambda, ('complex','complex'): lambda}, ('cube',):{...}, ... }
# thus (a) is more preferrable as there is less need to create a new function for a process that can already be done with the given documentation structure


##########
# Task 2 #
##########
# In the ordinary number package, a generic number operator is indexed by the
# name of the operator and a tuple of strings. For example, the add operator is
# indexed by ’add_ord’ and (’ordinary’, ’ordinary’); negation is indexed by
# ’negate_ord’ and (’ordinary’, ).
# In contrast, the constructor that creates an ordinary number is indexed by
# ’make_ord’ and just a string ’ordinary’. Explain why we have such a difference.

# Hint: Consider the differences in the process of the creation of a Generic-Num,
# such as create_ordinary, and the operations we can apply on Generic-Num, such
# as add. How is make_ord invoked, and how is add_ord invoked?

# Answer:

## process ##
# for the constructor, it returns a tuple as (str(RepType), value)
# an operator, such as add, will return apply_generic('add', ordinary1, ordinary2) where both ordinary1 and ordinary2 are as the aforementioned tuple structure
# the apply_generic function calls the type_tag function which loops through both ordinary1 and ordinary2 via the map function
# at each loop, it traverses through the tuple to obtain the str(RepType) for each ordinary-type number, resulting in ('ordinary','ordinary')
# next, there is the proc = get('add', ('ordinary','ordinary') ), where it will search in the _operation_table dictionary for _operation_table['add'][('ordinary','ordinary')]
# which in turn returns the function add_ord, thus proc = add_ord,
# the if-clause in apply_generic is satisfied to be True (since proc returned something rather than None/False), which results in add_ord(*map(content, (ordinary1, ordinary2)))
# content function works similar to type_tag function except it returns the value rather than the str(RepType)
# resulting in  make_ord(ordinary_value1, ordinary_value2) where both ordinary_value1 and ordinary_value2 are integers
# returning ('ordinary', ordinary_value1 + ordinary_value2)

# Thus, the difference bet the constructor and the generic number operator's index and their string and tuple keys respectively is because they are used at different parts
# of the process, where the operator takes in 2 objects resulting from the constructor

##########
# Task 3 #
##########

# There’s a right way and a wrong way to create a generic rational number. Here are two tries at
# producing 9/10. Which is the right way?

# first_try = create_rational(9, 10)
# second_try = create_rational(create_ordinary(9), create_ordinary(10))

# What happens when you use the wrong way to produce 9/10 and 3/10 and then try to add
# them? Why does this happen?

# Right way: second_try
# What happens: the Exception is raised when it reaches the type_tags = tuple(map(type_tag, args)) under the apply_generic part.
# Why it happens: This is because in the wrong way, the object created is ('rational', (9, 10)) as opposed to ('rational', (('ordinary', 9), ('ordinary', 10))) created by the right way
# when passed to the apply_generic function, at the mapping part, the type_tag function will read 9 instead of a string(RepType), of which there is no key in the _operation_table['add'] dictionary containing 9
# thus it results in the exception being raised.
# the correct way works because it does read a string, 'ordinary', for both the ordinary number objects inside the object
# and it results in ('ordinary', 'ordinary'), which is a key under _operation_table['add'] thus subsequent processes can continue

##########
# Task 4 #
##########

# Produce expressions that define r2_7 to be the generic rational number whose numerator part is
# 2 and whose denominator part is 7, and r3_1 to be the generic rational number whose numerator
# is 3 and whose denominator is 1. Assume that the expression
# >>> csq = square(sub(r2_7, r3_1))
# is evaluated. Draw a box and pointer diagram that represents csq.

# As an example, the following is a box and pointer diagram that represents x, a Generic-
# Ord number:
# x = create_ordinary(5)
#
#         +---+---+---+---+
# x  -->  |       |       |
#         +---+---+---+---+
#             |       |
#             v       v
#         "ordinary"  5

# FILL IN YOUR ANSWERS HERE:
# r2_7 = create_rational(create_ordinary(2), create_ordinary(7))
# r3_1 = create_rational(create_ordinary(3), create_ordinary(1))

# csq = square(sub(r2_7, r3_1))

## Sample ASCII box and pointer diagrams (with 2 components) for your convenience

##                   r2_7
##            +---+---+---+---+       +---+---+---+---+
##            |       |       |  -->  |       |       |  -->
##            +---+---+---+---+       +---+---+---+---+
##                |                       |
##                v                       v    
##            "rational"              +---+---+---+---+
##                                    |       |       |
##                                    +---+---+---+---+



##                   r3_1
##            +---+---+---+---+
##            |       |       |
##            +---+---+---+---+
##                |       |
##                v       v

##########
# Task 5 #
##########

# Within the generic rational number package, the internal add_rat function
# handled the addition operation. Why is it not
# possible to name this function "add"?

# Answer: within the add_rat function, the generic add function is already being called so if we named add_rat as add, it will end up being a recursion
# where the add in the add (supposed to be add_rat) function ends up being referred to the add (supposed to be add_rat)
# resulting in it recursively calling itself with no base case thus no end

##########
# Task 6 #
##########

from generic_arith import *

# Modify install_rational_package, indicating clearly your modifications.
def install_rational_package():
    def make_rat(x, y):
        return tag(reprat(x, y))
    def reprat(x, y):
        return (x, y)
    def numer(x): # (RepRat) -> Generic-Num (in this case Generic-Ord)
        return x[0]
    def denom(x): # (RepRat) -> Generic-Num (in this case Generic-Ord)
        return x[1]
    def tag(x):
        return attach_tag("rational", x)

    # add, sub, mul, div: (RepRat, RepRat) -> Generic-Rat
    def add_rat(x, y):
        return make_rat( add(mul(numer(x), denom(y)),
                             mul(denom(x), numer(y))),
                         mul(denom(x), denom(y)) )
    def sub_rat(x, y):
        return make_rat( sub(mul(numer(x), denom(y)),
                             mul(denom(x), numer(y))),
                         mul(denom(x), denom(y)) )
    def mul_rat(x, y):
        return make_rat( mul(numer(x), numer(y)),
                         mul(denom(x), denom(y)) )
    def div_rat(x, y):
        return make_rat( mul(numer(x), denom(y)),
                         mul(denom(x), numer(y)) )

    ##add-ins##
    ##RepRat: (('ordinary', 1), ('ordinary', 2))
    
    def negate_rat(x): # (RepRat) -> Generic-Rat
        return make_rat(negate(numer(x)),denom(x))
    
    def is_zero_rat(x): # (RepRat) -> Py-Bool
        return is_zero(numer(x)) # (RepRat) -> Generic-Num (in this case Generic-Ord) -> Py-Boolean
    
    def is_eq_rat(x, y): # (RepRat, RepRat) -> Py-Bool
        diff = sub_rat(x,y)  # (RepRat, RepRat) -> Generic-Rat (which is a type of Generic-Num)
        return is_zero(diff) # Generic-Num (in this case Generic-Rat) -> Py-Boolean
    
    put("make", "rational", make_rat)
    put("add", ("rational", "rational"), add_rat)
    put("sub", ("rational", "rational"), sub_rat)
    put("mul", ("rational", "rational"), mul_rat)
    put("div", ("rational", "rational"), div_rat)
    put("negate", ("rational",), negate_rat)
    put("is_zero", ("rational",), is_zero_rat)
    put("is_equal", ("rational", "rational"), is_eq_rat)
    

install_rational_package()

def create_rational(x, y):
    return get("make", "rational")(x, y)

# Change the values for the test variables below
r1_2 = create_rational(create_ordinary(1), create_ordinary(2))
r2_4 = create_rational(create_ordinary(2), create_ordinary(4))
r1_8 = create_rational(create_ordinary(1), create_ordinary(8))
left = sub(r1_2, mul(r2_4, r1_2))
right = add(r1_8, r1_8)
mid = div(r1_2, r2_4)
print(r1_2)
print(r2_4)
print(r1_8)
print(mid)
print(left)
print(right)
print(left == right)
#################
# Do not change #
#################
def gradeThis():
    if is_equal(sub(r1_2, mul(r2_4, r1_2)), add(r1_8, r1_8)):
        print("Well done!")
    else:
        print("Please check your solution.")
gradeThis()
