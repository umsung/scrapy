


def answer(par):
    count = 0
    length = 0
    temp = []
    item = []
    for i in par:
        print(type(i))
        if i>='0' and i<='9':
            count = count+1
            item.append(str(i))

        else:
            if count >= length:
                length = count
                temp = item

                count = 0
                item = []
            else:
                count = 0
                item = []

    temp = ''.join(temp)
    print('length:{}, temp:{}'.format(length, temp))


if __name__ == '__main__':
    answer('sasaf15455fa4fas5f4564564g56s4sg5gg')
