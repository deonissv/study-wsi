import csv
from math import log
from random import shuffle

class DescisionTreeNode:
    def __init__(self, atr_num, children):
        self.atr_num = atr_num
        self.children = children


    def classify(self, atributes):
        split_val = atributes[self.atr_num]
        child = self.children.get(split_val)
        if child is None:
            cls_vals = list(self.children.keys())
            most_common_cls_val = max(set(cls_vals), key=cls_vals.count)
            child = self.children.get(most_common_cls_val)
        return child.classify(atributes)



class DescisionTreeLeaf:
    def __init__(self, cls_val):
        self.cls = cls_val


    def classify(self, atributes):
        return self.cls


class TplPair:
    def __init__(self, tpl):
        self.cls = tpl[0]
        self.atributes = tpl[1:]
        self.atr_number = len(tpl) - 1


def read_data( path):
    with open(path) as csvfile:
        reader = csv.reader(csvfile)
        return [TplPair(tpl) for tpl in reader]


def split(dataset, atr_num):
    res = {}
    for pair in dataset:
        atr_val = pair.atributes[atr_num]
        res.setdefault(atr_val, []).append(pair)
    return res


def get_cls_freq(dataset):
    classes = {}
    for pair in dataset:
        if classes.get(pair.cls):
            classes[pair.cls] += 1
        else:
            classes[pair.cls] = 1
    return classes


def entropy(dataset):
    entropy = 0
    dataset_len = len(dataset)
    classes = get_cls_freq(dataset)
    for inst in classes.values():
        freq = inst / dataset_len
        entropy -= freq * log(freq)
    return entropy


def info(dataset, atr_num):
    subsets = split(dataset, atr_num)
    dataset_len = len(dataset)
    return sum([len(subset) / dataset_len * entropy(subset) for subset in subsets.values()])


def info_gain(dataset, atr_num):
    return entropy(dataset) - info(dataset, atr_num)


def id3(dataset, atributes):
    if all([dataset[0].cls != pair.cls for pair in dataset]):
        return DescisionTreeLeaf(dataset[0].cls)
    if len(atributes) == 0:
        max_freq_cls = max(get_cls_freq(dataset))
        return DescisionTreeLeaf(max_freq_cls)
    best_atr = max(atributes, key=lambda atr: info_gain(dataset, atr))
    subsets = split(dataset, best_atr)
    atributes.remove(best_atr)
    children = {atr: id3(subset, atributes.copy()) for atr, subset in subsets.items()}
    return DescisionTreeNode(best_atr, children)


def get_tree(dataset):
    atributes = list(range(dataset[0].atr_number))
    return id3(dataset, atributes)


def get_classes(dataset):
    classes = []
    for pair in dataset:
        if pair.cls not in classes:
            classes.append(pair.cls)
    return classes
