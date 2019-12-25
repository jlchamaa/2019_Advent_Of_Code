from collections import deque


class Repeater:
    def __init__(self):
        self.value = deque()
        self.value.append(1)

    def add_to_the_list(self, addition):
        self.value.append(addition)

    def run_computer(self):
        return self.get_from_the_list()

    def get_from_the_list(self):
        while True:
            yield self.value.popleft()


r = Repeater()
r.add_to_the_list(5)
r.add_to_the_list(5)
r.add_to_the_list(5)
print(next(r.run_computer()))
print(next(r.run_computer()))
print(next(r.run_computer()))
print(next(r.run_computer()))
r.add_to_the_list(6)
print(next(r.run_computer()))
