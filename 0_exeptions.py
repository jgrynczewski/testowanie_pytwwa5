def div(x, y):
    try:
        return x/y
    except:
        raise Exception("Coś poszło nie tak")

    # if y==0:
    #     return
    # else:
    #     return x/y

w1 = div(5,2)
print(w1)
w2 = div(5,0)
print(w2)
w3 = div(5, "asd")

