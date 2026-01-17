from actor.actor import Actor
from evaluator.evaluator import Evaluator
from reflection.reflection_generator import ReflectionGenerator
from memory.short_term import ShortTermMemory
from memory.long_term import LongTermMemory
from policy.policy import Policy
from utils.prompt_utils import build_prompt

class ReflexionPipeline:
    def __init__(self, env, config):
        self.env = env
        self.actor = Actor(config.MODEL_NAME)
        self.evaluator = Evaluator()
        self.reflection_generator = ReflectionGenerator()

        self.short_memory = ShortTermMemory()
        self.long_memory = LongTermMemory(config.MEMORY_SIZE)

    def run(self):
        for episode in range(config.MAX_TRIALS):
            state = self.env.reset()
            self.short_memory.clear()

            done = False
            env_result = None

            while not done:
                prompt = build_prompt(state, self.long_memory.get_all())
                action = self.actor.act(prompt)

                result = self.env.step(action)
                done = result["done"]
                env_result = result

                self.short_memory.add(state, action)
                state = result["observation"]

            trajectory = self.short_memory.get()
            reward = self.evaluator.evaluate(trajectory, env_result)

            reflection = self.reflection_generator.generate(
                trajectory, reward, self.long_memory.get_all()
            )

            self.long_memory.add(reflection)

            print(f"\nEpisode {episode}")
            print("Reward:", reward)
            print("Reflection:", reflection)
