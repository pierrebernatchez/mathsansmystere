Math Sans Mystere Server Configuration
======================================

We maintain a server to encourage teachers to take advantage of our collection.

The server plays two roles.

    - It generates exercise documents on behalf of teachers.
    - It acts as a collector of new question and answer candidate images uploaded for conversion to latex and addition to the repository.
      
This server generates exercise documents on behalf of teachers as follows:

    A teacher submits a list of question numbers via a web form.  The
    server compiles the latex file for the exercise, generates a .pdf
    document from that and returns an HTTP link for the result.

This server pools uploaded question images:

    Those images are converted to latex question snippets and added to
    our repository and then removed from the pool by volunteers.
    
    In order for someone to contribute a question to the repository
    they only need to make up a question and the answer to go with it
    on separate sheets of paper, scan (or snapshot) each and upload
    the pair to the collector.  From these images one of our
    volunteers will restate them as latex snippets, add those to the
    collection and render a proof for the teacher to review.


The purpose of the server is to accomplish that activity.

In order to accomplish that we need to 'git clone' the math sans
mystere question repository onto our server instance.  We also need to
install the python latexhelper tool which does the work of combining
question snippets into exercise document.

With those two elements we can accomplish our role.

The workflow of the server, once it has been initialized, is to
regularly pull newly contributed questions out of the git
repository, re-publish our full list document and continue to supply
exercise rendering service.


At this writing, the latexhelper tool has not yet been made public in
the python package index, so this prototype server doubles as the the
private package index source from which 'latexhelper' can be
installed.  At some future point we can switch to publishing
latexhelper to the public Python Package Index.  At such a time we
can dsipense with the private package index role as it will no longer
be required.
