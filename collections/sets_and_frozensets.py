# sets and frozen sets

# create a set

fruits = {"apple","banana", "cherry"}
print(fruits)

# Sets are UNORDERED and UNINDEXED

fruits.add("orange")
print(fruits)

fruits.remove("apple")
print(fruits)

# No duplicates in sets
fruits.add("banana")
print(fruits)

# convert a list to a set, to remove duplicates from that list

eg1 = ["one", "two", "three", "one"]

no_dupes = set(eg1)
print(no_dupes)

weird = {"helol", 1, "How", 4, 6,"know"}

print(weird)


# set operations

set_a = {1,2,3,4,5,6,7}
set_b = {5,6,7,8,9,10}

print(set_a | set_b)

# frozen sets are immutable

frozen_set = frozenset(["hello","world"])
print(frozen_set)

normal_set = {"let's", "learn"}
normal_set.add(frozen_set)
print(normal_set)
