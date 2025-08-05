def translator(s, t):
    vowels = "аеёиыоуэюя"
    words = s.split()
    s_output = []

    if t == "salt":
        mid_l = "с"
    elif t == "brick":
        mid_l = "к"

    for word in words:
        w = list(word)
        for c in range(len(w)):
            if w[c] in vowels:
                w[c] = w[c] + mid_l + w[c]
            elif w[c] in vowels.upper():
                w[c] = w[c] + mid_l.upper() + w[c]
        s_output.append("".join(w))
    
    return " ".join(s_output)

print("\033[1;34mПереводчик с русского на солёный/кирпичный язык\033[0m")
print("Данная программа переводит предложения с русского языка на так называемые \"солёный\" и \"кирпичный\" языки.\nСуть \"перевода\" заключается в следующем: после каждой гласной буквы ставится согласная буква в зависимости от типа языка (\033[1;36mс\033[0m для \"солёного\" языка, \033[1;31mк\033[0m для \"кирпичного\" языка), далее после этой буквы дублируется предшествующая гласная буква.\nДанные \"языки\" являются аналогами \"поросячьей латыни\", слегка изменённого английского языка.\n")

sentence = input("\033[1mВведите предложение\033[0m: ")
langtype = input("\033[1mВведите букву типа языка\033[0m (\033[1;36mс\033[0m - солёный, \033[1;31mк\033[0m - кирпичный, допускаются также буквы в верхнем регистре): ")
print()

if langtype == "с" or langtype == "С":
    print(translator(sentence, "salt"))
elif langtype == "к" or langtype == "К":
    print(translator(sentence, "brick"))
else:
    print("Неизвестный тип языка")
