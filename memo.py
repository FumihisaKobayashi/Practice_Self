

#入力文を返す(ワイルドカード)
@respond_to('.*')

def respond_func(message):
    #メッセージ文取得(そのまま返す)
    mes = message.body['text']

    message.reply(mes)

