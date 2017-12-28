file = 'text.txt'

fw = open(file, 'w')
fw.write('this is a test file\n')
fw.write('second line')
fw.close()

fr = open(file,'r')
text = fr.read()
fr.close()

print('from file: ', file, '\n', text)

