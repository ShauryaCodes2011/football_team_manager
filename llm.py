from ollama import chat
from ollama import ChatResponse

def invoke(prompt):
    response = chat(model='gpt-oss:120b-cloud', messages=[
    {
        'role': 'user',
        'content': prompt,
    },
    ])
    # or access fields directly from the response object
    return response.message.content
    
if __name__=="__main__":
    print("this name is wirrten in llm.py file",__name__)
    print(invoke("this is test prompt"))