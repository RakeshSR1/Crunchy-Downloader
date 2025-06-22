import os

langs = ["hiIN", "taIN", "teIN"]
res = os.getenv("RES", "1080p")
crunchy_domain = os.getenv("CRUNCHY_DOMAIN", "beta.crunchyroll.com")

for lang in langs:
    print(f"Starting download for {lang}")
    os.system(f"python3 main.py --dub --sub-lang {lang} --res {res} --domain {crunchy_domain}")
