woerter = {'Deutsch':'German', 'Jagen':'Hunt', 'Gehen':'Go'}

wb_umgekehrt = {}
for deutsch in woerter:
    englisch = woerter[deutsch]
    wb_umgekehrt[englisch] = deutsch #zugewiesen

print(woerter)
print(wb_umgekehrt)


woerter_sortiert = sorted(woerter.items())
print(woerter_sortiert)


print("schreibe ein Deutsches Wort hin:")
eingabe = str(input())
k = woerter.keys()
v = woerter.values()
try:
    if eingabe in k:
        print('Das Englische Wort lautet:', woerter[eingabe])
    elif eingabe in v:
        print('Das Deutsche Wort lautet:', wb_umgekehrt[eingabe])
    else:
        print("Das Wort ist nicht im Dictionary enthalten")
except:
    print(' ')




