progression_outcomes =  {
    0 : "Progress",
    1 : "Progress – module trailer ",
    2 : "Do not Progress – module retriever ",
    3 : "Exclude"
}
MAX_RANGE = 120

def process_credits(pass_,defer, fail):
    # cpnvert data into int
    pass_, defer, fail = list(map(int, [pass_, defer, fail]))
    if pass_ == MAX_RANGE:
        return 0
    elif (defer + fail) < 40: 
        return 1
    elif (defer + fail) > 40:
        if fail >= 80:
            return 3
        return 2
        
# validate the input
def valid(*opt):
    for x in opt:
        try:
            x = int(x)
        except ValueError:
            print(f"{x} is not an Integer!")
            return False
        if x > MAX_RANGE:
            print(f"{x} is not in range ({MAX_RANGE})")
            return False
    tot = list(map(int, opt))
    if sum(tot) > MAX_RANGE or sum(tot) < MAX_RANGE:
        print(f"Error, your credit input is not in valid <MAX CREDIT : {MAX_RANGE}>")
        return False
    return True

# helper func to get userinput
def prompt():
    return input("( pass defer fail ) > ").split(" ")


if __name__ == "__main__":
    print("NOTE : Enter your credit scores with a space seperation in respective order\n")
    a, b, c = prompt()
    while not valid(a, b, c):
        a, b, c = prompt()
    res = process_credits(a,b,c)
    print(progression_outcomes[res])
