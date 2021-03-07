poem = open('Mikhail Lermontov.txt', encoding='utf-8')
core = open('Core.html', 'r')

poem_lines = poem.readlines()

with open('Site.html', 'w', encoding='utf-8') as site:
    acc = 0
    idk = 0
    for item in core:
        site.write(item)
        acc += 1
        if acc == 6:
            site.write(4*' ' + 'Михаил Лермонтов')
        if acc == 23:
            site.write('<p>')
            for line in poem_lines:
                site.write(8*' ' + line + '<br>')
            site.write('</p>')
            site.write('\n')
                    
poem.close()
core.close()
site.close()
