# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!

#12. Count Items in Structure
#Given a head reference, count the number of items stored.
#Input: "head" → "node1" → "node2" → None
#Output: 3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def count_items(head):
    count = 0
    current = head
    while current is not None:
        count += 1
        current = current.next
    return count


if __name__ == "__main__":
    # Build a simple linked list: head → node1 → node2 → None
    head = Node("head")
    node1 = Node("node1")
    node2 = Node("node2")
    head.next = node1
    node1.next = node2

    print(count_items(head))  # Output: 3




#Reflection

#I chose a stack to solve the “Valid Parentheses” problem because it directly models the nesting 
#and reversal requirements of bracket matching. Every time I encounter an opening bracket, I push 
#it; every time I see a closing bracket, I must match it with the most recent opening bracket, which 
#is exactly what a LIFO structure provides. With a dictionary to map closing to opening brackets, 
#each character is processed in O(1) time, giving an overall O(n) runtime and O(n) space in the 
#worst case.

#The 30-minute limit shaped my decision to bias toward a structure I can implement quickly and 
#reason about confidently. While there are alternative approaches (like repeated string replacement) 
#they tend to be less efficient or trickier to get right under time pressure, especially with edge 
#cases. The stack approach easy to test, and minimizes additional thinking during 
#the timer.

#Trade-offs included disallowing non-bracket characters rather than normalizing or filtering them. 
#Depending on the exact spec, we could choose to ignore non-bracket characters; I rejected them to 
#reduce variety and keep tests clean within the time frame. I also favored clarity over 
#micro-optimizations: the dictionary and explicit checks make the code readable for interviewers 
#and easy to extend (e.g., adding new bracket types). In a longer session, I’d add property-based 
#tests, consider Unicode brackets, and separate parsing from validation for better modularity.

