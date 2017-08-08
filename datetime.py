import datetime

timestamp = str( unicode(datetime.datetime.now()).replace('-','').replace(' ','_').replace(':', '').replace('.','')[:-3])
print('backup_{}.zip'.format(timestamp))
