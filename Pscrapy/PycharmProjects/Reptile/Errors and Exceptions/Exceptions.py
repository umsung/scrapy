
MAX_ITEMS_QUOTA = 3
MAX_LENGTH_OF_NAME = 6

class CreateItemError(Exception):
    """Unable to create a account error"""

# 使用“抛出异常”替代“返回 (结果, 错误信息)”
def create_item(name):
    if len(name) > MAX_LENGTH_OF_NAME:
        raise CreateItemError('name of itme is to long')
    if len(name) > MAX_ITEMS_QUOTA:
        raise CreateItemError('items is full')
    return name

def create_for_input():
    name = input()
    try:
        item = create_item(name)
    except CreateItemError as e:
        # # 以 f开头表示在字符串内支持大括号内的python 表达式
        print(f'create item failed: {e}')
    else:
        print(f'item<{name}> created')
        
create_for_input()