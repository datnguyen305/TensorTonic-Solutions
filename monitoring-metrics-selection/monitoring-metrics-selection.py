import numpy as np 
def compute_monitoring_metrics(system_type, y_true, y_pred):
    """
    Compute the appropriate monitoring metrics for the given system type.
    """
    result = []
    TP = TN = FP = FN = 0
    if system_type == "classification":
        for yt, yp in zip(y_true, y_pred):
            if yt == 1 and yp == 1:
                TP += 1
            elif yt == 0 and yp == 0:
                TN += 1
            elif yt == 0 and yp == 1:
                FP += 1
            elif yt == 1 and yp == 0:
                FN += 1

        N = len(y_true)

        accuracy = (TP + TN) / N if N > 0 else 0.0
        precision = TP / (TP + FP) if (TP + FP) > 0 else 0.0
        recall = TP / (TP + FN) if (TP + FN) > 0 else 0.0
        f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0

        result.append(("accuracy", accuracy))
        result.append(("precision", precision))
        result.append(("recall", recall))
        result.append(("f1", f1))

    elif system_type == "regression":
        if len(y_true) == 0:
            result.append(("mae", 0.0))
            result.append(("rmse", 0.0))
        mse = np.mean((np.array(y_true) - np.array(y_pred)) ** 2)
        rmse = np.sqrt(mse)
        mae = np.mean(np.abs(np.array(y_true) - np.array(y_pred)))
        result.append(("mae", mae))
        result.append(("rmse", rmse))
    
    elif system_type == "ranking":
        k = 3
    
        # sort indices by predicted score descending
        indices = sorted(range(len(y_pred)), key=lambda i: y_pred[i], reverse=True)
    
        top_k = indices[:k]
    
        tp_at_k = sum(1 for i in top_k if y_true[i] == 1)
    
        precision_at_3 = tp_at_k / k if k > 0 else 0.0
    
        total_relevant = sum(y_true)
        recall_at_3 = tp_at_k / total_relevant if total_relevant > 0 else 0.0
    
        result.append(("precision_at_3", precision_at_3))
        result.append(("recall_at_3", recall_at_3))

    return sorted(result, key=lambda x: x[0])

        