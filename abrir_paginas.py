import webbrowser

paginas = [
    'https://painel.tomticket.com/login.html',
    'https://signin.aws.amazon.com/',
    'http://noc.hxbrasil.com.br/dashboards'
]


for pagina in paginas:
    webbrowser.open(pagina)
    