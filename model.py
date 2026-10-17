import torch
import torch.nn as nn


class IntentClassifier(nn.Module):
    def __init__(self, vocab_size, num_classes, embedding_dim=32, padding_idx=0):
        super().__init__()

        self.embedding = nn.Embedding(
            num_embeddings=vocab_size,
            embedding_dim=embedding_dim,
            padding_idx=padding_idx,
        )
        self.classifier = nn.Linear(embedding_dim, num_classes)

    def forward(self, token_ids):
        embeddings = self.embedding(token_ids)

        mask = (token_ids != 0).unsqueeze(-1)
        embeddings = embeddings * mask

        summed_embeddings = embeddings.sum(dim=1)
        token_counts = mask.sum(dim=1).clamp(min=1)
        sentence_embeddings = summed_embeddings / token_counts

        return self.classifier(sentence_embeddings)