def g(c,p):
 c=c.split('\n')
 o=[0]*len(max(c,key=len))
 for l in c:
  i=0
  for v in l:
	if v!=" ":o[i]=v
	i+=1
 t={"_":1,"/":5,"\\":-4}
 for v in o:
	if v=="U":break
	p-=t[v]
	if p<1:return
 return 1

powr = 27
course = """
      ____       ____ _
   __/    \     /    U \ 
__/        \   /        \_
            \_/
"""
print g(course,powr)
course = """
      ____       ////____ _
   __/    \     /    U \ 
__/        \   /        \_
            \_/
"""
print g(course,powr)
