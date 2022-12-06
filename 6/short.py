line = open('6/input2.txt').read().strip()

def test(length, i):
    return len(set(line[i-length:i])) == length

def f(length):
    return [test(length, i) for i in range(len(line))].index(True)

print(f"a: {f(4)}, b: {f(14)}")
