import re
from functools import reduce
import os 


f=open('ASTGenSuite.py','r')
o=open('result.txt','w')
list_lines=f.readlines()
start=300
number=0
tempexpect=''
for i in list_lines:
    if (i.find('def')!=-1 and i.find('self')!=-1 ):
        o.write(i)
    elif (i.find('#')!=-1 ):
        o.write(i)  
    elif (i.find('expect')!=-1 and i.find('=')!=-1 ):
        pass
    elif (i.find('self.assertTrue')!=-1):
        number=int(re.findall(r'\d+',i)[-1])
        o.write(i[0:i.find('self.assertTrue')]+'expect=\'\'\n')
        o.write(i)
    else:
        o.write(i)

f.close()
o.close()

os.system('cd .. & py run.py test ASTGenSuite & cd ./test/')

f=open('ASTGenSuite.py','w')
o=open('result.txt','r')

for i in o.readlines():
    if (i.find("#")!=-1):f.write(i)
    elif (i.find("expect=")!=-1):pass
    elif (i.find('self.assertTrue')!=-1):
        number=int(re.findall(r'\d+',i)[-1])
        try:
            ftemp=open('./solutions/'+str(number)+'.txt','r')
            temptab=i[0:i.find('self.assertTrue')]
            f.write(temptab+"expect="+ reduce(lambda x,y:x+y,ftemp.readlines(),'')+'\n')
            ftemp.close()
            f.write(i)
        except FileNotFoundError:
            f.write(i[0:i.find('self.assertTrue')]+'expect=\'\'\n')
            f.write(i)
            print('Không tìm thấy file solution số:'+str(number))
    else:
        f.write(i)

f.close()
o.close()




# elif (i.find('self.assertTrue')!=-1):
#         number=int(re.findall(r'\d+',i)[-1])
#         try:
#             ftemp=open('./solutions/'+str(number)+'.txt','r')
#             temptab=i[0:i.find('self.assertTrue')]
#             o.write(temptab+"expect="+ reduce(lambda x,y:x+y,ftemp.readlines(),'')+'\n')
#             ftemp.close()
#             o.write(i)
#         except FileNotFoundError:
#             o.write(i[0:i.find('self.assertTrue')]+'expect=\'\'\n')
#             o.write(i)
#             print('Không tìm thấy file solution số:'+str(number))