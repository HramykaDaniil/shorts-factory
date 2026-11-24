

import os
import time
from google import genai
from google.genai.errors import ServerError


def main():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not configured")

    client = genai.Client(api_key=api_key)

    model = "gemini-flash-lite-latest"

    prompt = (
        "Ответь одной короткой фразой на русском: "
        "Gemini успешно подключён к Shorts Factory."
    )

    for attempt in range(1, 4):
        try:
            print(f"Connecting to {model}, attempt {attempt}...")

            response = client.models.generate_content(
                model=model,
                contents=prompt,
            )

            print("Gemini connection successful!")
            print(response.text)
            return

        except ServerError as error:
            print(f"Gemini server error: {error}")

            if attempt < 3:
                delay = attempt * 20
                print(f"Retrying in {delay} seconds...")
                time.sleep(delay)

    raise RuntimeError("Gemini API unavailable after 3 attempts")


if __name__ == "__main__":
    main()
