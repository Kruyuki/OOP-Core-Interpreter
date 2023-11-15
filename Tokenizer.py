import re

RESERVED_WORDS = {
    "program": 1,
    "begin": 2,
    "end": 3,
    "int": 4,
    "if": 5,
    "then": 6,
    "else": 7,
    "while": 8,
    "loop": 9,
    "read": 10,
    "write": 11

}

SPECIAL_SYMBOLS = {
    ";": 12,
    ",": 13,
    "=": 14,
    "!": 15,
    "[": 16,
    "]": 17,
    "&&": 18,
    "||": 19,
    "(": 20,
    ")": 21,
    "+": 22,
    "-": 23,
    "*": 24,
    "!=": 25,
    "==": 26,
    "<": 27,
    ">": 28,
    "<=": 29,
    ">=": 30
    
    
}
# Regular expression for identifiers and integers
IDENTIFIER_REGEX = re.compile(r'^[A-Z][A-Z0-9]*$')
INTEGER_REGEX = re.compile(r'^\d+$')

class Tokenizer:
    def __init__(self, filename):
        self.file = open(filename, 'r')
        self.tokens = []
        self.cursor = 0
        self.tokenize_content()

    
    '''
    Until the cursor is smaller than content, 
    get its token at the cursor's location
    '''
    def get_token(self):
        if self.cursor < len(self.tokens):
            return self.tokens[self.cursor]
        return 34
        
    '''
    Gets the actual value(int) of token if it's integer
    '''
    def int_val(self):
        token = self.get_token()
        if token == 31:
            return int(self.tokens[self.cursor])
        print("ERROR - not an integer token")
        exit(1)

    '''
    If the token is identifier(32) return its name
    '''
    def id_name(self):
        token = self.get_token()
        if token == 32:
            return self.tokens[self.cursor]
        print("ERROR - not an identifier token")
        exit(1)

    '''
    Moves crsor and tokenize the content
    '''
    def skip_token(self):
        if self.cursor < len(self.tokens)-1:
           self.cursor = self.cursor + 1
        elif self.tokens[self.cursor] not in [33,34]:
            self.tokens = []
            self.cursor = 0
            self.tokenize_content()


    def tokenize_content(self):
        content = self.file.read()  # Read the entire file content
        i = 0  # Cursor to navigate through content

        while i < len(content):
            if content[i].isspace():  # Skip spaces
                i += 1
                continue
            # This part takes care of multi-character symbols
            if content[i:i + 2] in SPECIAL_SYMBOLS:
                self.tokens.append(SPECIAL_SYMBOLS[content[i:i + 2]])
                i += 2
                continue
            # This part takes care of single-character symbols
            if content[i] in SPECIAL_SYMBOLS:
                self.tokens.append(SPECIAL_SYMBOLS[content[i]])
                i += 1
                continue
            # This part takes care of reserved words/identifiers
            start = i  # Store the beginning of the word, will be updated through
                       # if statements above
            while i < len(content) and (content[i].isalpha() or content[i].isdigit()):
                i += 1
            word = content[start:i]
            if word in RESERVED_WORDS:
                self.tokens.append(RESERVED_WORDS[word])
            elif IDENTIFIER_REGEX.match(word):
                self.tokens.append(32)
            elif INTEGER_REGEX.match(word):
                self.tokens.append(31)
            else:
                self.tokens.append(34)  # Invalid token
                return

        self.tokens.append(33)  # EOF token



            

        
    


        
