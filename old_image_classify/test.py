idx = 'corgi_poodle23.jpg'

first = idx.replace("_", " ")
#second: remove .jpg
second = first.strip(".jpg")
if not second.isalpha():
    second_list = list(second)
    for letter in second_list:
        #if not letter.isalpha() or letter == " "
            #second_list.pop(letter)
        if " " in second_list:
            

