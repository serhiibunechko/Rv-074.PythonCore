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


kilobytes = size / 1000

if kilobytes >= 1000:
    megabytes = (kilobytes // 1000)
    kilobytes = kilobytes - (megabytes * 1000)
else:
    megabytes = 0

print(f'Filesize = {megabytes} MB and {round(kilobytes, 3)} KB')

