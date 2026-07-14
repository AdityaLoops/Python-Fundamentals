# NumPy — Useful Functions Reference

```python
import numpy as np
```

## Array Creation
| Function | Description |
|---|---|
| `np.array([1,2,3])` | Create array from list |
| `np.zeros((r,c))` | Array of zeros |
| `np.ones((r,c))` | Array of ones |
| `np.full((r,c), val)` | Array filled with `val` |
| `np.eye(n)` | Identity matrix |
| `np.arange(start, stop, step)` | Like `range()` but returns array |
| `np.linspace(start, stop, num)` | `num` evenly spaced values between start and stop |
| `np.empty((r,c))` | Uninitialized array (fast, garbage values) |
| `np.identity(n)` | Identity matrix (alias of `eye`) |
| `np.array(...).copy()` | Deep copy of array |

## Array Properties
| Function/Attr | Description |
|---|---|
| `arr.shape` | Dimensions tuple |
| `arr.ndim` | Number of dimensions |
| `arr.size` | Total number of elements |
| `arr.dtype` | Data type of elements |
| `arr.itemsize` | Bytes per element |
| `arr.nbytes` | Total bytes consumed |

## Reshaping & Manipulation
| Function | Description |
|---|---|
| `arr.reshape(r, c)` | Reshape without changing data |
| `arr.flatten()` | Flatten to 1D (returns copy) |
| `arr.ravel()` | Flatten to 1D (returns view when possible) |
| `arr.T` / `np.transpose(arr)` | Transpose |
| `np.concatenate([a, b], axis=0)` | Join arrays along an axis |
| `np.vstack([a, b])` | Stack vertically |
| `np.hstack([a, b])` | Stack horizontally |
| `np.split(arr, n)` | Split array into n equal parts |
| `np.tile(arr, reps)` | Repeat array |
| `np.repeat(arr, reps)` | Repeat elements |
| `np.expand_dims(arr, axis)` | Add a new axis |
| `np.squeeze(arr)` | Remove axes of length 1 |
| `arr.resize((r,c))` | Resize in place |

## Indexing / Slicing
| Function | Description |
|---|---|
| `arr[1:3, 0:2]` | Slice rows/cols |
| `arr[arr > 5]` | Boolean masking |
| `np.where(cond, a, b)` | Element-wise conditional select |
| `np.take(arr, indices)` | Take elements at indices |
| `np.select(condlist, choicelist)` | Multi-condition select |

## Math Operations
| Function | Description |
|---|---|
| `np.add`, `np.subtract`, `np.multiply`, `np.divide` | Elementwise ops (or use `+ - * /`) |
| `np.power(a, b)` | Elementwise power |
| `np.mod(a, b)` | Elementwise modulo |
| `np.sqrt(arr)` | Square root |
| `np.exp(arr)` | Exponential |
| `np.log(arr)`, `np.log2`, `np.log10` | Logarithms |
| `np.abs(arr)` | Absolute value |
| `np.round(arr, n)` | Round to n decimals |
| `np.floor(arr)`, `np.ceil(arr)` | Floor/ceil |
| `np.clip(arr, lo, hi)` | Clip values to range |
| `np.cumsum(arr)` | Cumulative sum |
| `np.cumprod(arr)` | Cumulative product |
| `np.diff(arr)` | Discrete difference between consecutive elements |

## Aggregations
| Function | Description |
|---|---|
| `np.sum(arr, axis=None)` | Sum |
| `np.mean(arr)` | Mean |
| `np.median(arr)` | Median |
| `np.std(arr)` | Standard deviation |
| `np.var(arr)` | Variance |
| `np.min(arr)`, `np.max(arr)` | Min/max |
| `np.argmin(arr)`, `np.argmax(arr)` | Index of min/max |
| `np.percentile(arr, q)` | q-th percentile |
| `np.prod(arr)` | Product of all elements |
| `np.count_nonzero(arr)` | Count non-zero elements |
| `np.unique(arr)` | Sorted unique elements |
| `np.unique(arr, return_counts=True)` | Unique elements + their counts |

## Sorting & Searching
| Function | Description |
|---|---|
| `np.sort(arr)` | Return sorted copy |
| `arr.sort()` | Sort in place |
| `np.argsort(arr)` | Indices that would sort array |
| `np.searchsorted(arr, val)` | Index to insert val in sorted array (binary search) |
| `np.nonzero(arr)` | Indices of non-zero elements |
| `np.flatnonzero(arr)` | Flattened indices of non-zero elements |

## Linear Algebra (`np.linalg`)
| Function | Description |
|---|---|
| `np.dot(a, b)` / `a @ b` | Matrix/dot product |
| `np.linalg.inv(a)` | Matrix inverse |
| `np.linalg.det(a)` | Determinant |
| `np.linalg.eig(a)` | Eigenvalues and eigenvectors |
| `np.linalg.norm(a)` | Vector/matrix norm |
| `np.linalg.solve(a, b)` | Solve linear system `ax = b` |
| `np.matmul(a, b)` | Matrix multiplication |
| `np.trace(a)` | Sum of diagonal elements |

## Random (`np.random`)
| Function | Description |
|---|---|
| `np.random.rand(r, c)` | Uniform random [0,1) |
| `np.random.randn(r, c)` | Standard normal distribution |
| `np.random.randint(low, high, size)` | Random integers |
| `np.random.choice(arr, size)` | Random sample from array |
| `np.random.shuffle(arr)` | Shuffle in place |
| `np.random.seed(n)` | Set seed for reproducibility |
| `np.random.permutation(arr)` | Return shuffled copy |

## Logical / Comparison
| Function | Description |
|---|---|
| `np.all(arr)` | True if all elements truthy |
| `np.any(arr)` | True if any element truthy |
| `np.array_equal(a, b)` | Check if arrays equal |
| `np.isnan(arr)` | Boolean mask of NaNs |
| `np.isinf(arr)` | Boolean mask of infinities |
| `np.logical_and/or/not(a, b)` | Elementwise logical ops |

## Useful Constants & Misc
| Item | Description |
|---|---|
| `np.nan` | Not-a-number |
| `np.inf` | Infinity |
| `np.pi`, `np.e` | Math constants |
| `arr.astype(np.int32)` | Cast dtype |
| `np.set_printoptions(precision=3)` | Control print formatting |

## Quick Example
```python
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)          # (2, 3)
print(a.sum(axis=0))    # column-wise sum -> [5 7 9]
print(a.sum(axis=1))    # row-wise sum -> [6 15]

b = np.arange(1, 10).reshape(3, 3)
print(np.linalg.det(b))

mask = a > 3
print(a[mask])           # [4 5 6]
```
