def make_number():
    num = input("What is your number, with a dollar sign?")
    clean_num = num.replace("$","")
    return clean_num
def final_num(n):
    num = float(n) / 100
    return num

noperc = make_number()
dec = final_num(noperc)
print(dec)