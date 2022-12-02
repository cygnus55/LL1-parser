def read_rules(filename):
    with open(filename, "r") as f:
        rules = list(map(lambda x: x.strip(), f.readlines()))
        return rules


def find_longest_prefix(first_term, second_term):
    zipped_list = list(zip(first_term, second_term))
    matched_list = [x[0] if x[0] == x[1] else "" for x in zipped_list]
    longest_prefix_list = []
    for letter in matched_list:
        if letter == "":
            break
        longest_prefix_list.append(letter)
    longest_prefix = "".join(longest_prefix_list)
    return longest_prefix


def left_factor(rules):
    for rule in rules:
        A, right_side = rule.split("->")
        A = A.strip()
        right_side = list(map(lambda x: x.strip(), right_side.split("|")))

        longest_prefices = []

        if len(right_side) >= 2:
            for term in right_side:
                for another_term in right_side:
                    if not term == another_term:
                        longest_prefix = find_longest_prefix(
                            term, another_term)
                        if not longest_prefix == "":
                            if len(longest_prefices) > 0:
                                for i in range(len(longest_prefices)):
                                    if longest_prefices[i].startswith(longest_prefix) or \
                                            longest_prefix.startswith(longest_prefices[i]):
                                        if len(longest_prefix) < len(
                                                longest_prefices[i]):
                                            longest_prefices[i] = longest_prefix
                                    else:
                                        if longest_prefix not in longest_prefices:
                                            longest_prefices.append(
                                                longest_prefix)
                            else:
                                longest_prefices.append(longest_prefix)

        # If α ≠ ε, replace all of the A-productions A → α β1 | α β2 |….| α βn |γ,
        # where γ represents all alternatives that do not begin with α, by

        # A → α A' | γ
        # A' → β1 | β2 |….| βn

        if len(longest_prefices) > 0:
            new_rules = []
            right_side_rules = []

            for prefix in longest_prefices:
                terms_with_prefix = list()
                for term in right_side:
                    if term.startswith(prefix):
                        new_term = term[len(prefix):]
                        if new_term == "":
                            new_term = "ε"
                        terms_with_prefix.append(new_term)
                B = A
                while any([x.startswith(B) for x in rules]) or \
                        any([x.startswith(B) for x in new_rules]):
                    B += "'"
                right_side_rules.append(f"{prefix}{B}")
                new_rules.append(
                    f"{B} -> {' | '.join([term for term in terms_with_prefix])}")

            # Terms without common prefix
            gamma = []

            for term in right_side:
                if not any([term.startswith(p) for p in longest_prefices]):
                    gamma.append(term)

            modified_rule = f"{A} -> {' | '.join(right_side_rules)}"
            if len(gamma) > 0:
                modified_rule += " | " + " | ".join(gamma)
            rules.append(modified_rule)
            rules.extend(new_rules)
            rules.remove(rule)

    return rules


if __name__ == "__main__":
    production_rules = read_rules("rules.txt")
    print("Production Rules:")
    for rule in production_rules:
        print(rule)
    new_rules = left_factor(production_rules[:])
    print("After left factoring: ")
    for rule in new_rules:
        print(rule)
