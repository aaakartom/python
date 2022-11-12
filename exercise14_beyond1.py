database_users = {'cool2010':'01WQa', 'jack':'123456ornk', 'she9834':'32y624'}
user_login = input('Enter username:')
user_password = input('Enter password:')


if user_password in database_users.values() and user_login in database_users.keys():
    print("Logged in successfully!")
else:
    print('Wrong username or password!')
