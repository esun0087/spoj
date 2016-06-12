t = int(input())
oper = ['+', '-', '*']

def process_add(a, b):
    a = a[::-1]
    b = b[::-1]
    L = max(len(a), len(b))
    min_l = min(len(a), len(b))
    ans = [0 for i in range(L+10)]
    add_data = 0
    for i in range(min(len(a), len(b))):
        x = a[i] + b[i] + add_data
        add_data = x // 10
        ans[i] = x % 10
    ans[min_l] = add_data
    return ans[::-1]

def process_reduce(a, b):
    L = max(len(a), len(b))
    a = a[::-1]
    b = b[::-1]
    min_l = min(len(a). len(b))
    ans = [0 for i in range(L+10)]
    reduce_data = 0
    for i in range(min(len(a), len(b))):
        a[i] -= reduce_data
        if a[i] < b[i]:
            a[i] += 10
            reduce_data = 1
        else:
            reduce_data = 0
        x = a[i] - b[i]
        ans[i] = x
    return ans[::-1]

def process_mul(a, b):
    add_data = 0
    a = a[::-1]
    b = b[::-1]
    L = max(len(a), len(b))
    ans = []
    for j in range(len(b)):
        tmp_ans = [0 for xx in range(L * 2 + 10)]
        for i in range(len(a)):
            x = a[i] * b[j] + add_data
            add_data = x // 10
            x = x % 10
            tmp_ans[i+j] = x
        tmp_ans[len(a)+j] = add_data
        ans.append(tmp_ans[::-1])
    final_ans = [0 for i in range(L * 2 + 10)]
    if len(ans) <= 1:
        ans.append(ans[0])
    else:
        for tmp in ans:
            final_ans = process_add(final_ans, tmp)
        ans.append(final_ans)
    return ans

for j in range(t):
    line = input()
    line = line.strip()
    for op in oper:
        if op in line:
            a, b = line.split(op)
            a = [int(i) for i in list(a)]
            b = [int(i) for i in list(b)]
            if op == '+':
                ans = process_add(a, b)
            if op == '-':
                ans = process_reduce(a, b)
            if op == '*':
                ans = process_mul(a, b)
            break
            
    