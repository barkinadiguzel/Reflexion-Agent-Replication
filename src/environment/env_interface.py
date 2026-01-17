class VisionEnv:
    def __init__(self, dataset):
        self.dataset = dataset
        self.idx = 0

    def reset(self):
        self.image, self.label = self.dataset[self.idx]
        return self.image

    def step(self, action):
        pred = action.lower().strip()
        gt = self.label

        success = (pred == gt)

        return {
            "observation": f"Ground truth: {gt}",
            "success": success
        }
