import pandas,sys

if len(sys.argv) != 3:
    print("Insufficient number of parameters.")

stream1 = open(sys.argv[1],'r')
stream2 = open(sys.argv[2],'r')

for i in range(100000):
    char1 = stream1.read(1)
    char2 = stream2.read(1)
    if(char1 != char2):
        print('1',end='')
    else:
        print('0',end='')
