letter_dict = {}
text = 'In this lecture we will review some additional functionalities of python built-in data structures.'
new_text = text.split()
update_text = new_text.split(",")
for word in update_text:
    for letter in word:
        if letter in letter_dict:
            letter_dict[letter] +=1
        else:
            letter_dict[letter] = 1

letter_dict.update({"list": "(words_list"})            

print(new_text)

print(dict(sorted(letter_dict.items)))