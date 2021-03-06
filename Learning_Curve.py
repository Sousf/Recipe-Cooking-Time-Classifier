#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import pandas as pd
from imblearn.over_sampling import RandomOverSampler
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler, MaxAbsScaler
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
from mlxtend.plotting import plot_learning_curves
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.model_selection import learning_curve
from sklearn.model_selection import ShuffleSplit

def plot_learning_curve(estimator, title, X, y, ylim=None, cv=None,
                        n_jobs=1, train_sizes=np.linspace(.1, 1.0, 5)):
    """
    Generate a simple plot of the test and training learning curve.

    Parameters
    ----------
    estimator : object type that implements the "fit" and "predict" methods
        An object of that type which is cloned for each validation.

    title : string
        Title for the chart.

    X : array-like, shape (n_samples, n_features)
        Training vector, where n_samples is the number of samples and
        n_features is the number of features.

    y : array-like, shape (n_samples) or (n_samples, n_features), optional
        Target relative to X for classification or regression;
        None for unsupervised learning.

    ylim : tuple, shape (ymin, ymax), optional
        Defines minimum and maximum yvalues plotted.

    cv : int, cross-validation generator or an iterable, optional
        Determines the cross-validation splitting strategy.
        Possible inputs for cv are:
          - None, to use the default 3-fold cross-validation,
          - integer, to specify the number of folds.
          - An object to be used as a cross-validation generator.
          - An iterable yielding train/test splits.

        For integer/None inputs, if ``y`` is binary or multiclass,
        :class:`StratifiedKFold` used. If the estimator is not a classifier
        or if ``y`` is neither binary nor multiclass, :class:`KFold` is used.

        Refer :ref:`User Guide <cross_validation>` for the various
        cross-validators that can be used here.

    n_jobs : integer, optional
        Number of jobs to run in parallel (default 1).
    """
    plt.figure()
    plt.title(title)
    if ylim is not None:
        plt.ylim(*ylim)
    plt.xlabel("Training examples")
    plt.ylabel("Score")
    train_sizes, train_scores, test_scores = learning_curve(
        estimator, X, y, cv=cv, n_jobs=n_jobs, train_sizes=train_sizes)
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)
    plt.grid()

    plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                     train_scores_mean + train_scores_std, alpha=0.1,
                     color="r")
    plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                     test_scores_mean + test_scores_std, alpha=0.1, color="g")
    plt.plot(train_sizes, train_scores_mean, 'o-', color="r",
             label="Training score")
    plt.plot(train_sizes, test_scores_mean, 'o-', color="g",
             label="Cross-validation score")

    plt.legend(loc="best")
    return plt

# x_train_original = pd.read_csv("../data/COMP30027_2021_Project2_datasets/recipe_train.csv", index_col = False, delimiter = ',', header=0)

# # oversample = RandomOverSampler(sampling_strategy='minority')

# train_label = x_train_original.loc[:,'duration_label']
# # X_train, X_test, y_train, y_test = train_test_split(x_train_original,train_label, test_size=0.4, stratify=train_label, random_state=42)



# # # First random oversampling, bring count of class 3 to be equal to the highest class count.
# # X_oversampled, y_oversampled = oversample.fit_resample(X_train, y_train)


# # # Second random oversampling, bring the count of class 2 to be equal to the other 2 classes
# # X_oversampled, y_oversampled = oversample.fit_resample(X_oversampled, y_oversampled)

# # # .value_counts()
# # # use recipe name as an example
# train_corpus = x_train_original.loc[:,['name','steps','ingredients']]



# # Joining columns for train
# train_corpus['steps'] = train_corpus['steps'].apply(eval)
# train_corpus['ingredients'] = train_corpus['ingredients'].apply(eval)
# train_corpus['steps'] = train_corpus['steps'].apply(' '.join)
# train_corpus['ingredients'] = train_corpus['ingredients'].apply(' '.join)

# train_corpus


# In[11]:


# all_words = []

# for i in range (0, len(train_corpus['steps'])):
#     s = ''
#     s += train_corpus.loc[i,'name'] + train_corpus.loc[i, 'steps'] + train_corpus.loc[i, 'ingredients']
#     all_words.append(s)
# all_words


# In[12]:


# from sklearn.feature_extraction.text import CountVectorizer
# # stop_word ='english' means deleting some common words like the, a,.... in list 'english'



# vectorizer = CountVectorizer(stop_words='english', max_features = 500)
# X = vectorizer.fit(all_words)
# vocab_dict = vectorizer.vocabulary_
# # vocab = np.array(vectorizer.get_feature_names())

# X_final = vectorizer.transform(all_words)
# X_final.shape


# ### Learning Curve Function

# In[3]:





# In[13]:


# from sklearn import svm

# LinearSVC_clf = svm.LinearSVC(dual=False, multi_class='ovr', random_state=0)
# SVC_clf = make_pipeline(StandardScaler(with_mean=False), MaxAbsScaler(), LinearSVC_clf)


# In[16]:


# title = "Learning Curves (LinearSVC)"
# # Cross validation with 100 iterations to get smoother mean test and train
# # score curves, each time with 20% data randomly selected as a validation set.
# cv = ShuffleSplit(n_splits=100, test_size=0.2, random_state=0)


# plot_learning_curve(SVC_clf, title, X_final, train_label, ylim=(0.7, 1.01), cv=cv, n_jobs=4)


# In[ ]:


# plt.show()

