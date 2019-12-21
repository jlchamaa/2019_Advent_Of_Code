#!/usr/bin/python3.6
DATA_FILE = "simple.txt"


def get_orbits_from_data(data_file):
    with open(data_file) as f:
        lines = f.readlines()
        clean_lines = [ line.strip() for line in lines]
        return [ tuple(line.split(")")) for line in clean_lines]

def create_tree(orbits):
    tree = {}
    for orbit in orbits:
        parent, child = orbit
        if parent not in tree:
            parent_planet = Planet(parent)
            tree[parent] = parent_planet
        if child not in tree:
            child_planet = Planet(child)
            tree[child] = child_planet
        tree[child].name_parent(parent)
    return tree


def count_orbits(tree):
    count = 0
    for name, planet in tree.items():
        parent = planet.parent
        while parent is not None:
            parent = tree[parent].parent
            count += 1
    return count


def shortest_distance(tree, p1 , p2):
    p1_distances, p2_distances = [],[]
    while p1 is not None:
        p1_distances.append(p1)
        p1 = tree[p1].parent
    while p2 is not None:
        p2_distances.append(p2)
        p2 = tree[p2].parent
    #TODO THIS WON'T WORK IF THEy BOTH ORBIT COM
    while p1_distances[-2] == p2_distances[-2]:
        p1_distances.pop()
        p2_distances.pop()
    return len(p1_distances) + len(p2_distances) - 4

class Planet:
    def __init__(self, name):
        self.name = name
        self.parent = None

    def __repr__(self):
        return "{} orbits {}".format(self.name, self.parent)

    def name_parent(self, parent):
        self.parent = parent


def main():
    orbits = get_orbits_from_data(DATA_FILE)
    tree = create_tree(orbits)
    return shortest_distance(tree, "YOU", "SAN")


if __name__ == "__main__":
    print(main())
