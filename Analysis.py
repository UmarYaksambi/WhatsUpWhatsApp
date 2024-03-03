# Program to Analyse and Visualize WhatsApp Group Chats 💬

import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import emojis

with open(r"C:\Users\umary\OneDrive\Desktop\WhatsApp Chat with FRIENDS FOREVER ❤️.txt", 'r', encoding= 'utf-8') as file:
    chats = file.read()         # Option to input chat file

# Cleaning Data 🧹
chats = chats.replace("\u202f", " ")
chats = chats.replace("<Media>", "<Media omitted>")

pattern = re.compile(r"(\d{2}/\d{2}/\d{4}), (\d{1,2}:\d{2}.[ap]m) - (.+?): (.+)")

matches = pattern.findall(chats)
df = pd.DataFrame(matches, columns=['Date', 'Time', 'Sender', 'Message'])

df = df[df['Message'] != 'This message was deleted']

df['Just Message'] = df['Message'].apply(emojis.decode)
df['Message in Words'] = df['Just Message'].str.split()
df['Word Count'] = df['Message in Words'].apply(len)

df['Just Emojis'] = df['Message'].apply(emojis.get)

df['Emoji Count'] = df['Message'].apply(emojis.count)

# TOTAL WORD COUNT BY SENDER PLOT
values = df.groupby('Sender')['Word Count'].sum()
values = values.sort_values(ascending=False)

plt.bar(values.index, values)

plt.xlabel('Sender')
plt.ylabel('Total Word Count')
plt.title('Total Word Count by Sender')

plt.xticks(rotation='vertical')

plt.tight_layout()
plt.show()


