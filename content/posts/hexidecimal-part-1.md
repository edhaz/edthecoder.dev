title: How hexadecimal helped me understand binary / 1 
slug: hexidecimal-part-1
category: Learning to Code
tags: binary, bitmap, C, hexadecimal, programming
date: 2018-01-07

This week the CS50x course I am working through is teaching (more accurately getting me to learn about) pointers in C, and using images to help understand the concept. I've been looking through bitmap files and getting to grips with how computers make images, something I've always been curious about. Three weeks ago I also looked at binary and how computers use only 1's and 0's to get stuff done. I thought I'd got to grips with it, but looking at hexadecimal, which is used for images, really cemented this understanding.

**What is hexadecimal?**
> **Instead of going up to 10 in each digit you go up to 16.**

In decimal we count, 0, 1, 2, ... 8, 9 and then we have to add another digit to get to 10 (two digits). Whereas in hexadecimal when we get past nine we use the letters a to f (which take up one digit (or bit in a computers perspective)). See this table for a clearer picture of this:

<div class="table-scroll">
<table cellspacing="0">
<colgroup width="85"></colgroup>
<colgroup span="10" width="20"></colgroup>
<colgroup span="6" width="28"></colgroup>
<tbody>
<tr>
<td height="17">Decimal</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>4</td>
<td>5</td>
<td>6</td>
<td>7</td>
<td>8</td>
<td>9</td>
<td>10</td>
<td>11</td>
<td>12</td>
<td>13</td>
<td>14</td>
<td>15</td>
</tr>
<tr>
<td height="17">Hexadecimal</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>4</td>
<td>5</td>
<td>6</td>
<td>7</td>
<td>8</td>
<td>9</td>
<td>A</td>
<td>B</td>
<td>C</td>
<td>D</td>
<td>E</td>
<td>F</td>
</tr>
</tbody>
</table>
</div>
&nbsp;

This means we can write bigger numbers in a shorter number of bits (digits).

`F` in hexadecimal would equal to 15. But what would `FF` equal to? Can you work it out?

In decimal the first digit of 35 is 3, but we know it represents 30 (3 * 10). 10 here is the base (decimal). We then add the next digit to the first (30 + 5 = 35).

In hexadecimal the first digit of `FF` is 15, but it actually represents 240 (15 * 16). 16 here is the base (hexadecimal). We then add the next digit to the first (240 + `F`  = 255). _Remember F = 15_.

Let's clarify this a little with one more example using a table. The number is 345. Here it is in decimal (base 10):

<div class="table-scroll">
<table cellspacing="0">
<colgroup width="85"></colgroup>
<colgroup span="3" width="39"></colgroup>
<colgroup width="85"></colgroup>
<tbody>
<tr>
<td height="17">Decimal number:</td>
<td>3</td>
<td>4</td>
<td>5</td>
<td></td>
</tr>
<tr>
<td height="17">Base to the power of each digit:</td>
<td>10^2</td>
<td>10^1</td>
<td>10^0</td>
<td></td>
</tr>
<tr>
<td height="17">Which equals:</td>
<td>100</td>
<td>10</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td height="17">Total:</td>
<td>300 +</td>
<td>40 +</td>
<td>5</td>
<td><strong>= 345</strong></td>
</tr>
</tbody>
</table>
</div>
&nbsp;

Whereas if we had 345 in hexadecimal (base 16) it would look like this:

<div class="table-scroll">
<table cellspacing="0">
<colgroup width="85"></colgroup>
<colgroup span="3" width="39"></colgroup>
<colgroup width="85"></colgroup>
<tbody>
<tr>
<td height="17">Hexadecimal number:</td>
<td>3</td>
<td>4</td>
<td>5</td>
<td></td>
</tr>
<tr>
<td height="17">Base to the power of each digit:</td>
<td>16^2</td>
<td>16^1</td>
<td>16^0</td>
<td></td>
</tr>
<tr>
<td height="17">Which equals:</td>
<td>256</td>
<td>16</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td height="17">Total:</td>
<td>768 +</td>
<td>64 +</td>
<td>5</td>
<td><strong> = 837</strong></td>
</tr>
</tbody>
</table>
</div>
&nbsp;

See if you can work out the hexadecimal versions of these decimal numbers: 11, 78, 613. _Use the tables to help_.

I hope this has helped spread at least a little light on the hexadecimal! In my next post I'll let you know why this is so helpful in computers, and why this has helped me with binary.

[You can find part 2 here.]({filename}/posts/hexidecimal-part-2.md)