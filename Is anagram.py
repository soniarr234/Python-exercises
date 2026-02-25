def isAnagram (str1, str2):
    array_str1 = list(str1.lower())
    array_str2 = list(str2.lower())

    if len (array_str1) != len(array_str2):
        print ("It not an anagram")
        return False

    #It an anagram
    array_str1.sort()
    array_str2.sort()

    if array_str1 == array_str2:
        print ("It an anagram")
        return True
    else:
        print ("It not an anagram")
        return False

print (isAnagram("amar", "roma"))
