import os
from openai import OpenAI

# Set the OPENAI_API_KEY environment variable
os.environ["OPENAI_API_KEY"] = "sk-proj-C2uyeEeMdazmkT8RhShGT3BlbkFJ86e1lnCR3yjaMlx1feeh"

# Initialize the OpenAI client
client = OpenAI()

def improve_sentence(sentence):
    """
    Improve a given sentence to make it clearer, more concise, and grammatically correct.
    
    Parameters:
    sentence (str): The sentence to be improved.
    
    Returns:
    str: The improved sentence.
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You will be provided with statements, and your task is to improve the sentence with the following summary of changes."
            },
            {
                "role": "user",
                "content": sentence
            }
        ],
        temperature=0.7,
        max_tokens=64,
        top_p=1
    )
    improved_sentence = response.choices[0].message['content'].strip()
    return improved_sentence
