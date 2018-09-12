country = input('選擇國家代號 tw, us : ')
age = input('輸入年齡: ')
age = int(age)
if country == 'tw':
    if age >= 18:
        print('可以考駕照')
    else:
        print('還不能考駕照')
elif country == 'us':
    if age >= 16:
        print('可以考駕照')
    else:
        print('還不能考駕照')
else:
    print('只能選 tw 或 us')
