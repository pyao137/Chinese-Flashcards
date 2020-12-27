# Chinese-Flashcards
Created by Peter Yao (pyao137 on Github)

This simple python program generates flashcards from a (properly formatted) .txt file of Chinese vocabulary.
The .txt file must be formatted in a specific way for the program to work. Each line of the file should contain 3 elements separated by hyphens or en dashes, or em dashes.
The first element must be a Chinese word. The other two elements can be whatever you wish. 
I personally chose to have the Chinese word's pinyin as the second element, and its English meaning as the third. This choice affected some of the varaible names in my program.
<br>Example: <br>
  简介 - Jiǎnjiè - introduction, synopsis, summary <br>
  征服 - Zhēngfú - conquer <br>
  风格 - Fēnggé - style <br>
If lines starting with Chinese characters do not contain 3 elements separated by 2 hyphens/en dashes/em dashes, they will be disregarded by the program. <br>

It is additionally possible to add lines of text starting with numbers in the .txt file. For example, the .txt file could look like: <br>
  24abc <br>
  即使 - Jí shǐ – even if <br>
  浪费 - Làng fèi - waste <br>
  危险 - Wéi xiǎn - danger <br>
  12/16/2020 <br>
  暗 - an - dark, dim <br>
  币 - Bì - coin, currency (eg: renminbi) <br>
The program will reads lines of text starting with numbers as separations of card sections. For instance, the file above would have two card sections: "24abc" and "12/16/2020."
Section "24abc" would contain the flashcards for 即使, 浪费, and 危险. Section "12/16/2020" would contain the flashcards for 暗 and 币. 
While running the flashcards program, the user is given the choice to flip through cards of a particular section, or all the cards on the .txt file. <br>

Just recall that *any* line of text starting with a number will be read as a card section separator.
Also recall that *any* line of text starting with a Chinese character and containing 2 hyphens/em dashes/en dashes will be read as a flashcard containing Chinese word data.
All other lines of text will be disregarded. This is how the .txt file containing data for the program to read should be formatted.
