#!/usr/bin/python3
for num in range(0, 99):
    print('{} = 0x{:x}'.format(num, num))


5-print_comb2.py

#!/usr/bin/python3
for num in range(0, 99):
    print('{:02d}, '.format(num), end='')
print('99')
