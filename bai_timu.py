import string
letters = string.ascii_letters
digits = string.digits
oper = ['*', '(', ')', '[', ']']
key_words = ['int', 'const']
def find_param_word(line):
    word = ''
    for c in line:
        if c in letters:
            word += c
        elif c in digits:
            word += c
        elif c in oper:
            if word in key_words :
                word = ''
            else:
                if word != '':
                    return word
        elif c == ' ' or c == ',' or c == ';':
            if word in key_words :
                word = ''
            else:
                if word != '':
                    return word

def parse_left(line):
    type_c = ''
    block_count = 0
    for i, c in enumerate(line):
        if c == ' ':
            if type_c != '':
                return type_c, i
            else:
                continue
        if c == '*':
            if type_c != '':
                return type_c, i
            else:
                type_c += c
                return type_c, i+1
        elif c == '(':
            if type_c != '':
                return type_c, i+1
            else:
                continue
        else:
            type_c += c
    return type_c, len(line)
       
def parse_right(line):
    type_c = ''
    block_count = 0
    for i, c in enumerate(line):
        if c == ' ':
            continue
        if c == ';':
            return type_c, i
        elif c == ')':
            if block_count == 0:
                return type_c, i+1
            else:
                block_count -= 1
        else:
            if c == '(':
                block_count += 1
        type_c += c
    
def parse_line(line):
    param_word = find_param_word(line)
    l_index = line.index(param_word)
    r_index = l_index + len(param_word)
    ans = []
    while 1:
        l_line = line[:l_index][::-1]
        l_result, pos_l = parse_left(l_line)
        r_result, pos_r = parse_right(line[r_index:])
        if l_result == '' and r_result == '':
            break
        ans.append(r_result)
        ans.append(l_result[::-1])
        print ('r\t%s\tl\t%s' % (r_result, l_result[::-1]))
        input()
        l_index -= pos_l
        r_index += pos_r
    print (ans[-1] + ' ' + param_word + ':', end = '')
    for i in ans[:-1]:
        if i == '*':
            print ('->', end= '')
        else:
            print (i, end = '')
    print (';')

s = 'int const*const*const func[5];'
parse_line(s)
    