t = int(input())


def find_first_big_pali(line):
    if len(line) == 1:
        return line, False
    if len(line) == 2:
        if line[0] == line[1]:
            return line, False
        line[0], line[1] = min(line[0], line[1]) + 1, min(line[0], line[1]) + 1
        return line, True
    line[1:-1], state = find_first_big_pali(line[1:-1])
    a, b = line[0], line[-1]
    if a != b:
        state = True
        if state:
            a, b = min(a, b), min(a,b)
        else:
            
            a, b = min(a, b) + 1, min(a, b) + 1
    line[0], line[-1] = a, b
    
    return line, state
    
def re_change_line(line):
    L = len(line)
    if L % 2 == 1:
        line[L//2] = (line[L//2] + 1) % 10
        if line[L//2] == 0:
            for i in range(L // 2 - 1, -1, -1):
                line[i] = (line[i] + 1) % 10
                line[L-i] = (line[L-i] + 1) % 10
                if line[i] != 0:
                    break
            if line[0] == 0:
                line.insert(0, 1)
                return find_first_big_pali(line)
        else:
            return line, True
    else:
        for i in range(L // 2, -1, -1):
            line[i] = (line[i] + 1) % 10
            line[L-i] = (line[L-i] + 1) % 10
            if line[i] != 0:
                break
        if line[0] == 0:
            line.insert(0, 1)
            return find_first_big_pali(line)
        
for i in range(t):
    line = input()
    line = line.strip()
    if int(line) == 10**len(line) - 1:
        line = str(10**len(line))
    line = [int(i) for i in line]
    line, s = find_first_big_pali(line)
    while not s:
        line, s = re_change_line(line)
    print (line)