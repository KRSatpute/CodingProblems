# CodingProblems
Various coding problems and solutions


Problem 1:
Given a root node of a binary tree, write a function that converts the binary tree to a tree where each node is the sum of all its children. For example, if the original tree is:

      8
    /   \
  -2     4
 / \    / \
5   1  2  -7

The new tree would be:

	     3 (5+1-2+2-7+4)
	   /   \
(5+1) 6     -5 (2-7)
	 / \    / \
	0   0  0   0
  


Problem 2:
In software engineering, two common shorthand abbreviations that people often use are "a11y" to represent "accessibility" and "i18n" to represent "internationalization". The numnbers in the shorthand simply represent a number of letters ("accessibility" is "a" then 11 letters then "y"). 

You can imagine this being extrapolated into a generic text matching system, where a number in a pattern represents that number of letters in a string. For example, the string "technology" would be matched by all of the following patterns:

- t8y (t-echnolog-y)
- t9 (t-echnology)
- 9y (technolog-y)
- tech2logy (tech-no-logy)
- 8g1 (technolo-g-y)
- te2n4y (te-ch-n-olog-y)
 
 and many others! Note that these patterns match many other strings as well. However, the word "technology" would not be matched by the pattern t9y, for example, because "technology" has 10 letters and "t9y" would only match 11-letter strings that start with "t" and end with "y".

 Please write a function that takes two strings as parameters, one string like "technology" and one pattern like "t8y", and returns a boolean indicating whether the given pattern matches the given string.
