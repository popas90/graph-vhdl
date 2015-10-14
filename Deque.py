class EmptyDeque(Exception):
    pass


class DequeNode:

    def __init__(self, data, left_ptr, right_ptr):
        self.data = data
        self.left = left_ptr
        self.right = right_ptr


class Deque:

    def __init__(self):
        self.size = 0
        self.left = None
        self.right = None

    def push_right(self, new_data):
        new_right = DequeNode(new_data, self.right, None)
        self.right = new_right
        self.left = self.left if self.size > 0 else self.right
        self.size += 1

    def push_left(self, new_data):
        new_left = DequeNode(new_data, None, self.left)
        self.left = new_left
        self.right = self.right if self.size > 0 else self.left
        self.size += 1

    def pop_right(self):
        self._validate()
        old_right = self.right
        self.right = self.right.left
        self.size -= 1
        self.left = None if self.size == 0 else self.left
        return old_right.data

    def pop_left(self):
        self._validate()
        old_left = self.left
        self.left = self.left.right
        self.size -= 1
        self.right = None if self.size == 0 else self.right
        return old_left.data

    def peek_left(self):
        return self.left.data if self.size > 0 else None

    def peek_right(self):
        return self.right.data if self.size > 0 else None

    # Stack interface - uses only right side of Deque
    def push(self, new_data):
        self.push_right(new_data)

    def pop(self):
        return self.pop_right()

    def preview_top(self):
        return self.peek_right()

    def _validate(self):
        if self.size == 0:
            raise EmptyDeque("Deque is empty !")
