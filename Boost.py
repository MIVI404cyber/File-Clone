import os, platform, time, sys
def xoss(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.06)
xoss('\n\033[1;32m[\033[1;91m√\033[1;92m]\033[1;93m Checking Update........✔️✔️');time.sleep(0.5)
def Update():
    exit('\033[1;32m[\033[1;91m√\033[1;92m]\033[1;96m Commands On Update Please Wait For Update')
def Run():
        bit = platform.architecture()[0]
        if bit == '64bit':
            xoss("\n\033[1;92m[\033[1;91m√\033[1;92m]\033[1;93m Congratulations Your \033[1;91m(\033[1;92m64 Bit\033[1;91m)\033[1;93m Device Support this Tools")
            xoss('\033[1;92m[\033[1;91m√\033[1;92m]\033[1;92m Follow My Facebook First')
            os.system('xdg-open https://www.facebook.com/mr.rohman.129')
            from B64 import main
            main()
        elif bit == '32bit':
            xoss("\n\033[1;92m[\033[1;91m√\033[1;92m]\033[1;93m Congratulations Your \033[1;91m(\033[1;92m32 Bit\033[1;91m)\033[1;93m Device Support this Tools ")
            xoss('\033[1;92m[\033[1;91m√\033[1;92m]\033[1;92m Follow My Facebook First')
            os.system('xdg-open https://www.facebook.com/mr.rohman.129')
            from B32 import main
            main()
        else:
            exit('\033[1;32m[\033[1;91m√\033[1;92m]\033[1;91m Connection & Network Error')
Run()
