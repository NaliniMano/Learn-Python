def countVowel(str):
    vowel="aeiouAEIOU"
    count=0
    for char in str:
            if char in vowel:
                count+=1
    return count

print(countVowel("This is beautiful day"))