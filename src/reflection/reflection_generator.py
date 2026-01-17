class ReflectionGenerator:
    def generate(self, trajectory, reward, memory):
        reflection = f"""
Trajectory:
{trajectory}

Reward: {reward}

What went wrong? What should be improved next time?
"""
        return reflection
