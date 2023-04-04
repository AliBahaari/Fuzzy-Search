from fuzzysearch import find_near_matches
from timeit import timeit


user_query = "من یک گوشی سامسونک می خواهم که قرمزرنگ و خوشگل باشد"

colors_spec = ["سفید", "آبی", "قرمز"]
brands_spec = ["شیائومی", "سامسونگ", "لنوو"]
all_specs = colors_spec + brands_spec

colors_dict = dict.fromkeys(colors_spec, "رنگ")
brands_dict = dict.fromkeys(brands_spec, "برند")
all_specs_dicts = colors_dict | brands_dict


def testSimilarity():
    for i in all_specs:
        found_text = find_near_matches(i, user_query, max_l_dist=1)
        if len(found_text) > 0:
            print(found_text[0].matched + ' - ' +
                  i + ' - ' + all_specs_dicts[i])


def testExact():
    allData = []

    for i in colors_spec:
        if i in user_query:
            allData.append(all_specs_dicts[i])

    for j in brands_spec:
        if j in user_query:
            allData.append(all_specs_dicts[j])

    print(allData)


def testAllExact():
    allData = []

    for i, j in zip(colors_spec, brands_spec):
        if i in user_query:
            allData.append(all_specs_dicts[i])

        if j in user_query:
            allData.append(all_specs_dicts[i])

    print(allData)

# Tests

# print(timeit(testSimilarity, number=100))
# print(timeit(testExact, number=10000))
# print(timeit(testAllExact, number=10000))
