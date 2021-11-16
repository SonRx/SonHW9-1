# Richard Son

# function.py that computes values for f(x) = x^2 + 2; for x = 0 to 9.
# print out the values for x and f(x)
def f(x):
    for i in range(x):
        y = i*i + 2
        print "value of x:", i , "/-/ value of f(x):", y

# square.py that prints out the square of all numbers from 0 to 19.        
def sq(x):
    for i in range(x):
        y = i*i
        print "the square of", i, "is", y

# cube.py that prints out the cube of odd numbers from 0 to 19 
# or the numbers themseves if they are even.
def cb(x):
    for i in range(x):
        if (i % 2 != 0): # check if number is odd or not
            y = i*i*i
            print "Odd number:", i, "/-/ cubed value:", y
        else:
            y = i
            print "Even number:", i, "/-/ reg value:", y

def main():
    print " ------- PART a ------- "
    f(10)
    print " ------- PART b ------- "
    sq(20)
    print " ------- PART c ------- "
    cb(20)

if __name__ == "__main__":
    main()

