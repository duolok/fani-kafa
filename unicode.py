cps = [
    range(0x00, 0x36F)
]

original_char = 'c'

count = 0
for cp in cps:
    for i in cp:
        print(f"{original_char}{chr(i)}".ljust(4), end="")
        count += 1
        if count % 16 == 0: print()

if count % 16 != 0:
    print()
