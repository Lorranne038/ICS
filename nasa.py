import requests

data = '2010-07-15' # Substitua por sua data de nascimento no formato AAAA-MM-DD

resultado = requests.get('https://api.nasa.gov/planetary/apod?api_key=jkQL29tuOefSzGdPJPaRwjH2jp9bre95jsQpmFnI&date={}'.format(data))
print(resultado.status_code)
print(resultado.json())