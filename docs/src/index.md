```
   _ \   \   __| __|__ __| __|
   |  | _ \ (    _|    | \__ \
  ___/_/  _\___|___|  _| ____/
```

Dacets is a tool for scientists (pros and amateurs) to facilitate handling and
tracking of research data files, associated experimental metadata and random
notes: where the files came from, where they are stored, what's inside, to which
project they belong, etc. It should be useful for individual use as well as for
collaborations.


# Quick start

## Installation

```
$ pip install dacets
$ dct -h
```

## Basic use

From shell

```
$ dct list
$ dct search lena
```

From python
```
from dacets import Dacets

dct = Dacets()
dct.list()
dct.search('lena')
```
