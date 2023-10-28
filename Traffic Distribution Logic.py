import time as t
print("Logic")
tdn = int(input('tdn:'))
tds = int(input('tds:'))
wtn = wts = rtn = rts = 30
if tdn >= 80:
    if tds <= 20:
        wts += 15
        wtn -= 15
        rtn += 15
        rts -= 15
    elif tds <= 50:
        wts += 8
        wtn -= 8
        rtn += 8
        rts -= 8
    elif tds < 80:
        wts += 3
        wtn -= 3
        rtn += 3
        rts -= 3
    elif tds >= 80:
        wts = wtn = rtn = rts = 30
elif tdn >= 60:
    if tds <= 20:
        wts += 10
        wtn -= 10
        rtn += 10
        rts -= 10
    elif tds <= 50:
        wts += 5
        wtn -= 5
        rtn += 5
        rts -= 5
    elif 50 <= tds < 80:
        wts = wtn = rtn = rts = 30
    elif tds >= 80:
        wtn += 5
        wts -= 5
        rts += 5
        rtn -= 5
elif tdn >= 40:
    if tds <= 20:
        wts += 7
        wtn -= 7
        rtn += 7
        rts -= 7
    elif tds <= 50:
        wts = wtn = rtn = rts = 30
    elif 50 <= tds < 80:
        wtn += 5
        wts -= 5
        rts += 5
        rtn -= 5
    elif tds >= 80:
        wtn += 10
        wts -= 10
        rts += 10
        rtn -= 10
elif tdn >= 20:
    if tds >= 80:
        wtn += 12
        wts -= 12
        rts += 12
        rtn -= 12
    elif tds >= 50:
        wtn += 8
        wts -= 8
        rts += 8
        rtn -= 8
    elif tds >= 20:
        wts = wtn = rtn = rts = 30
    elif tds < 20:
        wts += 3
        wtn -= 3
        rtn += 3
        rts -= 3
elif tdn < 20:
    if tds >= 80:
        wtn += 15
        wts -= 15
        rts += 15
        rtn -= 15
    elif tds >= 50:
        wtn += 10
        wts -= 10
        rts += 10
        rtn -= 10
    elif tds >= 20:
        wtn += 3
        wts -= 3
        rts += 3
        rtn -= 3
    elif tds < 20:
        wts = wtn = rtn = rts = 30

print('Traffic North:', tdn)
print('Traffic South:', tds)
print('Stop Time North:', wtn)
print('Stop Time South:', wts)
print('Go Time North:', rtn)
print('Go Time South:', rts)

