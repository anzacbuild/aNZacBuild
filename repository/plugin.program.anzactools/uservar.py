import os, xbmc, xbmcaddon

#########################################################
### User Edit Variables #################################
#########################################################
ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = 'aNZac Tools'
EXCLUDES       = [ADDON_ID, 'repository.anzacbuild']
# Text File with build info in it.
BUILDFILE      = 'https://raw.githubusercontent.com/anzacbuild/aNZacBuild/master/aNZacTools/builds.txt'
# How often you would list it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK    = 0
# Text File with apk info in it.
APKFILE        = 'https://raw.githubusercontent.com/anzacbuild/aNZacBuild/master/aNZacTools/apk.txt'
# Text File with Youtube Videos urls.  Leave as 'http://' to ignore
YOUTUBETITLE   = ''
YOUTUBEFILE    = 'http://'
# Text File for addon installer.  Leave as 'http://' to ignore
ADDONFILE      = 'http://'
# Text File for advanced settings.  Leave as 'http://' to ignore
ADVANCEDFILE   = 'http://'

# Dont need to edit just here for icons stored locally
PATH           = xbmcaddon.Addon().getAddonInfo('path')
ART            = os.path.join(PATH, 'resources', 'art')

#########################################################
### THEMING MENU ITEMS ##################################
#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'http://aftermathwizard.net/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS     = 'https://raw.githubusercontent.com/anzacbuild/aNZacBuild/master/aNZacTools/buildicon.png'
ICONMAINT      = 'https://raw.githubusercontent.com/anzacbuild/aNZacBuild/master/aNZacTools/maintanenceicon.png'
ICONSPEED      = 'https://raw.githubusercontent.com/anzacbuild/aNZacBuild/master/aNZacTools/speedicon.png'
ICONAPK        = 'https://raw.githubusercontent.com/anzacbuild/aNZacBuild/master/aNZacTools/apkicon.png'
ICONADDONS     = 'https://raw.githubusercontent.com/anzacbuild/aNZacBuild/master/aNZacTools/defaulticon.png'
ICONYOUTUBE    = 'https://raw.githubusercontent.com/anzacbuild/aNZacBuild/master/aNZacTools/defaulticon.png'
ICONSAVE       = 'https://raw.githubusercontent.com/anzacbuild/aNZacBuild/master/aNZacTools/defaulticon.png'
ICONTRAKT      = 'https://raw.githubusercontent.com/anzacbuild/aNZacBuild/master/aNZacTools/defaulticon.png'
ICONREAL       = 'https://raw.githubusercontent.com/anzacbuild/aNZacBuild/master/aNZacTools/defaulticon.png'
ICONLOGIN      = 'https://raw.githubusercontent.com/anzacbuild/aNZacBuild/master/aNZacTools/defaulticon.png'
ICONCONTACT    = 'https://raw.githubusercontent.com/anzacbuild/aNZacBuild/master/aNZacTools/defaulticon.png'
ICONSETTINGS   = 'https://raw.githubusercontent.com/anzacbuild/aNZacBuild/master/aNZacTools/icon.png'
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'Yes'
# Character used in seperator
SPACER         = '____'

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'white'
COLOR2         = 'green'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Alternate items      / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Current Build Header / %s is the menu item and is required
THEME4         = '[COLOR '+COLOR1+']Current Build:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Current Theme Header / %s is the menu item and is required
THEME5         = '[COLOR '+COLOR1+']Current Theme:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'Yes'
# You can add \n to do line breaks
CONTACT        = 'aNZac Build'
#Images used for the contact window.  http:// for default icon and fanart
CONTACTICON    = 'http://'
CONTACTFANART  = 'http://'
#########################################################

#########################################################
### AUTO UPDATE #########################################
########## FOR THOSE WITH NO REPO #######################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'Yes'
# Url to wizard version
WIZARDFILE     = 'https://raw.githubusercontent.com/anzacbuild/aNZacBuild/master/aNZacTools/builds.txt'
#########################################################

#########################################################
### AUTO INSTALL ########################################
########## REPO IF NOT INSTALLED ########################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'Yes'
# Addon ID for the repository
REPOID         = 'repository.anzacbuild'
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = 'https://raw.githubusercontent.com/anzacbuild/aNZacBuild/master/repository/addons.xml'
# Url to folder zip is located in
REPOZIPURL     = 'https://raw.githubusercontent.com/anzacbuild/aNZacBuild/master/repository/repository.anzacbuild/'
#########################################################

#########################################################
### NOTIFICATION WINDOW##################################
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'Yes'
# Url to notification file
NOTIFICATION   = 'https://raw.githubusercontent.com/anzacbuild/aNZacBuild/master/aNZacTools/notify.txt'
# Use either 'Text' or 'Image'
HEADERTYPE     = 'Text'
HEADERMESSAGE  = 'aNZac Build Tools'
# url to image if using Image 424x180
HEADERIMAGE    = 'http://'
# Background for Notification Window
BACKGROUND     = 'https://raw.githubusercontent.com/anzacbuild/aNZacBuild/master/aNZacTools/notifybackground.png'
#########################################################
