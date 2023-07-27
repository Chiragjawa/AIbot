import openai

openai.api_key = "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"

messages=[]
system_message = input("What type of chatbox do you want?\n")
messages.append({"role":"user" , "content": system_message})

print("New assistant is ready!")
while input!= "quit()":
    message = input("")
    messages.append({"role": "user","content": message})   
    response= openai.ChatCompletion.create(
       model="gpt-3.5-turbo",
       messages=messages
    )
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role":"assistant","content":reply})
    print("\n"+reply+"\n")
