import matplotlib.pyplot as plt
import json
from data import emotion_score

stress_list = []
depression_list = []

def get_stress_data():
    # Load the JSON data into a Python dictionary
    data_dict = json.loads(open('data/record.json').read())

    # Iterate through each day and get the emotion string
    for date, entry in data_dict.items():
        emotion = entry.get('emotion')
        if emotion:
            stress_list.append(emotion_score.stressful_emotions.get(emotion))
        else:
            print(f"No emotion data found for date: {date}")

def stress_graph(y_values, save_path):
    x_values = range(len(y_values))

    plt.plot(x_values, y_values, marker='o', linestyle='-')
    plt.xlabel('Number of Days')
    plt.ylabel('Stress Level (0-10)')
    plt.title('Stress Level Over Time')
    plt.xticks(x_values)  # Adjust the x-axis ticks to match data points

    plt.ylim(0, 10)  # Set the y-axis range from 0 to 10
    plt.grid(True)  # Add grid lines

    plt.savefig(save_path)
    plt.show()

def create_stress_graph():
    save_path = 'imgs/stress_graph.png'
    get_stress_data()
    stress_graph(stress_list, save_path)

def get_depress_data():
    # Load the JSON data into a Python dictionary
    data_dict = json.loads(open('data/record.json').read())

    # Iterate through each day and get the emotion string
    for date, entry in data_dict.items():
        emotion = entry.get('emotion')
        if emotion:
            depression_list.append(emotion_score.depressing_emotions.get(emotion))
        else:
            print(f"No emotion data found for date: {date}")

def depress_graph(y_values, save_path):
    x_values = range(len(y_values))

    plt.plot(x_values, y_values, marker='o', linestyle='-')
    plt.xlabel('Number of Days')
    plt.ylabel('Sadness (0-10)')
    plt.title('Sadness Over Time')
    plt.xticks(x_values)  # Adjust the x-axis ticks to match data points

    plt.ylim(0, 10)  # Set the y-axis range from 0 to 10
    plt.grid(True)  # Add grid lines

    plt.savefig(save_path)
    plt.show()

def create_depress_graph():
    save_path = 'imgs/depress_graph.png'
    get_depress_data()
    depress_graph(depression_list, save_path)
