"""
Key Insight: Instead of tracking distinct characters, focus on the most frequent character in the window. A window is valid if window_length - count(most_frequent_char) ≤ k. Expand the window by moving the right pointer and shrink it when invalid by moving the left pointer.
Why Sliding Window: You want the longest valid window, and sliding allows you to efficiently explore all possible substrings.z

Refined UMPIRE with Decision Tree Analogy
To address your confusion and incorporate a decision-like approach (similar to your Coin Change decision tree):

Understand
Find longest substring where, after ≤ k replacements, all characters are the same.
Input: s: str, k: int, Output: int.
Edge cases: s="", k=0, len(s)=1, all same characters, k ≥ len(s).
Constraints: All caps, 1 ≤ len(s) ≤ 10^5, 0 ≤ k ≤ len(s).
Intuition: Use a sliding window where replacements needed (window_length - max_freq) ≤ k.
Match
Like Longest Substring with At Most K Distinct Characters: Sliding window with frequency tracking.
Like Sliding Window Maximum: Track max property (here, frequency) in window.
Pattern: Sliding window with dynamic validity check.
Plan
Decision Analogy: At each position, decide to expand window (add character) or shrink (remove character) based on replacements needed.
Initialize freq dictionary, l=0, max_length=0, max_freq=0.
For each r:
Add s[r] to freq, update max_freq.
If (r - l + 1) - max_freq > k, shrink by moving l and updating freq.
Update max_length = r - l + 1.
Handle empty s: return 0.
Intuition Example: s="ABAB", k=2: Window [A,B,A,B] has max_freq=2 (A), replacements=2 ≤ k, length=4.
Implement
(See corrected code above.)

"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        freq = {}
        l, maxLength, maxFreq = 0, 0, 0
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            maxFreq = max(maxFreq, freq[s[r]])
            if (r - l + 1) - maxFreq > k:
                freq[s[l]] -=1
                l+=1
            maxLength = max(maxLength, r - l + 1)
        return maxLength

            

       






        