# VisualforcePreview

Visualforce Preview is a simple plugin to enable previewing Visualforce page in Sublime text. 

To use this plugin, first you need to setup your Salesforce domain by Preference > Package Settings > VisualforcePreview > Settings - User

Copy the template from Preferences > Package Settings > VisualforcePreview > Settings - Default, and change the domain into your own Salesforce domain. Then you are ready to go. 

To preview a VF page, simply click ctrl + alt + v in your VF page file (you need to save it first). Alternatively, you can click Tools >  VisualforcePreview > Visualforce Preview

## How to install ##

### Package Control ###

Install Will Bond's [Package Control](https://sublime.wbond.net/installation), and then:

* In the Command Palette, choose `Package Control: Install Package`
* Search for `VisualforcePreview` and install it

### Github ###

Go to your Sublime Text "Packages" directory (`Preferences` / `Browse Packages...`).

Then clone this GitHub repository:

    $ git clone https://github.com/Lanceshi2/VisualforcePreview.git "Visualforce Preview"