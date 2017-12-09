student_marks={"john":86.5,"jack":91.2,"jill":84.25,"harry":72.1,"joe":80.5}
print(student_marks)
asc=(sorted(student_marks.values()))
print(asc)
l=len(asc)
d=[]
while l!=0:
    d.append(asc[l-1])
    l=l-1
print("descending order=",d)
print(sum(student_marks.values())/float(len(student_marks)))










