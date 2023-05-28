from flask import Flask, render_template, jsonify, request

from gpt_index import SimpleDirectoryReader,GPTSimpleVectorIndex,LLMPredictor,PromptHelper
from langchain import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the environment variable

app = Flask(__name__)

# Environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = openai_api_key

def create_index(path):
    max_input = 4096
    tokens = 200
    chunk_size = 6000
    max_chunk_overlap = 20

    promptHelper = PromptHelper(max_input,tokens,max_chunk_overlap,chunk_size_limit=chunk_size)
    llmPredictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-ada-001",max_tokens=tokens))
    docs = SimpleDirectoryReader(path).load_data()
    vectorIndex = GPTSimpleVectorIndex(documents=docs,llm_predictor=llmPredictor,prompt_helper=promptHelper)

    vectorIndex.save_to_disk(r"vectorIndex.json")
    return vectorIndex

# Initialize the index
vector_index = create_index("output")

# History for the chatbot
history = []

def chatbot(query):
    base_prompt = "You're an Customer Service executive of Rauva, Your name is Houston if the user query comes in any language you need to respond in the same language as user, please respond here is the user query = "
    history.append(base_prompt + query)
    full_conversation = ' '.join(history)

    vIndex = GPTSimpleVectorIndex.load_from_disk("vectorIndex.json")
    response = vIndex.query(full_conversation, response_mode="compact")
    history.append(response.response)

    return response.response

@app.route("/")
def index_get():
    return render_template("base.html", script_root=request.script_root)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    message = data['message']

    if message.strip() != "":
        response = chatbot(f"User: {message}")

        if response:
            return jsonify({'answer': response})
        else:
            return jsonify({'answer': "Sorry, an error occurred. Please try again."})
    else:
        return jsonify({'answer': "Please enter a valid message."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
