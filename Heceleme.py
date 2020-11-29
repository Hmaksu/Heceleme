Main_Loop = 1
def vowel(letter111):
    if letter111 == "a" or letter111 == "ı" or letter111 == "o" or letter111 == "u" or letter111 == "e" or letter111 == "i" or letter111 == "ö" or letter111 == "ü":
        return True
    else:
        return False
while Main_Loop == 1:
    word_list = []
    word_list_2 = []
    letter_list = []
    spell_list = []
    phrase = input("Cümle\n")
    if phrase == "çıkış123":
        break
    phrase = phrase.lower()
    word_list_2 = phrase.split()
    for x in word_list_2:
        word_list.append(x)
        word_list.append(" ")
    word_list.pop()
    for x in word_list:
        for a in range(len(x)):
            t = a + 1
            if t > len(x):
                letter_list.append(x[a:])
            else:
                letter_list.append(x[a:t])
    for x in range(len(letter_list)):
        if letter_list[x] == " ":
            spell_list.append(" ")
        elif x == 0 or letter_list[x-1] == " ":
            if vowel(letter_list[x]) == True:
                try:
                    if vowel(letter_list[x+2]) == True:
                        spell_list.append(letter_list[x])
                    elif vowel(letter_list[x+1]) == True:
                        spell_list.append(letter_list[x])
                    else:
                        try:
                            if vowel(letter_list[x + 3]) == True:
                                spell_list.append(letter_list[x] + letter_list[x + 1])
                            else:
                                spell_list.append(letter_list[x] + letter_list[x + 1] + letter_list[x + 2])
                        except:
                            spell_list.append(letter_list[x]+letter_list[x+1]+letter_list[x+2])
                except:
                    try:
                        if vowel(letter_list[x+1]) == True:
                            spell_list.append(letter_list[x])
                        else:
                            spell_list.append(letter_list[x]+letter_list[x+1])
                    except:
                        spell_list.append(letter_list[x])
            else:
                try:
                    if vowel(letter_list[x+1]) == True:
                        try:
                            if vowel(letter_list[x+2]) == True:
                                try:
                                    if vowel(letter_list[x+3]) == True:
                                        spell_list.append(letter_list[x]+letter_list[x+1])
                                    else:
                                        try:
                                            if vowel(letter_list[x+4]) == True:
                                                spell_list.append(letter_list[x]+letter_list[x+1]+letter_list[x+2])
                                            else:
                                                spell_list.append(letter_list[x]+letter_list[x+1]+letter_list[x+2]+letter_list[x+3])
                                        except:
                                            spell_list.append(letter_list[x]+letter_list[x+1])
                                            spell_list.append(letter_list[x+2]+letter_list[x+3])
                                except:
                                    random_variable_for_else_func = 1
                            else:
                                try:
                                    if vowel(letter_list[x + 3]) == True:
                                        spell_list.append(letter_list[x] + letter_list[x + 1])
                                    else:
                                        try:
                                            if vowel(letter_list[x + 4]) == True:
                                                spell_list.append(letter_list[x] + letter_list[x + 1] + letter_list[x + 2])
                                            else:
                                                spell_list.append(letter_list[x] + letter_list[x + 1] + letter_list[x + 2] + letter_list[x + 3])
                                        except:
                                            spell_list.append(letter_list[x] + letter_list[x + 1] + letter_list[x + 2] + letter_list[x + 3])
                                except:
                                    spell_list.append(letter_list[x] + letter_list[x + 1] + letter_list[x + 2])
                        except:
                            spell_list.append(letter_list[x] + letter_list[x + 1])
                    else:
                        spell_list.append(letter_list[x])
                except:
                    spell_list.append(letter_list[x])
        else:
            if vowel(letter_list[x]) == False:
                try:
                    if vowel(letter_list[x+1]) == True:
                        try:
                            if vowel(letter_list[x+2]) == True:
                                spell_list.append(letter_list[x]+letter_list[x+1])
                            else:
                                try:
                                    if vowel(letter_list[x+3]) == True:
                                        spell_list.append(letter_list[x] + letter_list[x + 1])
                                    else:
                                        spell_list.append(letter_list[x] + letter_list[x + 1] + letter_list[x + 2])
                                except:
                                    spell_list.append(letter_list[x] + letter_list[x + 1]+letter_list[x+2])
                        except:
                            spell_list.append(letter_list[x] + letter_list[x + 1])
                    else:
                        random_variable_for_else_func = 1
                except:
                    random_variable_for_else_func = 1
    print(spell_list)
    
