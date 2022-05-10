# list1=["one","two","three","four","five"]
# list2=[1,2,3,4,5]
# dic={}
# for key in list1:
#     for value in list2:
#         dic[key]=value
#         list2.remove(value) 
#         break
# print(dic)


list1 = [1, 2, 3]
list2 = [4, 5, 6]
a_zip = zip(list1, list2) 
zipped_list = list(a_zip) 
print(zipped_list)
