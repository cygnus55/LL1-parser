def generate_parse_table(first_set, follow_set,
                         terminals, non_terminals, rules):
    terminals = list(terminals)
    terminals.append("$")
    terminals.remove("ε")

    ambiguous = False

    parse_table = dict()
    for nt in non_terminals:
        parse_table[nt] = dict()
        for t in terminals:
            parse_table[nt][t] = set()

    new_rules = []
    for rule in rules:
        A, right_side = rule.split("->")
        A = A.strip()
        right_side = right_side.strip()
        alpha = list(map(str.strip, right_side.split("|")))

        for term in alpha:
            for t in first_set[A] - {"ε"}:
                if not term == "ε":
                    parse_table[A][t].add(f"{A} -> {term}")
                    if len(parse_table[A][t]) > 1:
                        ambiguous = True
            if "ε" in first_set[A]:
                for t in follow_set[A]:
                    parse_table[A][t].add(f"{A} -> {term}")
                    if len(parse_table[A][t]) > 1:
                        ambiguous = True
            if "ε" in first_set[A] and "$" in follow_set[A]:
                parse_table[A]["$"].add(f"{A} -> {term}")
                if len(parse_table[A]["$"]) > 1:
                    ambiguous = True

    print(parse_table)
    return parse_table, ambiguous
