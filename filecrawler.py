import os

def main():
    origin = os.getcwd()
    check = []
    check += findDir()
    while len(check) > 2:
        for i in check:
            os.chdir(os.path.abspath(i))
            check += findDir()
            os.chdir(origin)
        check.pop(0)

def listDir():
    for i in os.listdir():
        print(i)
    
def findDir():
    check = []
    listDir()
    for i in os.listdir():
        if os.path.isdir(i):
            check.append(os.path.abspath(i))
            # print("meme", i, os.path.abspath(i))
    return check
    
def findMovie(d):
    for i in d:
        #if d is any movie file type
            #save dir name
        pass

if __name__ == "__main__":
    main()
