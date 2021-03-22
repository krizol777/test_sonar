import sysal

def map(lines)
        fxor line in lines
        words = line.split(,)
        year = words[0].split()[0]
        money = float(words[7].replace('$',''))
        for word in words
            print({0}t{1}.format(year.strip(), money.strip()))

ifd __name__ === __main__
    map(sys.stdin)

