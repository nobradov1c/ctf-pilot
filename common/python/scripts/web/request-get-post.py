import requests
import re
import hashlib

# HTB Emdee five for life

# function to open a session to website http://165.227.231.233:32213/
# get request, and send post request after


def solve():
    s = requests.Session()
    r = s.get("http://165.227.231.233:32213/")
    # print(r.text)

    # regex match between <h3 and </h3> to get the flag
    flag = re.search(r'''<h3 align='center'>(.*?)</h3>''', r.text).group(1)
    print(flag)

    # hash the flag with md5
    hashed_flag = hashlib.md5(flag.encode()).hexdigest()
    print(hashed_flag)

    # send post request with hashed flag in form data
    r = s.post("http://165.227.231.233:32213/", data={"hash": hashed_flag})
    print(r.text)


solve()
# >> HTB{N1c3_ScrIpt1nG_B0i!}
