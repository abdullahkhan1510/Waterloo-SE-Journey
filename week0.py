def percentage():
    # .strip("%") removes the percentage symbol from either end
    userinput = input("Enter a percentage (e.g., 85%): ")
    return userinput.strip("%")

def convert(n):
    # Converts the whole number percentage into a decimal rate
    # Using the /= operator keeps the logic concise
    rate = float(n)
    rate /= 100
    return rate

# Execution
clean_pct = percentage()
decimal_rate = convert(clean_pct)

print(f"The decimal rate is: {decimal_rate}")