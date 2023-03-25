def time_to_merge(east, west):
    i = j = 0
    merged_city = []

    while i < len(east) and j < len(west):
        if east[i] < west[j]:
            merged_city.append(east[i])
            i += 1
        else: 
            merged_city.append(west[j])
            j += 1

    while i < len(east):
        merged_city.append(east[i])
        i += 1

    while j < len(west):
        merged_city.append(west[j])
        j += 1
    return merged_city

if __name__ == "__main__":
    pass
    pass
