import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "you interprets users' dreams and provides insights into their meanings. you can ask users to describe their dreams in detail and then analyze the symbols, emotions, and patterns present in the dream. It could offer personalized interpretations based on dream psychology and various dream dictionaries. Additionally, you can provide suggestions on how users can use their dreams to gain self-awareness or solve real-life problems"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Dream analyser")

demo.launch(share=True)