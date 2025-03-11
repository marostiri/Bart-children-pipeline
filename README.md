# Bart-children-pipeline

## Description
With the rapid advancement of Large Language Models, their role in educational contexts has gained increasing attention due to their abilities to generate text. One relevant application in this field is Text Simplification (TS), which aims to reduce text complexity to enhance readability and accessibility. While many approaches to Text Simplification rely on the English language, research focusing on the Italian Language is limited. In particular, there is a lack of methods specifically designed to help 8- to 11-year-old children understand texts. To fill this gap, in this paper, we introduce a new resource for Italian Text Simplification. Our dataset is built by collecting texts from both the Italian Wikipedia and Vikidia, which is an online encyclopedia written for the studied age group. A Pre-trained Language Model is fine-tuned on this resource to generate simplified versions of Wikipedia pages that align with Vikidia’s linguistic style. The simplification process is further guided by a vocabulary built from Vikidia. This post-processing step enables the replacement of potentially complex terms in the output text with synonyms in the vocabulary that are accessible to children. The proposed approach is evaluated through qualitative assessments by elementary school teachers working with 10-year-old students. Through human evaluation, we show the effectiveness of the proposed Text Simplification system and its potential for educational purposes.

## Folder Structure

```
📦 Bart-children-pipeline
├── 📂 data          # Data with source information, dataset and vocabulary
├── 📂 generate_data   # Code to generate data 
├── 📂 models        # Models used
├── 📂 scraping       # Scraping code
└── README.md       # Project documentation
```

## Information

The folder does not contain the data and analysis obtained through Teacher Evaluation.

The data and results of human evaluation are not exposed.

In subfolder we explain how to run the code and download external dataset

We used GPU A6000 to run training and inference phase.

## Links
- [Italian Wikipedia](https://it.wikipedia.org/wiki/Pagina_principale)
- [Italian Vikidia](https://it.vikidia.org/wiki/Pagina_principale)
- [Hugginface models](https://huggingface.co/)
