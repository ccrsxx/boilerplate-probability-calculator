import copy
import random

class Hat:
    
    def __init__(self, **colors):
        self.contents = [color for color, draw in colors.items() for _ in range(draw)]

    def draw(self, draw):
        if draw >= len(self.contents):
            self.contents, poped_list = [], self.contents
            return poped_list
        return [self.contents.pop(random.randrange(len(self.contents))) for _ in range(draw)]

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    many = 0
    for _ in range(num_experiments):
        exact = 0
        same = {}
        cls = copy.deepcopy(hat)
        data = cls.draw(num_balls_drawn)
        for color in data:
            if color in expected_balls:
                same[color] = same.get(color, 0) + 1
        if len(same) != len(expected_balls):
            continue
        for k, v in expected_balls.items():
            if same[k] >= v:
                exact += 1
        if exact == len(expected_balls):
            many += 1
    return many / num_experiments
