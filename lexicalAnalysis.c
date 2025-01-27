#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Function to check if a word is a keyword
int isKeyword(char *word) {
    const char *keywords[] = {"int", "float", "if", "else", "while", "do", "return", "for", "break"};
    int num_keywords = sizeof(keywords) / sizeof(keywords[0]);
    for (int i = 0; i < num_keywords; i++) {
        if (strcmp(word, keywords[i]) == 0) {
            return 1; // It's a keyword
        }
    }
    return 0;
}

// Function to check if a character is an operator
int isOperator(char ch) {
    return (ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == '=');
}

// Function to check if a character is a delimiter
int isDelimiter(char ch) {
    return (ch == ',' || ch == ';' || ch == '(' || ch == ')' || ch == '{' || ch == '}');
}

// Function to check if an identifier is already printed
int isDuplicate(char identifiers[][100], int count, char *current) {
    for (int i = 0; i < count; i++) {
        if (strcmp(identifiers[i], current) == 0) {
            return 1; // Duplicate found
        }
    }
    return 0;
}

int main() {
    char input[500];
    char buffer[100];
    char identifiers[100][100];
    int id_count = 0;
    int i = 0, j = 0;

    printf("Name:Anshul_Parkar Batch:C23 Rollno:2203122\n");

    printf("Enter the input statements: ");
    scanf("%[^\n]", input); // Read a single line of input

    // Keywords
    printf("\nKeywords:       ");
    while (input[i] != '\0') {
        if (isalnum(input[i])) {
            buffer[j++] = input[i];
        } else {
            if (j != 0) {
                buffer[j] = '\0';
                if (isKeyword(buffer)) {
                    printf("%s ", buffer);
                }
                j = 0;
            }
        }
        i++;
    }

    // Identifiers
    printf("\nIdentifiers:    ");
    i = 0, j = 0;
    while (input[i] != '\0') {
        if (isalnum(input[i])) {
            buffer[j++] = input[i];
        } else {
            if (j != 0) {
                buffer[j] = '\0';
                if (!isKeyword(buffer) && !isdigit(buffer[0]) && !isDuplicate(identifiers, id_count, buffer)) {
                    strcpy(identifiers[id_count++], buffer); // Add identifier to the list
                    printf("%s ", buffer); // Print unique identifier
                }
                j = 0;
            }
        }
        i++;
    }

    printf("\nOperators:      ");
    for (i = 0; input[i] != '\0'; i++) {
        if (isOperator(input[i])) {
            printf("%c ", input[i]);
        }
    }

    printf("\nConstants:      ");
    i = 0, j = 0;
    while (input[i] != '\0') {
        if (isdigit(input[i])) {
            buffer[j++] = input[i];
        } else {
            if (j != 0) {
                buffer[j] = '\0';
                printf("%s ", buffer);
                j = 0;
            }
        }
        i++;
    }

    // Delimiters
    printf("\nDelimiters:     ");
    for (i = 0; input[i] != '\0'; i++) {
        if (isDelimiter(input[i])) {
            printf("%c ", input[i]);
        }
    }

    printf("\n");
    return 0;
}
