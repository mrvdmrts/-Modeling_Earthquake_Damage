from sklearn.model_selection import cross_val_score


def validate_fun(clf,X,y):
    scores = cross_val_score(clf, X, y, cv=5)
    return scores


