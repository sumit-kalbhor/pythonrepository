
def div(x,y):
    try:
        d = x/y
    except ZeroDivisionError:
        print("Can't divide by 0")
    else:
        print(d)
    finally:
        print("Execution is done")


div(1, 0)
div(4, 2)
