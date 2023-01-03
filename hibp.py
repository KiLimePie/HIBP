import time
import requests


with open("email.txt") as f:
    hg=f.readlines()
    hg=[x.strip() for x in hg]

head={"hibp-api-key":"(YOUR API KEY HERE)"}

result=[]

for i in hg:
    url=f"https://haveibeenpwned.com/api/v3/breachedaccount/{i}?truncateResponse=false"
    
    time.sleep(6)
    
    res=requests.get(url,headers=head)

    if res.status_code==200:
        result.append((i,res.json()))

with open("hibp.csv", "a+") as f:
    f.write("E-mail,Breach Count,Breaches w/ Passwords Compromised\n")

for i,res in result:
    name=[]
    data=[]

    for breach in res:
        name.append(breach["Name"])

        if "Passwords" in breach["DataClasses"]:
            data.append(breach["Name"] + " (" + breach["BreachDate"] + ")")

    if not data:
        data.append("None")

    count=len(name)
    dataline= str(data).replace(",", " |")

    with open("hibp.csv", "a+") as f:
        f.write(f"""{i},{count},{dataline}
""")