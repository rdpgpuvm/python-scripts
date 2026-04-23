def is_palindrome(s):
    """Checks if a string is a palindrome."""
    # Normalize by removing non-alphanumeric characters and making it lowercase
    processed_s = ''.join(filter(str.isalnum, s)).lower()
    return processed_s == processed_s[::-1]

def find_palindrome(text):
    """Simple function to demonstrate palindrome check."""
    if not text:
        return False
    return is_palindrome(text)

# Example Usage:
if __name__ == "__main__":
    test_strings = ["racecar", "A man, a plan, a canal: Panama", "hello world", "madam"]
    print("--- Palindrome Checker ---")
    for s in test_strings:
        result = find_palindrome(s)
        print(f"'{s}' is palindrome: {result}")