t = int(input())

def process_line(line):
    if len(line) == 1 && line[0] < 9:
        return  [line[0] + 1]
    elif len (line) == 1:
        return [11]
    else:
        tmp = list(line)
        L = len(tmp)
        l, r = 0, L - 1
        while l < r:
            tmp[r] =tmp[l]
            r -= 1
            l += 1
        if tmp > line:
            return tmp 
        cur = L // 2
        tmp[cur] += 1
        if tmp[cur] > 9:
            c = 1
        else:
            c = 0
        while c and cur < L:
            tmp[cur] = 0
            tmp[cur+1] += 1
            if tmp[cur+1] > 9:
                c = 1
            else:
                c = 0
        if cur == L:
            tmp.append(1)
        
        
for i in range(t):
    line = input()
    line = line.strip()
    if int(line) == 10**len(line) - 1:
        line = str(10**len(line))
    line = [int(i) for i in line]
    print (line)