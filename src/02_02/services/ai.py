import os
from openai import OpenAI
from dotenv import load_dotenv

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
load_dotenv()


def generate_review(review: str) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content":
                ("You are a sentiment classification bot, print out if the"
                 "user is happy or sad. Only print out happy or sad."),
            },
            {"role": "user", "content": review},
        ],
        temperature=0.7,
        max_tokens=150)

    # type: ignore
    response_message = response.choices[0].message.content  # type: ignore
    if response_message == "happy":
        return "Thanks for shopping with us, come back soon!"
    return ("Sorry to hear about your experience, here's a coupon for 20% off,"
            "type GPT20 to use it")
