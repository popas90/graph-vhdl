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
        if self.size == 0:
            return None
        old_right = self.right
        self.right = self.right.left
        self.size -= 1
        return old_right

    def pop_left(self):
        if self.size == 0:
            return None
        old_left = self.left
        self.left = self.left.right
        self.size -= 1
        return old_left

    def peek_left(self):
        return self.left

    def peek_right(self):
        return self.right
