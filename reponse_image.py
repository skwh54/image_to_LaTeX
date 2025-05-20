import ollama
import tempfile

def reponse_image(img_bytes: bytes,
                    model_name: str = "gemma3:latest") -> str:
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
        tmp.write(img_bytes)
        img_path = tmp.name

    response = ollama.chat(
        model=model_name,
        messages=[{
            "role": "user",
            "content": (
                "This image contains a math equation. "
                "Extract ONLY the raw LaTeX formula—no explanations, no LaTeX environments, just the code itself."
            ),
            "images": [img_path]
        }]
    )
    return response["message"]["content"].strip()
