from collections import defaultdict

def group_anagrams(strs):
    anagram_map = defaultdict(list)

    for word in strs:
        # Sort the word and use it as the key
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)
    
    # Return the grouped anagrams as a list of lists
    return list(anagram_map.values())

# Example usage
input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(input_list))
