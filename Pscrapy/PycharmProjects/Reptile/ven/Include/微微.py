import requests


def get_html(url):
    try:

        resp = rquests.get(url)
        if resp.status_code == 200:
            return resp.text
        return None
    except ConnectionError:
        print("error occur")
        return None


def main():
    url = 'http://www.weiweiqi.com/page/1'
    print(get_html(url))


if __name__ == '__main__':
    main()
