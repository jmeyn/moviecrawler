import os

def main():
    print(os.getcwd())
    check = []
    check += navigate()
    while len(check) > 1:
        for i in check:
            os.chdir(i)
            check += navigate()
            os.chdir("..")
            check.pop(0)
            print()
    

def listDir():
    for i in os.listdir():
        print(i)
    
def navigate():
    check = []
    listDir()
    for i in os.listdir():
        if os.path.isdir(i):
            check.append(i)
    return check
    
def check(d):
    for i in d:
        #if d is any movie file type
            #save dir name
        pass

if __name__ == "__main__":
    main()
