def rhythm(phrase):
    count = 0
    for i in range(len(phrase)):
        if phrase[i] == 'а':
            count+=1
    return count
res = list()
numberOfPhrases = int(input('Сколько фраз в Вашем стихотворении?: '))
for i in range(numberOfPhrases):
    res.append(input('Напишите новую фразу: '))
ctrl = list()
for i in range(len(res)):
    fin = rhythm(res[i])
    ctrl.append(fin)
test = 0
for i in range(len(ctrl)):
    if ctrl[0] == ctrl[i]:
        test+=1
if test == numberOfPhrases:
    print('Парам пам-пам')
else: 
    print('Пам парам')