from transformers import BartTokenizer, BartForConditionalGeneration # A Library with pre-trained transformer models suitable for text summarisation

tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')

def generate_summary(text): # Takes an input and generates a summary using the loaded BART model
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(inputs, max_length=150, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

text = "The Battle of Arkansas Post was fought from January 9 to 11, 1863, along the Arkansas River at Arkansas Post, Arkansas, as part of the Vicksburg campaign of the American Civil War. Major General Ulysses S. Grant of the Union army started to move against Vicksburg in November 1862."
summary = generate_summary(text)
print(summary)