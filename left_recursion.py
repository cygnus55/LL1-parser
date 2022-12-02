import re


def read_rules(filename):
    with open(filename, "r") as f:
        rules = list(map(lambda x: x.strip(), f.readlines()))
        return rules


def left_recursion(grammar):
    grammar = grammar.strip()
    a = re.split("\n", grammar)
    b = []
    c = []
    new_rules = []

    for element in a:
        b.append(re.split(r"->|\|", element))

    for element in b:
        d = []
        for side in element:
            stripped_str = side.strip()
            # e.append(side.split())
            d.append(stripped_str)
            # e = [j for sub in e for j in sub]
        c.append(d)
    print(c)

    whole_flag = False
    for count, element in enumerate(c):
        flag = False
        recursive = []
        nonrecursive = []
        for i in range(1, len(element)):
            if element[i].startswith(f"{element[0]} "):
                recursive.append(element[i][len(element[0]):].strip())
                flag = True
                # print("left recursion")
                if not whole_flag:
                    whole_flag =True
            else:
                nonrecursive.append(element[i])
        # print(recursive)
        # print(nonrecursive)
        if flag:
            c[count] = c[count][:1]
            new_variable = element[0]
            repeat = True
            while repeat:
                if any(new_variable in each for each in c):
                    new_variable = f"{new_variable}'"
                else:
                    repeat = False
            for nr in nonrecursive:
                c[count].append(f"{nr} {new_variable}")
            new = [f"{new_variable}"]
            for r in recursive:
                new.append(f"{r} {new_variable}")
            new.append("ε")
            c.append(new)
    if whole_flag:
        print('The grammar after removing left recursion is:')
        # print(c)
        for element in c:
            joined = (' | '.join(str(a) for a in element[1:]))

            print(f"{element[0]} -> {joined}")
            new_rules.append(f"{element[0]} -> {joined}")

    else:
        print('The grammar is not left recursive')
        new_rules = a

    return new_rules