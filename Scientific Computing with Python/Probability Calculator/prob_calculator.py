import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, no_of_balls in kwargs.items():
            for i in range(no_of_balls):
                self.contents.append(color)

    def draw(self, no_of_balls):
        balls_drawn = []

        # Draw all the available balls if requirement is more than no. of balls in hat
        if no_of_balls >= len(self.contents):
            balls_drawn = self.contents[:]
            self.contents.clear()
            return balls_drawn
        
        # Draw a ball randomly from the hat
        for i in range(no_of_balls):
            ball_drawn = random.choice(self.contents)
            balls_drawn.append(ball_drawn)
            self.contents.remove(ball_drawn)

        return balls_drawn

    def __str__(self):
        return f'{self.contents}'
        
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    success = 0

    for i in range(num_experiments):
        # Create a deepcopy of hat
        hat_copy = copy.deepcopy(hat)

        # Draw balls from hat
        balls_drawn = hat_copy.draw(num_balls_drawn)

        # Compare the outcome with requirements
        outcome = [balls_drawn.count(color) >= expected_balls[color] for color in expected_balls]

        # Requirement satisfied
        if all(outcome):
            success += 1

    probability = success / num_experiments

    return probability
