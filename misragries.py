from collections import Counter


class MisraGries(object):

    def __init__(self, k):
        self.k = k
        self.a = Counter()

    def process(self, stream):
        for j in stream:
            if j in self.a:
                self.a.update([j])
            elif len(self.a) < self.k - 1:
                self.a[j] = 1
            else:
                for l in self.a.keys():
                    self.a[l] -= 1
                    if self.a[l] == 0:
                        del self.a[l]

    def estimate(self, q):
        return self.a[q] if q in self.a else 0


class MisraGriesForHeavyHitters(MisraGries):

    def process(self, stream):
        super(MisraGriesForHeavyHitters, self).process(stream)
        self.a.subtract(self.a)  # reset counters keeping keys
        for j in stream:
            if j in self.a.keys():
                self.a.update([j])

    def estimate(self):
        return self.a
