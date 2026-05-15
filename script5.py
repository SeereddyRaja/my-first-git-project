import re
text = '''
ip address is 192.168.1.1, MAC Address is AA:BB:CC:DD:11:22, input counters are 1000 pkts/sec, output counters are 900 packets/sec
'''
ipadd_match = re.findall(r'\b(?:\d{1,3}\.\d{1,3}\.\d{1,3}\.)\d{1,3}\b', text)
print(ipadd_match)
macadd_match=re.findall(r'\b(?:[0-9a-fA-F]{2}[:]){5}[0-9a-fA-F]{2}\b', text)
print(macadd_match)
counters_match = re.findall(r'\b(?:\d+\s+\w+\/+\w+)\b', text)
print(counters_match)

username = "Raja"
age = 25
print(f"Hello, {username}")
print('"Hello"')
print("\"Hello\"")
pi = 3.14159
print(f"The value of pi is {pi:.2f}")
print("username:\tRaja")