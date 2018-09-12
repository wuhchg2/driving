country = input('你的國家 tw, us : ')
age = input('輸入你的年齡: ')
age = int(age)
if country == 'tw':
    if age >= 18:
        print('你可以考駕照')
    else:
        print('你還不能考駕照')
elif country == 'us':
    if age >= 16:
        print('你可以考駕照')
    else:
        print('你還不能考駕照')
   