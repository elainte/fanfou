import requests
import yagmail


def sendmail(str):
    yag = yagmail.SMTP(user="xxxx@163.com",
                       password="xxxx", host='smtp.163.com')
    contents = ['https://fanfou.com/register', '', '']
    yag.send('xxxxx@qq.com', 'subject', contents)


url = 'https://fanfou.com/register'
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36'}
with requests.get(url=url, headers=headers) as response:
    data2 = response.content.decode()
    #data2 = '已开放2....'  # test
    # print(data2)
    if data2 != '本站暂停注册。':
        try:
            sendmail(data2)
            pass
        except:
            pass
