import csv
import json

import jieba
import os

#读取文件
def  read_data(file_path):
    txt=open(file_path,'r',encoding='utf-8').read()
    txt = txt.lower()
    #print(txt)
    return txt
#将文件分词
def cut_list(data):
    word_list=jieba.lcut(data)
    print("分词后字符总长度：")
    print(len(word_list))
    return word_list
#统计分词个数放到字典中
def frequency(word_list):
    word_counts={}
    for word in word_list:
        word_counts[word]=word_counts.get(word,0)+1
    return word_counts
#将字典转化为列表按大到小排序
def sort_word(word_counts):
    word_counts_list=list(word_counts.items())
    word_counts_list.sort(key=lambda x:x[1],reverse=True)
    return  word_counts_list
#将统计后的内容输入到文件中
def data_output(file_path,out_data_list):
    #print(out_data_list)
    file_path=file_path+"_OutPut.txt"
    with open(file_path,'w',encoding='utf-8') as f_obj:
        for i in out_data_list:
            s=str(i[0])+"?/?"+str(i[1])+"?/?"
            f_obj.write(s)
        print("统计后输出文件:"+file_path)
        return file_path
#以上函数的总操作
def document(file_name):
    data=read_data(file_name)
    word_list=cut_list(data)
    word_counts_dict=frequency(word_list)
    word_counts_list=sort_word(word_counts_dict)
    file_paths=data_output(file_name,word_counts_list)
    return file_paths
#将txt转换为json
def generate(file):
    with open(file,"r",encoding="utf-8") as file:
        lists=file.read()
        lists1=lists.split("?/?")
        string_list = dict(zip(lists1[::2],lists1[1::2]))
        str0 = json.dumps(string_list,indent=4,ensure_ascii=False)
        return str0
        #print(str0)

def generates(path,str0):
    file_path = path + "_OutPut.json"
    with open(file_path,"w",encoding="utf-8") as f_ojb:
        f_ojb.write(str0)
    print("转换后输出文件:" + file_path)
    return file_path
def generatesg(path):
    str0=generate(path)
    file_path=generates(path, str0)
    return file_path
#根据key查找value
def traverse(data, fields, values=str):
    string=data[fields]
    values=string
    return values
#将string转换为dict
def outtraverse(file_path):
    with open(file_path,"r",encoding="utf-8") as f_rpj:
        str = f_rpj.read()
        data = json.loads(str)
        print("json读取出的字典：")
        print(data)
        return data
#将数据储存到csv中
def csvstorage(file):
    file_path = file + "_OutPut.csv"
    with open(file_path,"w",encoding="utf-8_sig",newline="") as f_ojb:
        data=outtraverse(file)
        datak = list(data.keys())
        datav = list(data.values())
        head=["分词","计数"]
        rows=list(zip(datak,datav))
        write=csv.writer(f_ojb)
        write.writerow(head)
        write.writerows(rows)
    print("储存后输出文件:" + file_path)
    return file_path


