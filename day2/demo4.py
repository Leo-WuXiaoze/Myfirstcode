import numpy
import pandas

ss = pandas.Series(data=[1, 2, 3], index=list('abc'), dtype=numpy.float16, name='test')
print('-' * 100)
print(ss, type(ss))
print('-' * 100)
print(ss.index, ss.values, type(ss.values))

print('-' * 100)
df = pandas.DataFrame(data=numpy.arange(12).reshape(3, 4),
                      index=list('abc'), columns=list('xyzw'),
                      dtype=numpy.float16)
print(df, type(df))
print(df.index, df.columns)
print(df.values, type(df.values))
