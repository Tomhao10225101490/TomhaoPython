n = int(input())
for i in range(n):
    print("case #%d:"%i)
    str_ = input()
    upper_counting  = 0
    lower_counting  = 0
    space_counting = 0
    number_counting  = 0
    other_counting  = 0
    for letter in str_:
        if letter.isuper():
            upper_counting += 1
        elif letter == " ":
            space_counting += 1
        elif letter.islower():
            lower_counting += 1
        elif letter.isdigit():
            number_counting += 1
        else:
            other_counting += 1
    print(upper_counting,lower_counting,space_counting,number_counting,other_counting)    
        
        
            