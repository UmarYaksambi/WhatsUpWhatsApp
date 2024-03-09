import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sb
import emojis
from collections import Counter

def clean_data(chats):
    # Cleaning Data
    chats = chats.replace("\u202f", " ")
    chats = chats.replace("\u200d", " ")
    chats = chats.replace("<Media>", "<Media omitted>")
    
    return chats

def load_chat_data(file_path):
    try:    
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
        
    except FileNotFoundError:
        print("The File does not exist at the location specified.\nPlease check for typos or provide the correct file path.")
        raise SystemExit

def extract_chat_data(chats):
    pattern = re.compile(r"(\d{2}/\d{2}/\d{4}), (\d{1,2}:\d{2}.[ap]m) - (.+?): (.+)")
    matches = pattern.findall(chats)
    df = pd.DataFrame(matches, columns=['Date', 'Time', 'Sender', 'Message'])
    df = df[df['Message'] != 'This message was deleted']
    
    return df

def analyze_and_visualize(df):
    # Adding additional columns
    df['Just Message'] = df['Message'].apply(emojis.decode)
    df['Message in Words'] = df['Just Message'].str.split()
    df['Word Count'] = df['Message in Words'].apply(len)
    df['Just Emojis'] = df['Message'].apply(emojis.get)
    df['Emoji Count'] = df['Message'].apply(emojis.count)

    # Total Word Count by Sender Plot
    values = df.groupby('Sender')['Word Count'].sum().sort_values(ascending=False)
    plot_bar_chart(values, 'Total Word Count by Sender', 'Sender', 'Total Word Count')

    # Total Word Count by Sender Plot (Top 20)
    values20 = values.head(20)
    plot_bar_chart(values20, 'Total Word Count by Sender (Top 20)', 'Sender', 'Total Word Count')

    # Most Emojis Sent (Top 20)
    values = df.groupby('Sender')['Emoji Count'].sum().sort_values(ascending=False)
    values20 = values.head(20)
    plot_bar_chart(values20, 'Total Emoji Count By Sender', 'Sender', 'Emojis Sent')

    # Most Used Emoji (Top 20)
    all_emojis = df['Just Emojis'].explode().dropna()
    emoji_counts = Counter(all_emojis)
    most_used_emoji = emoji_counts.most_common(20)
    print("Most Used Emoji:", most_used_emoji)

def plot_bar_chart(values, title, xlabel, ylabel):
    plt.bar(values.index, values)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(rotation='vertical')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # File path input
    file_path = input("Enter the path to the WhatsApp chat file: ")
    
    # Load and clean data
    chats = load_chat_data(file_path)
    chats = clean_data(chats)
    
    # Extract and analyze data
    df = extract_chat_data(chats)
    analyze_and_visualize(df)
