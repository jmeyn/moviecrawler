import os

#DEBUG: remove later
al = []

def main():
    origin = os.getcwd()
    check = []
    check += findDir(origin)
    while len(check) > 0:
        lStart = len(check)
        for i in check:
            check += findDir(os.path.abspath(i))
        check = check[lStart + 2:]
    os.chdir(origin)
    print(al, len(al))

def listDir():
    for i in os.listdir():
        print(i)
    
def findDir(d):
    os.chdir(d)
    check = []
    # listDir()
    for i in os.listdir():
        if os.path.isdir(i):
            check.append(os.path.abspath(i))
            # print("meme", i, os.path.abspath(i))
    #DEBUG: remove later
        else:
            al.append(i)
    #/DEBUG
    return check
    
def findMovie(d):
    for i in d:
        #if d is any movie file type
            #save dir name
        pass

if __name__ == "__main__":
    main()
    
