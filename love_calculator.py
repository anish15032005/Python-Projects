
def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()
    
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e
    
    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e
    
    
    score = int(str(first_digit) + str(second_digit))
    print(f"Your Love score is: {score}.")
    
print(''' ___        ______  ___      ___  _______       ______        __      ___       ______   ____  ____  ___            __  ___________  ______     _______   
|"  |      /    " \|"  \    /"  |/"     "|     /" _  "\      /""\    |"  |     /" _  "\ ("  _||_ " ||"  |          /""\("     _   ")/    " \   /"      \  
||  |     // ____  \\   \  //  /(: ______)    (: ( \___)    /    \   ||  |    (: ( \___)|   (  ) : |||  |         /    \)__/  \\__/// ____  \ |:        | 
|:  |    /  /    ) :)\\  \/. ./  \/    |       \/ \        /' /\  \  |:  |     \/ \     (:  |  | . )|:  |        /' /\  \  \\_ /  /  /    ) :)|_____/   ) 
 \  |___(: (____/ //  \.    //   // ___)_      //  \ _    //  __'  \  \  |___  //  \ _   \\ \__/ //  \  |___    //  __'  \ |.  | (: (____/ //  //      /  
( \_|:  \\        /    \\   /   (:      "|    (:   _) \  /   /  \\  \( \_|:  \(:   _) \  /\\ __ //\ ( \_|:  \  /   /  \\  \\:  |  \        /  |:  __   \  
 \_______)\"_____/      \__/     \_______)     \_______)(___/    \___)\_______)\_______)(__________) \_______)(___/    \___)\__|   \"_____/   |__|  \___) 
                                                                                                                                                          ''')
print('''
___d88888888b_____d88888888b
__d88?____d88b___d88b____`88b
_d8?_________d888b_________`8b
_8b_________________________d8
_b8__________________d8888b___d8888b
__d8________________d8?__d8b_d8b__`8b
___8ba_____________d8?_____d8b_____`8b
____`8da___________8b_______________d8
______`Y8b__________d8_____________8b
________`8b__________8ba_________ad8
__________`88_____88__`8da_____ab8?
____________8b___d8_____`Y8___8Y?
_____________`b_d?________`8_8?
______________`8?__________`8?
_______________"____________"
''')
n1 = input("Enter your name:\n")
n2 = input("Enter your partner's name:\n")

calculate_love_score(n1,n2)