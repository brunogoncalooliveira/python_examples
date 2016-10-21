from string import Template

mytemplate = """$title

aaaaa
bbbbb
ccccc

$subtitle

ddddd
eeeee
fffff

$list
"""

src = Template( mytemplate )

title = "This is the title"
subtitle = "And this is the subtitle"
list = ['first', 'second', 'third']
d={ 'title':title, 'subtitle':subtitle, 'list':'\n'.join(list) }

result = src.substitute(d)

print result
