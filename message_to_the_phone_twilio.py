from twilio.rest import Client
from TokenSid import account_sid, token_twillio,number#Token import, SID, recipient's phone number


def send_message(text='Hello white rabbit', receiver=number):
    try:
        account = account_sid
        token = token_twillio

        client = Client(account, token)

        message = client.messages.create(
            body=text,
            from_='+14055925046',
            to=receiver,

        )

        return 'The message has been sent'
    except Exception as ex:
        return 'Error message: Run Lola run!!!!'


def main():
    text = input('Please enter message')
    print(send_message(text=text, receiver=number))


if __name__ == '__main__':
    main()
