s = 'abHbbccDDDDD'
d = {}
for c in s:
    if c not in d.keys():
        d[c] = 1
    else:
        d[c] = d[c] + 1
for k, v in d.items():
    print('{} = {} times'.format(k,v))
