def eliminate_left_recursion(non_terminal, productions):
    alpha = []
    beta = []
    
    for prod in productions:
        if prod.startswith(non_terminal):
            alpha.append(prod[1:])  # Extract the part after the non-terminal
        else:
            beta.append(prod)
    
    if not alpha:
        return {non_terminal: productions}  # No left recursion
    
    new_non_terminal = non_terminal + "'"
    
    # New productions after elimination
    new_productions = {
        non_terminal: [b + new_non_terminal for b in beta],  # A → bA'
        new_non_terminal: [a + new_non_terminal for a in alpha] + ['ε']  # A' → aA' | ε
    }
    
    return new_productions

# Taking multiple grammar rules as input
grammar = {}

num_rules = int(input("Enter the number of grammar rules: "))

for _ in range(num_rules):
    non_terminal = input("\nEnter the non-terminal: ")
    productions = input(f"Enter productions for {non_terminal} (separated by '|'): ").split('|')
    grammar[non_terminal] = productions

# Eliminating left recursion for all non-terminals
new_grammar = {}

for non_terminal, productions in grammar.items():
    new_grammar.update(eliminate_left_recursion(non_terminal, productions))

# Display result
print("\nGrammar after eliminating left recursion:")
for nt, prods in new_grammar.items():
    print(f"{nt} → {' | '.join(prods)}")
