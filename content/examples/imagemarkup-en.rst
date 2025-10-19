Examples Positioning Images
===========================

:lang: en
:date: 2024-12-24 20:38:45+00:00
:tags: image markup, examples
:slug: imagemarkup
:category: Examples
:authors: Pierre Bernatchez
:summary: Examples

.. |copy| unicode:: 0xA9 .. copyright sign
		    
.. |---| unicode:: U+02014 .. em dash
   :trim:

   
Avoid overlapping image and text
--------------------------------

I have had issues with text and image cotent overlapping.

Two images side by side

.. code-block:: reStructuredText

   .. |ogopogo| image:: images/ogopogo.jpg
      :alt: ogopogo stamp	   


   .. |vingtdeux| image:: images/vingtdeux.jpg
      :alt: vingtdeux banner


   |ogopogo| <> |vingtdeux|

End of code block

**result**


.. |ogopogo| image:: images/ogopogo.jpg
   :width: 45%
   :alt: ogopogo stamp	   


.. |vingtdeux| image:: images/vingtdeux.jpg
   :width: 45%
   :alt: vingtdeux banner


|ogopogo| <> |vingtdeux|

New example
	   

Image with text above and below it

.. code-block:: reStructuredText

   .. |ogopogo100| image:: images/ogopogo.jpg
      :width: 100%
      :alt: ogopogo stamp	   

   Line above it.
   
   |ogopogo100|
   
   Line below it.
	     
**result**

.. |ogopogo100| image:: images/ogopogo.jpg
    :width: 100%
    :alt: ogopogo stamp	   

Line above it.

|ogopogo100|

Line below it.
	     
	   
