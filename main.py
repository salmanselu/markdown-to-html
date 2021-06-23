

command = input(">>")
markdown = open(command, 'r')
html = open(command[:-2]+'html', 'w')
lines = markdown.readlines()

for i in range(len(lines)):
# Header Tags:
    if lines[i][0] == '#':
        if '######' in lines[i]:
            lines[i] = lines[i].replace('\n', ' ')
            lines[i] = lines[i].replace('######', '<h6>')
            lines[i] += '</h6>'
        elif '#####' in lines[i]:
            lines[i] = lines[i].replace('\n', ' ')
            lines[i] = lines[i].replace('#####', '<h5>')
            lines[i] += '</h5>'
        elif '####' in lines[i]:
            lines[i] = lines[i].replace('\n', ' ')
            lines[i] = lines[i].replace('####', '<h4>')
            lines[i] += '</h4>'
        elif '###' in lines[i]:
            lines[i] = lines[i].replace('\n', ' ')
            lines[i] = lines[i].replace('###', '<h3>')
            lines[i] += '</h3>'
        elif '##' in lines[i]:
            lines[i] = lines[i].replace('\n', ' ')
            lines[i] = lines[i].replace('##', '<h2>')
            lines[i] += '</h2>'
        elif '#' in lines[i]:
            lines[i] = lines[i].replace('\n', ' ')
            lines[i] = lines[i].replace('#', '<h1>')
            lines[i] += '</h1>'

    lines[i] = lines[i].replace('  \n', '<br>')
html.writelines(lines)
html.close()
markdown.close()
