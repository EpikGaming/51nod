from itertools import permutations
S = input()
print('\n'.join(sorted(set(map(''.join,list(permutations(S)))))))