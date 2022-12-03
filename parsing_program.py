def parse_input(input_string, parse_table, non_terminals):
    steps = []
    input_string += "$"
    stack = ["$", "S"]
    while stack[-1] != "$":
        step = []
        a = input_string[0]
        step.append(" ".join(stack))
        step.append(input_string)
        if stack[-1] == a:
            stack.pop()
            input_string = input_string[1:]
            step.append(f"Pop {a}")
        elif stack[-1] not in non_terminals:
            step.append("Reject")
            steps.append(step)
            break
        elif not parse_table[stack[-1]][a]:
            print(stack[-1], a)
            step.append("Reject")
            steps.append(step)
            break
        else:
            rule = list(parse_table[stack[-1]][a])[0]
            step.append(f"M[{stack[-1]}, {a}]: {rule}")
            literals = rule.split("->")[1].strip().split(" ")
            stack.pop()
            if not "ε" in literals:
                for literal in reversed(literals):
                    stack.append(literal.strip())
        steps.append(step)
    if stack[-1] == "$":
        if input_string == "$":
            steps.append([" ".join(stack), input_string, "Accept"])
        else:
            steps.append([" ".join(stack), input_string, "Reject"])
    return steps

