import random
from game_data import data
import os

logo ="""

 /$$   /$$ /$$           /$$                                       /$$                              
| $$  | $$|__/          | $$                                      | $$                              
| $$  | $$ /$$  /$$$$$$ | $$$$$$$         /$$$$$$   /$$$$$$       | $$        /$$$$$$  /$$  /$$  /$$
| $$$$$$$$| $$ /$$__  $$| $$__  $$       /$$__  $$ /$$__  $$      | $$       /$$__  $$| $$ | $$ | $$
| $$__  $$| $$| $$  \ $$| $$  \ $$      | $$  \ $$| $$  \__/      | $$      | $$  \ $$| $$ | $$ | $$
| $$  | $$| $$| $$  | $$| $$  | $$      | $$  | $$| $$            | $$      | $$  | $$| $$ | $$ | $$
| $$  | $$| $$|  $$$$$$$| $$  | $$      |  $$$$$$/| $$            | $$$$$$$$|  $$$$$$/|  $$$$$/$$$$/
|__/  |__/|__/ \____  $$|__/  |__/       \______/ |__/            |________/ \______/  \_____/\___/ 
               /$$  \ $$                                                                            
              |  $$$$$$/                                                                            
               \______/                                                                             
"""

vs = """  _   ______
 | | / / __/
 | |/ /\ \  
 |___/___/  
 """           


def Ans_reciever():

    user_ans = input("\nwho has more followers? type 'A' or 'B': ").lower()

    if user_ans != "a" and user_ans != "b":
        print("invalid input!")
        return Ans_reciever()
    else:
        return user_ans
    
def ans_check(a,b,user_ans):

    if a["follower_count"] > b["follower_count"]:
        return user_ans == "a"
    else:
        return user_ans == "b"

famous_person = random.choice(data)
game_score = 0
game_continue = True

while game_continue:

    a = famous_person
    b = random.choice(data)

    while a == b:
        b = random.choice(data)

    print(logo)
    print(f"\t\t\t\t\t\t\t\t\t\tcurrent score: {game_score}")
    print("\nCompare A: "+a["name"]+", a "+a["description"]+", from "+a["country"])
    print(vs)
    print("Against B: "+b["name"]+", a "+b["description"]+", from "+b["country"])

    user_ans = Ans_reciever()
    game_continue = ans_check(a,b,user_ans)
    os.system('cls')

    if game_continue:
        print("\nyou are right!")
        game_score += 1

    elif not game_continue:
        print("\nyou are wrong!")
    
    if a["follower_count"] > b["follower_count"]:
        famous_person = a
    else:
        famous_person = b

print("\nGame Over!")
print(f"total score: {game_score}")