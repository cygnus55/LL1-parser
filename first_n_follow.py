import re
from prettytable import PrettyTable
grammars  = ['''S -> A
A -> a A''
A' -> d A' | e A' | ε
A'' -> B A' | C A'
B -> b B c | f
C -> g'''
, '''S -> A a A b | B b B a
A -> ε
B -> ε'''
,'''S -> A B C
A -> D E F
B -> ε
C -> ε
D -> ε
E -> ε
F -> ε''',
'''E -> T E'
E' -> + T E' | ε
T -> F T'
T' -> * F T' | ε
F -> ( E ) | id
''']

for grammar in grammars:
    grammar = grammar.strip()
    a = re.split("\n", grammar)
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
        joined = (' | '.join(str(a) for a in element[1:]))
        non_terminal.append(*element[0].split())
        for each in element:
            every_variable.extend(each.split())
        
        
    terminal = set(every_variable) - set(non_terminal)

    print(f'The given grammar is:\n{grammar}')
    def get_first(a, first, c):
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
                        while ('ε' in get_first(each.split()[value], first, c) and len(each.split()[value+1:]) > 0):
                            first[a].update(get_first(each.split()[value], first, c) - {'ε'})
                            value = value +1 
                        first[a].update(get_first(each.split()[value], first, c))
            return first[a]

    def get_follow( follow, c):
        for element in c:
            for each in element[1:]:
                j = each.split()
                for i in range(len(j)):
                    
                    if j[i] in non_terminal:
                        if not follow.get(j[i]):
                            follow[j[i]]= set([])
                        if i < len(j)-1:
                            if j[i+1] in non_terminal:
                                value = i+1
                                while ('ε' in first[j[value]] and len(j[value+1:]) >= 1):
                                    follow[j[i]].update(first[j[value]] - {'ε'})
                                    value = value+1
                                follow[j[i]].update(first[j[value]] - {'ε'})
                                if len(j[value+1:]) <= 0:
                                    follow[j[i]].update(follow[element[0]])
                            else:
                                follow[j[i]].update({j[i+1]})
                        else:               
                            follow[j[i]].update(follow[element[0]])
            
    first = {}
    follow = {f"{non_terminal[0]}" : {'$'}}

    for each_non_terminal in non_terminal:
        get_first(each_non_terminal, first, c)

    get_follow(follow,c)
    
    x = PrettyTable()
    x.field_names = ['Non Terminals', 'First', 'Follow']
    for each in non_terminal:
        x.add_row([each, first[each], follow[each]])
    print(x)