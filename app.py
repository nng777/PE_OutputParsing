import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
import json
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


def main() -> None:
    model_name = "Shritama/flanT5-text-json"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    text = (
        "The new Acme X1 laptop, released on 2025-09-10, "
        "features a 15-inch display and a 3.2 GHz processor. "
        "You can buy it on our website for $1200."
    )

    prompt = (
        "Extract the product name, release date, screen size, "
        "processor speed and price as a JSON object with keys "
        "product_name, release_date, screen_size, processor_speed and price.\n"
        f"Text: {text}"
    )

    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=128)
    json_str = tokenizer.decode(outputs[0], skip_special_tokens=True)

    try:
        data = json.loads(json_str)
    except json.JSONDecodeError:
        print("Model did not return valid JSON: \n", json_str)
        return

    print("product_name:", data.get("product_name"))
    print("release_date:", data.get("release_date"))
    print("screen_size:", data.get("screen_size"))
    print("processor_speed:", data.get("processor_speed"))
    print("price:", data.get("price"))


if __name__ == "__main__":
    main()