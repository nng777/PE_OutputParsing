"""
Extracting Information from Text
The task is to create a prompt that instructs a Large Language Model (LLM) to extract specific information from a given text and format it as a JSON object. Then, write a simple Python script to demonstrate how you would parse this JSON output.

1. The Text:
Use the following text as your input:
"The new Acme X1 laptop, released on 2025-09-10, features a 15-inch display and a 3.2 GHz processor. You can buy it on our website for $1200."

2. The Prompt:
Write a prompt that instructs the LLM to extract the following information from the text:
- Product name
- Release date
- Screen size
- Processor speed
- Price
The output from the LLM should be a JSON object with keys product_name, release_date, screen_size, processor_speed, and price.

3. The Python Script:
Write a Python script that:
3.1. Takes the JSON output from the LLM as a string.
3.2. Parses the JSON string into a Python dictionary.
3.3. Prints the value of the product_name and price keys.
"""