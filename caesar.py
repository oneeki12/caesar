abcs =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

mix = int(input("step: "))
msg = input("message: ").upper()
res = ''

for i in msg:
    place = abcs.find(i)
    n_place = place + mix

    if i in abcs:
        res += abcs[n_place]
    else:
        res += i

print(res)
