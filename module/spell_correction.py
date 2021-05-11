import xmlrpc.client

# url = 'http://104.43.10.38:9811/RPC2'
# url = 'http://2afbaac6632a.ngrok.io/RPC2'
url = 'localhost:8888/RPC2'
server = xmlrpc.client.ServerProxy(url)


def translate(word):
    response = server.translate({"text": word})
    return response.get('text')


def correct(sentence):
    return translate(sentence)
