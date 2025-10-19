Some Example RST Math Mark Up
=============================

:lang: en
:date: 2024-12-08 06:02:51+00:00
:tags: math markup, examples
:slug: mathmarkup
:category: Examples
:authors: Pierre Bernatchez
:summary: Examples of math mark up

.. |copy| unicode:: 0xA9 .. copyright sign
		    
.. |---| unicode:: U+02014 .. em dash
   :trim:

To markup math expressions in restructuredtext there are two ways to mark things up.
One, display style,  where each expression is emitted alone centered on a line [1]_.

The other, inline style, where the expression is emitted embedded in the surrounding text.

Simple subscripts and superscripts
----------------------------------

^ for superscript, _ for subscript

When the item is more than a single character use: ^{xx}, _{yy}


Quadratic Expression

*Displayed Markup*

.. code-block:: rst
		
   .. math::
      
      (a + b)^2 = (a + b)(a + b)
	  
      (a + b)(a + b) = a^2 + 2ab + b^2

*Result*

.. math::

   (a + b)^2 = (a + b)(a + b)
	  
   (a + b)(a + b) = a^2 + 2ab + b^2

*In line markup*

.. code-block:: rst

   :math:`(a + b)^2 = (a + b)(a + b)`
	  
   :math:`(a + b)(a + b) = a^2 + 2ab + b^2`

*Result*
	  
:math:`(a + b)^2 = (a + b)(a + b)`
      
:math:`(a + b)(a + b) = a^2 + 2ab + b^2`

   
Multiple Equations aligned at '\&' and separated at '\\'.
---------------------------------------------------------

*Display Markup*

.. code-block:: rst
		
   .. math::
      
      (a + b)^2 &= (a + b)(a + b) \\ &=  a^2 + 2ab + b^2
      
*Result*

.. math::

   (a + b)^2 &= (a + b)(a + b) \\ &=  a^2 + 2ab + b^2
   

*Inline Markup*

.. code-block:: rst
		
   :math:`(a + b)^2 &= (a + b)(a + b) \\ &=  a^2 + 2ab + b^2`
	  
*Result*

:math:`(a + b)^2 &= (a + b)(a + b) \\ &=  a^2 + 2ab + b^2`


Labels
------


This requires a sphinx extension, so we cannot illustrate the result
here.

*Markup*

.. code-block:: rst
   
   .. math:: e^{i\pi} + 1 = 0
      :label: euler

   Euler's identity, equation :eq:`euler`, was elected one of the most
   beautiful mathematical formulas.


Domain Symbols
--------------

*Display Markup*

Note how we escape a space character with \\ to retain a space character before the symbol.

.. code-block:: rst

   -
      .. math:: REAl\ \mathbb{R}

   -
      .. math:: INTEGER\ \mathbb{Z}

   -
      .. math:: NATURAL\ \mathbb{N}

   -
      .. math:: RATIONAL\ \mathbb{Q}

   -
      .. math:: IRRATIONAL\ \mathbb{P}

*Result*

-
   .. math:: REAl\ \mathbb{R}

-
   .. math:: INTEGER\ \mathbb{Z}

-
   .. math:: NATURAL\ \mathbb{N}

-
   .. math:: RATIONAL \mathbb{Q}

-
   .. math:: IRRATIONAL\ \mathbb{P}


*Inline Markup*

.. code-block:: rst
		
   - REAl :math:`\mathbb{R}`
   - INTEGER :math:`\mathbb{Z}`
   - NATURAL :math:`\mathbb{N}`
   - RATIONAL :math:`\mathbb{Q}`
   - IRRATIONAL :math:`\mathbb{P}`

*Result*

- REAl :math:`\mathbb{R}`
- INTEGER :math:`\mathbb{Z}`
- NATURAL :math:`\mathbb{N}`
- RATIONAL :math:`\mathbb{Q}`
- IRRATIONAL :math:`\mathbb{P}`

*Display Markeup*

.. code-block:: rst

   Euler's identity equation was elected one
   of the most beautiful mathematical formulas.

   .. math:: e^{i\pi} + 1 = 0   
      
*result*

Euler's identity equation was elected one
of the most beautiful mathematical formulas.

.. math:: e^{i\pi} + 1 = 0   

*Inline Markup*

.. code-block:: rst

   Euler's identity equation, :math:`e^{i\pi} + 1 = 0`, was elected one
   of the most beautiful mathematical formulas.
		
*result*

Euler's identity equation, :math:`e^{i\pi} + 1 = 0`, was elected one
of the most beautiful mathematical formulas.

*Display Markup*

.. code-block:: rst
		
   Since Pythagoras, we know that:
   
   .. math::
      a^2 + b^2 = c^2

*result*

Since Pythagoras, we know that:

.. math::
   a^2 + b^2 = c^2


*Inline Markup*

.. code-block:: rst
   
   Since Pythagoras, we know that: :math:`a^2 + b^2 = c^2`.

*Result*

Since Pythagoras, we know that: :math:`a^2 + b^2 = c^2`.
	      
*Display Markup*

.. code-block:: rst

   A mole of a substance is defined as the number of molecules of that
   substance it takes to make up its atomic weight in grams - That
   number is known as Avogadro's number.  It is constant for all
   molecules: approximately

   .. math::
      6.0221409e^{23}

*Result*

A mole of a substance is defined as the number of molecules of that
substance it takes to make up its atomic weight in grams - That
number is known as Avogadro's number.  It is constant for all
molecules: approximately

.. math::
   6.0221409e^{23}


*Inline Markup*

.. code-block:: rst

   A mole of a substance is defined as the number of molecules of that
   substance it takes to make up its atomic weight in grams - That
   number is known as Avogadro's number.  It is constant for all
   molecules: approximately :math:`6.0221409e^{23}`
   

*Result*

A mole of a substance is defined as the number of molecules of that
substance it takes to make up its atomic weight in grams - That
number is known as Avogadro's number.  It is constant for all
molecules: approximately :math:`6.0221409e^{23}`


.. [1] Our conversion from rst to html and to pdf in this project tends to drop the ball somewhat on centering displayed math text in output lines.



