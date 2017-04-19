# coding=utf8
from openpyxl import load_workbook
from pprint import pprint

def get_Excel_as_dict(file, sheet, getDictBy=None, fields=[]):

    wb2 = load_workbook(file)
    sheet = wb2[sheet]

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
                if row[header[ chave ]].value not in arr:
                    arr[row[header[ chave ]].value] = []
                tmp = {}
                for i in fields:
                    tmp[i] = row[header[ i ]].value
                arr[row[header[ chave ]].value].append(tmp)

    return arr


data = get_Excel_as_dict('Tabelas.xlsx', 'Tabelas', getDictBy='Grupo', fields=['Desc completa', u'Tabela' ])
