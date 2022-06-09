Math Exercise Document Repository
=================================

Overview
--------

We are building this repository with the immediate goal of supplying
materials for students preparing for a specific International
Baccalaureate test.

We want to leverage this effort as a pilot project for a more general
collection of math teaching materials that can be used easily and
effectively by teachers with a minimum of complications.

Currently Latex is the most used mark up language for anyone producing
mathematics documents.  To comply with that trend and maximize the
usefulness of the learning curve of maintaining the materials herein
we are using latex as our markup language for this project.

How our source files are organized.
-----------------------------------

Our exercise documents are generated .tex files which can then be compiled into .pdf documents.
They are made up of some predetermined latex preamble, some configurable
title and author information, and user selected question snippets [#snip]_
taken from our collection of questions.


..  [#snip] Snippets are latex marked up question files named like xNN.tex.  The have no preamble, and as such cannot be compiled alone.  They must be imported into a file that contains apreamble and the begin(document)/end(document) statements.
	    
All our questions are pooled in the following IB related categories [#ibcat]_.

   - algebra_and_numbers
   - calculus
   - functions
   - statistics_and_probability
   - geometry_and_trigonometry

Each pool is a collection of files of the form xNN.tex stored in a subdirectory named after the category.

   - tex/algebra_and_numbers/
     ...

Many of these questions include an acompanying figure or other image.  All such images are stored
in a corresponding image subdirectory.

   - images/algebra_and_numbers/
     ...


..  [#ibcat] Categories correspond to the five areas covered by International Baccalauriate (IB) math courses. 

Intended use.
-------------

Teachers would pick one of the 5 categories and then look through the document that
contains all the questions in the category. She would choose some of the question numbers
from that to make up the list wanted for the exersize.

The exercise document would be generated [#latexhelper]_ from the list, and the teacher
could give the resulting .pdf document to their students.




..  [#latexhelper] the latexhelper package tool 'gen_exercise' combines combines questions from the list with a preamble and configured information such as author into a complete latex document and compiles that document into a pdf document.
		   . 
 

