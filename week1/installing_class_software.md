# AIPI 510 - Setup

In this course we will be completing programming assignments using Python and several libraries which are commonly used by data scientists and machine learning engineers in industry. Mastery of these tools will set you up well to be prepared for a future role in an industry team. While you may chose to use a cloud service for your course project, all demos and assignments are also designed to be able to be run locally on your laptop.  

In this course we will be using GitHub for the distribution and collection of assignments.  First, follow the steps below to get git/GitHub set up:
- If you do not already have a GitHub account, create one at github.com  
- Install git on your laptop and authenticate with GitHub from git - follow the [instructions](https://docs.github.com/en/github/getting-started-with-github/set-up-git)
- Get familiar with using git and GitHub: walk through the [tutorial](https://opensource.com/article/18/1/step-step-guide-git)

The assignments and demo code for this course are in the form of [jupyter notebooks](https://jupyter-notebook.readthedocs.io/en/stable/).  To work on them, let's first get your work environment set up for data science programming.  To do so, you will need Python and several other libraries installed.  You have two options for setting up a work environment: 
1) Work locally on your laptop, or  
2) Use Google Colab to work in the cloud (free).

Follow the instructions below for either path to get set up for work.  Whether to work locally or work in the cloud is a matter of personal preference.  I personally like to work locally when I can, although if the setup instructions below appear complicated you may find it easier to work on Colab.

# Option 1: Work locally on your laptop

## Installing Anaconda and Python

- It is recommended to first install [Anaconda](https://docs.anaconda.com/anaconda/) and use the conda package manager to install needed packages:  
    - [Install Anaconda](https://docs.anaconda.com/anaconda/install/).  This should automatically install the latest version of Python on your computer.  For this course you should have Python 3.7 or greater
    - Now, read the [getting started guide](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html) to learn how to work with conda
    
## Installing needed packages
Install the needed packages for this course (these may already be installed with your default installation of Anaconda, but best to check not assume).  You may create a new conda environment (see getting started guide link above for instructions) or just use the base environment to install them.  See getting started guide above for how to install packages.  While you can use the Anaconda Navigator application that comes with the Anaconda download, I recommend you familiarize yourself with installing from the command line.  To install the packages, execute the following for each package at the command line on your laptop.
- jupyter notebooks: `conda install -c conda-forge notebook` 
- pandas (will also install numpy): `conda install -c anaconda pandas`  
- matplotlib: `conda install -c anaconda matplotlib` 
- scikit-learn: `conda install -c anaconda scikit-learn` 
- BeautifulSoup: `conda install -c anaconda beautifulsoup4`

## Clone the course demos repo to your computer
The demo notebooks for this course are saved in a [GitHub directory](https://github.com/AIPI520/aipi520_repo).  To download them to your computer, you can clone them from GitHub by doing the following:  
- Use the command line to navigate to the folder on your computer where you would like to store them
- Run the following to clone the *demo_notebooks* repository to your computer: `git clone https://github.com/AIPI520/aipi520_repo.git`


## Open a development environment and start work
Now that you have the necessary packages installed and have cloned the source material onto your computer you are ready to start work.  If you are working locally on your computer, you can choose which development environment you would like to use.  There are several options, but I recommend using either Jupyter Notebooks (which is a notebook editor that runs in the browser) or Microsoft's VSCode (a free IDE that has good support for notebooks).

To use Jupyter Notebooks:
- At the command line, type `jupyter notebook`
- The jupyter screen will automatically open in your browser at *localhost:8888/*  
- Navigate to the folder on your laptop where you wish to create and save your notebook and click at top right *New -> Notebook (Python 3)* to open a new notebook.  Then click *File -> Rename* to give it a name.
- Or, if you are opening an assignment template notebook you have cloned from GitHub (see assignment_instructions document), navigate to the local folder and open the notebook
- Notebooks should auto-save, but be sure to manually save when done.  To exit out of jupyter notebooks, close the windows in your browser, and hit `ctrl-c` from your command line.

To use VSCode:
- [Download VSCode](https://code.visualstudio.com) for free 
- Open VSCode and then select File -> Open and open a notebook (.ipynb) file
- Be sure to manually save your work periodically

# Option 2: Work in the cloud using Google Colab
Google Colaboratory is a free, cloud-based platform for creating and running code notebook files. The advantages of using Colab relative to your own laptop are that it requires no configuration (all needed libraries should already be pre-installed) and you get free access to GPUs to accelerate model training. Colab also integrates directly with GitHub so you can load notebooks from GitHub directly into Colab to edit and then push them back to GitHub when done.

If you would like to work using Colab, start by watching the [introductory video](https://www.youtube.com/watch?v=inN8seMm7UI).  Then, go through the following introduction notebooks to familiarize yourself with working in Colab.  You will need a free Google account to use Colab, so create one if you do not already have one.
- [Welcome to Colaboratory](https://colab.research.google.com/notebooks/intro.ipynb?utm_source=scs-index#scrollTo=5fCEDCU_qrC0)  
- [Installing libraries not in Colab](https://colab.research.google.com/notebooks/snippets/importing_libraries.ipynb)  
- [Using Colab with GitHub](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb)

## Open a notebook in Colab and begin work!
Open a new notebook, or load a demo notebook or assignment notebook from GitHub to begin work.  When you are done, you can save your work either in your Google Drive by selecting `File -> Save a copy in Drive` or to GitHub by selecting `File -> Save a copy to GitHub`


