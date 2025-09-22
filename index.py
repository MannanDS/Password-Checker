import re
import os
import argparse
import math

# Check if password is in the common passwords list
def is_common_password(password):
    file_path = os.path.join(os.path.dirname(__file__), "a.txt")
    with open(file_path, "r") as file:
        common_passwords = {line.strip() for line in file}
    return password in common_passwords

# Check password strength and return flags for failed checks
def check_password_strength(password):
    errors = {
        "length": len(password) < 8,  # Less than 8 characters
        "digit": re.search(r"\d", password) is None,  # No digit
        "uppercase": re.search(r"[A-Z]", password) is None,  # No uppercase letter
        "lowercase": re.search(r"[a-z]", password) is None,  # No lowercase letter
        "symbol": re.search(r"[ @!#$%^&*()<>?/\\|}{~:]", password) is None  # No special symbol
    }
    return errors

# Calculate entropy score (measure of randomness)
def calculate_entropy(password):
    charset_size = 0
    if re.search(r"[a-z]", password):
        charset_size += 26  # lowercase
    if re.search(r"[A-Z]", password):
        charset_size += 26  # uppercase
    if re.search(r"\d", password):
        charset_size += 10  # digits
    if re.search(r"[ @!#$%^&*()<>?/\\|}{~:]", password):
        charset_size += 32  # common symbols

    if charset_size == 0:
        return 0

    entropy = math.log2(charset_size ** len(password))  # log2(possibilities)
    return round(entropy, 2)

# Give user feedback based on missing rules + entropy
def give_feedback(errors, entropy):
    feedback = []
    if errors["length"]:
        feedback.append("Make it at least 8 characters long.")
    if errors["digit"]:
        feedback.append("Add at least one number.")
    if errors["uppercase"]:
        feedback.append("Add at least one uppercase letter.")
    if errors["lowercase"]:
        feedback.append("Add at least one lowercase letter.")
    if errors["symbol"]:
        feedback.append("Add at least one special symbol.")

    # Entropy strength hints
    if entropy < 28:
        feedback.append("Password entropy is very low — too predictable.")
    elif entropy < 36:
        feedback.append("Entropy is moderate — try making it longer.")
    elif entropy < 60:
        feedback.append("Entropy is strong — good job.")
    else:
        feedback.append("Excellent entropy — very strong password!")

    return feedback

# CLI handler
def main():
    parser = argparse.ArgumentParser(description="Check password strength and common usage.")
    parser.add_argument("password", nargs="?", help="Password to check")
    args = parser.parse_args()

    # Use CLI input or fallback to prompt
    password = args.password or input("Enter Password: ")

    # Check if password is common
    if is_common_password(password):
        print("⚠️ This is a common password. Please choose a more unique one.")
    else:
        # Run regex checks
        result = check_password_strength(password)

        # Calculate entropy
        entropy = calculate_entropy(password)
        print(f"🔢 Entropy score: {entropy} bits")

        # Give results + feedback
        if any(result.values()):
            failed = [k for k, v in result.items() if v]
            print("❌ Weak password. Issues found in:", ", ".join(failed))
        else:
            print("✅ Passed basic checks!")

        feedback = give_feedback(result, entropy)
        for tip in feedback:
            print("👉", tip)

# Entry point
if __name__ == "__main__":
    main()
