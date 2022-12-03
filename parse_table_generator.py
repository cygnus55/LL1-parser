from first_n_follow import get_first, get_first_exp


def generate_parse_table(first_set, follow_set,
                         terminals, non_terminals, rules, c):
    terminals = list(terminals)
    new_terminals = terminals[:]
    new_terminals.append("$")
    if "ε" in non_terminals:
        new_terminals.remove("ε")

    ambiguous = False

    parse_table = dict()
    for nt in non_terminals:
        parse_table[nt] = dict()
        for t in new_terminals:
            parse_table[nt][t] = set()

    new_rules = []
    for rule in rules:
        A, right_side = rule.split("->")
        A = A.strip()
        right_side = right_side.strip()
        alpha = list(map(str.strip, right_side.split("|")))

        for term in alpha:
            first_of_term = get_first_exp(term, first_set, c, terminals, non_terminals)
            for t in first_of_term - {"ε"}:
                parse_table[A][t].add(f"{A} -> {term}")
                if len(parse_table[A][t]) > 1:
                    ambiguous = True
            if "ε" in first_of_term:
                for t in follow_set[A]:
                    parse_table[A][t].add(f"{A} -> {term}")
                    if len(parse_table[A][t]) > 1:
                        ambiguous = True
            if "ε" in first_of_term and "$" in follow_set[A]:
                parse_table[A]["$"].add(f"{A} -> {term}")
                if len(parse_table[A]["$"]) > 1:
                    ambiguous = True

    return parse_table, ambiguous
