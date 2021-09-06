import randfacts


def getFacts():
    fact_list = []
    for i in range(0,40):
        x = randfacts.getFact()
        fact_list.append(x)
    return fact_list