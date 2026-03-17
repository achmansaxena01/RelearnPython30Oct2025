s = 'abHbbccDDDDD'
d = {}
for c in s:
    d[c] = d.get(c,0) + 1
for k, v in d.items():
    print('{} = {} times'.format(k,v))
