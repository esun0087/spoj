import string
letters = set(string.ascii_lowercase)
oper = {'+':0, '-':0, '*':1, '/':1, '^':2, '(':3, ')':3}
t = int(input())

def parse(line):
    letter_stack = []
    oper_stack = []
    real_list = []
    for c in line:
        if c in letters:
            letter_stack.append(c)
        else:
            if len(oper_stack) == 0:
                oper_stack.append(c)
            else:
                if c == '(':
                    oper_stack.append(c)
                elif c == ')':
                    while len(oper_stack) > 0:
                        #print (c, oper_stack)
                        #input()
                        k = oper_stack[-1]
                        if k != '(':
                            if k != '(' and k != ')':
                                letter_stack.append(k)
                            oper_stack.pop()
                        else:
                            oper_stack.pop()
                            break
                else:
                    while len(oper_stack) > 0:
                        k = oper_stack[-1]
                        if k == '(' or k == ')':
                            break

                        if oper[k] > oper[c]:
                            if k != '(' and k != ')':
                                letter_stack.append(k)
                            oper_stack.pop()
                        else:
                            break
                    oper_stack.append(c)
    letter_stack.extend(oper_stack[::-1])
    return letter_stack
                        
                        
for i in range(t):
    line = input()
    line = line.strip()
    line = list(line)
    ans = parse(line)
    print (''.join(ans))