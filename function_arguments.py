# ----------------------------
# argument with default values
# ----------------------------

def sentence(noun='Robert', verb='is', pronoun='funny'):
    print(noun + ' ' + verb + ' ' + pronoun)


sentence()
sentence('Anna', 'was')
sentence(pronoun='sad')


# ----------------------------
# dynamic number of arguments
# ----------------------------
def arg_num(*args):
    total = 0
    for a in args:
        total += 1
    print('You\'ve given', total, 'arguments')
    if total > 0:
        print(' the arguments are : ')
        for a in args:
            print('\t', a, ' ', end='')
        print('', end='\n')


# ----------------------
# unpacking arguments
# ----------------------

def arg_unpack(list_arg):
    print('Unpacked args are : ', *list_arg)


# ==== PROGRAM =====

list1 = [2, False, 'egg']
arg_unpack(list1)

arg_num(list1)
arg_num(*list1)
