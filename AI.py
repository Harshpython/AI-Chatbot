 
# to install openai run command pip install openai

import openai
openai.api_key="" #Enter your api key 

def chat_with_gpt(prompt):
    # IN this the chat completion is for python older version 
    # you can use according to yours
    response=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",# using  model of gpt turbo
        messages=[{"role":"user","content": prompt}]# the messages will be dispalyed
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":# writing the main function
    while True:
        user_input=input("ME:")
        if user_input.lower() in ["quit","exit","bye"]:
            break

        response=chat_with_gpt(user_input)# response generated

        print("Harsh Chatbot: ", response)
