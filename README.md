# TextAnalyzer
A little fun project that enables the fast analysis of large text files. The parent class `analyzer` enables processing large text files **line-by-line** to avoid having to load large files all at once into variables. The child class `textAnalyzer` is then mainly a showcase of how you might implement the parent class. It does things like calculate number of words, spaces, and outputs complete analyses for strings containing a certain substring. You could use this for filtering messages sent by one entity and analysing those.

## Installation
Make sure you have python installed. Copy the repo and run from your favourite terminal or editor. No special requirements for usage.

## Usage
Place the text file you wish to analyze alongside the `test.py` file, and make sure that the analyzer is initialized on the correct file name. `test.py` contains some examples of what you could do from there. 

## License

[MIT](https://choosealicense.com/licenses/mit/) license, Copyright © 2025 Rens van Eck.