from os import system
from termcolor import colored
from sys import platform
from googlesearch import search


try:
    os.system("cls||clear") #Works on linux and windows.
    print("")
    print(colored(r''' ________   __      ________  ______    ______     _______   ________                                                                     
    |"      "\ |" \    /"       )/" _  "\  /    " \   /"      \ |"      "\                                                                    
    (.  ___  :)||  |  (:   \___/(: ( \___)// ____  \ |:        |(.  ___  :)                                                                   
    |: \   ) |||:  |   \___  \   \/ \    /  /    ) :)|_____/   )|: \   ) ||                                                                   
    (| (___\ |||.  |    __/  \\  //  \ _(: (____/ //  //      / (| (___\ ||                                                                   
    |:       :)/\  |\  /" \   :)(:   _) \\        /  |:  __   \ |:       :)                                                                   
    (________/(__\_|_)(_______/  \_______)\"_____/   |__|  \___)(________/                                                                    
                                                                                                                                            
    ________  _______   _______  ___      ___  _______   _______        __    __   ____  ____  _____  ___  ___________  _______   _______   
    /"       )/"     "| /"      \|"  \    /"  |/"     "| /"      \      /" |  | "\ ("  _||_ " |(\"   \|"  \("     _   ")/"     "| /"      \  
    (:   \___/(: ______)|:        |\   \  //  /(: ______)|:        |    (:  (__)  :)|   (  ) : ||.\\   \    |)__/  \\__/(: ______)|:        | 
    \___  \   \/    |  |_____/   ) \\  \/. ./  \/    |  |_____/   )     \/      \/ (:  |  | . )|: \.   \\  |   \\_ /    \/    |  |_____/   ) 
    __/  \\  // ___)_  //      /   \.    //   // ___)_  //      /      //  __  \\  \\ \__/ // |.  \    \. |   |.  |    // ___)_  //      /  
    /" \   :)(:      "||:  __   \    \\   /   (:      "||:  __   \     (:  (  )  :) /\\ __ //\ |    \    \ |   \:  |   (:      "||:  __   \  
    (_______/  \_______)|__|  \___)    \__/     \_______)|__|  \___)     \__|  |__/ (__________) \___|\____\)    \__|    \_______)|__|  \___) 
                                                                                                                                            ''', 'blue'))

    print()
    print(colored('DSH version 1.0 ; https://github.com/falkensmz/dsh', 'blue'))
    print(colored('writer - falkensmz', 'blue'))
    print()

    server_name = input("DSH~# Enter relevant strings for DSH to look for : ")
    servers_number = int(input("DSH~# Enter a maximum numbers that DSH will look for : "))

    final_query = 'inurl:"/discord.com/invite/" intitle:' + server_name

    print(colored('DSH~# Hunting for servers ...', 'red'))
    print()

    count = 0 

    try:
        for i in search(final_query, tld="com", num=servers_number, stop=servers_number, pause=2):
            count += 1
            print(count, "-", i)
    except Exception as e:
        print(fr"DSH~# Err : {e}")

except KeyboardInterrupt:
    print("CTRL-C detected! Closing now ... ")
    exit()
