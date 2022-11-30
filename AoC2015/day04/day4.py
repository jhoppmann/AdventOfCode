import hashlib
import itertools

key = 'iwrupvqb'

for i in itertools.count(start=1):
    value = key + str(i)
    m = hashlib.md5()
    m.update(value.encode("utf-8"))
    hashedValue = m.hexdigest()
    if hashedValue[0:6:] == '000000':
        print(hashedValue)
        print(i)
        break
