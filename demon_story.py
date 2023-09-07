print(""" 
X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X
|                           ,,'``````````````',,                            |
X                        ,'`                   `',                          X
|                      ,'                         ',                        |
X                    ,'          ;       ;          ',                      X
|       (           ;             ;     ;             ;     (               |
X        )         ;              ;     ;              ;     )              X
|       (         ;                ;   ;                ;   (               |
X        )    ;   ;    ,,'```',,,   ; ;   ,,,'```',,    ;   ;               X
|       (    ; ',;   '`          `',   ,'`          `'   ;,' ;              |
X        )  ; ;`,`',  _--~~~~--__   ' '   __--~~~~--_  ,'`,'; ;     )       X
|       (    ; `,' ; :  /       \~~-___-~~/       \  : ; ',' ;     (        |
X  )     )   )',  ;   -_\  o    /  '   '  \    o  /_-   ;  ,'       )   (   X
| (     (   (   `;      ~-____--~'       '~--____-~      ;'  )     (     )  |
X  )     )   )   ;            ,`;,,,   ,,,;',            ;  (       )   (   X
| (     (   (  .  ;        ,'`  (__ '_' __)  `',        ;  . )     (     )  |
X  )     \/ ,".). ';    ,'`        ~~ ~~        `',    ;  .(.", \/  )   (   X
| (   , ,'|// / (/ ,;  '        _--~~-~~--_        '  ;, \)    \|', ,    )  |
X ,)  , \/ \|  \\,/  ;;       ,; |_| | |_| ;,       ;;  \,//  |/ \/ ,   ,   X
|",   .| \_ |\/ |#\_/;       ;_| : `~'~' : |_;       ;\_/#| \/| _/ |.   ,"  |
X#(,'  )  \\\#\ \##/)#;     :  `\/       \/   :     ;#(\##/ /#///  (  ',)# ,X
|| ) | \ |/ /#/ |#( \; ;     :               ;     ; ;/ )#| \#\ \| / | ( |) |
X\ |.\\ |\_/#| /#),,`   ;     ;./\_     _/\.;     ;   `,,(#\ |#\_/| //.| / ,X
| \\_/# |#\##/,,'`       ;     ~~--|~|~|--~~     ;       `',,\##/#| #\_// \/|
X  ##/#  #,,'`            ;        ~~~~~        ;            `',,#  #\##  //X
|####@,,'`                 `',               ,'`                 `',,@####| |
X#,,'`                        `',         ,'`                        `',,###X
|'  spb                          ~~-----~~                               `' |
X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X
""")


print("Welcome to the Paranormal Simulator")
print("Your adventure begins in your home, where as your laying in bed you hear a loud frightening growl")
print("The noise is coming from your closet, which is across the exit")
print("You can exit the room or open the closet to investigate")
print("Which action will you take?")

choice_1 = input(str("Exit or Open\n"))
choice_1.lower()

if choice_1 == "exit":
    print("You choose to ignore the loud growls in the closet and exit the room.")
    print("""
You have to leave your house to get away from the demon
You can run or you can get in your car and drive away""")
    print("Which action will you take?")
    choice_2 = input(str("Run or Drive\n"))
    choice_2.lower()
    if choice_2 == "drive":
        print("You chose to get in your car and drive away")
        print("As you drive off you realize you must take action!")
        print("You comeup with four options:")
        print("""
keep driving indefinitely
go get supplies to combat the demon
hide in a church
go to the police
""")
        print("Which action will you take?")
        choice_3 = input(str("Drive, Combat, Church, Police\n"))
        choice_3.lower()
        if choice_3 == "drive":
            print("You decide to keep driving, eventually running out of gas and stranding yourself")
            print("You hear a giant 'thud' on the roof of your car and realize the demon is carrying you away......")
            print("the night is filled with your final screams")
        elif choice_3 == "combat":
            print("You decide to combat the demon in attempt to kill it, so you head to the hardware store to buy "
                  "supplies")
            print("While in the market the lights go dark and you hear the demons screech......")
            print("the night is filled with your final screams")
        elif choice_3 == "church":
            print("You decide to go to your nearest church, as that is your best chance of survival")
            print("Safely inside, you no longer hear the demon around you, finally letting you fall asleep")
            print("You wake up and realize you made it through the night, you are safe......"
                  "for now")
        elif choice_3 == "police":
            print("You decide to alert the authorities")
            print("You arrive to the police station and tell the only policeman what you've been through")
            print("He laughs until his laugh turns sinister")
            print("Suddenly the man transforms into the demon and jumps towards you......")
            print("the night is filled with your final screams")

    else:
        print("""
You run out of your house as fast as you can but hear a chilling growl above you
You feel the demons claws stab your skin is it begins to lift you off your feet......
the night is filled with your final screams""")

else:
    print("You open the closet and are greeted with a gnarling demon......"
          "the night is filled with your final screams")



