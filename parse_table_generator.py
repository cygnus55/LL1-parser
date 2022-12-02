first_set = {'S': ''}
follow_set = {'S': {''}}


def generate_parse_table(first_set, follow_set,
                         terminals, non_terminals, rules):
    terminals = list(terminals)
    terminals.append("$")
    terminals.remove("ε")

    parse_table = dict()
    for nt in non_terminals:
        parse_table[nt] = dict()
        for t in terminals:
            parse_table[nt][t] = []

    new_rules = []
    for rule in rules:
        A, right_side = rule.split("->")
        A = A.strip()
        right_side = right_side.strip()
        alpha = list(map(str.strip, right_side.split("|")))

        for term in alpha:
            for t in first_set[A] - {"ε"}:
                parse_table[A][t].append(f"{A} -> {term}")
            if "ε" in first_set[A]:
                for t in follow_set[A]:
                    parse_table[A][t].append(f"{A} -> {term}")
            if "ε" in first_set[A] and "$" in follow_set[A]:
                parse_table[A]["$"].append(f"{A} -> {term}")

    print(parse_table)
    return parse_table
