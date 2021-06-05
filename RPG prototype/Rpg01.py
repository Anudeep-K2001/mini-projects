import random
import math



print("================Welcome to MMORPG game!!=============")
print("You are give 3 characters, pick one wisely")
print("=====================================================")
print("1) CHARMANDER -> atk : 100, def : 50, speed : 70")
print("2) BULBASUAR -> atk : 50, def : 70, speed: 100")
print("3) SQUIRTLE -> atk : 70, def : 100, speed : 50")



moves = {
    'A' : {
        'power' : 90,
        'accuracy' : 100,
    },
    'B' : {
        'power' : 150,
        'accuracy' : 70,
    },
    'C' : {
        'power' : 200,
        'accuracy' : 30,
    },
    'D' : {
        'power' : 500,
        'accuracy' : 10,
    }
}




charmander = {
    'name' : "Charmander",
    'atk' : 100,
    'def' : 50,
    'speed' : 70,

    'moves' : ['A','B','C','D'],
}

bulbasuar = {
    'name' : "Bulbasuar",
    'atk' : 50,
    'def' : 70,
    'speed' : 100,

    'moves' : ['A','B','C','D'],
}

squirtle = {
    'name' : "Squirtle",
    'atk' : 70,
    'def' : 100,
    'speed' : 50,

    'moves' : ['A','B','C','D'],
}


choices = {
    1 : charmander,
    2 : bulbasuar,
    3 : squirtle,
}


choice = int(input("ENTER WHAT CHARACTER YOU WOULD LIKE TO PICK (number) : "))

print(f"You have picked {choices[choice]['name']}")

opp_choice = random.randint(1,3)

print("=======================ENTERING BATTLE GROUND===================")
print("insert battle music")
print("𝄞𝄞𝄞𝄞𝄞𝄞𝄞𝄞𝄞𝄞♭♭♭♭♭♭♭♭♭♭♭♭♭♭𝄞𝄞𝄞𝄞♭♭𝄞♮𝄞𝄞𝄞𝄞𝄞♭♮♭𝄞𝄞𝄞♭♭♭♭♭♭♭♭♭")
print(f"A wild {choices[opp_choice]['name']} appeared")


print("You have following moves\nA => power : 90\taccuracy : 100\nB => power : 150\taccuracy : 70\nC => power : 200\taccuracy : 30\nD => power : 500\taccuracy : 10")

pokemon = choices[choice]
opp_pokemon = choices[opp_choice]


user_hp = 100
opp_hp = 100



def set_hp(damage, uOo):
    if not uOo:
        global user_hp
        user_hp -= round(damage)
    else:
        global opp_hp
        opp_hp -= round(damage)



def damage_done(pk, opk, move, uOo = 0):
    global moves
    if uOo:
        dmg = (pk['atk']/10 * moves[move]['power']/10)/(opk['def'] * 2) * 5
        print(f"you used {move}")

        if random.random() < (moves[move]['accuracy']/100):      
            set_hp(dmg, uOo)
            print(f"You dealt {dmg} Damage")
        else:
            print("but it missed")
    else:
        dmg = (opk['atk']/10 * moves[move]['power']/10)/(pk['def'] * 2) * 5
        print(f"opponent used {move}")

        if random.random() < (moves[move]['accuracy']/100):      
            set_hp(dmg, uOo)
            print(f"You lost {dmg} Hp")
        else:
            print("but it missed")








def user_turn(pk, opk):
    global user_hp, opp_hp
    ah = input("Enter Move Name : ")
    if ah in pk['moves']:
        #things go here
        damage_done(pk, opk, ah, 1)
    else:
        print("Invalid move, Try again")
        ah = user_turn(pk, opk)
    return ah


def opp_turn(opk, pk):
    
    global opp_hp
    opp_move = random.choice(['A','B', 'C', 'D'])
    damage_done(opk,pk, opp_move, 0)
    return





while 1:
    if pokemon['speed'] > opp_pokemon['speed']:
        user_turn(pokemon, opp_pokemon)
        opp_turn(opp_pokemon, pokemon)
    elif pokemon['speed'] < opp_pokemon['speed']:
        opp_turn(opp_pokemon, pokemon)
        user_turn(pokemon, opp_pokemon)
    else:
        x = random.randint(0,1)
        if x:
            user_turn(pokemon, opp_pokemon)
            opp_turn(opp_pokemon, pokemon)
        else:
            opp_turn(opp_pokemon, pokemon)
            user_turn(pokemon, opp_pokemon)


    print(f"USER HP : {user_hp}")
    print(f"OPPONENT HP : {opp_hp}")


    if (user_hp  <= 0) or (opp_hp <= 0):
        break

    
if user_hp < 0:
    print("You lost bruh")
else:
    print("kek you won")