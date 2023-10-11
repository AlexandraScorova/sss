def anna(lll):
    def inner():
        print("ko")
        lll()
    return inner

@anna
def ko1(): print("cfghj")

ko1()
ko1()