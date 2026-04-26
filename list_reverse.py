from __future__ import annotations
from typing import Optional
from node import Node

def list_reverse(first: Optional[Node]) -> Optional[Node]:
    """Reverses a singly-linked list in place with explicit type hints."""

    prev = None
    curr = first

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev
