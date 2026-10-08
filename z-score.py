import numpy as np
def detect_outliers_zscore(values,threshold=2.0):
    values=np.array(values,dtype=float)
    mean=np.mean(values)
    std=np.std(values)
    if std==0:
        return []
    z=np.abs((values-mean)/std)
    return values[z>threshold].tolist()
metrics=[10.0,12.0,12.0,13.0,12.0,11.0,14.0,100.0,12.0]
outliers=detect_outliers_zscore(metrics,threshold=2.0)
print(outliers)