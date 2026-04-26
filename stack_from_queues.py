"""
Stack implemented using two queues.

This module assumes a Queue class with: enqueue(int), dequeue()->int, front()->int, is_empty()->bool, clear()->None.
"""

from __future__ import annotations
from queue import Queue

class StackFromQueues:
    """
    A LIFO stack implemented using two FIFO queues.
    
    At any time, **exactly one** of q1 or q2 holds all the elements; the other is empty.
    Push appends to the non-empty queue.
    Top/Pop shift elements to expose/remove the most-recently-pushed value.
    """

    def __init__(self) -> None:
        # initialize/create the stack from queues
        self.q1 = Queue()
        self.q2 = Queue()

    def is_empty(self) -> bool:
        """
        Empty and returns True iff both queues are empty.
        """
        return self.q1.is_empty() and self.q2.is_empty()

    def push(self, value: int) -> None:
        """
        Enqueue into whichever queue is currently non-empty.
        """
        if not self.q1.is_empty():
            self.q1.enqueue(value)
        else:
            self.q2.enqueue(value)

    def _active_and_passive(self):
        """
        Helper: return (start, final) 
        'start' is the currently non-empty queue; 'final' is the empty queue.
        """
        if not self.q1.is_empty():
            return self.q1, self.q2
        else:
            return self.q2, self.q1

    def top(self) -> int:
        """
        Return the top value *without removing* it.

        Raises:
            AssertionError if the stack is empty.
        """
        assert not self.is_empty(), "top() called on empty stack"
        active, passive = self._active_and_passive()
        while True:
            value = active.dequeue()
            if active.is_empty():
                passive.enqueue(value)
                return value
            passive.enqueue(value)

    def pop(self) -> int:
        """
        Remove and return the top value.

        Raises:
            AssertionError if the stack is empty.
        """
        assert not self.is_empty(), "pop() called on empty stack"
        active, passive = self._active_and_passive()
        while True:
            value = active.dequeue()
            if active.is_empty():
                return value
            passive.enqueue(value)


    def clear(self) -> None:
        """
        Python's GC handles memory; we call clear() to break links and empty both queues.
        """
        self.q1.clear()
        self.q2.clear()

    
