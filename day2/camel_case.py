'''
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"
'''
# the best solution def to_camel_case(text):
# return text[:1] + text.title()[1:].replace('_', '').replace('-', '')

def main():

    print(to_camel_case("THE-StEalth_wARRIOR"))


def to_camel_case(text):
    
    #split the word at - and _
    split = text.replace("-", " ").replace("_", " ").split()
    
    #seperate first word
    first = split.pop(0)
    new_first = first[0] + first.title()[1:]
    
    new_list = []
    #capitalise remaining words
    for word in split:
        x = word.capitalize()
        new_list.append(x)
    
    #concatenate the first word to the new word
    new_word = new_first + "".join(new_list)
    
    return new_word

if __name__ == "__main__":
    main()

