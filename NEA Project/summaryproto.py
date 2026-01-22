# Import the tokenizer and model class for BART from the Hugging Face transformers library
from transformers import BartTokenizer, BartForConditionalGeneration

# This converts raw text into tokens that the model can understand
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')

# Load the pre-trained BART model fine-tuned for summarisation
model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')

# Define a function to generate a summary from an input text
def generate_summary(text):
    # Tokenise the input text and convert it into PyTorch tensors
    # max_length=1024 limits the input size (BART's maximum)
    inputs = tokenizer.encode(
        "summarize: " + text,
        return_tensors="pt",
        max_length=1024,
        truncation=True
    )

    summary_ids = model.generate(
        inputs,
        max_length=150,
        min_length=50,
        length_penalty=2.0,
        early_stopping=True  # early_stopping: stops generation once an end-of-sentence token is reached
    )

    # Decode the generated token IDs back into human-readable text
    # skip_special_tokens=True removes tokens like <s> and </s>
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary

article = (
    "World War II negatively impacted the company as Japanese authorities prohibited "
    "the diffusion of foreign card games, and as the priorities of Japanese society "
    "shifted, its interest in recreational activities waned. During this time, "
    "Nintendo was partly supported by a financial injection from Hiroshi's wife "
    "Michiko Inaba, who came from a wealthy family.[24] In 1947, Sekiryo founded the "
    "distribution company Marufuku Co., Ltd.[g] responsible for Nintendo's sales and "
    "marketing operations, which would eventually go on to become the present-day "
    "Nintendo Co., Ltd., in Higashikawara-cho, Imagumano, Higashiyama-ku, Kyoto.[2][3][7]"
)

summary = generate_summary(article)

print("Original Text:", article)
print("Summary:", summary)