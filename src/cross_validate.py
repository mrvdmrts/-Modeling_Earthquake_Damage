from sklearn.model_selection import cross_val_score
import numpy as np


def cross_validate(classifiers,X,y):
    """Cross validation Function

    Args:
        classifiers (): classifier list
        X (ndarray): Train Data
        y (ndarray): Target data

    Returns:
        Tupel: model scores, model
    """
    scores = [np.mean(cross_val_score(clf, X, y, cv=5)) for clf in classifiers]
    best_model = classifiers[np.argmax(scores)]
    return scores, best_model
    

