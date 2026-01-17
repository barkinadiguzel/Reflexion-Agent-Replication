def build_prompt(state, memories):
    memory_text = "\n".join(memories)

    prompt = f"""
You are an intelligent agent solving a task.

Past reflections:
{memory_text}

Current state:
{state}

Decide the best next action.
"""
    return prompt
