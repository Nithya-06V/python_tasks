from abc import ABC,abstractmethod
import numpy as np
class BaseDataTransformer(ABC):
    @abstractmethod
    def transform(self,data):
        pass
class NormalizerTransformer(BaseDataTransformer):
    def transform(self,data):
        maximum=max(data)
        return [round(x/maximum,2) for x in data]
class StandardizerTransformer(BaseDataTransformer):
    def transform(self,data):
        mean=np.mean(data)
        std=np.std(data)
        return [round((x-mean)/std,2) for x in data]
norm=NormalizerTransformer()
std_t=StandardizerTransformer()
print("Normalized :",norm.transform([10,20,50,100]))
print("Standardized:",std_t.transform([10,20,30,40,50]))