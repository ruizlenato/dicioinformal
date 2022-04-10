import httpx
from bs4 import BeautifulSoup

link = "https://www.dicionarioinformal.com.br/"

timeout = httpx.Timeout(20)
http = httpx.Client(http2=True, timeout=timeout, follow_redirects=True)


def definicao(query):
    r = http.get(link + query)
    soup = BeautifulSoup(r.text, "html.parser")
    tit = soup.find_all("h3", "di-blue")
    if tit == None:
        tit = soup.find_all("h3", "di-blue-link")
    title = []
    for i in tit:
        a = i.find("a")
        if a != None:
            title.append(a.get("title"))
    if a == None:
        tit = soup.find_all("h3", "di-blue-link")
    for i in tit:
        a = i.find("a")
        if a != None:
            title.append("você quiz dizer: {}".format(a.get("title")))
    ti = soup.find_all("p", "text-justify")
    tit = []
    for i in ti:
        ti = i.get_text()[17:].replace("""\n                """, "")
        tit.append(ti)
    des = soup.find_all("blockquote", "text-justify")
    des.append(" ")
    desc = []
    for i in des:
        try:
            des = (
                i.get_text()
                .replace("\n"[0], "")
                .replace("                 ", "")
                .replace("""\n                """, "")
            )
        except:
            if i == " ":
                des = ""
        desc.append(des)
    result = []
    max = 0
    for i in title:
        try:
            b = {
                "title": i.replace("\t", ""),
                "tit": tit[max].replace("\t", ""),
                "desc": desc[max].replace("\t", "").replace("                ", ""),
            }
            max += 1
            result.append(b)
        except:
            pass

    return dict(results=result)


def sinonimos(query):
    r = http.get(link + "sinonimos/" + query)
    soup = BeautifulSoup(r.text, "html.parser")
    a = soup.find("p", "text-justify")
    result = []
    for i in a.find_all("a"):
        result.append(i.get_text())
    a = soup.find("h4", "link_cinza").get_text()
    result = {"title": a, "sinonimos": result}
    return dict(results=result)


def antonimos(query):
    r = http.get(link + "antonimos/" + query)
    soup = BeautifulSoup(r.text, "html.parser")
    a = soup.find("p", "text-justify")
    result = []
    for i in a.find_all("a"):
        result.append(i.get_text())
    a = soup.find("h4", "link_cinza").get_text()
    result = {"title": a, "antonimos": result}
    return dict(results=result)


def relacionadas(query):
    r = http.get(link + "relacionadas/" + query)
    soup = BeautifulSoup(r.text, "html.parser")
    a = soup.find("p", "text-justify")
    result = []
    for i in a.find_all("a"):
        result.append(i.get_text())
    a = soup.find("h4", "link_cinza").get_text()
    result = {"title": a, "relacionadas": result}
    return dict(results=result)


def rimas(query):
    r = http.get(link + "rimas/" + query)
    soup = BeautifulSoup(r.text, "html.parser")
    a = soup.find_all("a")
    b = []
    for i in a:
        try:
            if "Significado de" in i.get("alt"):
                b.append(i.get_text())
        except:
            pass
    result = {"title": soup.find("title").get_text(), "rimas": b[4:]}
    return dict(results=result)
