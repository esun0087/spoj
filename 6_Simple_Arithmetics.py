t = int(input())
oper = ['+', '-', '*']

def process_add(a, b):
    a = a[::-1]
    b = b[::-1]
    L = max(len(a), len(b))
    min_l = min(len(a), len(b))
    ans = [0 for i in range(L+1)]
    add_data = 0
    for i in range(min(len(a), len(b))):
        x = a[i] + b[i] + add_data
        add_data = x // 10
        ans[i] = x % 10
    if len(a) > len(b):
        for i in range(len(b), len(a)):
            x = ans[i] + add_data + a[i]
            add_data = x // 10
            ans[i] = x % 10
    elif len(a) < len(b):
        for i in range(len(a), len(b)):
            x = ans[i] + add_data + b[i]
            add_data = x // 10
            ans[i] = x % 10
    else:
        ans[min_l] = add_data
    ans = ans[::-1]
    max_len = len(b)+1
    ans_pos = 0
    for i, k in enumerate(ans):
        if k != 0:
            if len(ans) - i >= max_len:
                max_len = len(ans) - i
            ans_pos = i
            break
    ans = [str(i) for i in ans]
    a = ''.join([str(i) for i in a[::-1]])
    b = ''.join([str(i) for i in b[::-1]])
    print (' '*(max_len - len(a))+a)
    print (' '*(max_len - len(b) - 1) + '+' + b)
    print ('-' * (max_len))
    print (' '* (max_len - (len(ans) - ans_pos)) + ''.join(ans[ans_pos:]))
    return ans[::-1]

def process_reduce(a, b):
    L = max(len(a), len(b))
    a = a[::-1]
    b = b[::-1]
    ans = [0 for i in range(L+1)]
    reduce_data = 0
    for i in range(min(len(a), len(b))):
        t = a[i] - reduce_data
        if t < b[i]:
            t += 10
            reduce_data = 1
        else:
            reduce_data = 0
        x = t - b[i]
        ans[i] = x
    for i in range(len(b), len(a)):
        t = a[i] - reduce_data
        if t < 0:
            t += 10
            reduce_data = 1
        else:
            reduce_data = 0
        x = t - 0
        ans[i] = x
    ans = ans[::-1]
    max_len = len(b)+1
    ans_pos = 0
    for i, k in enumerate(ans):
        if k != 0:
            if len(ans) - i >= max_len:
                max_len = len(ans) - i
            ans_pos = i
            break
    ans = [str(i) for i in ans]
    a = ''.join([str(i) for i in a[::-1]])
    b = ''.join([str(i) for i in b[::-1]])
    all_max_len = max(len(a), len(b) + 1, max_len)
    print (' '*(all_max_len - len(a))+a)
    print (' '*(all_max_len - len(b) - 1) + '-' + b)
    print (' '*(all_max_len - max_len) + '-' * (max_len))
    print (' '* (all_max_len - (len(ans) - ans_pos)) + ''.join(ans[ans_pos:]))
    return ans[::-1]

def help_add(a, b):
    a = a[::-1]
    b = b[::-1]
    L = max(len(a), len(b))
    min_l = min(len(a), len(b))
    ans = [0 for i in range(L+1)]
    add_data = 0
    for i in range(min(len(a), len(b))):
        x = a[i] + b[i] + add_data
        add_data = x // 10
        ans[i] = x % 10
    if len(a) > len(b):
        for i in range(len(b), len(a)):
            x = ans[i] + add_data + a[i]
            add_data = x // 10
            ans[i] = x % 10
    elif len(a) < len(b):
        for i in range(len(a), len(b)):
            x = ans[i] + add_data + b[i]
            add_data = x // 10
            ans[i] = x % 10
    else:
        ans[min_l] = add_data
    ans = ans[::-1]
    return ans
def process_mul(a, b):
    a = a[::-1]
    b = b[::-1]
    L = max(len(a), len(b))
    ans = []
    for j in range(len(b)):
        tmp_ans = [0 for xx in range(len(a) + 1)]
        add_data = 0
        for i in range(len(a)):
            x = a[i] * b[j] + add_data
            add_data = x // 10
            x = x % 10
            tmp_ans[i] = x
        tmp_ans[len(a)] = add_data
        ans.append(tmp_ans[::-1])
    final_ans = [0 for i in range(len(a) + len(b) + 1)]

    if len(ans) <= 1:
        pass
    else:
        for i, tmp in enumerate(ans):
            final_ans = help_add(final_ans, tmp+[0] * i)
        ans.append(final_ans)
    max_len = len(b) + 1
    first_max_len = max_len
    for i, k in enumerate(ans[0]):
        if k != 0:
            if len(ans[0]) - i >= max_len:
                first_max_len = len(ans[0]) - i
            break
    
    for i, k in enumerate(ans[-1]):
        if k != 0:
            if len(ans[-1]) - i >= max_len:
                max_len = len(ans[-1]) - i
            second_max_len = len(ans[-1]) - i
            break
    a = ''.join([str(i) for i in a[::-1]])
    b = ''.join([str(i) for i in b[::-1]])
    all_max_len = max(len(a), len(b) + 1, max_len)
    print (' '*(all_max_len - len(a))+a)
    print (' '*(all_max_len - len(b) - 1) + '*' + b)
    print (' '*(all_max_len - first_max_len) + '-' * (first_max_len))
    tag = False
    for i, arr in enumerate(ans):
        for j in range(len(arr)):
            if arr[j] != 0:
                arr = arr[j:]
                break
        tmp = ''.join([str(tt) for tt in arr])
        if i == len(ans) - 1:
            if tag:
                print (' '* (all_max_len-second_max_len) + '-' * (second_max_len))
            print (' '* (all_max_len - (len(tmp))) + ''.join(tmp))
        else:
            tag = True
            if tmp == '0' * len(tmp):
                print (' '*(all_max_len - i-1)+'0')
            else:
                print (' '*(all_max_len - len(tmp)-i)+tmp)

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
                process_add(a, b)
            if op == '-':
                process_reduce(a, b)
            if op == '*':
                process_mul(a, b)
            break
            
    