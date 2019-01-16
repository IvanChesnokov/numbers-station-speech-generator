# numbers-station-speech-generator
A python program that can generate a numeric message in the voice of many Numbers Stations. I mainly made this due to my fascination with [Numbers Stations](https://www.youtube.com/watch?v=Fv-IMcnL3OU) as well as a coding exercise to learn about creating UI. Because of this I ask you to humor me -  as release to release, the interface may change drastically.

Current release is Version 0.1.


## Installation

### For The Experienced User

This program runs on Python 3 with the following dependencies: `datetime`, `pyqt5`, and `pydub`, all of which *should* be downloadable via pip3.

### For The Inexperienced User (Windows)
Run the `install.bat` file included as administrator. It installs Python 3, and other dependencies which are used to run the program you are downloading. Make sure to type `Y` or `Yes` when prompted.

## Use
To run the program, open command prompt (Windows) or terminal (Linux) to the folder you downloaded the repository to and execute the command:

`python numberstation.py`

Type in your preferred message. You must only use numbers `0-9` and the underscore `_` character (which is used to denote silence between numeric groups). Any other values in the text box will cause a crash. There is no limit in length of your message. Next, choose from the dropdown box what station's voice you want to use. Currently only E06 and E07 are available to use. Then use the browse button to choose where you want to save. Make sure your file ends in `.mp3`. Finally, press the start button. When the window says complete, check the directory for the completed mp3 file.

### Disclaimer
Do not under ***any*** circumstances broadcast any outputs from this program over radio frequencies. You may get in trouble with domestic or foreign government agencies or law enforcement. The original numbers stations were used for espionage. It's best if you don't get mistaken for someone that is involved in espionage, treason, or any of that messy stuff.

## To-Do

* Input Validation of the text box
* Adding as many stations as possible to the program. The precedence of additions will be as follows (but may not always be adhered to):
  * Currently running English stations
  * Classic (well-known) inactive Stations, such as Yosemite Sam, Lincolnshire Poacher, Cherry Ripe, etc.
  * Currently running non-English stations
  * Other inactive stations


## Greetings

Greetz to:

* [Priyom.org](http://priyom.org/) for the wealth of information
* [The Conet Project](https://soundcloud.com/the-conet-project) and Irdial-Discs for the audio that I used
* [Curt Rowlett](https://www.youtube.com/channel/UCe5FPUKjHYMbUkG3zbOxfQw) for audio and personal entertainment
* [Peter Staal](https://www.youtube.com/channel/UCjyCsy5ujhnBUORY9IHtM7w) for the clear audio that comes from in-person recordings of the "Sprach/Morse Generator"



