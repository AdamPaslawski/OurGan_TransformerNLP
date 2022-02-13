# OurGan Pytorch

This is a fork of  https://github.com/williamSYSU/TextGAN-PyTorch where we implemented our own novel archtecture called OurGan (~/models/OurGan_D , ~/models/OurGan_G).

You can read our paper included in this repo at ~/OurGan.pdf


## Requirements

- **PyTorch >= 1.1.0**
- Python 3.6
- Numpy 1.14.5
- CUDA 7.5+ (For GPU)
- nltk 3.4
- tqdm 4.32.1
- KenLM (https://github.com/kpu/kenlm)

To install, run `pip install -r requirements.txt`. In case of CUDA problems, consult the official PyTorch [Get Started guide](https://pytorch.org/get-started/locally/).

## Other Implemented Models and Original Papers

### General Text Generation

- **SeqGAN** - [SeqGAN: Sequence Generative Adversarial Nets with Policy Gradient](https://arxiv.org/abs/1609.05473)
- **LeakGAN** - [Long Text Generation via Adversarial Training with Leaked Information](https://arxiv.org/abs/1709.08624)
- **MaliGAN** - [Maximum-Likelihood Augmented Discrete Generative Adversarial Networks](https://arxiv.org/abs/1702.07983)
- **JSDGAN** - [Adversarial Discrete Sequence Generation without Explicit Neural Networks as Discriminators](http://proceedings.mlr.press/v89/li19g.html)
- **RelGAN** - [RelGAN: Relational Generative Adversarial Networks for Text Generation](https://openreview.net/forum?id=rJedV3R5tm)
- **DPGAN** - [DP-GAN: Diversity-Promoting Generative Adversarial Network for Generating Informative and Diversified Text](https://arxiv.org/abs/1802.01345)
- **DGSAN** - [DGSAN: Discrete Generative Self-Adversarial Network](https://arxiv.org/abs/1908.09127)
- **CoT** - [CoT: Cooperative Training for Generative Modeling of Discrete Data](https://arxiv.org/abs/1804.03782)

### Category Text Generation

- **SentiGAN** - [SentiGAN: Generating Sentimental Texts via Mixture Adversarial Networks](https://www.ijcai.org/proceedings/2018/618)
- **CatGAN** (ours) - [CatGAN: Category-aware Generative Adversarial Networks with Hierarchical Evolutionary Learning for Category Text Generation](https://arxiv.org/abs/1911.06641)

  

## Licence

**MIT lincense**

