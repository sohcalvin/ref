import gensim

text = '''zoo keeps lion
giraffe monkey tigers are animals you can find in the zoo
wild animals in africa are amazing
animals protection agency
poaching tigers is illegal
new york city is a lively place
'''
sentences =  text.split(sep="\n")
tokenized = []
for s in sentences :
    tokenized.append(s.split())

print("\n---- tokenized -----\n", tokenized)

bigram_transformer = gensim.models.Phrases(tokenized)
print(bigram_transformer.vocab)

print("\n---- bigram_transformer -----\n", bigram_transformer[tokenized])
model = gensim.models.Word2Vec(bigram_transformer[tokenized], size=100, window=5, min_count=1, workers=4)

print("\n---- model.vocab -----\n", model.vocab)

result = model.most_similar(positive=["new_york"])

print(result)

