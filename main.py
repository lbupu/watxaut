def dec_returns(func):
    def wrapper(*args, **kwargs):
        print("I do something before")
        aux_out = func(*args, **kwargs)
        print("I do something after")
        return aux_out
    return wrapper


@dec_returns
def los_hahas():
    return "LOL"


a = los_hahas()
print(a)