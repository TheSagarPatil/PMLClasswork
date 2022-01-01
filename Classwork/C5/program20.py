import re as RE

POINTS = {
    '1':25,
    '2':18,
    '3':15,
    '4':12,
    '5':10,
    '6':8,
    '7':6,
    '8':4,
    '9':2,
    '10':1,
    None:'ERROR'
}
print(POINTS[str('1')])
txt = "1FP"
pos = RE.split("\D", txt)[0]
fastestLap = "F" in txt
pole = "P" in txt
print(pos, POINTS[pos], fastestLap, pole)
print(len(POINTS))