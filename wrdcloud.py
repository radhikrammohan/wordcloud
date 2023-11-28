import warnings

# Suppress NumPy deprecation warning
warnings.filterwarnings("ignore", category=DeprecationWarning, module="numpy")


import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords  # Import NLTK's stopwords

# Load the CSV file into a DataFrame
df = pd.read_csv('D:\Github\wordcloud\scp.csv')  # Replace 'your_file.csv' with the actual file name

# Concatenate all text data from the 'column_name' column (replace with your actual column name)
text = ' '.join(df['Title'].astype(str))

# Define a list of words to be removed
#custom_stopwords = ["physics informed", "machine learning", "data driven","physics","informed"]  # Add the words you want to remove

# Optionally, remove common English stopwords using NLTK
# stop_words = set(stopwords.words("english"))
# text_tokens = text.split()
# filtered_text = [word for word in text_tokens if word.lower() not in stop_words]
# text = ' '.join(filtered_text)

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Display the generated word cloud using Matplotlib
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
