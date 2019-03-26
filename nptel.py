import requests,bs4
x=input("enter the id:")
t=requests.get("https://nptel.ac.in/courses/nptel_download.php?subjectid="+x)
beauty=bs4.BeautifulSoup(t.content,features="lxml")
f_no,to_no=list(map(int,input("from(included) lec number to(excluded) lec number:").strip().split()))
f_no-=1
to_no-=1
def download(url):
    file=url[url.find("filename")+9:url.find(".flv")]+"--"+url[url.find("subjectName")+12:]+".flv"
    r=requests.get(url,stream=True)
    with open(file,"wb") as d:
        for data in r.iter_content(chunk_size=1024):
            d.write(data)
downloadlist=[]
for i in beauty.findAll("a"):
    if "FLV Download" == i.text:
        downloadlist.append("https://nptel.ac.in"+i["href"])
for i in downloadlist[f_no:to_no]:
    download(i)
