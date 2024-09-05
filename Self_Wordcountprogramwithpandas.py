# Word count program with pandas
import pandas as pd
import re

text_df = pd.read_csv('wordcount.txt', header=None, sep='\t', \
                      names=['lines'])

# Make all lines as lower case, split the lines, explode it to words, count the words and sort it
text_df['lines'] = text_df['lines'].apply(lambda x:re.sub(r'[^A-Za-z0-9\s]', '', str(x)))
text_df['lines'] = text_df['lines'].str.lower()

text_df['words'] = text_df['lines'].str.split(' ')
text_df.pop('lines')
text_df = text_df.explode('words')
text_group = text_df.value_counts().reset_index().sort_values(by='count', ascending=False)
# text_group.to_csv('result.csv', header=['words', 'count'], index_label='word')

filtered = text_group.head(5)
print(filtered)