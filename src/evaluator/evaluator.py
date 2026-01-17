class Evaluator:
    def evaluate(self, trajectory, env_result):
        if not env_result["success"]:
            return -1.0

        steps = len(trajectory)

        if steps <= 2:
            return 2.0

        return 1.0
