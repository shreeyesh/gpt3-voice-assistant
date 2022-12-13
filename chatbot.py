import openai

# Set up OpenAI API key
openai.api_key = "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"

# Define a function to generate a response
def generate_response(prompt):
    # Use OpenAI to generate a response to the prompt
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n = 1,
        stop = None,
        temperature = 0.5,
    )

    # Return the generated response
    return response["choices"][0]["text"]

# Ask the user for input
user_input = input("What can I help you with?\n")

# Generate a response and print it
response = generate_response(user_input)
print(response)
