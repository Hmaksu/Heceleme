import os
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
    
    
    f = open("Heceler.txt", "w")
    for x in spell_list:
        if x == " ":
            f.write(",")
            f.write(" ")
        else:
            f.write(x)
            f.write(" ")
    coder = open("Kod yazdırma.py", "w")
    coders_code = """import os\npath = os.path\nsource_group_count = 1\nword = 0\nspell = open("Heceler.txt", "r")\nspell_list = spell.read().split()\nfor x in range(len(spell_list)):\n    if spell_list[x] == ",":\n        spell_list[x] = " "\nvoicefile = open("Voice.py", "w")\nvoicefile.write("import pyglet\\n")\nvoicefile.write("import os\\n")\nvoicefile.write("player = pyglet.media.Player()\\n")\n\nfor x in spell_list:\n    if x == " ":\n        source_group_count += 1\n\nfor x in range(source_group_count):\n    code_line_1 = "source_group_"+str(x)+" = pyglet.media.SourceGroup()\\n"\n    voicefile.write(code_line_1)\n\nfor x in spell_list:\n    if x == " ":\n        word += 1\n    else:\n        code_line_2 = "source_group_"+str(word)+".add(pyglet.media.load(\'"+x+".wav\'))"\n        voicefile.write(code_line_2)\n        voicefile.write("\\n")\n\nfor x in range(source_group_count):\n    voicefile.write("player.queue(source_group_"+str(x)+")\\n")\n\n\nvoicefile.write("player.play()\\n")\ncode_line_3 = "os.startfile(\'Heceleme.py\')"+'\\n'\nvoicefile.write(code_line_3)\nvoicefile.write("pyglet.app.run()")\nos.startfile("Voice.py")\n"""
    coder.write(coders_code)
    os.startfile("Kod yazdırma.py")
    break
