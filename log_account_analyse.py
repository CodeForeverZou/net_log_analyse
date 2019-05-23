import re

pattern=re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}[\s][-].*")
f=open("E:\\last-1000-log","r+")
ss=f.read()
f.close()
result=pattern.findall(ss)

c_post=0
c_get=0
c_del=0
c_ip=0
dict={}     
dict2={}

for i in result:
    #post
    if i.find('GET')!=-1:
        c_get=c_get+1
    elif i.find('POST')!=-1:
        c_post=c_post+1
    elif i.find('DELETE')!=-1:
        c_del=c_del+1
        
    #ip
    ip=re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}",i)[0]
    if ip in dict:
        dict[ip]=dict[ip]+1
    else:
        dict.update({ip:1})
        

    #处理url
    str1=re.findall(r'\b(?:GET|POST|DELETE)(.*)(?:HTTP/\d\.\d)',i)
    if str1:
        str2=re.findall(r'(.*)\?',str1[0])
        if str2:
            if str2[0] in dict2:
                dict2[str2[0]]=dict2[str2[0]]+1
            else:
                dict2.update({str2[0]:1})
        else:
            if str1[0] in dict2:
                dict2[str1[0]]=dict2[str1[0]]+1
            else:
                dict2.update({str1[0]:1})

#生成前四个问题的答案
with open('E:\\accout.txt','w+',encoding='utf-8') as f:
    str1='合计访问：'+str(len(result)-1)+'\n'+'GET次数：'+str(c_get)+'\n'+'POST次数：'+str(c_post)+'\n'+'DELETE次数：'+str(c_del)+'\n'
    f.write(str1)
    f.write('ip'+'\t\t'+'次数'+'\n')
    for i in dict:
        #print(i)
        str2=str(i)+'\t'+str(dict[i])+'\n'
        f.write(str2)

#生成url的答案
ls=sorted(dict2.items(),key = lambda x:x[1],reverse = True)

with open('E:\\url.txt','w+',encoding='utf-8') as f:
    for i in ls:
        f.write(str(i[1])+'\t'+i[0]+'\n')

