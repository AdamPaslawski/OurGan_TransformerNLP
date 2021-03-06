# -*- coding: utf-8 -*-
import math

import torch
import torch.autograd as autograd
import torch.nn as nn
import torch.nn.functional as F

import config as cfg
from utils.helpers import truncated_normal_

from models.discriminator import CNNDiscriminator

# dis_filter_sizes = [2, 3, 4, 5]
# dis_num_filters = [300, 300, 300, 300]

n_heads = 4
n_transformer_layers = 3
class OurGAN_D(nn.Module):
    def __init__(self, embed_dim, max_seq_len, vocab_size, padding_idx, gpu=False, dropout=0.25):
        super(OurGAN_D, self).__init__()

        self.embed_dim = embed_dim
        self.max_seq_len = max_seq_len
        self.gpu = gpu
        # self.feature_dim = sum(dis_num_filters) 

        self.embeddings = nn.Linear(vocab_size, embed_dim, bias=False)

        # Returns BxTxD
        self.transformer = nn.TransformerEncoder(
            nn.TransformerEncoderLayer(embed_dim, nhead=n_heads),
            n_transformer_layers
        )


        # TODO consider adding activation/normalization?
        self.highway = nn.Sequential(
            nn.Linear(self.embed_dim * self.max_seq_len, self.embed_dim),
            nn.ReLU()
        )
        self.feature2out = nn.Sequential(
            nn.Linear(self.embed_dim, 100),
            nn.ReLU()
        )
        self.out2logits = nn.Sequential(
            nn.Linear(100, 1),
            nn.Sigmoid()
        )
        # self.dropout = nn.Dropout(dropout)

        self.init_params()

        self.pos_encoding = self.positional_encoding()
    
    def positional_encoding(self):
        p_idx = torch.arange(self.max_seq_len)[..., None]
        d_idx = torch.arange(self.embed_dim//2)[None, ...]
        sincos_term = p_idx / 10000**(2.0 * d_idx / self.embed_dim)

        sin_vals = torch.sin(sincos_term)
        cos_vals = torch.cos(sincos_term)

        encodings = torch.empty((self.max_seq_len, self.embed_dim))
        encodings[:, 0::2] = sin_vals
        encodings[:, 1::2] = cos_vals

        # Num patches x Embedding dimension
        encodings = encodings.cuda()

        return encodings

    def forward(self, inp):
        """
        Get logits of discriminator
        :param inp: batch_size * seq_len * vocab_size
        :return logits: [batch_size * num_rep] (1-D tensor)
        """
        emb = self.embeddings(inp) # batch_size * max_seq_len * embed_dim

        seqlen = inp.size(1)
        emb = emb + self.pos_encoding[:seqlen]

        trans = self.transformer(emb) # batch * max_seq_len * embed_dim

        x = self.highway(trans.flatten(start_dim=1)) #life is a highway.
        x = self.feature2out(x)
        x = self.out2logits(x)

        return x



    def init_params(self):
        for param in self.parameters():
            if param.requires_grad and len(param.shape) > 0:
                stddev = 1 / math.sqrt(param.shape[0])
                if cfg.dis_init == 'uniform':
                    torch.nn.init.uniform_(param, a=-0.05, b=0.05)
                elif cfg.dis_init == 'normal':
                    torch.nn.init.normal_(param, std=stddev)
                elif cfg.dis_init == 'truncated_normal':
                    truncated_normal_(param, std=stddev)
