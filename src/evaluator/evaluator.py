class Evaluator:
    def evaluate(self, trajectory, env_result):
        if env_result["success"]:
            return 1.0
        return 0.0
