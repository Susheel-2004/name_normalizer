import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

def normalize_name(name, country):
    

    prompt = f"""You are a Scandinavian name expert. Correct the given name based on common Scandinavian name patterns.
    The name is definitely incorrectly interpreted due to the presence of non-English or Scandinavian characters. So do not deviate too much from the original name.
    Look for possible substitutions of characters and common misspellings. Here are a few test cases to help you understand better:
    [
        "Ake" : Åke
        "Naeik": Nöik or Nøik
        "Gosta": Gösta
        "Soeren": Søren
        "Haakon": Håkon
        "Oskar": Óskar
        "Tord": Þord
        "Aesa": Æsa
        "Moose": Møse
    ]
    Name: "{name}" 
    Country: {country}
    Return the most probable correct name and 2-3 similar name variations (name the key other_names) in JSON string format only with absolutely no additional text.
    """

    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You correct misspelled Scandinavian names."},
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    response = chat_completion.choices[0].message.content
    return eval(response)

# print(normalize_name("Naeik Anders", "Sweden"))