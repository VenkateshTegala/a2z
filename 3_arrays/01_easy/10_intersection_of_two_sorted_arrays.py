nums1 = [1,2,2,3,3,4,5,6]
nums2 = [2,3,3,5,6,6,7]
#output = [2,2,3,3,5,6,6]
i = 0
j = 0
mylist = []
while(i < len(nums1) and j < len(nums2)):
    if nums1[i] < nums2[j]:
        i += 1
    elif nums1[i] == nums2[j]:
        mylist.append(nums1[i])
        i += 1
        j += 1
    else:
        j += 1 
print(mylist)