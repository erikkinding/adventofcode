# -*- coding: utf-8 -*-
import hashlib

class Day5:

    def __init__(self):
        self.lol = 0

    # Answer: 1a3099aa
    def day5_1(self):

        room_id = 'uqwqemis'
        password = ''
        inc = 0
        while len(password) < 8:
            m = hashlib.md5()
            m.update((room_id + str(inc)).encode('utf-8'))
            md5hash = m.hexdigest()
            if md5hash[:5] == '00000':
                password += md5hash[5:6]
                print(md5hash + ' | ' + password)
            inc += 1

        print(password)

    # Answer: 694190cd
    def day5_2(self):
        room_id = 'uqwqemis'
        password = ['','','','','','','','']
        inc = 0
        while len(set(password).intersection([''])) > 0:
            m = hashlib.md5()
            m.update((room_id + str(inc)).encode('utf-8'))
            md5hash = m.hexdigest()
            if md5hash[:5] == '00000':
                try:
                    position = int(md5hash[5:6])
                    if position < 8 and password[position] == '':
                        password[position] = md5hash[6:7]
                        print(password)
                except:
                    print('!!!')
                    pass

            inc += 1

        print('Password: ' + ''.join(password))
