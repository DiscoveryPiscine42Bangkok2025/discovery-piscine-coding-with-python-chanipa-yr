import sys

if len(sys.argv)!=3:
    print("none")
else:
    print(list(range(int(sys.argv[1]),int(sys.argv[2])+1)))