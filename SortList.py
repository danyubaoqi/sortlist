class SortList:
    def __init__(self, ls: list):
        self.data = ls
        self.result = []
        self.dic = {}

    def listToDict(self):
        dic = {}
        for i in self.data:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        self.dic = dic
        return dic

    def sortList(self):
        result = []
        if self.dic != {}:
            dic = self.dic
            for i in dic:
                result.append([i, dic[i]])
        else:
            dic = {}
            for i in self.data:
                if i not in dic:
                    dic[i] = 1
                else:
                    dic[i] += 1
            self.dic = dic
            for i in dic:
                result.append([i, dic[i]])
        sorted(result, key=lambda x: x[1], reverse=True)
        self.result = result
        return result
