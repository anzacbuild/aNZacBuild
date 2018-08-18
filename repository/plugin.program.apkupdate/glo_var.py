#######################################################################
 # ----------------------------------------------------------------------------
 # "THE BEER-WARE LICENSE" (Revision 42):
 # @tantrumdev wrote this file.  As long as you retain this notice you
 # can do whatever you want with this stuff. If we meet some day, and you think
 # this stuff is worth it, you can buy me a beer in return. - Muad'Dib
 # ----------------------------------------------------------------------------
#######################################################################

#######################################################################
# Import Modules Section
import xbmc, xbmcaddon, xbmcgui, xbmcplugin, base64
import os
#######################################################################

#######################################################################
# Set this to True to see the menu on non-android devices for dev work
DEVELOPER           = False
#######################################################################

#######################################################################
# Primary Addon Variables
AddonID             = xbmcaddon.Addon().getAddonInfo('id')
ADDON               = xbmcaddon.Addon(id=AddonID)
HOME                = xbmc.translatePath('special://home/')
ADDONS              = os.path.join(HOME, 'addons')
USERDATA            = os.path.join(HOME, 'userdata')
ADDON_DATA          = xbmc.translatePath(os.path.join(USERDATA, 'addon_data'))
ownAddon            = xbmcaddon.Addon(id=AddonID)
URL                 = "https://raw.githubusercontent.com/anzacbuild/aNZacBuild/master/AndroidAPK/"
NEWSURL             = "https://raw.githubusercontent.com/anzacbuild/aNZacBuild/master/rssfeed.xml"
ADDONTITLE          = "[B]APK Update[/B]"
#######################################################################

#######################################################################
# Filename Variables 
BASEURL             = URL
EMU_FILE            = BASEURL + "AndroidAPK.txt"
KODI_FILE           = BASEURL + "kodi.txt"
LIVETV_FILE         = BASEURL + "livetv.txt"
VOD_FILE            = BASEURL + "vod.txt"
MUSIC_FILE          = BASEURL + "music.txt"
SECURITY_FILE       = BASEURL + "security.txt"
SPORTS_FILE         = BASEURL + "sports.txt"
TOOLS_FILE          = BASEURL + "tools.txt"
#######################################################################

#######################################################################
# Theme Variables
FONTHEADER          = "Font14"
FANART              = xbmc.translatePath(os.path.join('special://home/addons/' + AddonID, 'fanart.jpg'))
ICON                = xbmc.translatePath(os.path.join('special://home/addons/' + AddonID, 'icon.png'))
ART                 = xbmc.translatePath(os.path.join('special://home/addons/' + AddonID, 'resources/art/'))
#######################################################################

#######################################################################
ADDONDATA           = os.path.join(USERDATA, 'addon_data', AddonID)
dialog              = xbmcgui.Dialog()
DIALOG              = xbmcgui.Dialog()
dp                  = xbmcgui.DialogProgress()
DP                  = xbmcgui.DialogProgress()
LOG                 = xbmc.translatePath('special://logpath/')
PLUGIN              = os.path.join(ADDONS, AddonID)
skin                = xbmc.getSkinDir()
USER_AGENT          = "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3"
#######################################################################
