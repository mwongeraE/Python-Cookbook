import optparse
from socket import *
from threading import *

screenLock = Semaphore(value=1)

def connScan(tgHost, tgPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgHost, tgPort))
        connSkt.send('ViolentPython\r\n')
        results = connSkt.recv(100)
        screenLock.acquire()
        print ('tcp open'% tgPort)
        print (str(results))
    except:
        screenLock.acquire()
        print ('tcp closed'% tgPort)
    finally:
        screenLock.release()
        connSkt.close()

def portScan(tgHost, tgPorts):
    try:
        tgIP = gethostbyname(tgHost)
    except:
        print ('Cannot resolve : Unknown host'% tgHost)
        return 
    try:
        tgName = gethostbyaddr(tgIP)
        print ('Scan results for: ' + tgName[0])
    except:
        print ('Scan results for: ' + tgIP)
    
    setdefaulttimeout(1)

    for tgPort in tgPorts:
        t = Thread(target=connScan, args=(tgHost, int(tgPort)))
        t.start()


def main():
    parser = optparse.OptionParser('usage%prog' + '-H <target host> -p <target port>')
    parser.add_option('-H', dest='tgHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgPort', type='string', help='specify target port[s] separated by comma')
    (options, args) = parser.parse_args()
    tgHost = options.tgHost
    tgPorts = str(options.tgPort).split(', ')
    if (tgHost == None) | (tgPorts[0] == None):
        print (parser.usage)
        exit(0)
    portScan(tgHost, tgPorts)


if __name__ == "__main__":
    main()