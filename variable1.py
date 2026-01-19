# Ask user for their name and greet them
name = input("What is your name ? ").strip().title()
# split input into two parts and take first part
first, last = name.split(" ")

print(f"Hello, {first}")