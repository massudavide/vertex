
def import_from_file(file):
    # define empty list
    places = []

    # open file and read the content in a list
    with open(file, 'r') as filehandle:
        places = [current_place.rstrip() for current_place in filehandle.readlines()]
    return places


def save_to_file(places_list, nome_file):
    with open(nome_file, 'w') as filehandle:
        filehandle.writelines("%s\n" % place for place in places_list)



