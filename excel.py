from openpyxl import load_workbook
from pprint import pprint

def get_Excel_as_dict(file, getDictBy=None, fields=[]):

    wb2 = load_workbook(file)
    sheet = wb2['Sheet1']

    first = True

    if getDictBy == None:
        raise Exception('O campo getDictBy tem que ter um valor que corresponde a um nome de coluna no ficheiro excel')

    header = {}

    chave = getDictBy
    arr = {}

    for row in sheet.rows:
        if first:
            for i in row:
                header[ i.value ] = i.col_idx - 1
            first = False
        else:
            if row[header[ chave ]].value != '':
                for i in fields:
                    if row[header[ chave ]].value not in arr:
                        arr[row[header[ chave ]].value] = {}
                    arr[row[header[ chave ]].value][i] = row[header[ i ]].value
    return arr

pprint(get_Excel_as_dict('example.xlsx', getDictBy='MyKeyField', fields=['Field1', u'Field2' ]))
