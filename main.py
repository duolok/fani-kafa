
def main():
    _ = +({} == {})
    __ = _ + _
    print('%\143' % (__ + 95))

    sequence = "Fani Kafa je najbolja!"
    keys = {}

    for i in range(1, 256):
        combination = ('%\143' % (_ * i))
        if combination in sequence:
            keys[i] = combination

        #print(f"{i} = {('%\143' % (_ * i))}")
        #print()

    print(sorted(keys.items()))


if __name__ == "__main__":
    main()
