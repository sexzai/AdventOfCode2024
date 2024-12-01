def intercalate(arr, left_arr, right_arr): 
    for i in range(0,len(arr)):
        if i % 2 == 0:
            left_arr.append(int(arr[i]))
        else: right_arr.append(int(arr[i]))

#def insertion_sort(arr):
#    for i in range(1,len(arr)):
#        j = i 
#        while arr[j - 1] > arr[j] and j > 0:
#            arr[j - 1], arr[j] = arr[j], arr[j - 1]
#            j -= 1

def comparison (left_arr, right_arr, value):
    if len(left_arr) == len(right_arr):
        for i in range(0,len(left_arr)):
            value += abs(left_arr[i] - right_arr[i])
        return value
    else: print('the lists lenghts cant be compared')

def occurences(left_arr,right_arr):
    value = 0
    for i in range(0,len(left_arr)):
        k = 0
        for j in range(0,len(right_arr)):
            if left_arr[i] == right_arr[j]:
                k += 1
        value += left_arr[i] * k
    return value
 

f = open('src/aocDay1.txt')
raw = f.read().split()
 

list_a = []
list_b = []
location_id = 0
similarity_score = 0

intercalate(raw, list_a, list_b)

list_a.sort() #insertion_sort(list_a)
list_b.sort() #insertion_sort(list_b)
location_id = comparison(list_a,list_b,location_id)
print(location_id)
similarity_score = occurences(list_a,list_b)
print(similarity_score)