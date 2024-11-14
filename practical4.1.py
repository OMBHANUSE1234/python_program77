# practical4.1.py

def set_union(set1, set2):
    return set1.union(set2)


def set_intersection(set1, set2):
    return set1.intersection(set2)


def set_difference(set1, set2):
    return set1.difference(set2)


def set_symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)


def set_subset(set1, set2):
    return set1.issubset(set2)


def set_superset(set1, set2):
    return set1.issuperset(set2)


def set_disjoint(set1, set2):
    return set1.isdisjoint(set2)


def add_element(set1, element):
    set1.add(element)


def remove_element(set1, element):
    set1.remove(element)


def clear_set(set1):
    set1.clear()


# Example usage
if __name__ == "__main__":
    s1 = {1, 2, 3}
    s2 = {3, 4, 5}

    print("Union:", set_union(s1, s2))
    print("Intersection:", set_intersection(s1, s2))
    print("Difference:", set_difference(s1, s2))
    print("Symmetric Difference:", set_symmetric_difference(s1, s2))
    print("Subset check:", set_subset(s1, s2))
    print("Superset check:", set_superset(s1, s2))
    print("Disjoint check:", set_disjoint(s1, s2))


