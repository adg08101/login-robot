import time
import keyboard
import easygui as eg


def login(user_name, password, mode, tabs):
    login_process(user_name, password, mode=mode, tabs=tabs)


def login_process(username, password, mode, tabs, sleep_time=0.5):
    keyboard.press('alt + tab')
    keyboard.release('alt + tab')
    time.sleep(sleep_time)

    if mode == 'User & Pass':
        keyboard.write(username, delay=0.1)

    if tabs == 'User Tab Pass Enter':
        if mode == 'User & Pass':
            keyboard.send('tab')
        time.sleep(sleep_time)
        keyboard.write(password, delay=0.1)
        time.sleep(sleep_time)
        keyboard.press('enter')
        exit(0)

    if tabs == 'No tabs':
        if mode == 'User & Pass':
            keyboard.send('enter')
            time.sleep(sleep_time * 3)
        keyboard.write(password, delay=0.1)
        keyboard.send('enter')
        exit(0)

    if tabs == 'One tab' or tabs == 'Two tabs':
        if mode == 'User & Pass':

            tab_on(tabs, sleep_time)

            time.sleep(sleep_time * 3)
            keyboard.write(password, delay=0.1)
            time.sleep(sleep_time)

            tab_on(tabs, sleep_time)

        else:
            keyboard.write(password, delay=0.1)
            time.sleep(sleep_time)

            tab_on(tabs, sleep_time)

        exit(0)


def tab_on(tabs, sleep_time):
    keyboard.send('tab')
    time.sleep(sleep_time)
    if tabs == 'Two tabs':
        keyboard.send('tab')
        time.sleep(sleep_time)
    keyboard.send('enter')


if __name__ == '__main__':
    file = open('users.txt.txt')
    users = []
    passwords = []

    pos = 0

    for user in file.readlines():
        if pos % 2 == 0:
            users.append(user)
        else:
            passwords.append(user)
        pos = pos + 1

    mode = ['User & Pass', 'Pass only']
    tabs = ['User Tab Pass Enter', 'No tabs', 'One tab', 'Two tabs']

    option_mode = eg.choicebox(msg='KAHUA Users and Pass Robot', title='Choose Mode', choices=mode)

    if option_mode:
        tabs_mode = eg.choicebox(msg='KAHUA Users and Pass Robot', title='Choose Tabs Mode', choices=tabs)
        option = eg.choicebox(msg='KAHUA Users and Pass Robot', title='Choose User', choices=users)
        login(str(option).replace('\n', ''), str(passwords[users.index(option)]).replace('\n', ''),
              mode=option_mode, tabs=tabs_mode)
    else:
        pass
