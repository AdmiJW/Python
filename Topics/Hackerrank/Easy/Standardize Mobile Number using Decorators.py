

# Decorators are quite an useful concept not only in Python, but functional programming in general
#
# WHat are decorators? It essentially 'decorates' a function, by adding codes to be ran before the call
# of the function, and after the call of the function.
# Decorators are also a function. Think of it as a 'factory' of new function, which take in your original
# function as material, and produces a brand new function which will execute your original function in
# the newly produced function at some point, but with added functionality alongside it.
#
# It might just be useful to think of it as constructors of functions.
#
# For more info on decorators, read the blog:
#       http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/


# First map the phone numbers to be unified, it can be done by string slicing and formatting
# Then, only ran the sorting function with the unified phone numbers passed in
def wrapper(f):
    def fun(l):
        l = map(lambda x: f"+91 {x[-10:-5]} {x[-5:]}", l)
        f(l)
    return fun


@ wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input() ) ) ]
    sort_phone(l)