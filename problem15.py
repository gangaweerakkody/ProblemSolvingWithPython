def double_chars(s: str) -> str:
    return ''.join([char * 2 for char in s])

# Example usage:
print(double_chars("now"))    # Output: "nnooww"
print(double_chars("123a!"))  # Output: "112233aa!!"
