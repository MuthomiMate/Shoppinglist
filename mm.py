current_dict = {'corse': 378, 'cielo': 209, 'mute': 16}

def gen_replace_value_with_definition(key_to_find, definition):
    for key in current_dict.keys():
        if key == key_to_find:
            current_dict[key] = definition
            yield True
    yield False

found = False
while not found:
    found = next(gen_replace_value_with_definition('corse', 'Definition of "corse" via generator'))

print(current_dict)