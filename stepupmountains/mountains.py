from models import Mountain

def add_climbed_attribute_to_all(mountain_list, climbed):
    for mountain in mountain_list:
        mountain.add_climbed_attribute(climbed)
    
