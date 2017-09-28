def number_needed(a, b):
    
    common=set([c for c in a])&set([c for c in b])
    print(len(common))
    print(len(set([c for c in a])))
    print(len(set([c for c in b])))
    first_deletions=len(set([c for c in a])-common)+len(set([c for c in b])-common)
    common_min_freq={c:min([a.count(c),b.count(c)]) for c in common}
    print(common_min_freq)
    print({c:a.count(c) for c in common})
    print({c:b.count(c) for c in common})
    second_deletions=sum([abs(a.count(c)-b.count(c)) for c in common])
    return first_deletions+second_deletions

a = input().strip()
b = input().strip()

print(number_needed(a, b))
