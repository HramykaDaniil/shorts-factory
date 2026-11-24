import os
from google import genai


def main():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not configured")

    client = genai.Client(api_key=api_key)

    print("Connecting to Gemini...")

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents="Ответь одной короткой фразой на русском: Gemini успешно подключён к Shorts Factory."
    )

    print("Gemini response:")
    print(response.text)


if __name__ == "__main__":
    main()
