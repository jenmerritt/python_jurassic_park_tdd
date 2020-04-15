from collections import namedtuple

Diet_Data = namedtuple("Diet_Data", "date carnivore herbivore omnivore")

# I chose this solution to capture the diet data. This way different "snapshots" in time could be captured in the same format and potentially compared over time.
