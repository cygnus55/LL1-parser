import re
from prettytable import PrettyTable


def prepare_grammar(grammar):
    a = grammar[:]
    b = []
    c = []
    every_variable = []
    non_terminal = []

    for element in a:
        b.append(re.split(r"->|\|", element))

    for element in b:
        d = []
        for side in element:
            stripped_str = side.strip()
            d.append(stripped_str)
        c.append(d)

    for element in c:
        non_terminal.append(*element[0].split())
        for each in element:
            every_variable.extend(each.split())

    terminal = set(every_variable) - set(non_terminal)

    return a, b, c, non_terminal, terminal


def get_first(a, first, c, terminal, non_terminal):
    if first.get(a):
        return first[a]
    elif a in terminal:
        return {a}
    else:
        first[a] = set([])
        for element in c:
            if element[0] == a:
                for each in (element[1:]):
                    value = 0
                    while ('ε' in get_first(each.split()[value], first, c, terminal, non_terminal) and len(each.split()[value+1:]) > 0):
                        first[a].update(get_first(each.split()[value], first, c, terminal, non_terminal) - {'ε'})
                        value = value + 1
                    first[a].update(get_first(each.split()[value], first, c, terminal, non_terminal))
        return first[a]


def get_follow(follow, c, terminal, non_terminal, first):
    for element in c:
        for each in element[1:]:
            j = each.split()
            for i in range(len(j)):

                if j[i] in non_terminal:
                    if not follow.get(j[i]):
                        follow[j[i]]= set([])
                    if i < len(j)-1:
                        if j[i+1] in non_terminal:
                            value = i + 1
                            while ('ε' in first[j[value]] and len(j[value+1:]) >= 1):
                                follow[j[i]].update(first[j[value]] - {'ε'})
                                value = value + 1
                            follow[j[i]].update(first[j[value]] - {'ε'})
                            if len(j[value+1:]) <= 0:
                                follow[j[i]].update(follow[element[0]])
                        else:
                            follow[j[i]].update({j[i+1]})
                    else:
                        follow[j[i]].update(follow[element[0]])


def get_first_exp(exp, first, c, terminal, non_terminal):
        first_of_exp = set()
        value = 0
        while ('ε' in get_first(exp.split()[value], first, c, terminal, non_terminal) and len(exp.split()[value+1:]) > 0):
            first_of_exp.update([*get_first(exp[value], first, c, terminal, non_terminal) - {'ε'}])
            value = value + 1
        first_of_exp.update([*get_first(exp.split()[value], first, c, terminal, non_terminal)])
        return first_of_exp


if __name__ == "__main__":
    grammar = [
        "S -> A B",
        "B -> b B' | ε",
        "B' -> C B' | ε",
        "A -> a b A' | ε",
        "A' -> A | ε",
        "C -> c C'",
        "C' -> ε | C"
    ]

    a, b, c, non_terminal, terminal = prepare_grammar(grammar)
    first = {}
    follow = {f"{non_terminal[0]}" : {'$'}}

    for each_non_terminal in non_terminal:
        get_first(each_non_terminal, first, c, terminal, non_terminal)

    get_follow(follow, c, terminal, non_terminal, first)

    x = PrettyTable()
    x.field_names = ['Non Terminals', 'First', 'Follow']
    for each in non_terminal:
        x.add_row([each, first[each], follow[each]])
    print(x)

    print(get_first_exp("ε", first, c, terminal, non_terminal))