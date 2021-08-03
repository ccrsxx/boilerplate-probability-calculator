import copy
import random

class Hat:
    
    def __init__(self, **colors):
        self.contents = [color for color, draw in colors.items() for _ in range(draw)]

    def draw(self, draw):
        if draw > len(self.contents):
            return self.contents
        return [self.contents.pop(random.randrange(len(self.contents))) for _ in range(draw)]

def experiment(hat, num_balls_drawn, num_experiments, **expected_balls):
    pass


x = Hat(red=5, orange=3, black=2)

# shit = {}
# sample = x.draw(10)
# for i in sample:
#     shit[i] = shit.get(i, 0) + 1
# print('up', shit)

# check = {i: sample.count(i) for i in sample}
# print(check)
