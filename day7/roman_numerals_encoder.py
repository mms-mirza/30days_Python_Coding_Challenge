def main():

    integer = int(input("Enter a positive integer between 1 and 3999: "))

    print(solution(integer))


def solution(n):

    # create dictionary with roman numberal keys with corresponding numeric values
    roman_dict = {  1: "I",
                    5: "V",
                    10: "X",
                    50: "L",
                    100: "C",
                    500: "D",
                    1000: "M",
                }

    # create a list with n represented in positional notation with base 10 [1000s, 100s, 10s, 1s]
    num_list = [int(num) * 10**i for i, num in enumerate(reversed(str(n)))]
    num_list.reverse()

    roman_numlist = []

    for num in num_list:
        # check if num is less than 4000
        if num < 4000:
            # check if num corresponds with a key in roman_dict
            if num in roman_dict:
                # append corresponding roman numeral value to roman_numlist
                roman_numlist.append(roman_dict[num])

            # check if number is greater than 1000 but less than 4000
            elif num > 1000:
                # append M up to 3 times to the thousands column
                while num >= 1000:
                    roman_numlist.append(roman_dict[1000])
                    num -= 1000

            # check if number is greater than 500 but less than a 1000
            elif num > 500:
                if num < 900:
                    # append D once to the hundreds column if less than 900
                    roman_numlist.append(roman_dict[500])
                    # append C up to 3 times to the hundreds column
                    while num > 500 and num <= 800:
                        roman_numlist.append(roman_dict[100])
                        num -= 100
                # num is 900, append CM to hundreds column     
                else:
                    roman_numlist.append(roman_dict[100])
                    roman_numlist.append(roman_dict[1000])

            # check if number is greater than 100 but less than 500
            elif num > 100:
                # check if num is less than 400
                if num < 400:
                    # append C up to 3 times to the hundreds column
                    while num >= 100:
                        roman_numlist.append(roman_dict[100])
                        num -= 100
                # num is 400, append CD to hundreds column
                else:
                    roman_numlist.append(roman_dict[100])
                    roman_numlist.append(roman_dict[500])

            # check if number is greater than 50 but less than a 100
            elif num > 50:
                if num < 90:
                    # append L once to the tens column if less than 90
                    roman_numlist.append(roman_dict[50])
                    # append X up to 3 times to the tens column
                    while num > 50 and num <= 80:
                        roman_numlist.append(roman_dict[10])
                        num -= 10
                # num is 90, append XC to tens column     
                else:
                    roman_numlist.append(roman_dict[10])
                    roman_numlist.append(roman_dict[100])

            # check if number is greater than 100 but less than 50
            elif num > 10:
                # check if num is less than 40
                if num < 40:
                    # append X up to 3 times to the tens column
                    while num >= 10:
                        roman_numlist.append(roman_dict[10])
                        num -= 10
                # num is 40, append XL to tens column
                else:
                    roman_numlist.append(roman_dict[10])
                    roman_numlist.append(roman_dict[50])

            # check if number is greater than 5 but less than 10
            elif num > 5:
                if num < 9:
                    # append V once to the tens column if less than 9
                    roman_numlist.append(roman_dict[5])
                    # append I up to 3 times to the tens column
                    while num > 5 and num <= 8:
                        roman_numlist.append(roman_dict[1])
                        num -= 1
                # num is 9, append IX to tens column     
                else:
                    roman_numlist.append(roman_dict[1])
                    roman_numlist.append(roman_dict[10])

            # check if number is greater than 1 but less than 5
            elif num > 1:
                # check if num is less than 4
                if num < 4:
                    # append I up to 3 times to the ones column
                    while num >= 1:
                        roman_numlist.append(roman_dict[1])
                        num -= 1
                # num is 4, append IV to ones column
                else:
                    roman_numlist.append(roman_dict[1])
                    roman_numlist.append(roman_dict[5])
        else:
            print("Enter a positive integer between 1 and 3999")

    return "".join(roman_numlist)            

if __name__ == "__main__":
    main()
