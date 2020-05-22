import pygeoip
import os
from termcolor import colored
import sys
import time
import folium
import webbrowser


reaper_graphic = '''
██████╗ ███████╗ █████╗ ██████╗ ███████╗██████╗ 
██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗
██████╔╝█████╗  ███████║██████╔╝█████╗  ██████╔╝
██╔══██╗██╔══╝  ██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
██║  ██║███████╗██║  ██║██║     ███████╗██║  ██║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
'''

reaper_small = '''
  ___ ___   _   ___ ___ ___ 
 | _ \ __| /_\ | _ \ __| _ \ 
 |   / _| / _ \|  _/ _||   /
 |_|_\___/_/ \_\_| |___|_|_\                   
'''

def check():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def logo():
    check()
    print(colored(reaper_graphic, 'red'))
    print(colored('{?}======={ DEVELOPED BY: ORANGEMAN }========{?}', 'cyan'))



def menu():
    check()
    logo()
    print('[1] Accounts')
    print('[2] IP')
    print('[3] Export')
    print('[0] EXIT')
    choice = input('reaper> ')
    if choice == '0':
        print('THANKS FOR USING REAPER')
        sys.exit(1)
    elif choice == '1':
        ACCOUNTS()
    elif choice == '2':
        IP()
    elif choice == '3':
        EXPORT()
    else:
        print(colored('ERROR INVALID SELECTION', 'red'))
        menu()

def ACCOUNTS():
    check()
    logo()
    print(colored('ENTER THE FIRST NAME', 'red'))
    f_name = input('reaper> ')
    print(colored('ENTER THE LAST NAME', 'red'))
    l_name = input('reaper> ')
    check()
    logo()
    print('[1] Google')
    print('[2] Facebook')
    print('[3] Twitter')
    print('[4] YouTube')
    print('[5] HaveIBeenPwned (EMAIL)')
    print('[6] LinkedIn')
    acc = input('reaper> ')
    if acc == '1':
        webbrowser.open('https://plus.google.com/s/' + f_name + ' ' + l_name + '/people')
        menu()
    if acc == '2':
        webbrowser.open('https://www.facebook.com/search/top/?init=quick&q=' + f_name + ' ' + l_name)
        menu()
    if acc == '3':
        webbrowser.open('https://twitter.com/search?f=users&vertical=default&q= ' + f_name + ' ' + l_name)
        menu()
    if acc == '4':
        webbrowser.open('http://www.youtube.com/results?search_query=' + f_name + '+' + l_name)
        menu()
    if acc == '5':
        webbrowser.open('https://haveibeenpwned.com/')
        menu()
    if acc == '6':
        webbrowser.open('https://fr.linkedin.com/pub/dir/' + f_name + '/' + l_name)
        menu()
    else:
        print(colored('ERROR INVALID SELECTION', 'red'))
        menu()

def IP():
    check()
    logo()
    print(colored('ENTER IN THE IP', 'red'))
    ip = input('reaper> ')
    check()
    logo()
    gip = pygeoip.GeoIP('GeoLiteCity.dat')
    try :
        res = gip.record_by_addr(ip)
        for key, val in res.items() :
            print(colored('%s : %s' % (key, val), 'red'))
        latitude = res.get('latitude')
        longitude = res.get('longitude')
        m = folium.Map(location=[latitude, longitude], zoom_start=13)
        folium.Marker(location=[latitude, longitude], popup="IP Location").add_to(m)
        m.save('location.html')
        filename = 'location.html'
        webbrowser.open_new_tab(filename)
        menu()
    except Exception as e :
        print(f'ERROR: {e}')
        time.sleep(3)
        menu()

def EXPORT():
    check()
    logo()
    print(colored('ENTER THE FIRST NAME', 'red'))
    f_name = input('reaper> ')
    print(colored('ENTER THE LAST NAME', 'red'))
    l_name = input('reaper> ')
    print('ENTER IN AGE')
    age = input('reaper> ')
    print('ENTER IN EMAIL')
    email = input('reaper> ')
    print('ENTER IN ADDRESS')
    addy = input('reaper> ')
    print('ENTER IN CITY')
    city = input('reaper> ')
    print('ENTER IN STATE/PROVINCE')
    state = input('reaper> ')
    print('ENTER IN COUNTRY')
    country = input('reaper> ')
    print('ENTER IN IP')
    ip_add = input('reaper> ')
    f = open('dox.txt', 'w+')
    f.write(reaper_small + '\n')
    f.write('---------------------------------------------------' + '\n')
    f.write('Full Name: ' + f_name + ' ' + l_name + '\n')
    f.write('Age: ' + age + '\n')
    f.write('Email: ' + email + '\n')
    f.write('Location: ' + addy + ', ' + city + ', ' + state + ', ' + country + '\n')
    f.write('IP: ' + ip_add + '\n')
    f.write('---------------------------------------------------' + '\n')
    f.close()
    print('FILE SAVED TO THE SAME DIRECTORY: dox.txt')
    menu()



menu()
