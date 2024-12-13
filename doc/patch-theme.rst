How I make use of pelican themes.
=================================

Tinkering with themes is best done in a cloned local version of the
collection.

I like to start from a cloned copy of the collection, add any tweaks I
need, and then make a patch file that can re-apply my changes from the
original collection.

It is the patch file that I preserve for posterity in my project repository.


Installing the setup I use for tweaking and making patches.
-----------------------------------------------------------
I chose to clone into my home directory

.. code-block:: bash
		
    pushd ${HOME} >/dev/null
    
    # Local clone we are going to tweak
    git clone --recursive https://github.com/getpelican/pelican-themes

    # Locan pristine original we will use for diffs.
    cp -r ${HOME}/pelican-themes ${HOME}/pelican-themes.orig

    # Protect pristine version from unnoticed inadvertent changes.
    chmod -w --recursive ${HOME}/pelican-themes.orig/
    popd >/dev/null

		
Reminder:  Although I have not had occasion to use it yet, one can also clone theme plugins like this:

.. code-block:: bash
		
    git clone --recursive https://github.com/getpelican/pelican-plugins


Day to Day theme tweaks
-----------------------

Make changes to the contents of ${HOME}/pelican-themes as and when required.
When you do, regenerate the project patch file to include your changes.

generate/regenerate patch file:

.. code-block:: bash
   
   cd ${HOME}/pelican-themes
   diff --exclude=index -Naru --exclude='*.ttf' ../pelican-themes.orig . > {HOME}/allrepos/mathsansmystere/themes.patch

Note:

  | -N --new-file treat absent files as empty
  | -a --text treat all files as text
  | -r --recursive recursively compare subdirectories
  | -u -U --unified[=NUM] Output NUM lines of unified context (default 3)
  |
  | The exclude=index is to avoid a .git/index file that yield illegible noidr
  
  

**Undo Changes**

.. code-block:: bash
		
   cd ${HOME}/pelican-themes
   patch -Rs -p0 < {HOME}/allrepos/mathsansmystere/themes.patch

Note:
  
  | Remember that directories created by patch must be removed manually
  | -R  --reverse  Assume the patch was created with old and new files swapped
  | -s  --silent  be quiet unless error occurs
  | -pN Strip smallest filepath prefix containing N slashes. 0 means full path.

**Apply Patch Changes**
  
.. code-block:: bash
		
   cd ${HOME}/pelican-themes
   patch -s -p0 < {HOME}/allrepos/mathsansmystere/themes.patch


