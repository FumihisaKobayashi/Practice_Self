

#入力文を返す
@respond_to('')

def respond_func(message):
    #メッセージ文取得
    mes = message.body['text']

    message.reply(mes)
