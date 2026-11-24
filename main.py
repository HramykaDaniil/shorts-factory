import os
import requests


def main():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not configured")

    url = "https://generativelanguage.googleapis.com/v1beta/models"

    response = requests.get(
        url,
        headers={"x-goog-api-key": api_key},
        timeout=30,
    )

    print("API status:", response.status_code)
    response.raise_for_status()

    models = response.json().get("models", [])

    print("\nAvailable models supporting generateContent:\n")

    for model in models:
        methods = model.get("supportedGenerationMethods", [])

        if "generateContent" in methods:
            print(
                model.get("name"),
                "|",
                model.get("displayName")
            )

    print("\nModel list completed.")


if __name__ == "__main__":
    main()
