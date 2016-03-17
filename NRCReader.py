__author__ = 'mhbashari'


class NRCReader:
    def __init__(self, NRCAddress="NRC-emotion-lexicon-wordlevel-alphabetized-v0.92.txt"):
        self.nrc_address = NRCAddress
        self.data = {}

    def load(self):
        with open(self.nrc_address, "r", encoding="utf-8") as nrc_file:
            for line in nrc_file.readlines():
                splited = line.replace("\n", "").split("\t")
                word, emotion, value = splited[0], splited[1], splited[2]
                if word in self.data.keys():
                    self.data[word].append((emotion, int(value)))
                else:
                    self.data[word] = [(emotion, int(value))]

    def vectorize(self, sentence:list):
        out = {}
        for word in sentence:
            if word in self.data.keys():
                for item in self.data[word]:
                    if word in out.keys():
                        out[word] += (item[0], item[1])
                    else:
                        out[word] = (item[0], item[1])
        return out

    def get_emotion(self, word, emotion):
        emotions = self.data[word]
        for emot in emotions:
            if emot[0] == emotion:
                return emot[1]
