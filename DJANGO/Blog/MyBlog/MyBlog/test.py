# INPUT = "CAT"

# Expected Result: "CAT","CTA","ACT","ATC","TCA","TAC"

def perms(word):
  for x in word:
    for y in word:
      print(x,y)


perms("CAT")










# a = [1,2,3,4,5,6,7,8,9,10]
# b = [5,6,7,8,9,10,11,12,13,14,15]
# c = []
# for x in a:
# 	if x in b:
# 		c.append(x)
# print(c)
# c=[]
# a= set(a)
# b = set(b)
# c =  a & b  #a.union(b)

# print(c)
# person = {"name":"John", "age":23, "location":"Pune", "new":23}
# a={value:key for key,value in person.items()}

# print(a)

# l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# b = sum([x for x in l if x%4==0])
# print(b)
# import copy

# a = [1,2,3,4,6,5,9,5,3,1,1,2,3,4,5,6]
# b = copy.deepcopy(a[1:])
# bucket = []
# index = 0
# bucket.append([])
# for x in range(len(b)):
#  # bucket.append([])
#   print(a[x] , b[x])
#   if a[x] < b[x]:
#     bucket[index].append(a[x])
#   else:
#     bucket.append([])
#     index+=1
# max_len = 0
# index = 0
# for x in range(len(bucket)):
#   if len(bucket[x]) > max_len:
#     index = x

# print('longest sequence is {}'.format(bucket[index]))
# for x in bucket:
#   if len(x)>max_len:
#     max_len=x

# print(a)
# print(max(bucket))
# print(bucket)



# # # temp = []* len(a)

# # # var = False
# # # for x in range(len(a)):
# # #   if not var:
# # #     temp.append([])
# # #     var = True
# # #   if a[x]==a[x+1]:

# # #     temp[0].append(x)
# # #   else:
# # #     var = False

# # # print(temp)
