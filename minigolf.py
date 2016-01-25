def g(c,p):
 o=[''.join(x).split()[0] for x in zip(*c.split('\n'))]
 t={"_":1,"/":5,"\\":-4,'0':0}
 for v in o:
	if v=="U" or p<1:return p>0
	p-=t[v]

def prep_course(course):
 course = '\n'.join(course.split('\n')[1:])
 course = '\n'.join(course.split('\n')[:-1])
 return course

powr = 27
course = prep_course("""
____  _ 
    \/ U
""")
print g(course,powr) #True
course = prep_course("""
      ____       ____ _   
   __/    \     /    U \  
__/        \   /        \_
            \_/           
""")
print g(course,powr) #True

course = prep_course("""
      ____       //// _   
   __/    \     /    U \  
__/        \   /        \_
            \_/           
""")
print g(course,powr) #False

course = prep_course("""
_____//\\\\\U
""")
print g(course,powr) #True

powr=15 
print g(course,powr) #false 

powr=30 
print g(course,powr) #true
