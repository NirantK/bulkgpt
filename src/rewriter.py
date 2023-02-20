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
        max_tokens=400,
        frequency_penalty=0.7,
        presence_penalty=0.8,
    )
    return str(response.choices[0].text)


if __name__ == "__main__":
    SAMPLE = """ 
Release date:
CRAVITY's New Album will be released on March 7th 2023.
The shipment will be after this date.

CRAVITY's 5th Mini Album - MASTER:PIECE (KiT ALBUM)

Contents :
- 1 Album package
- 1 Air-kit
- 1 Title credit card
- 1 Post card
- 1 Photocard set (24ea)
- Member photocard (Random 1 out of 9)
The outer case/box is simply for protecting goods. (Damages such as scratches or discoloration on the case/box cannot be compensated.)
    """
    print(rewrite(SAMPLE))
