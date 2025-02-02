
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"]) #The problem

stations = {} # Define Hash
stations["kone"] = set(["id", "nv", "ut"]) # Add hash functions 
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])


def approximation_algorithm(states_needed, stations):
    final_stations = set() # Final result
    while states_needed: # Run until states_needed == None
        best_station = None
        states_covered = set() # Define variables
        for station, states_for_station in stations.items(): # Look for the most widely station 
            covered = states_needed & states_for_station # Intersection between states_needed and states_for_station
            if len(covered) > len(states_covered): 
                best_station = station
                states_covered = covered
        states_needed -= states_covered # Remove items in the set
        final_stations.add(best_station) # Add the station for the answer
    return print(final_stations)

approximation_algorithm(states_needed, stations)