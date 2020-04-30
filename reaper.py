import pygeoip
import os
from termcolor import colored
import sys
import time

reaper_graphic = '''
██████╗ ███████╗ █████╗ ██████╗ ███████╗██████╗ 
██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗
██████╔╝█████╗  ███████║██████╔╝█████╗  ██████╔╝
██╔══██╗██╔══╝  ██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
██║  ██║███████╗██║  ██║██║     ███████╗██║  ██║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
'''

while True:
    os.system('clear')
    print(colored(reaper_graphic, 'red'))
    print(colored('{?}======={ DEVELOPED BY: ORANGEMAN }========{?}', 'cyan'))
    print(colored('ENTER IN THE IP YOU WANT TO LOCATE'))
    ip = input('reaper> ')

    gip = pygeoip.GeoIP('GeoLiteCity.dat')
    try:
        res = gip.record_by_addr(ip)
        for key,val in res.items():
            print(colored('%s : %s' % (key,val), 'red'))
        sys.exit(1)
    except Exception as e:
        print(f'ERROR: {e}')
        print('CHECK IP VALIDITY')
        time.sleep(3)
        continue