SublimTek
=========

A plugin to adapt Sublime Text 2 for every day usage at Epitech

## Features

* Indent C files according to the "Norme" (like the classic Emacs)
* Much more comming (insertion of the header, auto-verifying of the "Norme", ...)

## Installation

* The easiest way to install SublimTek is via the excellent Package Control Plugin ([installation](http://wbond.net/sublime_packages/package_control/installation))
	* SublimeTek is not inside the "official" Package Control Channel, you need to add it manually
		1. Open the Command Palette
		2. Select "Package Control: Add Repository"
		3. Type "https://github.com/geekuillaume/SublimTek"
	1. Open the Command Palette
	2. Select "Package Control: Install Package"
	3. Select "SublimTek"
* If you don't want to install Package Control you can simply clone the repository inside the "Package directory"
	1. Go in ~/.config/sublime-text-2/Packages/
	2. Clone the git repo : git clone https://github.com/geekuillaume/SublimTek.git

## Usage

* First, for every C file you want to use this plugin with you need to activate the "Epitech" mode
	1. Open your file
	2. Open the Command Palette
	3. Select "SublimTek: Activate Epitech mode"
* Then, each time the file is saved, it will be indented according like it would be with the classic Emacs
* If you want to stop the "Epitech" mode
	1. Go to your file
	2. Open the Command Palette
	3. Select "SublimTek : Deactivate Epitech mode"

## Credits

Plugin created by [Guillaume Besson](http://besson.co/) ([geekuillaume](http://geekuillau.me/))