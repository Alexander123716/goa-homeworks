def check_discount(age):
    if age < 18:
        return "You got discount"
    else:
        return "You didn't get discount"

# Example usage:
age = 16  # Change this to test with different ages
result = check_discount(age)
print(result)
