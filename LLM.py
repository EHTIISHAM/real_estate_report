from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load the tokenizer and model
tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-base")
model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-base")


input_text = (
    """Provide a suggested pricing strategy for buying a house with these details: 
    - Location: Teaneck, NJ
    - Listing price: $1,400,000
    - Comparable properties: $1,350,000 to $1,800,000
    - Market trends: rising prices, high demand, low inventory."""
    "Generate a market trend analysis for Teaneck, NJ based on details mentioned above"
    "What should be the price offering and what are the Additional Consideration before buying house"
)

# Tokenize input
inputs = tokenizer.encode(input_text, return_tensors="pt")


# Generate output
outputs = model.generate(inputs, max_length=500, num_beams=16, early_stopping=True)

# Decode the output
result = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("Generated Market Trends:\n", result)
