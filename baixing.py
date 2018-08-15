#coding=utf-8
import copy
import requests
import requests
import re
import requests,sys,re,time
import datetime
reload(sys)
sys.setdefaultencoding( "utf-8" )
path = "./baixing/"

def returnFangList(page_num):
    if page_num == 1:
        url = "http://shanghai.baixing.com/zhengzu/#fromac"
    else:
        url = "http://shanghai.baixing.com/zhengzu/?page="+str(page_num)+""
    print url
    url_list = []
    headers = {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.9",
        'cache-control': "no-cache",
        }

    response =requests.request("GET", url, headers=headers)
    url_list += re.findall("/hezu/.*?htm",response.text)
    url_list += re.findall("/chuzu/.*?htm", response.text)
    url_list = list(set(url_list))


    return url_list

def writeList(url_list,name = path+"url_list"):
    with open(name, "r") as file:
        old = eval(file.read())
    old += url_list
    old = list(set(old))
    print len(old)
    with open(name, "w") as file:
        file.write(str(old))
def readList(name = path+"url_list"):
    with open(name, "r") as file:
        old = eval(file.read())
    return old


def setCheck(url,name=path+"set_url_list"):
    with open(name, "r") as file:
        old = eval(file.read())
    if url in old:
        return False
    return True

def writeSet(url,name=path+"set_url_list"):
    with open(name, "r") as file:
        old = eval(file.read())
    old.append(url)
    with open(name, "w") as file:
        file.write(str(old))
def getMessage(url,poxy=False):
    headers = {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.9",
        'cache-control': "no-cache",
    }
    url = "http://zu.sh.fang.com" + url
    a = ""
    if poxy:
        response = requests.request("GET", url, headers=headers)
    else:
        response = requests.request("GET", url, headers=headers)
        a = response.text
    try:
        name = re.findall("agentName: '(.*)\'", a)[0]
        phone = re.findall("agentMobile: '(.*)\'", a)[0]
        comName = re.findall("comName: '(.*)\'", a)[0]
        if "扫码看电话" in phone:
            print "扫码看电话"
            return False
        with open(path+"all", "a+") as file:
            file.write(name + "\t" + phone + "\t" + url +"\t" +comName+"\t"+ datetime.datetime.now().strftime('%Y%m%d%H%M%S')+"\n")
        with open(path+"set", "r") as file:
            if name in file.read():
                print "重名"
                return True
        with open(path+"set", "a+") as file:
            file.write(name + "\t" + phone + "\t" + url +"\t" +comName+"\t"+ datetime.datetime.now().strftime('%Y%m%d%H%M%S')+ "\n")
        return True
    except:
        return False

if __name__=='__main__':

    for i in range(1,2):
        print i
        time.sleep(2)
        writeList(returnFangList(i))

    # failse = 0
    # succ = 0
    # for url in readList():
    #     print url
    #     if not setCheck(url):
    #         print "pass"
    #         continue
    #     if getMessage(url):
    #         succ += 1
    #     else:
    #         failse += 1
    #     writeSet(url)
    #     if failse > 5:
    #         failse = 0
    #         print "init"
    #         time.sleep(3600)
    #     print "failse:", failse, "  succ:", succ
    #     time.sleep(60)


