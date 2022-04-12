python virtual environment setup
================================

To have a good control over pre-requisite library modules
for our software, we run in a python virtual environment.

That means that whenever you want to use the software
you must first invoke that virtual environment like this:

::
   
    source ${HOME}/mathsansmystere_venv/bin/activate

Below we describe how to set up a project virtual environment.

First we create a virtual  environment and make it our current one..


Install non pip packages we are going to rely on.

.. code-block:: bash
		
    sudo apt install rst2pdf               # For  generating mathsansmystere's own  documentation
    sudo apt-get install texlive-latex-bas # For pdflatex (used to convert latex to pdf)
    sudo apt install texlive-lang-french texlive-lang-spanish # for french and spanish babel languages
    sudo apt install s3cmd                 # publishing to S3 bucket


Set up credentials for accessing S3 bucket where docs will be published.

.. code-block:: bash

    s3cmd --configure


You will be prompted for responses to a series of questions.
Respond with <enter> or yes (whichever is appropriate) for all responses
except the ones below.

::

    Access Key: your access key beginning with AKIA
    Secret Key: the secret key for the above access key
    Default Region: US
    Encryption password: The encryption key we (may) use to encypt/decrypt uploading/downloading


Set up the virtual python environement we want.

.. code-block:: bash


    deactivate     # Omit this unless you are alread in a different virtual environement
    cd ${HOME}
    sudo apt install python3.8-venv  # This is required on ubuntu systems in order for the next command to work
    python3.8 -m venv mathsansmystere_venv  # >= python3.8 otherwise latexhelper wont install     
    source mathsansmystere_venv/bin/activate

We install the pip bare essentials.

.. code-block:: bash
    
    python -m pip install -U pip
    pip install --no-cache-dir wheel
    pip install --no-cache-dir setuptools_rust
    pip install --no-cache-dir twine

We install our latex generator tool into our virtual environment.

.. code-block:: bash
    
    pip uninstall  latexhelper

    pip install --no-cache-dir markdown  # latexhelper needs this

    pip install --no-cache-dir  -i https://mathsansmystere.bernatchez.net:3141/pbernatchez/dev latexhelper
    
    # OR until our private packege index is securely accessible via SSL

    pip install --no-cache-dir --trusted-host mathsansmystere.bernatchez.net -i http://mathsansmystere.bernatchez.net:3141/pbernatchez/dev latexhelper
    
   
