import os
import gensim
import eg_gensim_data



sentences = eg_gensim_data.sentences
# jd = eg_gensim_data.jd.split()
# cv = eg_gensim_data.cv.split()

model = gensim.models.Word2Vec(sentences, size=100, window=5, min_count=1, workers=4)
for k,v in model.vocab.items() :
    if (k == "hollywood") :print(k,">>",v)
z =[["hollywood", "zoolander"],["apple", "zoolander","cider"], ["hollywood","jumping", "jack", "flash"]]


model.train(z)
model.train(z)

for k,v in model.vocab.items() :
    if (k == "hollywood") :print(k,">>>>>",v)
print(model.most_similar(["hollywood"]))
print(model.most_similar(["zoolander"]))


# model = pickle.load(open(os.path.join(path_specifier.getPicklePath(), gensim_model_file), "rb"))

# for k, v in model2.vocab.items():
#     print(k, ">>", v)
