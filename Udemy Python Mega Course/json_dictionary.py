import json

folder_path = r"C:\Users\rjakowenko\Documents\700_PYTHON\PyCode\Udemy Python Mega Course\files"
data = json.load(open(folder_path+'\data.json'))
word = ''

def listtostring(lst):
    msg = ''
    i = 0
    for l in lst:
        i = i + 1
        msg = msg + '\t' + str(i) + ') ' + str(l) + '\n'
    return msg


def translate(word):
    try:
        msg = listtostring(data[word.lower()])
    except KeyError:
        msg = 'no such word in my dictionary'
    except:
        msg = 'oops! an error occurred'
    return msg


while word.lower() != 'q':
    try:
        word = input('enter word to get description or Q to exit: ')
        if word.lower() != 'q':
            print('\n'+word.upper()+' :')
            print(translate(word))
    except:
        print('oh no! there was some error, try again')
