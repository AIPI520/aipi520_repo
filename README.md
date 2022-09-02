# Modeling Process and Algorithms (AIPI 520) Course Repo
Welcome to the GitHub repo for AIPI 520: Modeling Process and Algorithms at Duke University.  This repo accompanies the course, which is part of [Duke's AI Master of Engineering program](http://ai.meng.duke.edu) and is taught by [Jon Reifschneider](https://ai.meng.duke.edu/faculty/jon-reifschneider).  This course is designed as an introduction to the process of building machine learning models and a tour of the main ML algorithms in use today, including both their theoretical underpinnings and their practical implementation.  The focus of the course is on the classical ML techniques although two weeks are dedicated to deep learning.

This repo contains code notebooks with code examples which accompany the course as well as in-class exercises which we will complete during the scheduled lecture sessions.  Assignments will be distributed separately via Sakai and GitHub Classroom.

## Weekly Schedule
Our course will follow the below schedule: 
- Week 1: Introduction to machine learning  
- Week 2: Modeling process, splitting data, cross-validation  
- Week 3: Evaluating model performance  
- Week 4: Linear regression  
- Week 5: Regularization  
- Week 6: Logistic regression  
- Week 7: Support vector machines and KNN classification  
- Week 8: Artificial neurons and neural networks  
- Week 10: Neural networks continued  
- Week 11: Tree models and ensembling  
- Week 12: Boosting ensembles
- Week 13: Clustering

## Best Practices
In this course we will be doing a lot of Python programming.  In order to help yourself avoid making errors and also make your code easier to read by others, pay attention to styling.  Here are a few of what I consider to be the most important practices to ensure you are writing clean, professional code:  
- **Write straightforward, explicit code where possible.**  There are often many different ways to write the same function in Python.  Whenever possible, try to write in the simplest, most obvious way rather than more complex, less obvious ways.  This helps others easily understand what you are doing.
- **Use descriptive variable names.** Rather than calling something `var1`, try to name it something more descriptive e.g. `education_level`.  This helps you remember what information each variable contains when you come back later to review your code, and also makes it much easier for others to understand what your code is doing.  
- **Add lots of comments.** Generally, the more the better.  At a minimum you should have a comment for every function.  Preferably one that is written in the form of a docstring containing a brief description of what the function does and then a list of inputs and returns.  Comments help you remember later what your code does and make it much easier for others to follow the code you have written.  
- **Use sufficient white space.** Add a space between every operator in your code, and separate chunks within functions with empty lines to break long chunks of code up visually.  
- **Use unit tests to catch errors.** Make liberal use of unit tests (e.g. `assert len(a) == 50`).  Unit tests help check your code as you write to ensure that things are running as you expect them to.  Unit tests can also be used with NumPy arrays and pandas DataFrames, e.g. `assert pd.notnull(employees["salary"].all()`)

Please review [this guide](https://docs.python-guide.org/writing/style/) for important tips on writing good Python.  The formal style guide for Python is called PEP-8, and [this site](https://pep8.org) does a good job presenting the most important ideas clearly.