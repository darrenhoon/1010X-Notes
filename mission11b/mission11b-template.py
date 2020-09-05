#
# CS1010X --- Programming Methodology
#
# Mission 11b
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

# Collaborator: <Myself, which is why the answer for Task 1, 2, and 3 are gonna be the same as Mission 11a >

###############
# Mission 11b #
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

# There’s a right way and a wrong way to create a generic complex number. Here are two tries at
# producing 9+10i. Which is the right way?

# first_try = create_complex(9, 10)
# second_try = create_complex(create_ordinary(9), create_ordinary(10))

# What happens when you use the wrong way to produce 9+10i and 3+10i and then try to add
# them? Why does this happen?

# Right way: second_try
# What happens: the Exception is raised when it reaches the type_tags = tuple(map(type_tag, args)) under the apply_generic part.
# Why it happens: This is because in the wrong way, the object created is ('complex', (9, 10)) as opposed to ('complex', (('ordinary', 9), ('ordinary', 10))) created by the right way
# when passed to the apply_generic function, at the mapping part, the type_tag function will read 9 instead of a string(RepType), of which there is no key in the _operation_table['add'] dictionary containing 9
# thus it results in the exception being raised.
# the correct way works because it does read a string, 'ordinary', for both the ordinary number objects inside the object
# and it results in ('ordinary', 'ordinary'), which is a key under _operation_table['add'] thus subsequent processes can continue

##########
# Task 4 #
##########

# Produce expressions that define c2_plus_7i to be the generic complex number whose real part is 2
# and whose imaginary part is 7, and c3_plus_1i to be the generic complex number whose real part
# is 3 and whose imaginary part is 1. Assume that the expression
# >>> csq = square(sub(c2_plus_7i, c3_plus_1i))
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
# c2_plus_7i = create_complex(create_ordinary(2), create_ordinary(7))
# c3_plus_1i = create_complex(create_ordinary(3), create_ordinary(1))

# csq = square(sub(c2_plus_7i, c3_plus_1i))

## Sample ASCII box and pointer diagrams (with 2 components) for your convenience
##            +---+---+---+---+
##            |   |   |    ---|--->
##            +---+---+---+---+
##                |
##                v

##            +---+---+---+---+
##            |   |   |   |   |
##            +---+---+---+---+
##                |       |
##                v       v

##########
# Task 5 #
##########

# Within the generic complex number package, the internal add_com function
# handled the addition operation. Why is it not
# possible to name this function "add"?

# Answer: within the add_com function, the generic add function is already being called so if we named add_com as add, it will end up being a recursion
# where the add in the add (supposed to be add_com) function ends up being referred to the add (supposed to be add_com)
# resulting in it recursively calling itself with no base case thus no end


##########
# Task 6 #
##########

from generic_arith import *

# Modify install_complex_package, indicating clearly your modifications.
def install_complex_package():
    def make_com(x, y):
        return tag(repcom(x, y))
    def repcom(x, y):
        return (x, y)
    def real(x):
        return x[0]
    def imag(x):
        return x[1]
    def tag(x):
        return attach_tag("complex", x)

    # add, sub, mul, div: (RepCom, RepCom) -> Generic-Com
    def add_com(x, y):
        return make_com( add(real(x), real(y)),
                         add(imag(x), imag(y)) )
    def sub_com(x, y):
        return make_com( sub(real(x), real(y)),
                         sub(imag(x), imag(y)) )
    def mul_com(x, y):
        return make_com( sub(mul(real(x), real(y)),
                             mul(imag(x), imag(y))),
                         add(mul(real(x), imag(y)),
                             mul(real(y), imag(x))))
    def div_com(x, y):
        com_conj = complex_conjugate(y)
        x_times_com_conj = content(mul_com(x, com_conj))
        y_times_com_conj = content(mul_com(y, com_conj))
        return make_com( div(real(x_times_com_conj), real(y_times_com_conj)),
                         div(imag(x_times_com_conj), real(y_times_com_conj)))
    def complex_conjugate(x):
        return (real(x), negate(imag(x)))


    ##add-ins##
    ##RepCom: (('ordinary', 1), ('ordinary', 2))
    
    def negate_com(x): # (RepCom) -> Generic-Com
        return make_com(negate(real(x)),negate(imag(x)))
    
    def is_zero_com(x): # (RepCom) -> Py-Bool
        return is_zero(real(x)) and is_zero(imag(x)) # (RepCom) -> Generic-Num (in this case Generic-Ord) -> Py-Boolean
    
    def is_eq_com(x, y): # (RepCom, RepCom) -> Py-Bool
        return x == y # since the data structure is the same, unlike in Rational Numbers
    
    put("make", "complex", make_com)
    put("add", ("complex", "complex"), add_com)
    put("sub", ("complex", "complex"), sub_com)
    put("mul", ("complex", "complex"), mul_com)
    put("div", ("complex", "complex"), div_com)
    put("negate", ("complex",), negate_com)
    put("is_zero", ("complex",), is_zero_com)
    put("is_equal", ("complex", "complex"), is_eq_com)

install_complex_package()

def create_complex(x,y):
    return get("make", "complex")(x, y)

# Change the values for the test variables below
c_neg3_plus_10i = create_complex(create_ordinary(-3), create_ordinary(10))
c1_plus_2i = create_complex(create_ordinary(1), create_ordinary(2))
c1_plus_3i = create_complex(create_ordinary(1), create_ordinary(3))
c0_plus_0i = create_complex(create_ordinary(0), create_ordinary(0))
print(is_zero(c0_plus_0i))

#################
# Do not change #
#################
def gradeThis():
    if is_equal(sub(c_neg3_plus_10i, mul(c1_plus_2i, c1_plus_3i)), add(c1_plus_2i, c1_plus_3i)):
        print("Well done!")
    else:
        print("Please check your solution.")
gradeThis()
