import pywhatkit

def send_message_inst():
    mobile = input("Введите номер получателя: ")
    message = input("Введите сообщение: ")
    pywhatkit.sendwhatmsg_instantly(phone_no=mobile, message=message)

def main():
    send_message_inst()

if __name__ == '__main__':
    main()