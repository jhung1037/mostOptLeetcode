from collections import Counter
from collections import defaultdict

arr = [1,2,1,3,4,2,4,3,3,4]
res = 0
ref = Counter(arr)
check_ref = defaultdict(set)
for k, v in ref.items():
    check_ref[v].add(k)
for i in range(len(arr)):
    if len(arr)-i <= res:
        break
    dic = ref.copy()
    check = check_ref.copy()
    for j in range(len(arr)-1,i-1,-1):
        if j-i < res:
            break
        if len(check) == 1:
            res = j-i+1
        
        if len(check[dic[arr[j]]]) == 1:
            del check[dic[arr[j]]]
        else:
            check[dic[arr[j]]].discard(arr[j])
        dic[arr[j]] -= 1
        check[dic[arr[j]]].add(arr[j])
        if dic[arr[i]] == 0:
            del dic[arr[i]]
            del check[dic[arr[j]]]
    
    if len(check_ref[ref[arr[i]]]) == 1:
        del check_ref[ref[arr[i]]]
    else:
        check_ref[ref[arr[i]]].discard(arr[i])
    ref[arr[i]] -= 1
    check_ref[ref[arr[i]]].add(arr[i])
    if ref[arr[i]] == 0:
        del ref[arr[i]]
        del check_ref[ref[arr[i]]]

print(res)