def tokenize(code):
    tokens = []
    i = 0

    while i < len(code):
        ch = code[i]

        # Skip comments //
        if ch == "/" and i + 1 < len(code) and code[i + 1] == "/":
            while i < len(code) and code[i] != "\n":
                i += 1
            continue

        # Skip whitespace
        if ch.isspace():
            i += 1
            continue

        # Identifiers / keywords
        if ch.isalpha():
            word = ""
            while i < len(code) and code[i].isalpha():
                word += code[i]
                i += 1
            word_upper = word.upper()
            if word_upper in ("LET", "PRINT"):
                tokens.append(("KEYWORD", word_upper))
            else:
                tokens.append(("IDENT", word))
            continue

        # Numbers
        if ch.isdigit():
            num = ""
            while i < len(code) and code[i].isdigit():
                num += code[i]
                i += 1
            tokens.append(("NUMBER", int(num)))
            continue

        # Operators & symbols
        if ch in "+-*/=;":
            tokens.append(("SYMBOL", ch))
            i += 1
            continue

        # Illegal characters
        print(f"Warning: Illegal character '{ch}' ignored")
        i += 1

    return tokens


