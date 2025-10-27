from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas = ['João', 'Maria', 'José', 'Ana']

camisetas = [['Preta', 'Branca', 'Azul'], ['P', 'M', 'G'], ['Masculina', 'Feminina']]

print_iter(combinations(pessoas, 2))
print("-----------------")
print_iter(permutations(pessoas, 2))
print("-----------------")
print_iter(product(*camisetas))
 