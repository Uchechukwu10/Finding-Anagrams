# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):

	word = word.lower()
	anagram = anagram.lower()

	if(len(word) == len(anagram)): 
		wordSorted = sorted(word)
		anagramSorted = sorted(anagram)
		
		if(wordSorted == anagramSorted):
			return True
		else:
			return False

	else: 
		return False


print(find_anagram("Lacks", "Slack"))


