def longest_common_prefix(strs):
    str=''
    equ=False
    for a in strs:
        if len(str)<len(a):
            str=a
            equ = False
        elif len(str)==len(a):
            equ = True
    if not equ:
        return str
    else:
        return ''
print(longest_common_prefix(['llll','g','fg','llll','llll','ll']))