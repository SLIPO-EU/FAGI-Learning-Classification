# FAGI Learning - Classification Module
## SLIPO-EU
Python code for FAGILearning feature in the road for [FAGI v3.0](https://github.com/SLIPO-EU/FAGI).



## FAGILearning 

FAGILearning implements the major steps of a traditional process for classification, exploring domain-specific training features specifically designed for handling the validation and fusion of linked POI entities.

The first step of the process is constructing an initial training dataset, which consist of labelled instances (pairs of linked POIs).

The second step consists in representing each pair of linked POIs in a multidimensional feature space; essentially, represent each pair as a feature vector (feature extraction). 

The third step regards evaluating a set of different algorithms for classification and its the subject of this repository.

## Problem Formulation
For a given pair of POI datasets, A and B which contain POI entities accompanied with several properties describing characteristics of each POI(e.g. name, address, phone, website, email, coordinates), as well as a links file L, which contains a set of links connecting POIs from A with POIs from B.
Considering a POI a in A that is linked with a POI b in B, and the sets of properties {Pa,i} and {Pb,i} that describe them respectively, FAGI handles two tasks:

* **Decide validation action**. Decide whether POIs a and b actually correspond to the same real-world entity or they are wrongly interlinked. This can be formulated as a *binary classification* problem with output classes “accept” and “reject”.

* **Decide fusion action**. Decide which is the most fitting fusion action for each pair i of matching properties (Pa,i, Pb,i) of the two POIs. This can be formulated as a *multi-class classification* problem, with the different fusion actions being considered as the classes of the problem.

Our goal is to develop the functionality that facilitates the accurate execution of the above two tasks, requiring the minimum effort by the user both in the selection of validation/fusion actions and in the post-processing, manual examination/validation of the fusion results.
## Classification

We experiment with several classification algorithms, for both link validation and fusion action recomendation. The algorithms used are:
* K-Nearest Neighbors
* Support Vector Machines(linear and RBF)
* Decision Trees
* Random Forests
* AdaBoost
* Gradient Boosting
* Extra Trees
* Neural Networks

In out experiments, we utilize the [scikit-learn](http://scikit-learn.org) framework and [Keras](https://keras.io/).