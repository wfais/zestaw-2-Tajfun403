from typing import Any

def dodaj_element(wejscie):
    # może warto zdefiniować zagnieżdżoną funkcję
    # list, last in this list, nest depth
    nestMap: list[tuple[Any, Any, int]] = []

    def researchNest(lst: Any, level: int):
        try:
            if isinstance(lst, dict):
                last = 0
                lst = lst.values()
                for key, val in enumerate(lst):
                    researchNest(val, level + 1)
                    last = val
                nestMap.append((lst, last, level))
            elif isinstance(lst, (list, tuple)):
                last = 0
                if not len(lst) == 0:
                    for subList in lst:
                        researchNest(subList, level + 1)
                        last = subList
                nestMap.append((lst, last, level))
        except:
            # Not iterable!
            ""
    
    researchNest(wejscie, 1)

    nestMap.sort(key = lambda x: x[2], reverse=True)
    maxLevel = nestMap[0][2]
    # print(nestMap)

    # if only max depth items are tuples, then we need to nuke them as they cannot be appended to
    #
    if all(isinstance(lst, tuple) for lst, last, level in nestMap if level == maxLevel):
        maxLevel -= 1

    print(f"Max depth:", maxLevel)
    for lst, last, level in nestMap:
        if level < maxLevel:
            break
        if isinstance(lst, list):
            lst.append(last + 1)

    return wejscie

if __name__ == '__main__':

    input_list = [
     1, 2, 
     [3, 4, [5, {"klucz": [5, 6], "tekst": [1, 2]}], 5],
     "hello", 
     3, 
     [4, 5], 
     5, 
     (6, (1, [7, 8]))
    ]


    input_list = [[], {"a": ()}, [1, 2, 3, 4]]
    # input_list = [1, 2, [[], {"klucz": [], "tekst": []}], 3]

    output_list = dodaj_element(input_list)
    print(input_list)   