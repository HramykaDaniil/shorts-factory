
import os
from google import genai


def main():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not configured")

    client = genai.Client(api_key=api_key)

    model = "gemini-3.5-flash-lite"

    print(f"Connecting to {model}...")

    response = client.models.generate_content(
        model=model,
        contents=(
            "Ответь одной короткой фразой на русском: "
            "Gemini успешно подключён к Shorts Factory."
        ),
    )

    if not response.text:
        raise RuntimeError("Gemini returned an empty response")

    print("\nGemini connection successful!")
    print(response.text)


if __name__ == "__main__":
    main()
