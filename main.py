
import os
from google import genai
from google.genai.errors import ServerError


def main():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not configured")

    client = genai.Client(api_key=api_key)

    models = [
        "gemini-3.8-flash",
        "gemini-3.7-flash",
    ]

    prompt = (
        "Ответь одной короткой фразой на русском: "
        "Gemini успешно подключён к Shorts Factory."
    )

    for model in models:
        try:
            print(f"Connecting to {model}...")

            response = client.models.generate_content(
                model=model,
                contents=prompt,
            )

            print(f"Successfully connected to {model}")
            print("Gemini response:")
            print(response.text)
            return

        except ServerError as error:
            print(f"{model} is temporarily unavailable: {error}")

    raise RuntimeError("All Gemini models are currently unavailable")


if __name__ == "__main__":
    main()
