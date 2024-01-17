import re

def solution(new_id):
    new_id = new_id.lower()
    print(new_id)
    new_id = re.sub(r'[^a-z0-9_.\-]', '', new_id)
    print(new_id)
    new_id = re.sub(r'\.+', '.', new_id)
    print(new_id)
    new_id = re.sub(r'^\.|\.$', '', new_id)
    print(new_id)
    if len(new_id) == 0:
        new_id += "a"
    if len(new_id) >= 16:
        new_id = re.sub(r'\.$', '', new_id[:15])
    if len(new_id) <= 2:
        new_id = new_id.ljust(3, new_id[-1])
        
    return new_id