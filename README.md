This project focuses on text-based classification, specifically in the domain of fact-checking statements. The dataset comprises statements paired with verdicts, where the verdicts are binary labels indicating the statements' truthfulness. The goal is to develop and evaluate machine learning models for automating the classification of statements as either true or false.

The project involves tasks such as data preprocessing, exploratory data analysis, feature engineering, and the implementation of various machine learning algorithms. Natural Language Processing (NLP) techniques are employed to extract meaningful features from the textual data. Additionally, statistical tests, including chi-square analysis, are performed to explore relationships between categorical variables.

The evaluation metrics, such as accuracy, precision, recall, and F1 score, are employed to assess the performance of the models. The project provides insights into the efficiency of different algorithms in handling the fact-checking task and aims to contribute to the field of automated content verification.

### model_and_analysis.ipynb:
This notebook encompasses the entire data science pipeline, starting with data exploration and preprocessing, followed by model creation and analysis. The steps involved are:
* Data Loading and Exploration: The dataset, containing statements and their corresponding verdicts, is loaded and explored to gain insights into the data distribution, null values, and key statistics.
* Data Preprocessing: The textual data undergoes preprocessing steps such as text cleaning, handling missing values, and transforming categorical labels into numerical representations suitable for machine learning models.
* Exploratory Data Analysis (EDA): Comprehensive EDA is conducted to understand the distribution of verdicts, uncover patterns, and identify potential features. Visualizations are used to illustrate key findings.
* Feature Engineering: Relevant features are engineered, especially focusing on extracting meaningful information from the textual statements using techniques like TF-IDF or word embeddings.
* Model Building: Various machine learning algorithms are employed to build classification models. This includes traditional algorithms such as Logistic Regression and SVM, as well as ensemble methods like made up of Random Forest, svm and Logistic Regression . Model performance metrics are computed, and models are fine-tuned accordingly.

### NLP_model.ipynb:
This notebook is dedicated to the creation of a Natural Language Processing (NLP) model using GloVe embeddings. The main highlights include:
* Introduction to GloVe: An introduction to GloVe embeddings and their significance in NLP tasks.
* Tokenization and Padding: The textual data is tokenized, and padding is applied to ensure consistent input dimensions for the model.
* Model Architecture: The NLP model is constructed using a bag-of-words linear classifier (BOW-LC) approach. It involves an embedding layer to convert text into continuous embeddings and a * linear layer for classification.
* Training and Evaluation: The model is trained using GloVe embeddings, and its performance is evaluated using standard metrics such as accuracy. The training process is visualized to * analyze the convergence and performance over epochs.

 By separating the tasks into these two notebooks, the project maintains a clear and organized structure, allowing for a focused exploration of both traditional machine learning approaches and advanced NLP techniques using GloVe embeddings
