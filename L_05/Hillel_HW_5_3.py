import string
string_text = input('Please enter text ')
for el in string.punctuation:
    string_text = string_text.replace(el, "")
hashtag = "#" + string_text.title().replace(" ", "")
if len(hashtag)>140:
    result = hashtag[:140]
    print(result)
print(hashtag)