
# SinglePremium

A demo project for single premium calculation

## Setup
1. Install git and checkout the [git code repository]
2. Install python version 3.7 [python]. Remember to check of "add Python to path".
3. Install virtualenv by 

    `python -m pip install -U virtualenv`

5. Change working directory into the git code repository root
6. Create a virutal environment. In a terminal go to the git code repository root and enter the command:

   `python -m venv venv\SinglePremium`

    and install required packages by 

    `.\venv\SinglePremium\Scripts\activate`
    `python -m pip install -r requirments.txt`

7. Any python modules under src need to be available to other scripts. This can be done in a couple of ways. You can 
setup and install the python modules by executing the setup.py command below which will install the packages to the 
conda environments site-packages folder but with a symlink to the src folder so modifications are reflected immediately. 

   `python setup.py develop`
   
    As an alternative you may prefer to set the python path directly from the console, within notebooks, test scripts 
    etc. From Pycharm you can also right click the src folder and select the _Mark Directory As | Source Root_ option.

8. .. Place your own project specific setup steps here e.g. copying data files ...

When distributing your module, you can create a Python egg with the command `python setup.py bdist_egg` and upload the egg.



## Initial File Structure

```
├── .gitignore               <- Files that should be ignored by git. Add seperate .gitignore files in sub folders if 
│                               needed
├── conda_env.yml            <- Conda environment definition for ensuring consistent setup across environments
├── README.md                <- The top-level README for developers using this project.
├── requirements.txt         <- The requirements file for reproducing the analysis environment, e.g.
│                               generated with `pip freeze > requirements.txt`. Might not be needed if using conda.
├── setup.py                 <- Metadata about your project for easy distribution.
│
├── data
│   ├── processed            <- The final, canonical data sets for modeling.
│   └── raw                  <- The original, immutable data dump.
│
├── docs                     <- Documentation
│   ├── data_science_code_of_conduct.md  <- Code of conduct.
│   ├── process_documentation.md         <- Standard template for documenting process and decisions.
│   └── writeup              <- Sphinx project for project writeup including auto generated API.
│      ├── conf.py           <- Sphinx configurtation file.
│      ├── index.rst         <- Start page.
│      ├── make.bat          <- For generating documentation (Windows)
│      └── Makefikle         <- For generating documentation (make)
││
├── notebooks                <- Notebooks for analysis and testing
│   ├── eda                  <- Notebooks for EDA
│   │   └── example.ipynb    <- Example python notebook
│   ├── features             <- Notebooks for generating and analysing features (1 per feature)
│   ├── modelling            <- Notebooks for modelling
│   └── preprocessing        <- Notebooks for Preprocessing 
│
├── scripts                  <- Standalone scripts
│   ├── data                 <- scripts for data preping. Going from raw to processed
│   │   └── score.py         <- Scoring script
│   └── example.py           <- Example sctipt
│
├── src                      <- Code for use in this project.
│   └── singlepremium       <- Example python package - place shared code in such a package
│       ├── __init__.py      <- Python package initialisation
│       ├── examplemodule.py <- Example module with functions and naming / commenting best practices
│       ├── features.py      <- Feature engineering functionality
│       ├── io.py            <- IO functionality
│       └── pipeline.py      <- Pipeline functionality
│
└── tests                    <- Test cases (named after module)
    ├── test_notebook.py     <- Example testing that Jupyter notebooks run without errors
    └── singlepremium       <- singlepremium tests
        ├── examplemodule    <- examplemodule tests (1 file per method tested)
        ├── features         <- features tests
        ├── io               <- io tests
        └── pipeline         <- pipeline tests
```

## Testing
Reproducability and the correct functioning of code are essential to avoid wasted time. If a code block is copied more 
than once then it should be placed into a common script / module under src and unit tests added. The same applies for 
any other non trivial code to ensure the correct functioning.

To run tests, install pytest using pip or conda (should have been setup already if you used the conda_env.yml file) and 
then from the repository root run
 
```
pytest
```

## Automated Document Generation
A [sphinx](https://www.sphinx-doc.org/) project is provided under docs/writeup that will generate writeup that
also includes automatically generated API information for any packages. The output can be created in multiple
formats including html and pdf. When master is pushed to gitlab, this process can happen automatically and be published at https://pages.gitlab.kpmg.no/singlepremium. To run locally execute the following commands:
 
```
cd docs/writeup
make html
```

On Windows this will run the make.bat, a Makefile is also included for those using the 'make' command.


## Development Process
Contributions to this template are greatly appreciated and encouraged.

To contribute an update simply:
* Create a new branch / fork for your updates.
* Check that your code follows the PEP8 guidelines (line lengths up to 120 are ok) and other general conventions within this document.
* Ensure that as far as possible there are unit tests covering the functionality of any new code.
* Check that all existing unit tests still pass.
* Edit this document if needed to describe new files or other important information.
* Create a pull request.

## Important Links
* https://drivendata.github.io/cookiecutter-data-science/ - Why use this project structure?
* https://notebooks.azure.com/ - Managed Python/R Environment
* https://gitlab.kpmg.no/ - Git version control in KPMG
* https://github.com/drivendata/data-science-is-software - Nice video and code for why project structure, version control and documentation is important


## References
* 

[//]: #
   [python]: <https://www.python.org/downloads/>
