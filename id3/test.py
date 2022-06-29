from id3 import *


def test(dataset):
    run_num = 1
    precisions = []
    classes = get_classes(dataset)
    conf_matrix = {cls_val: {cls_value: 0 for cls_value in classes} for cls_val in classes}
    for i in range(run_num):
        shuffle(dataset)
        split_point = 3 * len(dataset) // 5
        train_set = dataset[:split_point]
        test_set = dataset[split_point:]

        descision_tree = get_tree(train_set)
        correct = 0
        for tmp_pair in test_set:
            prediction = descision_tree.classify(tmp_pair.atributes)
            conf_matrix[tmp_pair.cls][prediction] += 1
            if tmp_pair.cls == prediction:
                correct += 1
        precisions.append(correct / len(test_set))
    precision = sum(precisions) / len(precisions)
    for k in conf_matrix:
        for key in conf_matrix[k]:
            conf_matrix[k][key] = conf_matrix[k][key] / run_num
    return precision, conf_matrix

def print_talbe(conf_matrix):
    print('-'*77)
    legend = 'expected \\ prediction'
    print(f'|{legend:^24}|' + ''.join([f"{val:^24}| " for val in conf_matrix.keys()]))
    print('-'*77)
    for vals in conf_matrix:
        print(f'|{vals:^24}|' + ''.join([f"{val:^24}| " for val in conf_matrix[vals].values()]))
        print('-'*77)


def main():
    data = read_data("agaricus-lepiota.data")
    precision, conf_matrix = test(data)
    print(f"mushroom | precision: {round(precision, 3)}")
    print_talbe(conf_matrix)
    print('')

    data = read_data("breast-cancer.data")
    precision, conf_matrix = test(data)
    print(f"breast-cancer | precision: {round(precision, 3)}")
    print_talbe(conf_matrix)



if __name__ == "__main__":
    main()



# results for 20 runs

# mushroom | precision: 1.0
# -----------------------------------------------------------------------------
# | expected \ prediction  |           p            |            e            |
# -----------------------------------------------------------------------------
# |           p            |         1563.4         |           0.0           |
# -----------------------------------------------------------------------------
# |           e            |          0.0           |          1686.6         |
# -----------------------------------------------------------------------------

# breast-cancer | precision: 0.646
# -----------------------------------------------------------------------------
# | expected \ prediction  |  no-recurrence-events  |    recurrence-events    |
# -----------------------------------------------------------------------------
# |  no-recurrence-events  |         61.65          |          18.95          |
# -----------------------------------------------------------------------------
# |   recurrence-events    |         21.75          |          12.65          |
# -----------------------------------------------------------------------------

#     -- drzewa są zbytnio rozbudowane, i nadmiernie dopasowane do zbioru uczacego, ale mimo tego szybkość zgadywania jest dość wysoka
#     -- brak wsparcia atrybutów ciągłych
#     -- źle działa dla zestawów o małej liczbie atrybutów
#     -- wyniki dość mocno zależą od jakości danych(dataset`u)
#     -- problem diagnostyki raku jest zdecydowanie bardziej złożony, więc skuteczność jest niższa