def anagram(s1, s2):
    
    print('s1: '+ s1 + ' s2: ' + s2)
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    
    print('s1: '+ s1 + ' s2: ' + s2)
    print(s1 == s2)
    s3 = sorted(s1)
    s4 = sorted(s2)
    
    print('s1: '+ str(s3) + ' s2: ' + str(s4))
    print(s3 == s4)
    return sorted(s1) == sorted(s2)

print(anagram('dog', 'god,'))

print()