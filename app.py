import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
from transformers import AutoModelForCausalLM, AutoTokenizer


def main():
    model_name = "microsoft/phi-2"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    #ensure the tokenizer has a padding token to avoid generation warnings
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    model.config.pad_token_id = tokenizer.pad_token_id

    text = (
        "The new Acme X1 laptop, released on 2025-09-10, "
        "features a 15-inch display and a 3.2 GHz processor mantap kali. "
        "You can buy it on our website for $1200."
    )

    prompt = (
        "Extract the product name, release date, screen size, processor speed and price from following text:"
        f" {text} "
        "Generated output must be displayed as a flat JSON format"
    )

    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=128)
    thestring = tokenizer.decode(outputs[0], skip_special_tokens=True)

    print(thestring)


if __name__ == "__main__":
    main()