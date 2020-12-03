alter = {'Peter':31, 'Julia':28, 'Werner':35}
alter_umgekehrt = {}
for name in alter:
    personenalter = alter[name]
    print("Personenalter:", personenalter)
    alter_umgekehrt[personenalter] = name# name  wird zugewiesen
    print("alter_umgekehrt:",alter_umgekehrt)
print(alter_umgekehrt)
print(alter)