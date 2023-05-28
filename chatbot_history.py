######### CHATBOT INTERACTIVE FLOW ######################

import openai
import csv
import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')  # Retrieve the API key from environment variables

# Set up OpenAI API key
openai.api_key = openai_api_key

def load_csv_data(file_path):
    data = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            question = row[0].strip()
            answer = row[1].strip()
            data[question] = answer
    return data

def get_answer(question, context, csv_data):
    if question in csv_data:
        return csv_data[question]
    else:
        prompt = f"{context}\nUser: {question}\nAI:"
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens=500,  # Adjust max_tokens as needed
            n=1,
            stop=None,
            temperature=0.7
        )
        answer = response.choices[0].text.strip()
        return answer

# csv_file_path = "chatbot_data_program_details.csv"  # Replace with the path to your CSV file
# csv_data = load_csv_data(csv_file_path)

# context = "I want you to act as a education counsellor that I am having a conversation with. Your name is 'Houston'. You will provide me with answers from the given info and suggest some institutes from the csv if the question is relevant to institutes.  Refuse to answer any question not about the info. Never break character."
# while True:
#     question = input('User: ')
#     answer = get_answer(question, context, csv_data)
#     context += f"\nUser: {question}\nAI: {answer}"
#     print(f"AI: {answer}")


########## CHATBOT cONSIDERING SUGGESTIONS FROM DATASET ######################

# import openai
# import csv
# import os
# from dotenv import load_dotenv

# load_dotenv()
# openai_api_key = os.getenv('OPENAI_API_KEY')  # Retrieve the API key from environment variables

# # Set up OpenAI API key
# openai.api_key = openai_api_key

# def load_csv_data(file_path):
#     data = {}
#     with open(file_path, 'r', encoding='utf-8') as file:
#         csv_reader = csv.reader(file)
#         for row in csv_reader:
#             question = row[0].strip()
#             answer = row[1].strip()
#             data[question] = answer
#     return data

# def truncate_context(context, max_tokens):
#     tokens = context.split()
#     if len(tokens) <= max_tokens:
#         return context
#     else:
#         return ' '.join(tokens[-max_tokens:])

# def is_greeting(input_text):
#     greetings = ['hi', 'hello', 'hey']
#     return input_text.lower() in greetings

# def get_answer(question, context, csv_data):
#     if question in csv_data:
#         return csv_data[question]
#     else:
#         prompt = f"{context}\nUser: {question}\nAI:"
#         max_context_tokens = 4096  # Maximum context tokens allowed by the model
#         prompt = truncate_context(prompt, max_context_tokens)
#         response = openai.Completion.create(
#             engine='text-davinci-003',
#             prompt=prompt,
#             max_tokens=500,  # Adjust max_tokens as needed
#             n=1,
#             stop=None,
#             temperature=0.7
#         )
#         ai_answer = response.choices[0].text.strip()
#         if is_greeting(question):
#             return ai_answer
#         else:
#             suggestions = [answer for q, answer in csv_data.items() if question.lower() in q.lower()]
#             answer = f"{ai_answer}\n\nSuggested institutes: {', '.join(suggestions)}" if suggestions else ai_answer
#             return answer

# csv_file_path = "chatbot_data_program_details.csv"  # Replace with the path to your CSV file
# csv_data = load_csv_data(csv_file_path)

# context = ""
# while True:
#     question = input('User: ')
#     answer = get_answer(question, context, csv_data)
#     context += f"\nUser: {question}\nAI: {answer}"
#     print(f"AI: {answer}")

#################################################################################################################

# import openai
# import csv
# import os
# from dotenv import load_dotenv

# load_dotenv()
# openai_api_key = os.getenv('OPENAI_API_KEY')  # Retrieve the API key from environment variables

# # Set up OpenAI API key
# openai.api_key = openai_api_key

# def load_csv_data(file_path):
#     data = {}
#     with open(file_path, 'r', encoding='utf-8') as file:
#         csv_reader = csv.reader(file)
#         for row in csv_reader:
#             question = row[0].strip()
#             answer = row[1].strip()
#             data[question] = answer
#     return data

# def truncate_context(context, max_tokens):
#     tokens = context.split()
#     if len(tokens) <= max_tokens:
#         return context
#     else:
#         return ' '.join(tokens[-max_tokens:])

# def is_greeting(input_text):
#     greetings = ['hi', 'hello', 'hey']
#     return input_text.lower() in greetings

# def get_answer(question, context, csv_data):
#     if question in csv_data:
#         return csv_data[question]
#     else:
#         prompt = f"{context}\nUser: {question}\nAI:"
#         max_context_tokens = 4096  # Maximum context tokens allowed by the model
#         prompt = truncate_context(prompt, max_context_tokens)
#         response = openai.Completion.create(
#             engine='text-davinci-003',
#             prompt=prompt,
#             max_tokens=500,  # Adjust max_tokens as needed
#             n=1,
#             stop=None,
#             temperature=0.7
#         )
#         ai_answer = response.choices[0].text.strip()
#         if is_greeting(question):
#             return ai_answer
#         else:
#             suggestions = [inst for inst in csv_data.keys() if question.lower() in inst.lower()]
#             answer = f"{ai_answer}\n\nSuggested institutes: {', '.join(suggestions)}" if suggestions else ai_answer
#             return answer

# csv_file_path = "chatbot_data_program_details.csv"  # Replace with the path to your CSV file
# csv_data = load_csv_data(csv_file_path)

# context = ""
# while True:
#     question = input('User: ')
#     answer = get_answer(question, context, csv_data)
#     context += f"\nUser: {question}\nAI: {answer}"
#     print(f"AI: {answer}")
