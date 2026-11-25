def outer(func):
    def inner():
        print("code start")
        func()
        print("code end")
    return inner
@outer
def greet():
    print("Hello brother")
# greet=outer(greet)
greet()