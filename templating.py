rom string import Template
#open the file

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


#filein = open( 'foo.txt' )
#read it
#src = Template( filein.read() )
src = Template( mytemplate )
#document data
title = "This is the title"
subtitle = "And this is the subtitle"
list = ['first', 'second', 'third']
d={ 'title':title, 'subtitle':subtitle, 'list':'\n'.join(list) }
#do the substitution
result = src.substitute(d)
print result
