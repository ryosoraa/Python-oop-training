class Hero:
    amounthero = 0
    allhero = []

    def __init__(self, name, health, power, defend):
        self.name = name
        self.health = health
        self.power = power
        self.defend = defend
        Hero.amounthero += 1
        hero = [health, power, defend]
        Hero.allhero.append(name)
        print('='*50)
        print(f'Membuat Hero Baru : {name}')
        print(f'Atrribut Hero     : {hero}')
        print(f'Jumlah Hero Baru  : {Hero.amounthero}')
        print(f'Semua Hero        : {Hero.allhero}')


hero1 = Hero('Valir', 100, 20, 10)
hero2 = Hero('Alpha', 200, 20, 30)
