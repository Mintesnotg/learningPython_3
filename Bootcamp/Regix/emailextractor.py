import re

text="Contact us at support@example.com or sales@company.org for more details"

ptrn=r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

emails=re.findall(ptrn,text)

print(emails)

