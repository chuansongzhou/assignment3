
"""
Queue implemented using two stacks (s1 and s2).

- Enqueue pushes onto s1.
- Dequeue/front shift elements from s1 to s2 when s2 is empty, then operate on s2.
- Empty iff both stacks are empty.

This module provides both:
- A Pythonic class `QueueFromStacks`.
"""

from __future__ import annotations

# Use the appropriate import based on your project layout:
# If this file is inside a package with stack.py:
# from .stack import Stack
# Otherwise, if it's a simple script in the same directory:
from stack import Stack


class QueueFromStacks:
    """
    FIFO queue implemented using two LIFO stacks:
    - s1 collects enqueued elements,
    - s2 serves dequeues/fronts by reversing s1 when needed.
    """

    def __init__(self) -> None:
        # Equivalent to queue_from_stacks_create()
        self.s1 = Stack()
        self.s2 = Stack()

    def is_empty(self) -> bool:
        """        
        Empty and returns True iff both stacks are empty.
        """
        return self.s1.is_empty() and self.s2.is_empty()
        
    def enqueue(self, value: int) -> None:
        """
        Push onto s1.
        """
        self.s1.push(value)
        
    def _shift_if_needed(self) -> None:
        """
        Move all elements from s1 to s2 *only if* s2 is empty.
        This makes the oldest element (front of queue) appear on top of s2.
        Amortized O(1) per operation.
        """
        if self.s2.is_empty():
            while not self.s1.is_empty():
                self.s2.push(self.s1.pop())

                
    def front(self) -> int:
        """
        Return the front value without removing it.
        
        Raises:
           AssertionError if the queue is empty.
        """
        assert not self.is_empty(), "queue is empty"
        self._shift_if_needed()
        return self.s2.peek()

        
    def dequeue(self) -> int:
        """
        Remove and return the front value.
        
        Raises:
           AssertionError if the queue is empty.
        """
        assert not self.is_empty(), "queue is empty"
        self._shift_if_needed()
        return self.s2.pop()
        
    def clear(self) -> None:
        """
        Frees both stacks. Python GC handles memory; this breaks links explicitly.
        """
        self.s1.clear()
        self.s2.clear()
