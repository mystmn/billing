from collections import defaultdict

class custom(object):

    def forEach(self,x="" ,y=""):
        for x in y.keys():
            print "the key name is '%s' and its value is %s" % (x, y[x])

    def combineList(self, a, b):
        #listA = ["id", "name", "city", "state"]
        #listB = ["1", "Paul", "Columbus", "ohio", "43232"]

        if not len(a) == len(b):
                print "List don't match"

        d = defaultdict(list)
        for x, y in zip(a, b):
            d[x].append(y)
        d = dict(d)

        return d