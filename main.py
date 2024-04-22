from random import *
f = open("Words.txt")
f = [i.replace("\n","").lower() for i in f]

word = list(map(str, f[randint(0,len(f)-1)]))
otvet = ['*'] * len(word)

hp = 5
answere = ""

print("Количество букв в слове:", len(word))

while otvet != word:
    print("Введите букву:")
    answere = input().lower()
    if answere in word:
        for i in range(len(word)):
            if word[i] == answere:
                otvet[i] = answere
    else:
        hp-=1
        if hp == 0:
            print("Вы проиграли")
            print("Загаданное слово -", "".join(word))
            break

    print(*otvet, sep='')
    print('Количество оставшихся жизней:', hp, '\n')
else:
    print('Вы победили')