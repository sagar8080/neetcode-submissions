class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)

        # track longest substring containing only one chr
        max_len = 0

        # track maximum frequency
        max_freq = 0

        # contain character counts
        char_counts = defaultdict(int)

        # two pointer to iterate over the array, find substrings
        l, r = 0, 0

        # iterate
        for r in range(n):
            # get the character counts
            char_counts[s[r]] += 1

            # get the current maximum frequency
            max_freq = max(max_freq, char_counts[s[r]])

            # curr window length: len of substring
            if (r - l + 1) - max_freq > k:
                char_counts[s[l]] -= 1
                l +=  1
        
            max_len = max(max_len, r - l + 1)

        return max_len



