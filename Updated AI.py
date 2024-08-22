# import openai for performing tasks
 
import openai

# Set your OpenAI API key
api_key = ""
openai.api_key = api_key 
 
  
def ask_question(question)
:# writing a fuction about the model based on  the requirements
    try:
        # Provide the question to the model and get the response
        response = openai.ChatCompletion(
            engine="text-davinci-002",  # Choose the engine based on your preference
            # like you can set to gpt-3.5 turbo
            
            prompt=question, # using prompt command
            max_tokens=100,
            temperature=0.7# setting the temperature
        )
        return response.choices[0].text.strip()# to return the prompt answer
    except Exception as e:
        print("An error occurred:", e)
        return None
#Driver code

def main():
    print("Welcome to the Chatbot!")
    print("Type 'exit' to end the conversation.")

    while True:# condition
        user_input = input("You: ")# input the question
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        # Get the response from the chatbot
        response = ask_question(user_input)
        if response:# response generated
            print("Chatbot:", response)
        else:
            print("Chatbot: Sorry, I couldn't understand that.")


if __name__ == "__main__":
    main()# main function called
