import string
letters = set(string.ascii_letters)
oper = {'+':0, '-':0, '*':1, '/':1, '^':2, '(':3, ')':3}
t = int(input())

class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = ''
        
def parse(line):
    letter_stack = []
    oper_stack = []
    real_list = []
    for c in line:
        if c in letters:
            node = Node()
            node.value = c
            letter_stack.append(node)
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
                                node = Node()
                                node.value = k
                                node.right = letter_stack.pop()
                                node.left = letter_stack.pop()
                                letter_stack.append(node)
                            oper_stack.pop()
                        else:
                            oper_stack.pop()
                            break
                else:
                    while len(oper_stack) > 0:
                        k = oper_stack[-1]
                        if k == '(' or k == ')':
                            break
                        if oper[k] >= oper[c]:
                            if k != '(' and k != ')':
                                node = Node()
                                node.value = k
                                node.right = letter_stack.pop()
                                node.left = letter_stack.pop()
                                letter_stack.append(node)
                            oper_stack.pop()
                        else:
                            break
                    oper_stack.append(c)
    while len(oper_stack) != 0:
        node = Node()
        node.value = oper_stack.pop()
        node.right = letter_stack.pop()
        node.left = letter_stack.pop()
        letter_stack.append(node)
        
    
    return letter_stack

print_oper = {'+':0, '-':0, '*':1, '/':1}
for i in letters:
    print_oper[i] = 0
def print_node(node):
    if node.value in letters:
        print (node.value, end = '')
        return
    
    l_node = node.left
    r_node = node.right
    if print_oper[node.value] > print_oper[l_node.value]:
        if l_node.value not in letters:
            print ('(', end='')
        print_node(l_node)
        if l_node.value not in letters:
            print (')', end = '')
        print (node.value, end = '')
        print_node(r_node)
    if print_oper[node.value] == print_oper[l_node.value]:
        print_node(l_node)
        if node.value == '-' or node.value == '/':
            print ('(', end = '')
            print (node.value, end = '')
            print (')', end='')
            print_node(r_node)
        else:
            print (node.value, end = '')
            print_node(r_node)
    if print_oper[node.value] < print_oper[l_node.value]:
        print_node(l_node)
        print (node.value, end = '')
        print_node(r_node)
for i in range(t):
    line = input()
    line = line.strip()
    line = list(line)
    ans = parse(line)
    node = ans[0]
    print_node(node)
    print ()