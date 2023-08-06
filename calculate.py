from data import emotion_score
import json

def calculate_confidence_scores(stress_levels, sadness_levels):
    mental_problems = []
    if 6<mean_last_quartile(sadness_levels)<10:
        mental_problems.append("Major Depressive Disorder (MDD)")
    if 6<mean_last_quartile(stress_levels)<10:
        mental_problems.append("Generalized Anxiety Disorder (GAD)")
    if abs(mean_quartile_before_last(sadness_levels) - mean_last_quartile(sadness_levels))>4:
        mental_problems.append("Bipolar Disorder")
    if mean_quartile_before_last(sadness_levels) > mean_last_quartile(sadness_levels) and abs(mean_quartile_before_last(sadness_levels) - mean_last_quartile(sadness_levels))>4:
        mental_problems.append("Adjustment Disorder")
    if len (mental_problems) == 0:
        return "A Good Mental Health!"
    elif len (mental_problems) >= 1:
        list_string = ""
        for i, sentence in enumerate(mental_problems, 1):
            list_string += f"{i}. {sentence}\n"
        return list_string

def mean_last_quartile(lst):
    quartile_start_index = int(0.75 * len(lst))  # Calculate the index where last quartile starts
    last_quartile = lst[quartile_start_index:]  # Slice the list from that index to the end
    mean_last_quartile = sum(last_quartile) / len(last_quartile)  # Calculate the mean of last quartile
    print(mean_last_quartile)
    return mean_last_quartile


def mean_quartile_before_last(lst):
    quartile_start_index = int(0.75 * len(lst))  # Calculate the index where last quartile starts
    quartile_before_start_index = int(0.5 * len(lst))  # Calculate the index where quartile before last quartile starts
    quartile_before_last = lst[
                           quartile_before_start_index:quartile_start_index]  # Slice the list between the two indices

    if len(quartile_before_last) == 0:
        return 0  # Return 0 or any default value if the list is empty to avoid division by zero

    mean_quartile_before_last = sum(quartile_before_last) / len(
        quartile_before_last)  # Calculate the mean of quartile before last quartile
    return mean_quartile_before_last


def stress_lvl():
    stress_list = []
    data_dict = json.loads(open('data/record.json').read())
    for date, entry in data_dict.items():
        emotion = entry.get('emotion')
        if emotion:
            stress_list.append(emotion_score.stressful_emotions.get(emotion))
        else:
            print(f"No emotion data found for date: {date}")
    return stress_list

def depress_lvl():
    depress_list = []
    data_dict = json.loads(open('data/record.json').read())
    for date, entry in data_dict.items():
        emotion = entry.get('emotion')
        if emotion:
            depress_list.append(emotion_score.depressing_emotions.get(emotion))
        else:
            print(f"No emotion data found for date: {date}")
    return depress_list

def is_stressed():
    stress_list = stress_lvl()
    if mean_last_quartile(stress_list) > 5:
        return True
    else:
        return False

def is_depressed():
    depress_list = depress_lvl()
    if mean_last_quartile(depress_list) > 5:
        return True
    else:
        return False

def get_mental_health():
    return calculate_confidence_scores(stress_lvl(), depress_lvl())