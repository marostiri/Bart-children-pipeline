# Bart-children-pipeline

## Folder Structure

```
📦 ProjectName
├── eval-models.ipynb     # Code to evaluate models
├── post-process.ipynb   # Code to generate post-processed text
├── training.ipynb        # Code to training models
└── README.md       # Project documentation
```

## Usage

If you want to train models, you have to:
- Have the dataset in 'data/final'
- set variable 'PATH_' at the beginning of the code
  
If you want to post-process text, you have to:
- Unzip models in 'models' folder or train one using 'training.ipynb'
- Have the dataset and vocabulary in 'data/final' 
- set variable 'PATH_' at the beginning of the code
  
If you want to evalute models, you have to:
- Unzip models in 'models' folder or train one using 'training.ipynb'
- Have the dataset in 'data/final'
- set variable 'PATH_' at the beginning of the code

## Information

We used GPU A6000 to run training and inference phase.
You can run eval-models.ipynb on a T4 GPU
