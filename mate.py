cities = {'Kapsabet': {'Kisumu': 100,
                       'Nairobi': 200,
                       'Molo': 150},
          'Nakuru': {'Kapsabet': 200,
                     'Molo': 100},
          'Nairobi': {'Nakuru': 250,
                      'Garissa': 300,
                      'Mombasa': 600,
                      'Kajiado': 50},
          'Kajiado': {'Nairobi': 50,
                      'Molo': 200},
          'Mombasa': {'Nairobi': 600}}


source='Molo'
destination='Garissa'
if source in cities.keys():
  result = cities[source]
  destinationd=result[destination]
  print (destinationd)
print ("Destination not found")






# def distance(source, destination):
#     distance = 0
#     for key in cities:
#         source = cities[source]
# #
# # print cities[key]
# #        print key
#         for value in cities[key]:
#             if cities[key] != cities[key][value]:
#                # source = cities[source[value]]  # the key value is the source
#                 # destination = cities[destination[value]]
#                 distance += cities[destination][value]
#             return distance
#                 # print value
#             # print cities[key][value]
#         # print key[value,value]
# distance('Nakuru','Molo')

# distance_ = []
# def calc_distance (source, destination):
#
#     for a_city in cities[city]:
#         if destination in cities[city] and a_city in places:
#             if city in cities[source]:
#                 print city
#                 print a_city
#                 distance.append(cities[source][city])
#                 distance.append(cities[city][a_city])
#                 added = 0
#                 for x in distance:
#                     added += x
#                 print ('From {source} to {dest} is {added}')
#             else:
#                 pass
#         else:
#             return False
#
#
#     for city in cities:
#         if places[0] in cities:
#             calc_distance(places[0], places[1])
#         elif places[1] in cities:
#             calc_distance(places[1], places[0])
#         else:
#             print 'Source 1 is not in list'
#
#     distance_()
