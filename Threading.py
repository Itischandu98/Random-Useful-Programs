### Using Threading for running multiple loops simultaniously
### REALLY IMPORTANT AND SURPRISINGLY USEFUL AT TIMES
import threading
import time

def thisisit():
    global inpt
    while(inpt != 'stop'):
        print('This loop keeps running')
        time.sleep(0.5)
1
def main():
    global inpt
    inpt='dont stop'
    x=threading.Thread(target=thisisit)
    x.start()
    inpt=str(input('enter stop'))

main()