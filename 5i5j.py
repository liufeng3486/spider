#coding=utf-8
import copy
import requests
import requests
import re
import requests,sys,re,time
import datetime
reload(sys)
sys.setdefaultencoding( "utf-8" )
path = "./5i5j/"
#要有cookie

def returnFangList(page_num):
    if page_num == 1:
        url = "https://sh.5i5j.com/zufang/"
    else:
        url = "https://sh.5i5j.com/zufang/n"+str(page_num)+"/"
    print url
    url_list = []
    headers = {
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.9",
        'cookie': "_Jo0OQK=537075C4061DE7C199A8EE4CAA13FF249B81B78E827A16BD0786ABD394D99206665C104780D4D08B4C62BC153FCBD0B2A407A11AACED015A8480583A65BC0488DEC52C543717FD271179EEE1053E299EFA59EEE1053E299EFA5BBE3842C9B21EBF1GJ1Z1ZA==; PHPSESSID=sakkehq8rsr4ph8gvkm04oc89q; domain=sh; yfx_c_g_u_id_10000001=_ck18081514124319217273069581495; yfx_f_l_v_t_10000001=f_t_1534313563913__r_t_1534313563913__v_t_1534313563913__r_c_0; yfx_mr_n_10000001=baidu%3A%3Amarket_type_ppzq%3A%3A%3A%3A%3A%3A%3A%3A%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3Ash.5i5j.com%3A%3A%3A%3A%3A%3A%25E5%25B7%25A6%25E4%25BE%25A7%25E6%25A0%2587%25E9%25A2%2598%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3A179%3A%3Apmf_from_adv%3A%3Ash.5i5j.com%2F; yfx_mr_f_n_10000001=baidu%3A%3Amarket_type_ppzq%3A%3A%3A%3A%3A%3A%3A%3A%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3Ash.5i5j.com%3A%3A%3A%3A%3A%3A%25E5%25B7%25A6%25E4%25BE%25A7%25E6%25A0%2587%25E9%25A2%2598%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3A179%3A%3Apmf_from_adv%3A%3Ash.5i5j.com%2F; yfx_key_10000001=; _ga=GA1.2.371671377.1534313564; _gid=GA1.2.1622758701.1534313564; Hm_lvt_94ed3d23572054a86ed341d64b267ec6=1534313564; Hm_lpvt_94ed3d23572054a86ed341d64b267ec6=1534313567",
        'cache-control': "no-cache",
        # 'postman-token': "89d53069-cfc1-e3ed-e357-68a67b948f13"
    }

    response =requests.request("GET", url, headers=headers)
    url_list += re.findall("/zufang/.*?html",response.text)
    # url_list += re.findall("/chuzu/.*?htm", response.text)
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
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.9",
        'cookie': "_Jo0OQK=537075C4061DE7C199A8EE4CAA13FF249B81B78E827A16BD0786ABD394D99206665C104780D4D08B4C62BC153FCBD0B2A407A11AACED015A8480583A65BC0488DEC52C543717FD271179EEE1053E299EFA59EEE1053E299EFA5BBE3842C9B21EBF1GJ1Z1ZA==; PHPSESSID=sakkehq8rsr4ph8gvkm04oc89q; domain=sh; yfx_c_g_u_id_10000001=_ck18081514124319217273069581495; yfx_f_l_v_t_10000001=f_t_1534313563913__r_t_1534313563913__v_t_1534313563913__r_c_0; yfx_mr_n_10000001=baidu%3A%3Amarket_type_ppzq%3A%3A%3A%3A%3A%3A%3A%3A%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3Ash.5i5j.com%3A%3A%3A%3A%3A%3A%25E5%25B7%25A6%25E4%25BE%25A7%25E6%25A0%2587%25E9%25A2%2598%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3A179%3A%3Apmf_from_adv%3A%3Ash.5i5j.com%2F; yfx_mr_f_n_10000001=baidu%3A%3Amarket_type_ppzq%3A%3A%3A%3A%3A%3A%3A%3A%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3Ash.5i5j.com%3A%3A%3A%3A%3A%3A%25E5%25B7%25A6%25E4%25BE%25A7%25E6%25A0%2587%25E9%25A2%2598%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3A179%3A%3Apmf_from_adv%3A%3Ash.5i5j.com%2F; yfx_key_10000001=; _ga=GA1.2.371671377.1534313564; _gid=GA1.2.1622758701.1534313564; Hm_lvt_94ed3d23572054a86ed341d64b267ec6=1534313564; Hm_lpvt_94ed3d23572054a86ed341d64b267ec6=1534313567",
        'cache-control': "no-cache",
        # 'postman-token': "89d53069-cfc1-e3ed-e357-68a67b948f13"
    }
    url = "https://sh.5i5j.com" + url
    a = ""
    if poxy:
        response = requests.request("GET", url, headers=headers)
    else:
        response = requests.request("GET", url, headers=headers)
        a = response.text
    try:
        data  = re.findall("<div class=\"jjr_tou\">.*\n\t\t\t\t(.*)</a.*\n\t\t\t<li>(.*)</", a)
        for solo in data:
            name = solo[0];phone = solo[1]
            with open(path+"all", "a+") as file:
                file.write(name + "\t" + phone + "\t" + url +"\t"+ datetime.datetime.now().strftime('%Y%m%d%H%M%S')+"\n")
            set = False
            with open(path+"set", "r") as file:
                if name in file.read():
                    set = True
            print "set",set
            if not set:
                with open(path+"set", "a+") as file:
                    file.write(name + "\t" + phone + "\t" + url +"\t"+ datetime.datetime.now().strftime('%Y%m%d%H%M%S')+ "\n")
        return True
    except:
        return False

if __name__=='__main__':
    # for i in range(2,15):
    #     print i
    #     time.sleep(2)
    #     writeList(returnFangList(i))


    failse = 0
    succ = 0
    for url in readList():
        print url
        if not setCheck(url):
            print "pass"
            continue
        if getMessage(url):
            succ += 1
        else:
            failse += 1
        writeSet(url)
        if failse > 5:
            failse = 0
            print "init"
            time.sleep(3600)
        print "failse:", failse, "  succ:", succ
        time.sleep(60)


