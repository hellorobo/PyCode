import json
from difflib import get_close_matches


folder_path = r"C:\Users\rjakowenko\Documents\700_PYTHON\PyCode\Udemy Python Mega Course\files"
data = json.load(open(folder_path+'\data.json'))
word = ''
reply = ''


def listtostring(lst):
    msg = ''
    i = 0
    for l in lst:
        i = i + 1
        msg = msg + '\t' + str(i) + ') ' + str(l) + '\n'
    return msg


def translate(word):
    try:
        msg = data[word.lower()]
    except KeyError:
        msg = '-1'
    except:
        msg = '-9'
    return msg


while word.lower() != 'q':
    try:
        word = input('enter word to get description or Q to exit: ')
        if word.lower() != 'q':
            print('\n'+word.upper()+' :')
            msg = (translate(word))
            if msg == '-1':
                reply = ''
                match = get_close_matches(word, data.keys())[0]
                if len(match) > 0:
                    while reply.lower() not in ('y', 'n'):
                        reply = input("did you mean \"%s\" instead y/n ? " % match.upper())
                        if reply == 'y':
                            print('\n' + match.upper() + ' :')
                            print(listtostring(translate(match)))
                        elif reply == 'n':
                            break
                else:
                    msg = 'Word not found in dictionary'
            elif msg == '-9':
                msg = 'Ooops! Error occurred!'
            else:
                print(listtostring(msg))
        else:
            print('Goodbye!')
    except:
        print('oh no! there was some error, try again')
