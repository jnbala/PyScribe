import re
def main():
    pyscribe_log = open('pyscribe_logs.txt', 'w')
    x = 5
    pyscribe_log.write('From line 4: Watching variable x'+ '\n')
    x = 3
    y = "world"
    x = 5

if __name__=="__main__":
    main()
