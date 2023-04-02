import time


class daynames:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
    def t1(self):
        print('1+1=2')

if __name__ == '__main__':

    e1 = daynames('Mon')
    e2 = daynames('Wed')
    e3 = daynames('Tue')
    e4 = daynames('Thu')

    e1.nextval = e3
    e3.nextval = e2
    e2.nextval = e4

    thisvalue = e1

    while thisvalue:
            print(thisvalue.dataval)
            print(thisvalue)
            thisvalue = thisvalue.nextval


print(time.strftime('%Y-%m-%d %H:%M:%S'))

