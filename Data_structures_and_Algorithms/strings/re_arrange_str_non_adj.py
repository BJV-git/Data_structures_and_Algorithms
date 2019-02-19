def reorder(s):
    a = sorted(sorted(s), key=s.count)
    print(a,'after sorted')
    h = len(a) // 2
    a[1::2], a[::2] = a[:h], a[h:]

    return ''.join(a)*(a[-1:]!=a[-2:-1])

    print(a)

print(reorder('aaabb'))