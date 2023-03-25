def time_to_merge(west,east):
    return

def get_merge_sorted_list(unsorted_list):
    if len(unsorted_list)==1:
        return unsorted_list
    midland = (int(len(unsorted_list))//2)

    east_side = unsorted_list[:midland]
    west_side = unsorted_list[midland:]

    half_east = get_merge_sorted_list(east_side)
    half_west = get_merge_sorted_list(west_side)

    return time_to_merge(half_east,half_west)

    
if __name__ == "__main__":
    pass