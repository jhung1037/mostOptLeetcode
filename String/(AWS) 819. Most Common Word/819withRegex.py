from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Convert banned words to a set for O(1) lookup
        banned_set = set(banned)
        
        # Use regex to split the paragraph into words
        words = re.findall(r'\w+', paragraph.lower())
        
        # Count word frequencies, excluding banned words
        word_counts = Counter(word for word in words if word not in banned_set)
        
        # Return the most common word
        return max(word_counts, key=word_counts.get)