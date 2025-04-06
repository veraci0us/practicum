from box import Box


def add_property(places, obj):
    box_obj = Box(obj)
    for place in places:
        property = place['property']
        value = place['value']
        if place['root']:
            box_obj[property] = value
        else:
            nested_obj = box_obj.get(place['nest'], Box())
            nested_obj[property] = value
            box_obj[place['nest']] = nested_obj

    return box_obj
