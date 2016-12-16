# -*- coding: utf-8 -*-
import hashlib
import time

class Day5:

    def __init__(self):
        self.haxxor = True

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
        while '' in password:
            m = hashlib.md5()
            m.update((room_id + str(inc)).encode('utf-8'))
            md5hash = m.hexdigest()
            if md5hash[:5] == '00000':
                try:
                    position = int(md5hash[5:6])
                    if position < 8 and password[position] == '':
                        password[position] = md5hash[6:7]
                except:
                    pass

            # visualized h4xx0r output
            if self.haxxor and int(time.time()) % 3 == 0:
                haxx = ''
                for index, c in enumerate(password):
                    if c == '':
                        haxx += md5hash[index:index+1]
                    else:
                        haxx += '[' + c + ']'

                print(haxx)

            inc += 1

        print('Password: ' + ''.join(password))
