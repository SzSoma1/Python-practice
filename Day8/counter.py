def calculate_love_score(name1, name2):
    true = [ 'T', 'R', 'U', 'E']
    love = ['L', 'O', 'V', 'E']
    combined_names = (name1 + name2).upper()
    count1 = 0
    count2 = 0
    
    for letters1 in true:
        for letters2 in combined_names:
            if letters2 == letters1:
                count1 += 1
        
    for letter1 in love:
        for letter2 in combined_names:
            if letter2 == letter1:
                count2 += 1
                
    score = int(str(count1) + str(count2))
    print(score)
    
calculate_love_score (name1="Kanye West", name2="Kim Kardashian")