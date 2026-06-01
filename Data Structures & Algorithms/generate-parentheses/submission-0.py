
"""
Understand:
Given n which represents the number of pairs of paranthesis, return all the possible combinations of the well formed paranthesis
Input: integer n, output is the list of the formed pairs
Edge cases. n is 0, 
Constraints: Only the parentheis
Match:
Like valid parenthesis, the generated paranthesis have to be valid and therefore we can exploit the use of the stack becauase of its LIFO

Plan:
Brute Force Way which is not really efficient
Generate all the possible paranthesis combinations and then check if they are valid
In generating them, ensure that the open and the close brackets are the same number
Then for each combination, check validity.

Efficient way is back tracking.
Only add an open paranthesis if open < n
Only add a close paranthesis if close < open
Its valid IFF open = close = n
do it recusively



So what I am finding out is that we have to make a decision tree.
Decision Tree is like this.
node - the current choice we have made so far
each branch -  a decision, either include, skip an element or choose it
each path from root to leaf - this is one complete combination or subset or permutation

 Backtracking is:

building a solution piece by piece

removing the last piece when it fails or after finishing with it

trying the next alternative

So to build a decision tree right, its like brute force solution for the most part
So we have an empty root
def build(s, openN, closeN):
    if (openN == len(s) == closeN):
        return "".join(s)
    
    if openN < n:
        s.append("(")
        build(s, openN + 1, closeN)
        s.pop()
    if closeN < openN
        s.append(")")
        build(s, openN, closeN + 1)
        s.pop()

So you come up with a decision tree right, at this stage, I have made this choice "". Then from here, I could either pick open bracket or close bracket  and I also need to
Check if I still have enough open brackets right etc. Then after you have this you have a bunch of constraints that you need to satisfy, you know that you need to pick open before close, you know you need to have a max of n for both close and open and also you know that you need to return the string once the length you have is 2 * n. When you then convert this into recursion, whatever conditions leading to the base case they are stated first.
Then you are like cool, then you need a condition thats gonna control the adding of an open bracket, you add one as long as this is less than n. So you either add the open bracket or not. So you add, and then you build the rest of the string with that. And then you have to pop so that this is now the part where you have to go back to the other decision right, so we are done with open bracket, pop it so you go to the original prior to the open and then now we decide what we are gonna do for the next pahse
next phase is us checking if its valid to add the closed bracket and then we do that , if we add it, then we have got to pop it back out. 
   
  🌳 Decision Tree & Backtracking — Core Idea
✅ When generating combinations, permutations, or subsets, you’re building a decision tree.

Node → Represents the current choice (partial solution) you’ve built so far.

Branch → Represents a decision at that point (e.g., include an element, skip it, or choose it).

Path from root to leaf → Represents one full solution (a complete combination, subset, or permutation).

💡 What is Backtracking?
Backtracking is a strategy where you:

Build the solution piece by piece.

Remove the last piece (undo the choice) when it fails or after finishing with it.

Try the next alternative at that decision point.

It is like a smart form of brute force:
You explore all possible paths, but efficiently, by pruning invalid paths early and reusing partial solutions.

🚀 Example: Generating Parentheses
🎯 Goal: Generate all valid strings of n pairs of parentheses.

Key constraints:

You can’t have more ) than ( at any point.

You can have at most n ( and at most n ).

The string is complete when its length is 2 * n.

🧠 How the decision tree works
1️⃣ Start with an empty string ("") — this is the root.
2️⃣ At each stage, decide:

Can I add (? (if openN < n)

Can I add )? (if closeN < openN)

3️⃣ After making a choice:

Recursively build the rest of the string.

After recursion, pop the last character (backtrack) so you can try other choices from that point.

📝 General recursion structure
python
Copy
Edit
def build(s, openN, closeN):
    if openN == closeN == n:
        # Solution complete
        return "".join(s)

    if openN < n:
        s.append("(")
        build(s, openN + 1, closeN)
        s.pop()  # Backtrack: undo the "("

    if closeN < openN:
        s.append(")")
        build(s, openN, closeN + 1)
        s.pop()  # Backtrack: undo the ")"
⚡ The thought process in building the tree
At the root: I’ve made the choice "" (empty string).

From here, I can pick ( or ) → I check if conditions allow it (enough open, can close).

Each decision grows the string and pushes us deeper in the tree.

After building a path, I backtrack by popping the last choice and exploring the next valid option.

Once a path reaches length 2 * n, we’ve found a complete valid string. 
   
    """

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        backtrack(0, 0)
        return res
            
            


        