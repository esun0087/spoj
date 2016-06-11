t = int(input())

def process_line(line):
    if len(line) == 1 and line[0] < 9:
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
        m = L // 2
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
            cur += 1
        if cur == L:
            tmp.append(1)
        L = len(tmp)
        m = L // 2
        return tmp[-1:-m-1:-1] + tmp[m:]
        
for i in range(t):
    line = input()
    line = line.strip()
    if int(line) == 10**len(line) - 1:
        line = str(10**len(line))
    line = [int(i) for i in line]
    line = process_line(line)
    line = [str(i) for i in line]
    print (''.join(line))