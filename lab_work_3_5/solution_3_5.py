"""
Write a program that will take username and password,
checks if they are in registered users dictionary,
if they are present – print “Access Granted”,
if not – handle it using KeyError Eception handling.
Raise RuntimeError and handle it if the name is empty.
"""
registered_users = {
    'Bohdan':'123z',
    'Galyna':'321d',
    'Ivan':'654k',
    'Vitaly':'876f',
    'Yevgen': '987a'
}
try:
    username = input('Please, enter your username:')
    password = input('Please, enter your password:')

    if username == '':
        raise RuntimeError

    if registered_users[username] == password:
            print('Access Granted!')
            if not password.isalnum():
                while True:
                    print('You password is not alphanumeric!')
                    new_password = input('Please, enter correct new password value:')
                    if new_password.isalnum():
                        registered_users[username] = new_password
                        print('Your new password successfully saved!')
                        break
    else:
        raise Exception

except RuntimeError:\
    print('Empty username passed!')

except KeyError:
    print('There is no user with such username!')

except Exception:
    print('Incorrect password!')