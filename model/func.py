from collections import defaultdict


def forEach(x="", y=""):
    for x in y.keys():
        print "the key name is '%s' and its value is %s" % (x, y[x])


def combineList(a, b):
    if not len(a) == len(b):
        print "List don't match"

    d = defaultdict(list)
    for x, y in zip(a, b):
        d[x].append(y)
        d = dict(d)

    return d


def dictValueExist(urlQuery, dictList):
    default = False

    if isinstance(dictList, dict):
        return next((k for k, v in dictList.items() if v == urlQuery), None)

    else:
        return default

def ExtendList(x=None):
    y = []
    listNumb = len(x)
    for eachC in x:
        y.extend(eachC)

    y.append(listNumb)
    return y
