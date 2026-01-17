from collections import deque

class LongTermMemory:
    def __init__(self, max_size):
        self.memory = deque(maxlen=max_size)

    def add(self, reflection):
        self.memory.append(reflection)

    def get_all(self):
        return list(self.memory)
