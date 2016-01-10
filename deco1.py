def makebold(fn):
    def wrapper():
        return "<b>" + fn() + "<b>"
    return wrapper

def makeitalic(fn):
    def wrapper():
        return "<i>" + fn() + "<i>"
    return wrapper

# 1st decorator
#@makebold
#@makeitalic
#def say():
#    return "hello"

# 2nd decorator
def say():
    return "hello"
# say = makebold(makeitalic(say))
say = makebold(say)
print say()

# 3rd deco
