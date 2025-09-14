def cesar_crypt(message: str, shift: int) -> str: #функція яка шифруе повідомлення і зсувае кожну букву через shift
    message_enc = ''           #пустий рядок куди будемо додавати зашифромане символи
    for i in message:         # проходимо по кожному символу у повідомленні
        message_enc += chr(ord(i) + shift)         # беремо символ переробляемо в число потім пересуваемо його і назад у символ
    return message_enc                       # повертаемо шифроване повідомлення

def decrypt(message: str, shift: int) -> str:       #функція расшифрування прауюе по такому ж самому принципу
    return cesar_crypt(message, -shift)            # тільки тут ми шефруемо назад, а ні вперед через знак "-"

message_to_enc = input('Enter message to enc: ')  #вводимо повідомленя яке хочемо зашифрувати
shift_n = int(input('Enter key: '))               # вводимо ключ на скильки позицій ми хочема зсунути символи

encr = cesar_crypt(message_to_enc, shift_n)        #шифружмо повідомлення
print(encr)                                    #виводимо зашифроване повідомлення
print(decrypt(encr, shift_n))             # тут ми разшифровуемо назад повідомлення .
