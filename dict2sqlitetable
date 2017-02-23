# coding=utf8
import sqlite3
from io import StringIO
import csv

# Find the best implementation available on this platform
try:
    from cStringIO import StringIO
except:
    from StringIO import StringIO

def get_dict_from_csv(csvilename, sep=';'):
    """lê um ficheiro e devolve um dicionario com os dados desse ficheiro.

    Keyword arguments:
        csvilename -- nome do ficheiro
        sep -- separador do ficheiro (default ;)
    """
    a = open(csvilename, 'rb')
    filecontent = a.read().replace('\0', '')
    a.close()

    csvfile = StringIO(filecontent)

    texto = csvfile.read()
    dialect = csv.Sniffer().sniff(texto, delimiters=sep)
    csvfile.seek(0)
    reader = csv.DictReader(csvfile, dialect=dialect)

    dict = []

    for line in reader:
        line.pop('', None)
        dict.append( line )

    return dict

#def create_sqlite_db_table_from_dict(dict, dbname, tablename ):

def get_fields_from_dict(dict):
    """lê um array do tipo:

    arr = [ {campo1: valor1, campo2: valor2},
            {campo1: valor3, campo2: valor4}]

    e apura as respectivas colunas (campo1 e campo2)

    Keyword arguments:
        dict -- nome do argumento
    """
    return dict[0].keys()


def build_create_table_syntax_from_dict( dict, tablename ):
    """Recebe um array e cria um statement de CREATE TABLE com base no 1º registo

    lê um array do tipo:

    arr = [ {campo1: valor1, campo2: valor2},
            {campo1: valor3, campo2: valor4}]

    esta função chama a função get_fields_from_dict(dict)

    Keyword arguments:
        dict -- nome do argumento
        tablename -- nome do argumento
    """
    keys = get_fields_from_dict( dict )
    create_table_statement = "CREATE TABLE {} (".format(tablename)
    for column in keys:
        create_table_statement += column + ','
    create_table_statement = create_table_statement[:-1] + ');'

    return create_table_statement


def load_table_from_dict(database, tablename, dict, overwrite=False):
    """Recebe um array e cria base de dados sqlite, caso não exista.
    Cria também uma tabela de nome tablename e alimenta-a com os dados do array.

    lê um array do tipo:

    arr = [ {campo1: valor1, campo2: valor2},
            {campo1: valor3, campo2: valor4}]

    esta função chama a função get_fields_from_dict(dict)

    Keyword arguments:
        database -- nome do ficheiro da bd sqlite
        tablename -- nome do argumento
        dict -- nome do argumento
        overwrite -- se for True, indica que a database pode ser esgamada
    """
    create_syntax =  build_create_table_syntax_from_dict(dict, tablename)

    con = sqlite3.connect(database)
    con.text_factory = str
    cur = con.cursor()
    if overwrite == True:
        cur.execute("DROP TABLE IF EXISTS {}".format(tablename))
    cur.execute(create_syntax)

    for reg in dict:
        #print (reg)
        first = True
        tupple = ()
        fields_statement = ''
        for i in reg:
            tupple += (reg[i],)
            if first:
                first = False
            else:
                fields_statement += ', '
            fields_statement += i

        values = ('?,'*len(tupple))[:-1]
        sql_statement =  "insert into {}({}) values ({})".format(tablename, fields_statement,values)

        cur.execute(sql_statement, tupple)
    con.commit()

    #print(tupple)

def load_table_from_csv(database, tablename, filename, overwrite=False):
    """lê um ficheiro csv e invoca a função load_table_from_dict para criar e carregar a tabela
    """

    dict = get_dict_from_csv(filename)

    load_table_from_dict(database, tablename, dict, overwrite)



#load_table_from_csv('mem.sqlite', 'tab0022', 'jan2017.txt', overwrite=True )

