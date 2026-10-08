import re

def extract_contacts(text):
    emails=re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',text)
    phones=re.findall(r'(?<!\d)(?:\+91\s?)?[6-9]\d{9}(?!\d)',text)
    return {"emails":emails,"phones":phones}
text="Contact support at ravi.kumar@techcorp.in or admin@sales.co. Direct helpline: +91 9876543210 or call 8765432109."
print(extract_contacts(text))