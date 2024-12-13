Some Example Restructuredtext Math Mark Up
==========================================

:lang: en
:date: 2024-12-08 06:02:51+00:00
:tags: math markup, examples
:slug: mathmarkup
:category: Exemples
:authors: Pierre Bernatchez
:summary: Exemples

.. |copy| unicode:: 0xA9 .. copyright sign
		    
.. |---| unicode:: U+02014 .. em dash
   :trim:


To markup math expressions in restructuredtext there are two ways to mark things up.
One, display style,  where each expression is emitted alone centered on a line.
The other, inline style, where the expression is emitted embedded in the surrounding text.
We  will illustrate both types starting with display style.

Simple subscripts and superscripts
----------------------------------



Multiple Equations aligned at '&' and separated at '\\'
^ superscript
_ subscript

When the superscript or subscript is more than a single character
use
^{xx}
_{yy}

**Displayed Math**

Quadratic Expression

*Markup*

::

   .. math::
   
       (a + b)^2  &=  (a + b)(a + b) \\
                  &=  a^2 + 2ab + b^2

*Result*

.. math::

   (a + b)^2  &=  (a + b)(a + b) \\
              &=  a^2 + 2ab + b^2

Avogadro's Number
	      
*Markup*

::

   .. math::

      6.0221409e^{23}

*Result*

.. math::

   6.0221409e^{23}


**Inline Math**


*Markup*

::
   
   Since Pythagoras, we know that: :math:`a^2 + b^2 = c^2`.

*Result*

   Since Pythagoras, we know that: :math:`a^2 + b^2 = c^2`.
	      
*Markup*

::

   Avogadro came up with this number: :math:`6.0221409e^{23}`
   

*Result*

   Avogadro came up with this number: :math:`6.0221409e^{23}`


**Labels**

*Markup*

:: 
   
   .. math:: e^{i\pi} + 1 = 0
      :label: euler

      Euler's identity, equation :eq:`euler`, was elected one of the most
      beautiful mathematical formulas.


*Result*

  Currently this gets rejected because the :label: attribute is not supported.
  I think that is a sphinx extension.


Euler's identity, equation \:eq\:`euler`, was elected one of the most
beautiful mathematical formulas.


Euler's identity equation, :math:`e^{i\pi} + 1 = 0`, was elected one
of the most beautiful mathematical formulas.


Euler's identity equation was elected one of the most beautiful
mathematical formulas.

.. math::

   e^{i\pi} + 1 = 0
      

Domain Symbols
--------------

.. code-block:: rst
		
   REAl :math:`\mathbb{R}`
	 
   INTEGER :math:`\mathbb{Z}`

   NATURAL :math:`\mathbb{N}`
	 
   RATIONAL :math:`\mathbb{Q}`

   IRRATIONAL :math:`\mathbb{P}`

Result:

   REAl :math:`\mathbb{R}`
	 
   INTEGER :math:`\mathbb{Z}`

   NATURAL :math:`\mathbb{N}`
	 
   RATIONAL :math:`\mathbb{Q}`

   IRRATIONAL :math:`\mathbb{P}`
      



