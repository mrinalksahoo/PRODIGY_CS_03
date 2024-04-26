import re


def check_password_strength(password):
    # Define criteria
    length_criteria = 8
    uppercase_criteria = False
    lowercase_criteria = False
    digit_criteria = False
    special_char_criteria = False

    # Check length
    if len(password) >= length_criteria:
        length_criteria = True

    # Check for uppercase, lowercase, digits, and special characters
    for char in password:
        if char.isupper():
            uppercase_criteria = True
        elif char.islower():
            lowercase_criteria = True
        elif char.isdigit():
            digit_criteria = True
        elif char in "!@#$%^&*()_+-=[]{}|;:,.<>?":
            special_char_criteria = True

    # Determine strength level
    if length_criteria and uppercase_criteria and lowercase_criteria and digit_criteria and special_char_criteria:
        return "Very Strong"
    elif length_criteria and uppercase_criteria and lowercase_criteria and digit_criteria:
        return "Strong"
    elif length_criteria and uppercase_criteria and lowercase_criteria:
        return "Moderate"
    elif length_criteria and (uppercase_criteria or lowercase_criteria):
        return "Weak"
    else:
        return "Very Weak"


# Main function
def main():
    while True:
        password = input("Enter a password: ")
        strength = check_password_strength(password)
        print("Password strength:", strength)

        # Ask if user wants to continue
        choice = input("Do you want to continue? (yes/no): ")
        if choice.lower() != "yes":
            break


if __name__ == "__main__":
    main()
