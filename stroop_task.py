"""
Stroop Task. Note that this task is run and tested on Spyder Windows. You may need to make changes to run on other software and platforms, especially for colored text section.

Author : Farrokh Karimi

Institute for Research in Fundamental Sciences (IPM)

farrokhkarimi.github.io
"""

import time
import random
import pandas
from termcolor import colored
from pynput import keyboard

trials = 40
stimulus_time = 2.0 # seconds

colors = ['red', 'green', 'blue', 'yellow']
df = pandas.DataFrame(columns = ['word', 'color', 'matched', 'pressed_key', 'status', 'response_time'])

congruent_num = congruent_time = incongruent_num = incongruent_time = 0
flag = True

input('This is stroop test.\n\nPress Esc key if you want to stop while the test is running.\n\nIn the test process, press {r, g, b, y} keys for {red, green, blue, yellow} colors.\n\nClick at the end of this line and press the Enter key to continue...')
print('\n',1)
time.sleep(0.5)
print('\n',2)
time.sleep(0.5)
print('\n',3)
time.sleep(0.5)
print('\nGo...\n')
time.sleep(1)

for i in range(trials):
    
    matched = 0
    
    word = random.choice(colors)
    color = random.choice(colors)
    
    if word == color:
        matched = 1
    
    print('+')
    time.sleep(0.5)
    
    print(colored(word, color, attrs = ['bold']))
    
    t0 = time.time()
    
    # The keyboard listener will be running in this block
    with keyboard.Events() as events:
        
        event = events.get(stimulus_time)
        
        response_time = round(time.time() - t0, 3)
        
        if response_time > stimulus_time:
            response_time = stimulus_time
            
        if event is None:
            print('wrong\n')
            pressed_key=None
            check = False
            status=3
        else:
            pressed_key = str(event.key)
            check = True
        
        if check:
            # red
            if pressed_key == "'r'":
                if color != 'red':
                    print('wrong\n')
                    status = 2
                else:
                    print('correct\n')
                    status = 1
                    if word == 'red':
                        congruent_num += 1
                        congruent_time += response_time
                    else:
                        incongruent_num += 1
                        incongruent_time += response_time
                    
            # green
            elif pressed_key == "'g'":
                if color != 'green':
                    print('wrong\n')
                    status = 2
                else:
                    print('correct\n')
                    status = 1
                    if word == 'green':
                        congruent_num += 1
                        congruent_time += response_time
                    else:
                        incongruent_num += 1
                        incongruent_time += response_time
                        
            # blue
            elif pressed_key == "'b'":
                if color != 'blue':
                    print('wrong\n')
                    status = 2
                else:
                    print('correct\n')
                    status = 1
                    if word == 'blue':
                        congruent_num += 1
                        congruent_time += response_time
                    else:
                        incongruent_num += 1
                        incongruent_time += response_time
                        
            # yellow
            elif pressed_key == "'y'":
                if color != 'yellow':
                    print('wrong\n')
                    status = 2
                else:
                    print('correct\n')
                    status = 1
                    if word == 'yellow':
                        congruent_num += 1
                        congruent_time += response_time
                    else:
                        incongruent_num += 1
                        incongruent_time += response_time
                        
            # check for Esc or other pressed keys
            elif pressed_key == 'Key.esc':
                flag = False
                print('\nYou broke the test!\nFinish.')
                break
            else:
                print('wrong\n')
                status = 2
    
    # save responses
    data = {'word':word, 'color':color, 'matched':matched, 'pressed_key':pressed_key, 'status':status, 'response_time':response_time}
    df.loc[i] = pandas.Series(data)

# results
if flag:
    
    # calculate average congruent time
    if not(congruent_num):
        congruent = 0
    else:
        congruent = congruent_time / congruent_num
    
    # calculate average incongruent time    
    if not(incongruent_num):
        incongruent = 0
    else:
        incongruent = incongruent_time / incongruent_num
    
    # print the outputs
    print('\nYour speed in correct trials:\n')
    print('Congruent: {} ms\n'.format(congruent))
    print('Incongruent: {} ms\n'.format(incongruent))
    print('Your sroop effect is congruent minus incongruent: {} ms'.format(round(incongruent - congruent, 3)))
    
    df.to_csv('responses.csv')
    
    time.sleep(2)
    
    # printiing responses table
    while True:
        res = input('Whould you like to see your responses table? (y/n) ')
        if res == 'y':
            print('\nhint for matched (word and color): 1=compatible, 0=incompatible')
            print('\nhint for status: 1=correct, 2=wrong, 3=timeout\n')
            print(df)
            break
        elif res == 'n':
            print('Good luck!\nBye')
            break
        else:
            print('\nplease insert y or n')