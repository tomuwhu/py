from urllib.request import urlopen
with urlopen('https://es6.eu/') as response:
    for key, line in enumerate(response):
        line = line.decode('utf-8')
        print( key, line, end="" )