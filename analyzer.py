import re
import random
import string

def check_length(pw):
    return len(pw) >= 8

def has_uppercase(pw):
    return bool(re.search(r'[A-Z]', pw))

def has_lowercase(pw):
    return bool(re.search(r'[a-z]', pw))

def has_number(pw):
    return bool(re.search(r'\d', pw))

def has_special_char(pw):
    return bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', pw))

def analyze_password(password):
    score = 0
    suggestions = []

    # Check each rule
    if check_length(password):
        score += 1
    else:
        suggestions.append("Make it at least 8 characters long.")

    if has_uppercase(password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter (A-Z).")

    if has_lowercase(password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter (a-z).")

    if has_number(password):
        score += 1
    else:
        suggestions.append("Include at least one number (0-9).")

    if has_special_char(password):
        score += 1
    else:
        suggestions.append("Include at least one special character (!@#$%^&*).")

    # Strength evaluation
    if score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Medium"
    elif score == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return strength, suggestions

import random
import string

def generate_strong_password(length=12):
    """Generate a strong password with guaranteed complexity"""
    if length < 4:
        raise ValueError("Password length must be at least 4 to include all character types.")

    # Required characters
    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    special = random.choice(string.punctuation)

    # Fill the rest with random characters from all types
    all_chars = string.ascii_letters + string.digits + string.punctuation
    remaining = [random.choice(all_chars) for _ in range(length - 4)]

    # Combine everything
    password_list = [lower, upper, digit, special] + remaining

    # Shuffle to avoid predictable positions
    random.shuffle(password_list)

    # Join to form the final password
    return ''.join(password_list)

# --- MAIN PROGRAM ---
if __name__ == "__main__":
    print("🔒 Password Strength Analyzer 🔒")
    user_password = input("Enter your password: ")

    strength, tips = analyze_password(user_password)

    # Color codes
    RED = "\033[91m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    BRIGHT_GREEN = "\033[1;92m"
    RESET = "\033[0m"

    # Choose color based on strength
    if strength == "Weak":
        color = RED
    elif strength == "Medium":
        color = YELLOW
    elif strength == "Strong":
        color = GREEN
    else:
        color = BRIGHT_GREEN

    print(f"\nPassword Strength: {color}{strength}{RESET}")

    if tips:
        print("\nSuggestions to improve your password:")
        for t in tips:
            print("- " + t)

        # Suggest a strong password if weak or medium
        if strength in ["Weak", "Medium"]:
            new_password = generate_strong_password()
            print(f"\n💡 Suggested Strong Password: {new_password}")
    else:
        print("✅ Your password is very strong! Good job.")

