in_msg = 'google.com: domain of oliviagrish@mail.ru designates 94.100.185.63'
atpos = in_msg.find('@')
sppos = in_msg.find(' ', atpos)
print(atpos)
print(sppos)
host = in_msg[atpos + 1 : sppos]
print(host)
