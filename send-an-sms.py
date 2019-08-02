import nexmo

client = nexmo.Client(key='1ab7c0c7', secret='YgseZGHunR4thMOQ')

client.send_message({
    'from': 'CM',
    'to': 639676877218,
    'text': 'FUCK YOU KANG BUANGA KA ! KAMATAY ! BC2 PA ! LECHE KA ! ',
})