class ShortTermMemory:
    def __init__(self):
        self.trajectory = []

    def add(self, state, action):
        self.trajectory.append((state, action))

    def clear(self):
        self.trajectory = []

    def get(self):
        return self.trajectory
