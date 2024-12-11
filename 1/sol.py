def get_lists():
    list1 = []
    list2 = []
    with open("input", "r") as f:
        lines = f.readlines()
        for line in lines:
            nums = line.split("   ")
            list1 += [int(nums[0])]
            list2 += [int(nums[1])]
        list1.sort() 
        list2.sort() 
    return list1, list2
    
def sum_distances():
    tot_distance = 0
    list1, list2 = get_lists()
    for i in range(0, len(list1)):
        tot_distance += abs(list1[i] - list2[i])

    return tot_distance

print(sum_distances())

def similarity_score():
    similarity_score = 0
    list1, list2 = get_lists() 
    hashmap = {}
    for num in list2:
        if num in hashmap:
            hashmap[num] += 1
        else:
            hashmap[num] = 1
    for num in list1:
        if num in hashmap:
            similarity_score += num*hashmap[num]

    return similarity_score  

print(similarity_score())