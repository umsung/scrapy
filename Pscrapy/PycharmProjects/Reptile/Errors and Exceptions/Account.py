import decimal

class createAccountError(Exception):
    """asdas"""

class Account():
    def __init__(self,username, balance):
        self.username = username
        self.balance = balance

    @classmethod
    def from_string(cls,s):
        try:
            username,balance = s.split()
            balance = decimal.Decimal(float(balance))
        except ValueError:
            # 可以在异常信息里提供出现意料之外结果的原因,抛出异常，到上级捕获，把一种类型的错误转化成另一种类型
            raise createAccountError('input must follow pattern "{ACCOUNT_NAME} {BALANCE}"')
            # raise
            # raise语句如果不带参数 就会把当前错误原样抛出。
            

        if balance < 0:
            raise createAccountError('balance can not be negative')
        return cls(username=username, balance=balance)

def caculate_total_balance(accounts_data):

    result = 0
    for account_string in accounts_data:
        try:
            user = Account.from_string(account_string)
        # 捕获异常
        except createAccountError as e:
            print(f'{e}')
        else:
            result += user.balance
    print(result) 

def accountNull():
    username = ''
    balance = 0

    @classmethod
    def from_string(cls,s):
        raise NotImplementedError

accounts_data = ['piglei 96.5','cotton 21','invalid_data','roland $invalid_balance','alfred -3','testad']

caculate_total_balance(accounts_data)