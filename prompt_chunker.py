import sys
import os
import argparse
from datetime import datetime

def split_prompt(text, split_length):
    if split_length <= 0:
        raise ValueError("Max length must be greater than 0.")

    num_parts = -(-len(text) // split_length)
    file_data = []

    for i in range(num_parts):
        start = i * split_length
        end = min((i + 1) * split_length, len(text))

        if i == num_parts - 1:
            content = f'[START PART {i + 1}/{num_parts}]\n' + text[start:end] + f'\n[END PART {i + 1}/{num_parts}]'
            content += '\nALL PARTS SENT. Now you can continue processing the request.'
        else:
            content = f'Do not answer yet. This is just another part of the text I want to send you. Just receive and acknowledge as "Part {i + 1}/{num_parts} received" and wait for the next part.\n[START PART {i + 1}/{num_parts}]\n' + text[start:end] + f'\n[END PART {i + 1}/{num_parts}]'
            content += f'\nRemember not answering yet. Just acknowledge you received this part with the message "Part {i + 1}/{num_parts} received" and wait for the next part.'

        file_data.append({
            'name': f'{datetime.now().strftime("%Y%m%d%H%M%S")}-chunk-{i + 1}.txt',
            'content': content
        })

    return file_data

def save_chunks(chunks, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for chunk in chunks:
        file_path = os.path.join(output_dir, chunk['name'])
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(chunk['content'])
        print(f"Chunk saved to {file_path}. To copy run the following commap and paste into chatGPT")
        print(f"\033[92m cat {file_path} | pbcopy \033[0m ")

def main():
    parser = argparse.ArgumentParser(description="Process and chunk a prompt.")
    parser.add_argument('split_length', type=int, help='Length of each chunk')
    parser.add_argument('-out', type=str, required=True, help='Output directory for chunk files')

    args = parser.parse_args()

    input_text = sys.stdin.read()

    print("""
Please copy the following initial instruction followed by each of the chunk files.

----------
\033[92m
The total length of the content that I want to send you is too large to send in only one piece.
        
For sending you that content, I will follow this rule:
        
[START PART 1/10]
this is the content of the part 1 out of 10 in total
[END PART 1/10]
        
Then you just answer: "Received part 1/10"
        
And when I tell you "ALL PARTS SENT", then you can continue processing the data and answering my requests.
\033[0m 
----------
""")

    chunks = split_prompt(input_text, args.split_length)
    save_chunks(chunks, args.out)

if __name__ == "__main__":
    main()

