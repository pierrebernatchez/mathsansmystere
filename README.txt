
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

Note regarding organization of the source files in this repository.
===================================================================

Our exercise documents are maintained as .tex files in the base
directory of this repository:

At this writing we currently have these files:
  algebra_and_numbers.tex
  calculus.tex
  functions.tex
  statistics_and_probability.tex
  trig.tex

Each of the above files contains its own latex preamble, and a list of
import statements, one import statement for each question in the
exercise.  They import individual questions from a subdirectory which
contains individual question '.tex' files.

The question files have no preamble, and as such cannot be compiled
alone. They must rather be imported into a file which contains a
preamble and the begin(document)/end(document) statements.

When a question file refers to an image using '\includegraphics' the
location of such an image is given by the '\graphicspath' directive in
the preamble of the file that imports the question.  We have organized
directories for those under the images/ directory. See below.

For your information, template refers to files we keep as a reminder
of the latex source used to compose these questions and exercises.

Question file subdirectories are all under the tex/ subdirectories.
As Follows:
   tex/algebra_and_numbers/
   tex/calculus/
   tex/functions/
   tex/statistics_and_probability/
   tex/template/
   tex/trig/

Image file subdirectories are all under the images/ subdirectory.
As Follows:
  images/algebra_and_numbers/
  images/calculus/
  images/functions/
  images/statistics_and_probability/
  images/template/
  images/trig/


