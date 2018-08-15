#coding=utf-8
import copy
import requests
import requests
import re
import requests,sys,re,time
import datetime
reload(sys)
sys.setdefaultencoding( "utf-8" )

def gettitle(id):
    url = "https://zhongyuandichan.anjuke.com/gongsi-jjr-"+str(id)+"/"
    print url

    headers = {
        # 'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.9",
        # 'cookie': "aQQ_ajkguid=D12BEC18-C614-C12F-16CD-6CB77CDDF839; 58tj_uuid=f104f149-cd05-473d-a55c-b8fb93b2bba5; als=0; lps=http%3A%2F%2Fwww.anjuke.com%2F%3Fpi%3DPZ-baidu-pc-all-biaoti%7Chttps%3A%2F%2Fwww.baidu.com%2Fs%3Fwd%3D%25E5%25AE%2589%25E5%25B1%2585%25E5%25AE%25A2%26rsv_spt%3D1%26rsv_iqid%3D0xa6256f990005fc9f%26issp%3D1%26f%3D8%26rsv_bp%3D0%26rsv_idx%3D2%26ie%3Dutf-8%26tn%3Dbaiduhome_pg%26rsv_enter%3D1%26rsv_sug3%3D4%26rsv_sug1%3D5%26rsv_sug7%3D100; twe=2; sessid=AC6AA77A-81A9-CAFC-86FC-6D054F0CC1A2; _ga=GA1.2.590706054.1534230996; _gid=GA1.2.1762135429.1534230996; isp=true; Hm_lvt_c5899c8768ebee272710c9c5f365a6d8=1534231001; Hm_lpvt_c5899c8768ebee272710c9c5f365a6d8=1534231001; ajk_member_captcha=5e923b81ffd711ddb545a96fc5f06d3f; wmda_uuid=b5bf947defb04c1199e6f05dfec3db4d; wmda_new_uuid=1; wmda_visited_projects=%3B6289197098934; __xsptplusUT_8=1; wmda_session_id_6289197098934=1534240639120-b508bce1-63c1-5598; new_session=0; ctid=11; init_refer=https%253A%252F%252Fwww.baidu.com%252Fs%253Fwd%253D%2525E5%2525AE%252589%2525E5%2525B1%252585%2525E5%2525AE%2525A2%2526rsv_spt%253D1%2526rsv_iqid%253D0xa6256f990005fc9f%2526issp%253D1%2526f%253D8%2526rsv_bp%253D0%2526rsv_idx%253D2%2526ie%253Dutf-8%2526tn%253Dbaiduhome_pg%2526rsv_enter%253D1%2526rsv_sug3%253D4%2526rsv_sug1%253D5%2526rsv_sug7%253D100; new_uv=2; propertys=m73fsx-pdg3qa_m73fsn-pdfwpy_; __xsptplus8=8.3.1534240741.1534240882.5%232%7Cwww.baidu.com%7C%7C%7C%25E5%25AE%2589%25E5%25B1%2585%25E5%25AE%25A2%7C%23%23VaHfC53wD0YUCthctcpqeFPSYVuhuFyj%23",
        'cache-control': "no-cache",
        # 'postman-token': "61a274ba-59b3-79aa-bc3c-5db24105bd2d"
        }
    with  requests.request("GET", url, headers=headers) as response:
        a = response.text
    try:
        with open("zjname", "a+") as file:
            file.write(re.findall("title>(.*?)</title", a)[0] +"\t"+str(id)+"\n")
        print id
    except:
        print "not get"

def return58list(page_num):
    if page_num == 1:
        url = "https://sh.58.com/hezu"
    else:
        url = "https://sh.58.com/hezu/pn"+str(page_num)+"/"
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
    url_list += re.findall("//sh.58.com/hezu/.*?shtml",response.text)
    url_list = list(set(url_list))
    return url_list

def writeList(url_list,name = "./data_58/url_list"):
    with open(name, "r") as file:
        old = eval(file.read())
    old += url_list
    old = list(set(old))
    print len(old)
    with open(name, "w") as file:
        file.write(str(old))
def readList(name = "./data_58/url_list"):
    with open(name, "r") as file:
        old = eval(file.read())
    return old

def set58(url,name="./data_58/set_58_url_list"):
    with open(name, "r") as file:
        old = eval(file.read())
    if url in old:
        return False
    return True
def write58set(url,name="./data_58/set_58_url_list"):
    with open(name, "r") as file:
        old = eval(file.read())
    old.append(url)
    with open(name, "w") as file:
        file.write(str(old))
def get58message(url,poxy=False):
    headers = {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.9",
        'cache-control': "no-cache",
    }
    url = "http:" + url
    print url
    a = ""
    if poxy:
        response = requests.request("GET", url, headers=headers)
    else:
        response = requests.request("GET", url, headers=headers)
        a = response.text
    try:
        name = re.findall("fcpc_detail_sh_xingming\'\)\"\>(.*)<", a)[0]
        phone = re.findall("house-chat-txt\">(.*)<", a)[0]
        if "扫码看电话" in phone:
            print "扫码看电话"
            return False
        with open("./data_58/58", "a+") as file:
            file.write(name + "\t" + phone + "\t" + url +"\t" + datetime.datetime.now().strftime('%Y%m%d%H%M%S')+"\n")
        with open("./data_58/58set", "r") as file:
            if name in file:
                print "重名"
                return True
        with open("./data_58/58set", "a+") as file:
            file.write(name + "\t" + phone + "\t" + url +"\t" + datetime.datetime.now().strftime('%Y%m%d%H%M%S')+ "\n")
        return True
    except:
        return False


if __name__=='__main__':
    failse = 0
    succ = 0
    for url in readList():
        if not set58(url):
            print "pass"
            continue
        if get58message(url):
            write58set(url)
            succ += 1
        else:
            failse +=1
        if failse > 5:
            failse = 0
            print "init"
            time.sleep(3600)
        print "failse:",failse,"  succ:",succ
        time.sleep(60)
