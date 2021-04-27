# encoding: utf-8

while True:
    size = input('Please enter filesize in bytes: ').strip()

    if size.isdigit():
        size = int(size)
        break
    else:
        print()
        print('Please enter correct numerical value.')
        print()


kilobytes = size / 1024

if kilobytes >= 1024:
    megabytes = (kilobytes // 1024)
    kilobytes = kilobytes - (megabytes * 1024)
else:
    megabytes = 0

print(f'Filesize = {megabytes} MB and {round(kilobytes, 3)} KB')

