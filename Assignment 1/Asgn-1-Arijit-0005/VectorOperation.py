import numpy as np
from dataclasses import dataclass

@dataclass
class Vector:
    mat1: list
    mat2: list

    @property
    def add(self) -> list:
        return self.mat1 + self.mat2
    
    @property
    def mul(self) -> list:
        return self.mat1 * self.mat2
    
    @property
    def dot(self) -> int:
        return np.dot(self.mat1, self.mat2)
    
    @property
    def cross(self) -> int:
        return np.cross(self.mat1, self.mat2)
    
    @property
    def isOrthogonal(self) -> bool:
        return np.isclose(np.dot(self.mat1, self.mat2), 0)
    
    @property
    def isParallel(self) -> bool:
        return np.allclose(np.cross(self.mat1, self.mat2), 0)