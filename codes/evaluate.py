import Levenshtein
import json


def word_distance(s, t):
    s = s.lower().strip()
    t = t.lower().strip()
    d = Levenshtein.distance(s, t)
    return d


def word_equal(s, t):
    return word_distance(s, t) <= 1


def word_list_extract(s):
    s = s.replace(",", " ").replace('"',' ').replace("'", " ")
    s = s.strip().split(" ")
    result = []
    for word in s:
        if word in ['of', 'the', 'a', 'on', 'in']:
            continue
        result.append(word)
    return result


def Jaccard_phrase_distance(s, t):
    s = word_list_extract(s)
    t = word_list_extract(t)

    total_num = len(s) + len(t)
    match_num = 0
    for word_s in s:
        for word_t in t:
            if word_equal(word_s, word_t):
                t.remove(word_t)
                match_num += 1
                break

    return 1 - match_num / (total_num - match_num)


def evaluate_top_k_result(user_result, ground_truth, threshold=0.2):
    s = user_result
    t = ground_truth
    lens = len(s)
    lent = len(t)
    total_num = lens + lent
    match_num = 0
    for name_s in s:
        for name_t in t:
            if Jaccard_phrase_distance(name_s, name_t) <= threshold:
                t.remove(name_t)
                match_num += 1
                break

    recall = match_num / lent
    precision = match_num / lens
    return recall, precision


def evaluate(predicted_result_file, ground_truth_file="ground_truth.json"):
    with open(predicted_result_file) as f:
        predicted_result = json.load(f)
    with open(ground_truth_file) as f:
        ground_truth = json.load(f)

    r, p = 0, 0
    for idx in ground_truth["affliation"]:
        try:
            recall, precision = evaluate_top_k_result(ground_truth["affliation"][idx], predicted_result["affliation"][idx])
            r += recall
            p += precision
            print(idx, recall, precision)
        except Exception as ee:
            print(ee)
    print(r / len(ground_truth["affliation"]), p / len(ground_truth["affliation"]))

if __name__ == "__main__":
    evaluate("/root/dataset/shi_test/extract_university.json")