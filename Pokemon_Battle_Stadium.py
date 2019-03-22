import random


class Pokemon:
    def __init__(self, name, moves, hp, cry, weakness):
        self.name = name
        self.moves = moves
        self.hp = hp
        self.cry = cry
        self.weakness = weakness

    def turn(self, other):
        movecount = random.randrange(0, 5)
        Moves.attack(self.moves[movecount], other)
        print('{}: {}'.format(self.name, self.moves[movecount].name))
        if other.hp <= 0:
            print(commentry[5])
        elif self.moves[movecount].dmg == 0:
            print(commentry[4])
        elif self.moves[movecount].dmg > 0 and self.moves[movecount].dmg < 20:
            print(commentry[0])
        elif self.moves[movecount].dmg >= 20 and self.moves[movecount].dmg < 30:
            print(commentry[1])
        elif self.moves[movecount].dmg >= 30 and self.moves[movecount].dmg < 40:
            print(commentry[2])
        elif self.moves[movecount].dmg >= 40:
            print(commentry[3])

        if self.moves[movecount].dmg > 0 and other.hp > 0 :
            print('{}\'s health is down to {}'.format(other.name, other.hp))
        if other.hp <= 0:
            print('{} is unable to move {} won the match'.format(other.name, self.name))
        elif self.hp <= 0:
            print('{} is unable to move {} won the match'.format(self.name, other.name))

        print('')
        


class Moves:
    def __init__(self, name, dmg, tipe):
        self.name = name
        self.dmg = dmg
        self.tipe = tipe

    def attack(self, other):
        if self.tipe in other.weakness and self not in moveused:
            self.dmg = self.dmg * 2
            moveused.append(self)
            other.hp = other.hp - self.dmg
        else:
            other.hp = other.hp - self.dmg


def pow(x, y):
    return random.randrange(x, y + 1)


# some moves
quickattack = Moves('Quick Attack', pow(10, 20), 'normal')
thunderbolt = Moves('Thunder Bolt', pow(20, 30), 'electric')
irontail = Moves('Iron Tail', pow(15, 25), 'steel')
thunderpunch = Moves('Thunder Punch', pow(15, 25), 'electric')
flamethrower = Moves('Flame Thrower', pow(20, 30), 'fire')
firepunch = Moves('Fire Punch', pow(15, 25), 'fire')
dragonrage = Moves('Dragon Rage', 20, 'dragon')
wingattack = Moves('Wing Attack', pow(15, 25), 'fly')
skullbash = Moves('Skull Bash', pow(20, 30), 'normal')
hydropump = Moves('Hydro Pump', pow(20, 30), 'water')
bubblebeam = Moves('Bubble Beam', pow(10, 20), 'water')
bite = Moves('Bite', pow(15, 25), 'dark')
vinewhip = Moves('Vine Whip', pow(10, 20), 'grass')
razorleaf = Moves('Razor Leaf', pow(15, 25), 'grass')
takedown = Moves('Take Down', pow(20, 30), 'normal')
solarbeam = Moves('Solar Beam', pow(25, 35), 'grass')
slam = Moves('Slam', pow(15, 25), 'normal')
hyperbeam = Moves('Hyper Beam', pow(25, 40), 'normal')
rockthrow = Moves('Rock Throw', pow(15, 25), 'rock')
earthquake = Moves('Earthquake', pow(20, 30), 'ground')
seismictoss = Moves('Seismic Toss', pow(20, 30), 'fighting')
lick = Moves('Lick', pow(15, 25), 'ghost')
nightshade = Moves('Night Shade', pow(20, 30), 'ghost')
psychic = Moves('Psychic', pow(20, 30), 'psychic')
icebeam = Moves('Ice Beam', pow(25, 30), 'ice')

miss = Moves('Missed', 0, None)

# some pokemons
pikachu = Pokemon('Pikachu', [quickattack, irontail, thunderpunch, thunderbolt, miss], 130, 'pika!',
                  ['grass', 'ground'])
blastoise = Pokemon('Blastoise', [bubblebeam, bite, skullbash, hydropump, miss], 150, 'blasssstoise!',
                    ['electric', 'grass'])
charizard = Pokemon('Charizard', [dragonrage, firepunch, wingattack, flamethrower, miss], 160, 'charrrr!',
                    ['water', 'electric'])
venusaur = Pokemon('Venusaur', [vinewhip, razorleaf, takedown, solarbeam, miss], 170, 'venusaaaaur!',
                   ['fire', 'ground'])
dragonite = Pokemon('Dragonite', [thunderbolt, dragonrage, slam, hyperbeam, miss], 180, 'dragoooooniiiiite!!!!',
                    ['rock', 'ice', 'dragon'])
golem = Pokemon('Golem', [takedown, rockthrow, earthquake, seismictoss, miss], 160, 'Gooolllleeeem!!!!!!',
                ['grass', 'water', 'ice', 'fight'])
gengar = Pokemon('Gengar', [lick, nightshade, psychic, hyperbeam, miss], 150, 'Geeeeennnngaaaaar!!!',
                 ['ground', 'psychic', 'ghost'])
lapras = Pokemon('Lapras', [icebeam, hydropump, bubblebeam, slam, miss], 160, 'Lappppprrrassss!',
                 ['electric', 'grass', 'rock', 'fighting'])
commentry = ['That\'s not very effective', 'That hurts ', 'That\'s super effective', 'That\'s a critical hit',
             'That\'s a miss', 'That\'s a Knock Out move!!!!!!']
moveused = []
pokemons = [pikachu, charizard, venusaur, blastoise]
redcorner = random.choice(pokemons)
pokemons.remove(redcorner)
bluecorner = random.choice(pokemons)

print('''\t Welcome to the Pokemon Battle Stadium
 `;-.          ___,
  `.`\_...._/`.-"`
    \        /      ,
    /()   () \    .' `-._
   |)  .    ()\  /   _.'
   \  -'-     ,; '. <
    ;.__     ,;|   > \
   / ,    / ,  |.-'.-'
  (_/    (_/ ,;|.<`
    \    ,     ;-`
     >   \    /
    (_,-'`> .'
         (_,'
         
In Red Corner we have {0}
{0}: {1}
And in Blue Corner we have {2}
{2}: {3}
So let\'s begin!
'''.format(redcorner.name, redcorner.cry, bluecorner.name, bluecorner.cry))
while redcorner.hp >= 0 or bluecorner.hp >= 0:
    redcorner.turn(bluecorner)
    if bluecorner.hp <= 0:
        winner = redcorner
        break
    bluecorner.turn(redcorner)
    if redcorner.hp <= 0:
        winner = bluecorner
        break


print('Congratulations {} for winning the battle'.format(winner.name))
print('''Stay Tuned for more exciting battles
so what are you waiting for 
click the run button again 
Until Then leave a Like and follow and comment''')
