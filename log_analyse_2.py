import re

pattern=re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}[\s][-].*")
f=open("E:\\last-1000-log","r+")
ss=f.read()
f.close()
result=pattern.findall(ss)

n=0
#print(result[0])
dict={}
#print(re.findall(r'\bGET(.*)[(HTTP/\d\.\d)|[?]]',result[0]))

for i in result:

    str1=re.findall(r'\b(?:GET|POST|DELETE)(.*)(?:HTTP/\d\.\d)',i)
    if str1:
        str2=re.findall(r'(.*)\?',str1[0])
        if str2:
            if str2[0] in dict:
                dict[str2[0]]=dict[str2[0]]+1
            else:
                dict.update({str2[0]:1})
        else:
            if str1[0] in dict:
                dict[str1[0]]=dict[str1[0]]+1
            else:
                dict.update({str1[0]:1})

ls=sorted(dict.items(),key = lambda x:x[1],reverse = True)

with open('E:\\url.txt','w+',encoding='utf-8') as f:
    for i in ls:
        f.write(str(i[1])+'\t'+i[0]+'\n')

'''
f=open('E:\\url.txt','w+',encoding='utf-8')
for i in result:

    
    str1=re.findall(r'\b(?:GET|POST|DELETE)(.*)(?:HTTP/\d\.\d)',i)
    if str1:
        str2=re.findall(r'(.*)\?',str1[0])
        if str2:
            f.write(str2[0]+'\n')
        else:
            f.write(str1[0]+'\n')
    else:
        f.write('\n')
        
f.close()
'''
'''
        if n<15:
        n=n+1
        #print(re.findall(r'\b(?:GET|POST|DELETE)(.*)(?:HTTP/\d\.\d)',i))
        str1=re.findall(r'\b(?:GET|POST|DELETE)(.*)(?:HTTP/\d\.\d)',i)[0]
        str2=re.findall(r'(.*)\?',str1)
        
    if i!='':
        str1=re.findall(r'\bGET(?:.*)HTTP/\d\.\d',i)[0]
        str2=re.findall(r'.*\?',str(str1))
        with open('E:\\url.txt','w+',encoding='utf-8') as f:    
            if str2:
                f.write(str2[0]+'\n')
            else:
                f.write(str1+'\n')
        

    with open('E:\\url.txt','w+',encoding='utf-8') as f:
        str1=re.findall(r'\bGET(?:.*)HTTP/\d\.\d',i)
        if str1:
            str2=re.findall(r'.*\?',str(str1))
            f.write(str1[0]+'\n')
        elif str2:
            f.write(str1+'\n')
        
    


    #post
    if i.find('GET')!=-1:
        c_get=c_get+1
    elif i.find('POST')!=-1:
        c_post=c_post+1
    elif i.find('DELETE')!=-1:
        c_del=c_del+1

    #ip
    #print(re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}",i)[0])
    ip=re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}",i)[0]
    if ip in dict:
        dict[ip]=dict[ip]+1
    else:
        dict.update({ip:1})


with open('E:\\accout.txt','w+',encoding='utf-8') as f:
    str1='合计访问：'+str(len(result)-1)+'\n'+'GET次数：'+str(c_get)+'\n'+'POST次数：'+str(c_post)+'\n'+'DELETE次数：'+str(c_del)+'\n'
    f.write(str1)
    f.write('ip'+'\t\t'+'次数'+'\n')
    for i in dict:
        #print(i)
        str2=str(i)+'\t'+str(dict[i])+'\n'
        f.write(str2)

'''
