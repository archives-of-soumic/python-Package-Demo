# package_demo
This is how you create a simple python package:
```
project
|
|__ setup.py
|
|__ myPackage
     |
     |_  somePython.py
     |_  __init__.py
```

And the setup file should be like this:
```
from setuptools import setup

setup(
    # Whatever arguments you need/want
)

```

## INSTALLATION 
1. ```$ virtualenv env```
2. ```$ source env/bin/activate``` 
3. ```$ pip install  git+https://github.com/fahimfarhan/package_demo.git``` 

Or you can create a `requirements.txt` file and add this as requirements:
 ```
 git+https://github.com/fahimfarhan/package_demo.git
 ```
 and then: 
 ```
    $ pip install -r requirements.txt --upgrade
 ```

## USAGE
```$touch start.py``` and then add this code segment in it:

```
from measure import metrics, norms

if __name__ == "__main__":
    
    metrics.metric(1)
    norms.norms()
    pass

```

## References
https://uoftcoders.github.io/studyGroup/lessons/python/packages/lesson/