from unsloth import FastLanguageModel
from transformers import AutoTokenizer
import re
import torch
from utils import find_most_relevant_context

model_name = "unsloth/Llama-3.2-3B-Instruct"
model = FastLanguageModel.from_pretrained(model_name, load_in_4bit=True)
FastLanguageModel.for_inference(model)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def get_assistant_response(user_message):
    context_list = ["Project presentation 2-5 pm", "Movie 6-8 pm"]
    context = find_most_relevant_context(user_message, context_list)
    messages = [
        {"role": "system", "content": "Provide a reply based on the context."},
        {"role": "user", "content": f"{user_message} context: {context}"}
    ]
    inputs = tokenizer.apply_chat_template(messages, tokenize=True, return_tensors="pt").to("cuda")
    outputs = model.generate(input_ids=inputs, max_new_tokens=64, temperature=0.5)
    text = tokenizer.batch_decode(outputs)[0]
    match = re.search(r"<\|start_header_id\|>assistant<\|end_header_id\|>\n\n(.*?)<\|eot_id\|>", text)
    return match.group(1) if match else "No response."
