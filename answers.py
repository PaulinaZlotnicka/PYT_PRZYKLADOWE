#wszystkie zadania w jednym pliku
#zadanie 8 nie działa 100% poprawnie ale tu utknełam i nie mam pojęcia jak poprawić... wskazówki mile widzane
#wielka prośba o info czy przygotowanie pliku pod egzamin jest ok (zrzuciłam importy na górę pliku, zostawiłam testowe printy)


import random
from flask import Flask, request
from my_phonebook import pb

#zadanie 4
def revers_sentence(text):
    try:
        text = text.lower()
        text_rev = text[::-1]
        return text_rev.title()
    except AttributeError:
        return "wpisałeś cyfry a nie zdanie"
    except Exception as e:
        e_type = str(e)
        return "Nie można wykonać operacji: {}".format(str(e))
    
rev = revers_sentence("Ala ma kota")
print(rev) # Atok Am Ala

rev = revers_sentence("Python is easy")
print(rev) # Ysae Si Nohtyp

rev = revers_sentence(4444)
print(rev) # Ysae Si Nohtyp


#zadanie 5
def count_char(sentence, letter):
    try: 
        letter = letter.lower()
        sentence = sentence.lower()
    except AttributeError:
        return "wpisz litery"
    out = [i for i in sentence if i == letter]
    return len(out)

        

n = count_char("Ala ma kotA",'a')
print(n) # 4
n = count_char("ala ma kota",'A')
print(n) # 4
n = count_char("Python is easy",'a')
print(n) # 0
#tu jest mały błąd w zadaniu => masz a w słowie easy wiec odp 1 a nie 0
n = count_char("Python is easy", 2)
print(n)


#zadanie 6
def list_filter(int_values, *my_el):
    try:
        for p in my_el:
            for el in int_values:
                if el % p == 0:
                    int_values.remove(el)
        return int_values
    except TypeError:
        return "sprawdź przez co dzielisz"
    except ZeroDivisionError:
        return "nie dziel przez zero"

result = list_filter([1,8,15,20,11], 20)
print(result) # [1,8,15,11]
result = list_filter([1,8,15,20,11], 20,4)
print(result) # [1,15,11]
result = list_filter([1,8,15,20,11], 2, 5)
print(result) # [1,11]



#zadanie 7
def get_random_elements(my_list, no_el=1):
    try:
        return random.sample(my_list, no_el)
    except Exception:
        return "no way to do this"

print(get_random_elements([1,2,6,3,7])) # [2]
print(get_random_elements([1,2,6,3,7],3)) # [6,2,7]
print(get_random_elements([1,2,6,3,7],16)) # Wyjątek!



#zadanie 8
app = Flask(__name__)


def file_as_string(file_path):
    buff = ""
    file_to_read = open(file_path,'r')
    while True:
        line = file_to_read.readline()
        if line == "":
            break
        buff += line

    file_to_read.close()
    return buff

def build_web_page(content,title='My new page'):    
    base_html = file_as_string('phonebook_base.html')
    return base_html.format(title,content)

def checker(user_in):
    cont = ''
    for pb_line in pb:
        for key in pb_line:
            if user_in in pb_line[key]:
                cont = "{}: {}".format(pb_line["nickname"], pb_line["number"])
    return build_web_page(cont)

@app.route("/pbk")
def task8():
    form_base = file_as_string("phonebook_form.html")
    return build_web_page(form_base,title="zadanie8")

@app.route("/pbk", methods =['POST'])
def task8_post():
    form_base = file_as_string("phonebook_form.html")
    nickname_given = request.form['nickname']
    number_given = request.form['number']
    if nickname_given != '' or number_given != '':
        if nickname_given != '':
            return checker(nickname_given)
        elif number_given != '':
            return checker(number_given)
    else:
        return "brak danych"


if __name__ == "__main__":
    app.run()

