#import pdb

set1 = {"beans", "Meat", "yam"}
set2 = {"beans", "rice", "Yam"}
#pdb.set_trace()
#set1.remove("yam")
#set1.add("yam")
set3 = set1 & set2
#set1.union(set2)

#set3.issubset(set1)

print(set3)