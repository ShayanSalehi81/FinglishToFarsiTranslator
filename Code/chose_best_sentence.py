import numpy as np
from transformers import BertTokenizer, BertModel
from sklearn.metrics.pairwise import cosine_similarity

tokenizer = BertTokenizer.from_pretrained('HooshvareLab/bert-base-parsbert-uncased')
model = BertModel.from_pretrained('HooshvareLab/bert-base-parsbert-uncased')

def get_sentence_embedding(sentence):
    inputs = tokenizer(sentence, return_tensors='pt', padding=True, truncation=True, max_length=512)
    outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).detach().numpy()

def return_best_sentence(sentences):
    top_sentences = [s[1] for s in sentences[:10]]
    embeddings = [get_sentence_embedding(sentence) for sentence in top_sentences]

    similarities = cosine_similarity(np.vstack(embeddings))

    max_sim_score = -1
    best_sentence = ''
    for i in range(len(similarities)):
        for j in range(i + 1, len(similarities[i])):
            if similarities[i][j] > max_sim_score:
                max_sim_score = similarities[i][j]
                best_sentence = top_sentences[i]
    
    return best_sentence