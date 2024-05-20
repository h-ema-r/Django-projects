# BioBlogs & MalariaCellClassifier
“BioBlogs and MalariaCellClassifier” is a multifaceted project that combines the 
functionality of a blogging platform with a sophisticated machine learning model for 
malaria cell classification. The project aims to provide a comprehensive solution that 
addresses both the need for knowledge sharing in the healthcare domain and the 
advancement of malaria diagnostics through machine learning.
<br>
"BioBlogs and MalariaCellClassifier" utilizes Django, a Python web framework, to 
create an intuitive web interface enabling users to write blogs, register accounts, and access 
user-contributed content. Leveraging Convolutional Neural Networks (CNNs) for malaria 
cell classification.

## NOTE : 
**Models1** contains 1  folder and 2 files.
- dataset folder named = cell_images  which contains train and test dataset
- notebook = malaria-detection.ipynb
- and saved model = **[saved-model](https://drive.google.com/drive/folders/1kwmNOUoUBB0vIaKqpVkqwDYMofQhsvCd?usp=sharing)**
  
**size of dataset and saved model is too large to upload to github.**

## Data source 
The dataset used for training the model is available at [Data source](https://www.kaggle.com/iarunava/cell-images-for-detecting-malaria)
<br>
Given dataset was manually split into training and testing datasets, maintaining the 
distribution of infected and uninfected images in each set. The dataset consists of a total 
of 27,294 images belonging to 2 classes for training and 264 images belonging to the 
same 2 classes for validation. Here are further details:
- Training Dataset: Contains 27,294 images. 
- Validation Dataset: Contains 264 images. 
- Classes: The dataset is divided into 2 classes: infected and uninfected cells.

## Files:
**requirements.txt:**
This file contains all the dependencies required to run the application.

**BioBlogsNMalariaCellClassifier/models1/malaria-detection.ipynb**
- This notebook contains the code for training a malaria detection model using Convolutional Neural Network (CNN).<br>
- Once training is completed, the trained model is saved to a file using following command for future use.<br>
```bash
model.save('malaria-detection-model.h5')
```

## Output Video:
![Output](https://github.com/h-ema-r/Django-projects/blob/main/BioBlogs%20and%20MalariaCellClassifier-django.zip)

