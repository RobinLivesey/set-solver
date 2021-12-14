from random import randrange
import itertools

class FeatureDefinition:
    def __init__(self, name, values):
        self.name = name
        self.values = values

class SetComponent:
    def __init__(self, feature_values):
        self.feature_values = feature_values

feature_definitions = [
    FeatureDefinition("Count", ["1", "2", "3"]),
    FeatureDefinition("Shade", ["Solid", "Stripped", "Outlined"]),
    FeatureDefinition("Color", ["Red", "Purple", "Green"]),
    FeatureDefinition("Shape", ["Oval", "Squiggle", "Diamond"])
]

def create_random_set_component(feature_definitions):
    feature_values = []
    for feature_def in feature_definitions:
        rand = randrange(3)
        feature_values.append(feature_def.values[rand])
    return SetComponent(feature_values)

# Generate some random components
# TODO: Automated method to load 
components = []
count = 12
for i in range(count):
    components.append(create_random_set_component(feature_definitions))

# Find all possible sets
all_perms = list(itertools.combinations(components, 3))

# Find actual sets
def validate_set(perm, feature_definitions):
    is_set = True
    # reason = ""
    for i in range(len(feature_definitions)):
        name = feature_definitions[i].name
        values = []
        for comp in perm:
            values.append(comp.feature_values[i])
        # print(name, values)
        if len(set(values)) == 2:
            is_set = False
            # reason = "%s: Two are %s and one is not." % (name, max(set(values), key=values.count))
    return is_set
    
    # if is_set:
    #     print("THIS IS A SET")
    # else:
    #     print("NOT A SET")
    #     print(reason)
    
    
for perm in all_perms:
    is_set = validate_set(perm, feature_definitions)
    if is_set:
        print("SET")
    