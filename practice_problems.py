"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False

Justification:
I used a set because sets only keep unique items.
Each time we check if a product ID is already there, which is very fast (O(1)).
This makes it easy to find duplicates in one quick pass through the list.

"""

def has_duplicates(product_ids):
    #print(*** Problem 1 ***)
    seen = set()
    for pid in product_ids:
        if pid in seen:
            print("True - duplicates found")
            return True
        seen.add(pid)
    print("False - no duplicates found")
    return False


"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"

Justification:
A set is perfect here because it only keeps unique values.
Every add is fast, and we can get the count by just checking the size of the set.
This makes it simple and efficient to track unique numbers.


"""

from collections import deque

class TaskQueue:
    def __init__(self):
        self._q = deque()

    def add_task(self, task):
        """Add a task to the back of the queue. O(1)."""
        self._q.append(task)
        print(f"Task added: {task}")

    def remove_oldest_task(self):
        """
        Remove and return the oldest task (front of the queue).
        Returns None if the queue is empty.
        """
        if not self._q:
            print("No tasks to remove.")
            return None
        task = self._q.popleft()
        print(f"Task removed: {task}")
        return task


"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2

# Justification:
# I used a set because sets only keep unique items.
# Each time we check if a product ID is already there.
# This makes it easy to find duplicates in one quick pass through the list.

"""

class UniqueTracker:
    def __init__(self):
        self._seen = set()

    def add(self, value):
        """Record a value from the stream. Average O(1)."""
        self._seen.add(value)

    def get_unique_count(self):
        """Return the number of distinct values observed so far. O(1)."""
        return len(self._seen)


#code check
if __name__ == "__main__":
    # Problem 1
    print("*** Problem 1 ***")
    assert has_duplicates([10, 20, 30, 20, 40]) is True
    assert has_duplicates([1, 2, 3, 4, 5]) is False


    # Problem 2
    print("*** Problem 2 ***")
    tq = TaskQueue()
    tq.add_task("Email follow-up")
    tq.add_task("Code review")
    assert tq.remove_oldest_task() == "Email follow-up"
    assert tq.remove_oldest_task() == "Code review"
    assert tq.remove_oldest_task() is None

    # Problem 3
    print("*** Problem 3 ***")
    tracker = UniqueTracker()
    tracker.add(10)
    tracker.add(20)
    tracker.add(10)
    tracker.add(30)
    tracker.add(40)
    print("Unique Count: ", tracker.get_unique_count())

    print("All sample checks passed.")