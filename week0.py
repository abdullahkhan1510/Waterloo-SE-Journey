def get_value():
    # .strip("$") specifically targets the dollar sign at the start/end
    user_input = input("Enter a value with a dollar sign ($): ")
    return user_input.strip("$")

def calculate_decimal(n):
    # Using the /= operator is a sleek way to divide the variable by 100
    value = float(n)
    value /= 100
    return value

# Execution
clean_val = get_value()
result = calculate_decimal(clean_val)
print(result)