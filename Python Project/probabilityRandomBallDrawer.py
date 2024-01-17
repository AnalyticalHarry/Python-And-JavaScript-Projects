import copy
import random

#Hat class to represent a hat containing colored balls
class Hat:
    def __init__(self, **balls):
        #initialising the contents of the hat based on the provided counts
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    #method to randomly draw a specified number of balls from the hat
    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            return self.contents
        balls_drawn = random.sample(self.contents, num_balls)
        for ball in balls_drawn:
            self.contents.remove(ball)
        return balls_drawn

#probability of drawing a specific combination
def calculate_probability(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0

    #experiment multiple times
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        expected_balls_copy = copy.deepcopy(expected_balls)

        success = True
        for ball in balls_drawn:
            if ball in expected_balls_copy:
                expected_balls_copy[ball] -= 1
                if expected_balls_copy[ball] == 0:
                    del expected_balls_copy[ball]
                    if not expected_balls_copy:
                        break
            if not expected_balls_copy:
                break
        if expected_balls_copy:
            success = False

        if success:
            successful_experiments += 1

    #probability of success
    probability = successful_experiments / num_experiments
    return probability

#hat with colored balls and expected combination
hat = Hat(blue=5, red=4, green=2)
expected_balls = {"red": 1, "green": 2}

#number of balls to be drawn and experiments
num_balls_drawn = 4
num_experiments = 10000

#estimated probability 
probability = calculate_probability(hat, expected_balls, num_balls_drawn, num_experiments)
print(f"The estimated probability is: {probability:.4f}")
