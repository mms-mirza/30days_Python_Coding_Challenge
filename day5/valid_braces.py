'''
Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.

Examples
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False    
'''
    
def main():

    print(valid_braces("{[()]}")) #output True
    print(valid_braces(")(}{][")) #output False
    print(valid_braces("[(])"))


def valid_braces(string):
    
    opening_braces = [] #store opening braces
    
    map_braces = {close: open for close, open in zip(')]}', '([{')} #map closing braces to opening braces
    
    for brace in string: #iterate over braces in input string
        
        if brace in map_braces: #check if brace is a closing brace
            top_open_brace = opening_braces.pop() if opening_braces else "empty" #if list contains elements pop top open brace, otherwise list is empty
                 
            if map_braces[brace] != top_open_brace: #check if current closing brace matches the corresponding opening brace
                return False #braces match is invalid, therefore False
                
        else: #push brace to opening_braces as it is an opening brace
            opening_braces.append(brace)
    
    return not opening_braces #if opening_braces is empty all corresponding opening and closing pairs are valid, therefore True


if __name__=="__main__":
    main()