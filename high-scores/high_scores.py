class HighScores(object):

    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[-1]
    
    def personal_best(self):
        return max(self.scores)

    def personal_top(self):
        self.scores.sort(reverse = True)
        return self.scores[:3]

    def report(self):
        best = self.personal_best()
        latest = self.latest()

        if latest >= best:
            message = "Your latest score was {0}. That's your personal best!".format(latest)
        else:
            mod_best = best - latest
            message = "Your latest score was {0}. That's {1} short of your personal best!".format(latest, mod_best)

        return message