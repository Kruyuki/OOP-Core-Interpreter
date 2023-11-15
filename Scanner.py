import sys

def isIdentifier(s):
        #Identfier must beign with upper case letter
        if not s[0].isupper(): return False
        for c in s[1:]:
            #Identifier must be followed with upper case letter or numbers
            if not c.isdigit() and not c.isupper():
                return False
        return True

class Scanner:
    #Reserved keywords
    reserved = {"program": 1, "begin": 2, "end": 3, "int": 4, "if": 5,
                "then": 6, "else": 7, "while": 8, "loop": 9, "read": 10, "write": 11}

    #Special symbols
    symbols = {";": 12, ",": 13, "=": 14, "!": 15, "[": 16, "]": 17, "&&": 18, "||": 19,
               "(": 20, ")": 21, "+": 22, "-": 23, "*": 24, "!=": 25, "==": 26, "<": 27, ">": 28, "<=": 29, ">=": 30}

    #White space symbols
    whitespace = {"\t", " ", "\n", "\r"}

    #Special starting symbols
    specialStartingSymbols = {'!', '=', '<', '>', '|', '&'}

    #Constructor
    def __init__(self, fileName):
        self.file = open(fileName, 'r')
        self.tokens = []
        self.tokenizeLine()
    
    def tokenizeLine(self):
        # Read a line from the file
        line = self.file.readline()

        # Check for an empty line
        if len(line) == 0:
            self.tokens.append(("_EOF", 33))
            return

        # Holds tokens
        lineArr = []
        # String to accumulate characters to form a token
        s = ""
        
        # i is the index, c is the character
        i = 0
        while i < len(line):
            c = line[i]

            # Character is a white space or a symbol or a special starting symbol followed by a valid combination with the next character
            if c in self.whitespace or c in self.symbols or (c in self.specialStartingSymbols and i+1 < len(line) and c + line[i+1] in self.symbols):
                # Token
                if len(s) > 0:
                    tt = self.tokenType(s)
                    lineArr.append((s, tt))
                    # Check not EOF
                    if tt == 34:
                        self.tokens = lineArr
                        return
                    
                # Handle special starting symbols with valid combinations
                if c in self.specialStartingSymbols and i+1 < len(line) and c + line[i+1] in self.symbols:
                    lineArr.append((c + line[i+1], self.symbols[c + line[i+1]]))
                    i += 1
                # Character a symbol
                elif c in self.symbols:
                    lineArr.append((c, self.symbols[c]))
                s = ""
            else:
                # Character part of a token
                s += c
            # Move to the next character
            i += 1

        # Leftover token from s after loop
        if len(s) > 0:
            tt = self.tokenType(s)
            lineArr.append((s, tt))
            if tt == 34:
                self.tokens = lineArr
                return

        # Update self.tokens to be lineArr if lineArr is not empty
        # Otherwise call tokenizeLine recursively to process the next line
        if lineArr:
            self.tokens = lineArr
        else:
            self.tokenizeLine()

    def tokenType(self, s):
        if s == "_EOF":
            return 33
        elif s in self.reserved:
            return self.reserved[s]
        elif s in self.symbols:
            return self.symbols[s]
        elif s.isdigit():
            return 31
        elif isIdentifier(s):
            return 32
        else:
            return 34

    def getToken(self):
         if len(self.tokens) > 0:
            res = self.tokens[0][1]
            if res == 34:
                print(
                    f"ERROR: Invalid token {self.tokens[0][0]} encountered! Terminating program")
            return res

    def skipToken(self):
        #Move token cursor to the next token 
        if len(self.tokens) > 0:
            self.tokens.pop(0)
        #No tokens so call tokenzieLine
        if len(self.tokens) == 0:
            self.tokenizeLine()

    def intVal(self):
        #Return integer value
        if self.getToken() == 31:
            return int(self.tokens[0][0])
        else:
            print("ERROR: Token is not of type integer!")
            return ""

    def idVal(self):
        #Return identifier
        if self.getToken() == 32:
            return self.tokens[0][0]
        else:
            print("ERROR: Token is not of type identifier!")
            return ""

if __name__ == "__main__":
    inpFile = sys.argv[1]
    scanner = Scanner(inpFile)

    #Token type
    tokenType = 0
    #Continue until we find illegal token or EOF
    while tokenType != 33 and tokenType != 34:
        #Return token type
        tokenType = scanner.getToken()
        #Print token type without moving
        print(tokenType, end=" ")
        #Advance Cursor
        scanner.skipToken()
