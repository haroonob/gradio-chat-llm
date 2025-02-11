import openai

from audio import text_to_speech
from config import MODEL, SYSTEM_MESSAGE, tools
from image_generator import generate_vacation_image
from tools import handle_tool_call


def chat(history):
    messages = [{"role": "system", "content": SYSTEM_MESSAGE}] + history
    response = openai.chat.completions.create(model=MODEL, messages=messages, tools=tools)
    image = None
    if response.choices[0].finish_reason == "tool_calls":
        message = response.choices[0].message
        response, city = handle_tool_call(message)
        messages.append(message)
        messages.append(response)
        image = generate_vacation_image(city)
        response = openai.chat.completions.create(model=MODEL, messages=messages)
    reply = response.choices[0].message.content
    history += [{"role": "assistant", "content": reply}]

    return history, image,text_to_speech(reply)