import re

def lexical_analysis(code):
    # Define token patterns
    token_patterns = [
        ("KEYWORD", r"\b(def|return|if|else|while|for|break|continue|import|from|as)\b"),
        ("IDENTIFIER", r"\b[A-Za-z_][A-Za-z0-9_]*\b"),
        ("NUMBER", r"\b\d+(\.\d+)?\b"),
        ("OPERATOR", r"[+\-*/%=<>!&|]"),
        ("SEPARATOR", r"[(),:{}[\]]"),
        ("STRING", r"\".?\"|'.?'"),
        ("WHITESPACE", r"\s+"),
        ("UNKNOWN", r".")
    ]

    # Compile token patterns into regex
    token_regex = re.compile("|".join(f"(?P<{name}>{pattern})" for name, pattern in token_patterns))

    tokens = []
    for match in token_regex.finditer(code):
        token_type = match.lastgroup
        token_value = match.group(token_type)
        if token_type != "WHITESPACE":  # Ignore whitespace
            tokens.append((token_type, token_value))
    
    return tokens

# Example function for analysis
sample_code = """
int position, initial, rate;
position = initial + rate * 60;
"""

# Perform lexical analysis
tokens = lexical_analysis(sample_code)

print("\nName-Anshul Parkar Batch-C23 Rollno-2203122\n")

# Print tokens
print("Tokens:")
for token in tokens:
    print(token)