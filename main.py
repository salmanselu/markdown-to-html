

command = input(">>")
markdown = open(command, 'r')
html = open(command[:-2]+'html', 'a')
lines = markdown.readlines()

for line in lines:
# Header Tags:
    if line[0] == '#':
        if '######' in line:
            line = line.replace('######', '<h6>')
            line += '<h6>'
        if '#####' in line:
            line = line.replace('#####', '<h5>')
            line += '<h5>'
        if '####' in line:
            line = line.replace('####', '<h4>')
            line += '<h4>'
        if '###' in line:
            line = line.replace('###', '<h3>')
            line += '<h3>'
        if '##' in line:
            line = line.replace('##', '<h2>')
            line += '<h2>'
        if '#' in line:
            line = line.replace('#', '<h1>')
            line += '<h1>'
    html.write(line)
html.close()
markdown.close()
