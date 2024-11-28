from transformers import pipeline

classifier = pipeline("sentiment-analysis",model="distilbert-base-uncased-finetuned-sst-2-english")
res = classifier("Conda is a pain")
print(res)