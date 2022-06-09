python virtual environment setup
================================

To have a good control over pre-requisite library modules
for our software, we run in a python virtual environment.

So we must first create such an environment.

Initial set up of our virtual environment
-----------------------------------------

Make sure we have our pre-requisites installed.

.. code-block:: bash

    snap install rst2pdf                   # For  generating mathsansmystere's own  documentation
    sudo apt-get install texlive-latex-bas # For pdflatex (used to convert latex to pdf)
    sudo apt install texlive-lang-french texlive-lang-spanish # for french and spanish babel languages
    sudo apt install s3cmd                 # publishing to S3 bucket


Set up credentials for accessing S3 bucket where docs will be published.

.. code-block:: bash

    s3cmd --configure -c ${HOME}/s3conf_mathsansmystere

You will be prompted for responses to a series of questions.
Respond with <enter> or yes (whichever is appropriate) for all responses
except the ones below.

::

    Access Key: your access key beginning with AKIA
    Secret Key: the secret key for the above access key
    Default Region: US
    Encryption password: The encryption key we (may) use to encypt/decrypt uploading/downloading


Create a virtual  environment and make it our current one..

.. code-block:: bash

    deactivate                               # Get out of your current virtual environment
    cd ${HOME}
    sudo apt install python3.8-venv          # on ubuntu systems we need this for the next command to work
    python3.8 -m venv mathsansmystere_venv   # >= python3.8 otherwise latexhelper wont install     
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
    
    # Pick one of the two below. Using https is more secure if you can do that.
    pip install --no-cache-dir  -i https://mathsansmystere.bernatchez.net:3141/pbernatchez/dev latexhelper
    # OR
    pip install --no-cache-dir --trusted-host mathsansmystere.bernatchez.net -i http://mathsansmystere.bernatchez.net:3141/pbernatchez/dev latexhelper
    
    
Now each time we want to use our software we must first invoke that
virtual environment.

.. code-block:: bash
   
    source ${HOME}/mathsansmystere_venv/bin/activate


On our instance or workstation we can put the above command in our
login .profile so that it is invoked automatically each time we log
in.  On our instance we appended the following snippet to the
end of .profile.

.. code-block:: bash

    # This is some extra code we can paste to the end of .projile files
    # To automatically activate the virtual python environment for mathsansmystere SW
    # To jump to the cloned git hub mathsansmystere project directory
    # To emit some feedback about what server you just logged into
    #
    
    #
    # Added by for mathsansmystere usage
    #
    if [ -f "${HOME}/mathsansmystere_venv/bin/activate" ] ; then
       source "${HOME}/mathsansmystere_venv/bin/activate"
    fi
    #
    # Added by for mathsansmystere and devpi usage
    #
    if [ -x "/usr/bin/ec2metadata" ] ; then
       MYIP=`/usr/bin/ec2metadata --public-ipv4`
       MYGROUP=`/usr/bin/ec2metadata --security-groups`
       MYUSERDATA=`(/usr/bin/ec2metadata | /usr/bin/grep 'user-data:' | cut -s --delimiter=\' -f 2 - )`
       echo \#############################################################
       echo \# ${MYIP} ':' ${MYUSERDATA} ':' ${MYGROUP}
       echo \#############################################################
    fi
    #
    # Added by for gen_exercise usage
    #
    CLONEDDIR="${HOME}/collab/mathsansmystere"
    if [ -d "${CLONEDDIR}" ] ; then
       cd "${CLONEDDIR}"
    fi
    





