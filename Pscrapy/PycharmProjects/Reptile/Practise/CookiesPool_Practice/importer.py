from db  import AccountRedisClient

conn = AccountRedisClient(name='tet')

def dowm(account, parm='---'):
    username, password = account.split(parm)
    result = conn.set(username,password)
    print('账号:{},密码:{}'.format(username,password))
    print('录入成功' if result else '录入失败')

def scan():
    print('请输入账号密码组, 输入exit退出读入')
    while True:
        account = input()
        if account == 'exit':
            break
        dowm(account)


if __name__ == "__main__":
    scan()
