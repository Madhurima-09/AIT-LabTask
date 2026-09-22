class MonkeyBananaProblem:
    def __init__(self):
        self.monkey_pos = "at_banana"
        self.box_pos = "at_corner"
        self.monkey_height = "on_floor"
        self.has_banana = False

    def solve(self):
        if self.monkey_pos == "at_banana" and self.monkey_height == "on_floor":
            self.monkey_pos = self.box_pos
            print("Action: walks to box")

            self.monkey_pos = "at_banana"
            print("Action: Push box under banana")

            self.monkey_height = "on_box"
            print("Action: climb onto box")

            self.has_banana = True
            print("Action: Grab banana")


problem = MonkeyBananaProblem()
problem.solve()
