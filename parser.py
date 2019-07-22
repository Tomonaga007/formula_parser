def parse_formula(formula):

    result = {}
    stack = []

    num = 0

    for idx in range(len(formula)+1):
        char = "Q" if (idx == len(formula)) else formula[idx]
        if char.isupper():
            if stack:
                atom = ""
                while stack:
                    atom = stack.pop() + atom
                if atom in result:
                    result[atom] += (num or 1)
                else:
                    result[atom] = (num or 1)
                num = 0
            stack.append(char)
        elif char.islower():
            stack.append(char)
        elif char.isdigit():
            num = num * 10 + int(char)

    return result


if __name__ == "__main__":
    print(parse_formula("H2O"))
    print(parse_formula("Mg2COOH"))
    print(parse_formula("NH2"))
