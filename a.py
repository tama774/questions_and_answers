import argparse
from random import shuffle
import pandas as pd

parser = argparse.ArgumentParser(description='このプログラムの説明（なくてもよい）')

parser.add_argument('file', help='参照するExcelファイル')
parser.add_argument('-t', '--tag', help='指定するタグ')
parser.add_argument('--list-tags', action='store_true')
parser.add_argument('-c', '--count', type=int)
parser.add_argument('-r', '--random', action='store_true')

args = parser.parse_args()

file_name = args.file
select_tag = args.tag

df = pd.read_excel(file_name)

items = []
all_tags = set()

test_title = file_name
questions = []

for idx, row in df.iterrows():
    question_text = row['questions']
    answer_text = row['answers']
    tags = []
    for tag_idx in range(3):
        if f"tag{tag_idx}" in row:
            tag = f"tag{tag_idx}"
            tags += [row[tag]]
            all_tags.add(row[tag])
    if (not select_tag) or (select_tag in tags):
        questions += [{
            'question': question_text,
            'answer': answer_text
        }]

if args.list_tags:
    for tag in all_tags:
        print(tag)
    exit()

if args.random:
    shuffle(questions)

count=1
print(f"# {file_name}")
for question in questions:
    print(f"{count}: {question['question']}")
    count += 1

print()
count = 1
print(f"# {file_name}")
for question in questions:
    print(f"{count}: {question['answer']}")
    count += 1
