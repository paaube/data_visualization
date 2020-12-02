from random import choice

class RandomWalk:
    """A class to generate random walks"""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk"""
        self.num_points = num_points

        # all walks start at (0, 0)
        self.x_val = [0]
        self.y_val = [0]

    def get_step(self):
        """Calculate the steps"""

        # decide which direction to go and how far to go in that direction
        direction = choice([1,-1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step

    def fill_walk(self):
        """Calculate all the points in the walk"""

        # keep taking steps until the walk reaches the desired length
        while len(self.x_val) < self.num_points:
            
            x_step = self.get_step()
            y_step = self.get_step()

            # reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # calculate the new position
            x = self.x_val[-1] + x_step
            y = self.y_val[-1] + y_step

            self.x_val.append(x)
            self.y_val.append(y)
            
