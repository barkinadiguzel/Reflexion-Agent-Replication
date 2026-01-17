class Policy:
    def __init__(self, memory):
        self.memory = memory

    def build_prompt(self, state):
        memories = "\n".join(self.memory.get_all())
        prompt = f"""
Past Reflections:
{memories}

Current State:
{state}

What is the best next action?
"""
        return prompt
