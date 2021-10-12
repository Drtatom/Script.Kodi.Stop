import os
import xbmc
import xbmcaddon
import xbmcvfs

__addon__      = xbmcaddon.Addon()
__author__     = __addon__.getAddonInfo('author')
__scriptid__   = __addon__.getAddonInfo('id')
__scriptname__ = __addon__.getAddonInfo('name')
__cwd__        = __addon__.getAddonInfo('path')
__version__    = __addon__.getAddonInfo('version')
__language__   = __addon__.getLocalizedString

__cwd__        = xbmcvfs.translatePath( __addon__.getAddonInfo('path') )
__profile__    = xbmcvfs.translatePath( __addon__.getAddonInfo('profile') )
__resource__   = os.path.join( __cwd__, 'resources', 'lib' )


class MyPlayer( xbmc.Player ):
  def __init__( self, *args, **kwargs ):
    xbmc.Player.__init__( self )
    xbmc.log('MyPlayer - init')
    self.paused = False

  def onPlayBackStopped( self ):
    self.paused = False

  def onPlayBackEnded( self ):
    self.paused = False

  def onPlayBackStarted( self ):
    self.paused = False

  def onPlayBackPaused( self ):
    self.paused = True

  def onPlayBackResumed( self ):
    self.paused = False

player_monitor = MyPlayer()

counter = 0
delay = int(__addon__.getSetting("delay") or 60)

monitor = xbmc.Monitor()
while not monitor.abortRequested():
  if player_monitor.paused == True:
    counter += 1
    if counter > delay*300:
      player_monitor.stop()
      counter = 0
  else:
    counter = 0
  xbmc.sleep(200)