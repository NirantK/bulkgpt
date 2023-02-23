import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")


def rewrite(sku_description: str) -> str:
    """
    Rewrites a description using GPT3.

    Args:
        description (str): _description_

    Returns:
        str: _description_
    """
    prompt = f"""This is a product description. Rewrite this in your own words to improve conversion and make it more casual. Add a call to action. Keep the same meaning:\n\n{sku_description}"""

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.2,
        max_tokens=420,
        frequency_penalty=0.7,
        presence_penalty=0.8,
    )
    return str(response.choices[0].text)
