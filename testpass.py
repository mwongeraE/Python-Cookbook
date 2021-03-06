import crypt

def testPass(cryptPass):
    salt = cryptPass[0:2]
    dictFile = open('dictionary.txt', 'r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word, salt)
        if (cryptWord == cryptPass):
            print ("Found Password: " + word )
            return
        print ("Password not found")
        return 

def main():
    passFile = open('password.txt')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(":")[0]
            cryptPass = line.split(':')[1].strip(' ')
            print ("Cracking pwd for:" + user)
            testPass(cryptPass)

if __name__ == "__main__":
    main()