import re

def lexical_analysis(code):
    # Define token patterns
    token_patterns = [
        ("KEYWORD", r"\b(def|return|if|else|while|for|break|continue|import|from|as|int|float)\b"),
        ("IDENTIFIER", r"\b[A-Za-z_][A-Za-z0-9_]*\b"),
        ("NUMBER", r"\b\d+(\.\d+)?\b"),
        ("OPERATOR", r"[+\-*/%=<>!]"),
        ("DELIMITER", r"[(),:{};\[\]]"),
        ("STRING", r"\".*?\"|'.*?'"),
        ("WHITESPACE", r"\s+"),
        ("UNKNOWN", r".")
    ]

    # Compile token patterns into a regex
    token_regex = re.compile("|".join(f"(?P<{name}>{pattern})" for name, pattern in token_patterns))

    tokens = []  # List to store all tokens
    for match in token_regex.finditer(code):
        token_type = match.lastgroup
        token_value = match.group(token_type)
        if token_type != "WHITESPACE":  # Ignore whitespace
            tokens.append((token_type, token_value))

    return tokens


def format_output(tokens):
    # Categorize tokens
    keywords = set()
    identifiers = set()
    operators = set()
    constants = set()
    delimiters = []

    for token_type, token_value in tokens:
        if token_type == "KEYWORD":
            keywords.add(token_value)
        elif token_type == "IDENTIFIER":
            identifiers.add(token_value)
        elif token_type == "NUMBER":
            constants.add(token_value)
        elif token_type == "OPERATOR":
            operators.add(token_value)
        elif token_type == "DELIMITER":
            delimiters.append(token_value)

    # Print tokens in the desired format
    print("Keywords:      ", " ".join(keywords))
    print("Identifiers:   ", " ".join(identifiers))
    print("Operators:     ", " ".join(operators))
    print("Constants:     ", " ".join(constants))
    print("Delimiters:    ", " ".join(delimiters))


# Sample code input
sample_code = """
int position, initial, rate;
position = initial + rate * 60;
"""

print("\nName-Anshul_Parkar Batch-C23 Rollno-2203122\n")

# Perform lexical analysis
tokens = lexical_analysis(sample_code)

# Format and display the output
format_output(tokens)
