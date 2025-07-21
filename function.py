def evaluate_fit_by_recall(recall_train, recall_test, threshold=0.05):
    """
    Evaluasi apakah model underfit, overfit, atau good fit berdasarkan recall.
    
    Parameters:
    - recall_train: recall pada data training (float)
    - recall_test: recall pada data test (float)
    - threshold: toleransi perbedaan recall antara train dan test (default 0.05 / 5%)

    Returns:
    - String: 'Underfit', 'Overfit', atau 'Good Fit'
    """
    if recall_train < 0.7 and recall_test < 0.7:
        return 'Underfit'
    elif abs(recall_train - recall_test) > threshold:
        return 'Overfit'
    elif abs(recall_train - recall_test) <= threshold:
        return 'Good Fit'
    else:
        return 'Perlu Investigasi Lanjut'
    

def roc_auc_score_criteria(score):
    if score >= 0.9 and score <= 1:
        return print("Good")
    elif score >= 0.8 and score <0.9:
        return print("Fair")
    elif score >= 0.7 and score <0.8:
        return print("Decent")
    elif score >= 0.6 and score <0.7:
        return print("Not Great")
    elif score < 0.6:
        return print("Poor")