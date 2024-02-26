#  ###############################################################################
# Created By : Nikhil Shivarkar               Verified By:                 (Date)
# Updated By:                    (Date)       Verified By:                 (Date)
#
# Description: 
# This is Test Suite for Integration Partner Test cases
# VA-1 - VerifyMonitoringPageIsOpened.
# VA-2 - Verify1x1tileIsOpened.
# VA-3 - Verify2x2tileIsOpened.
# VA-4 - Verify3x3tileIsOpened
# VA-5 - VerifyResourceTreeCollapses
# VA-6 - VerifyResourceTreeExpands
# VA-7 - VerifySelectedCameraOnMonitoringPage
# VA-8 - VerifyPlaybackIconShowsTimeLine - JIRA task - 15685 - (Sanity) Monitoring rectangle : playback icon (https://vicon-security.atlassian.net/browse/DCA-183)
# VA-8 - VerifySelectedMicOnMonitoringPage
# VA-9 - VerifyUngroupedResourcesCollapsed
# VA 10 - VerifyUngroupedResourcesExpand
# VA 11 - Verify views is running on Monitoring  (https://vicon-security.atlassian.net/browse/VA-4772)
# VA 12 - Verify tour is displayed on monitoring (https://vicon-security.atlassian.net/browse/VA-4770)
# VA 13 - VerifyWebpageIsOpenedOnMonitoring
# VA 14 - VerifyMapIsOpenedOnMonitoring
# VA 15 - VerifyVAXDoorIsOpenedOnMonitoring
# VA 16 - VerifyAllRightClickOptionsAreVisible
# VA 17 - VerifyRightClickOptionToOpenThumbnailPage
# VA 18 - VerifyRightClickOptionToOpenMuseumPage
# VA 19 - VerifyRightClickOptionToOpenExportFormOfCamera
# VA 20 - VerifyAllRightClickOptionsForMicAreVisible
# VA 21 - VerifyRightClickOptionToOpenExportFormOfMic
# VA 22 - VerifyAllRightClickOptionsForRelayAreVisible
# VA 23 - VerifyAllRightClickOptionsForMapAreVisible
# VA 24 - VerifyRightClickOptionToOpenMapFormMapGallary
# VA 25 - VerifyAllRightClickOptionsForVAXactionPlanAreVisible
# VA 26 - VerifyAllRightClickOptionsForVAXDoorAreVisible
# VA 27 - DoubleClickOn2x2tileToExpandvideoChannelStream
# VA 28 - VeifySingleVideoChannelDetachedWindowIn1x1tile
# VA 29 - VeifySingleAudioChannelDetachedWindowIn1x1tile
# VA 30 - VeifySingleMapDetachedWindowIn1x1tile
# VA 31 - VeifySingleViewDetachedWindow
# VA 32 - VeifySingleTourDetachedWindow
# VA 33 - VerifyOverrideNewVideoChannelOnExistingVideoChannel
# VA 34 - VerifyOverrideNewWebpageOnExistingWebpage
# VA 35 - VerifyOverrideNewViewOnExistingView
# VA 36 - VerifyOverrideNewTourOnExistingTour
# VA 37 - VerifyOverrideNewMapOnExistingMap
# VA 38 - VerifyOverrideWebpageOnExistingVideoChannel
# VA 39 - VerifyOverrideViewOnExistingVideoChannel
# VA 40 - VerifyOverrideTourOnExistingVideoChannel
# VA 41 - VerifyOverrideMapOnExistingVideoChannel
# VA 42 - VerifyOverrideVAXDoorOnExistingVideoChannel
# VA 43 - VerifyOverrideViewOnExistingTour
# VA 44 - VerifyOverrideMapOnExistingWebpage

#################################################################################

# Pre-requisite :-  
# 1) Required Video Channels - 172.20.0.238 , 172.20.0.234
# 2) Required Audio Channels - 172.20.0.238 , 172.20.0.234 (Make sure both are visible on Monitoring page.)
# 3) Required pair of all resources added in appliaction with their default name.  -- It is pending in this code because Configuration page is not implemented yet.

def preRequisiteMethodToAddDevices():
    #CommonUtility.openConfigurationPage()
    Delay(1000)
    #Clicks the 'ChromiumWebBrowserConfigurationHomePage' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.ChromiumWebBrowserConfigurationHomePage.Click(648, 190)
    Delay(500)
    #Clicks the 'ChromiumWebBrowserConfigurationHomePage' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.ChromiumWebBrowserConfigurationHomePage.Click(386, 113)
    Delay(3000)
    #Clicks the 'ChromiumWebBrowserConfigurationHomePage' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.ChromiumWebBrowserConfigurationHomePage.Click(891, 159)
    #Enters '172.20.0.238' in the 'pageLocalhostConfigurationHomeLa' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.ChromiumWebBrowserConfigurationHomePage.pageLocalhostConfigurationHomeLa.Keys("172.20.0.238")
    Delay(3000)
    #Clicks the 'ChromiumWebBrowserConfigurationHomePage' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.ChromiumWebBrowserConfigurationHomePage.Click(834, 261)
    #Clicks the 'ChromiumWebBrowserConfigurationHomePage' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.ChromiumWebBrowserConfigurationHomePage.Click(1312, 784)
    Delay(1000)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.ChromiumWebBrowserConfigurationHomePage).BlockByText("Successfully added", spNearestToCenter).Click()
    #Clicks the 'ChromiumWebBrowserConfigurationHomePage' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.ChromiumWebBrowserConfigurationHomePage.Click(1546, 44)
    Delay(2000)
    #Clicks the 'ChromiumWebBrowserConfigurationHomePage' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.ChromiumWebBrowserConfigurationHomePage.Click(386, 113)
    Delay(1000)
    #Clicks the 'ChromiumWebBrowserConfigurationHomePage' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.ChromiumWebBrowserConfigurationHomePage.Click(891, 159)
    Delay(1000)
    #Enters '172.20.0.238' in the 'pageLocalhostConfigurationHomeLa' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.ChromiumWebBrowserConfigurationHomePage.pageLocalhostConfigurationHomeLa.Keys("172.20.0.234")
    Delay(3000)
    #Clicks the 'ChromiumWebBrowserConfigurationHomePage' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.ChromiumWebBrowserConfigurationHomePage.Click(834, 261)
    Delay(1000)
    #Clicks the 'ChromiumWebBrowserConfigurationHomePage' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.ChromiumWebBrowserConfigurationHomePage.Click(1312, 784)
    Delay(1000)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.ChromiumWebBrowserConfigurationHomePage).BlockByText("devices", spNearestToCenter).Click()
    #Clicks the 'ChromiumWebBrowserConfigurationHomePage' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.ChromiumWebBrowserConfigurationHomePage.Click(1546, 44)

import CommonUtility
import MonitoringTestCases

def VerifyMonitoringPageIsOpened():
    CommonUtility.Login()
    MonitoringTestCases.verifyMonitoringPageIsOpened()
    
def VerifyChangeLayouts():                      #15373 - (Sanity) Monitoring : change layout
    MonitoringTestCases.clickOn1x1tileView()
    MonitoringTestCases.verify1x1tileIsOpened()    
    Delay(500)
    MonitoringTestCases.clickOn2x2tileView()
    MonitoringTestCases.verify2x2tileIsOpened()    
    Delay(500)
    MonitoringTestCases.clickOn3x3tileView()
    MonitoringTestCases.verify3x3tileIsOpened()     
    
def VerifyApplicationSwitchesTabs():            #15672	(Sanity) Monitoring : switching between tabs  
     MonitoringTestCases.clickOn1x1tileView()
     MonitoringTestCases.dragAndDropCamera1OnMonitoring()
     MonitoringTestCases.VerifyExpectedCamera1isDraggedOnMonitoring()
     Delay(300)
     MonitoringTestCases.addSecondViewOnMonitoringPage()
     MonitoringTestCases.clickOnSecondLayOut()
     MonitoringTestCases.dragAndDropCamera2OnMonitoring()
     Delay(300)
     MonitoringTestCases.ClickOnFirstLayout()
     MonitoringTestCases.VerifyExpectedCamera1isDraggedOnMonitoring()

#-----------------------------------------------------------------------
        
def VerifyResourceTreeCollapses():    
    MonitoringTestCases.collapseResourceTree()
    
def VerifyResourceTreeExpands():        
    MonitoringTestCases.expandResourceTree()

#-----------------------------------------------------------------------        
    
def VerifyFullScreenInMonitoringPageAndRestartApp():            #11954 - (Sanity) Full Screen In Monitoring Page and close app    &&&&   11417	(Sanity) Return to full screen and Close browser, Open new browser
    MonitoringTestCases.fullScreen()
    MonitoringTestCases.fullScreenRestartApp()

def VerifySelectedCameraOnMonitoringPage():        
    MonitoringTestCases.clickOn1x1tileView()
    MonitoringTestCases.dragAndDropCamera1OnMonitoring()  
    MonitoringTestCases.VerifyExpectedCamera1isDraggedOnMonitoring()    
    
def VerifyMonitoringRectangleExportIconForCamera():                #15682 - (Sanity) Monitoring rectangle : export icon
    MonitoringTestCases.exportFromCameraStreamOnMonitoringPage()    
      
def VerifyCloseButtonOfMonitoringTile():      #15686	(Sanity) Monitoring rectangle : close button 
    MonitoringTestCases.dragAndDropCamera1OnMonitoring()
    Delay(1000)
    MonitoringTestCases.closeResourceFromMonitoring() 
    Delay(1000) 
    MonitoringTestCases.verifyResourceIsClosed()    
    
def VerifySelectedMic1OnMonitoringPage():        
    MonitoringTestCases.clickOn1x1tileView()
    MonitoringTestCases.dragAndDropMic1OnMonitoring()   #Make sure that expected Mic is Visible on Monitoring page.   
    MonitoringTestCases.clickOnStopAllBtn() 
    
def VerifyStopAll():
    MonitoringTestCases.dragAndDropCamera1OnMonitoring() 
    MonitoringTestCases.dragAndDropMic1OnMonitoring()
    MonitoringTestCases.clickOnStopAllBtn()
    MonitoringTestCases.verifyCameraAndMicAreStopped()    
    
def verifyExpectedRelayOutputIsVisibleOnMonitoringpage():      #15663 - (Sanity) Monitoring : Relay output 
    MonitoringTestCases.visiblityOfRelayOutput()    
    
def VerifyViewIsClosed():                             #15392 - (Sanity) Monitoring : close view
    MonitoringTestCases.dragAndDropView1OnMonitoring()   
    Delay(1000)
    MonitoringTestCases.clickOnStopAllBtn()
    Delay(1000) 
    MonitoringTestCases.verifyResourceIsClosed()    
#-----------------------------------------------------------------------
    
def VerifyUngroupedResourcesCollapsedAndExpanded():   #15688 -	(Sanity) Monitoring rectangle: expand/collapse icon 
    MonitoringTestCases.ClickOnUngrouped()
    MonitoringTestCases.verifyResourcesAreHiddenUnderUngrouped()
    Delay(2000)
    MonitoringTestCases.ClickOnUngrouped()
    MonitoringTestCases.verifyResourcesAreHiddenUnderUngrouped()    
#-----------------------------------------------------------------------
    
def VerifyView1IsRunningOnMonitoring2x2View():    #829 - Showing Player in 1x1 layout temporarily - 2x2 layout of "Views" resource (Pending code for Configuration to add new tour)  
    MonitoringTestCases.clickOn1x1tileView()
    MonitoringTestCases.dragAndDropView1OnMonitoring()    #Make sure that expected View is Visible on Monitoring page.
    MonitoringTestCases.clickOnStopAllBtn()
    
def VerifyView1IsRunningOnMonitoring4x4View():   #832	Showing Player in 1x1 layout temporarily - 4x4 layout of "Views" resource
    Delay(2000)
    MonitoringTestCases.clickOn1x1tileView()
    MonitoringTestCases.dragAndDropView2OnMonitoring()   
    
def VerifyTour1IsRunningonMonitoring():               #15661 - (Sanity) Monitoring : tour    (Pending code for Configuration to add new tour)
    MonitoringTestCases.clickOnStopAllBtn()
    MonitoringTestCases.clickOn1x1tileView()
    MonitoringTestCases.dragAndDropTour1OnMonitoring()    #Make sure that expected Tour is Visible on Monitoring page.
    MonitoringTestCases.clickOnStopAllBtn()
    
def VerifyWebpage1IsOpenedOnMonitoring():
    MonitoringTestCases.clickOn1x1tileView()
    MonitoringTestCases.dragAndDropWebpage1OnMonitoring()    #Make sure that expected Webpage is Visible on Monitoring page.
    MonitoringTestCases.closeResourceFromMonitoring()    
    
def VerifyMap1IsOpenedOnMonitoring():
    MonitoringTestCases.clickOn1x1tileView()
    MonitoringTestCases.dragAndDropMap1OnMonitoring()    #Make sure that expected Map is Visible on Monitoring page.
    MonitoringTestCases.closeResourceFromMonitoring()    
    
def VerifyVAXDoor1IsOpenedOnMonitoring ():
    MonitoringTestCases.clickOn1x1tileView()
    MonitoringTestCases.dragAndDropVAXdoor1OnMonitoring()    #Make sure that expected Door is Visible on Monitoring page.
    MonitoringTestCases.closeResourceFromMonitoring()

#-----------------------------------------------------------------------    
    
def VerifyAllRightClickOptionsForCameraAreVisible():     #15667	(Sanity) monitoring: right click on camera 
    CommonUtility.closeApplication()
    Delay(5000)
    CommonUtility.Login()
    MonitoringTestCases.rightClickOptionsOfCamera()
 
def VerifyRightClickOptionToOpenThumbnailPage():   
    MonitoringTestCases.rightClickOptionsOfCamera()
    MonitoringTestCases.cameraRightClickOptionsToThumbnailSearchPage()
    
def VerifyRightClickOptionToOpenMuseumPage():   
    MonitoringTestCases.rightClickOptionsOfCamera()
    MonitoringTestCases.cameraRightClickOptionsToMuseumSearchPage()
    
def VerifyRightClickOptionToOpenExportFormOfCamera():    #15668	(Sanity) Monitoring: right click on audio 
    MonitoringTestCases.rightClickOptionsOfCamera()
    MonitoringTestCases.cameraRightClickToExport()   
# VerifyRightClickOptionToOpenAuxWindow(): and VerifyRightClickOptionToOpenConfigurationPage() are pending due to Configuration page.
    
def VerifyAllRightClickOptionsForMicAreVisible():     
    MonitoringTestCases.rightClickOptionsOfMic()
    
def VerifyRightClickOptionToOpenExportFormOfMic():  
    MonitoringTestCases.rightClickOptionsOfMic()
    MonitoringTestCases.micRightClickToExport()    
# NavigateToConfiguration page to select MIC is pending due to new Configuration page.    

def VerifyAllRightClickOptionsForViewAreVisible():     #15670	(Sanity) Monitoring:  right click on view   
    MonitoringTestCases.rightClickOptionsOfView()
     
def VerifyRightClickOptionToOpenExportFormOfView():  
    MonitoringTestCases.rightClickOptionsOfView()
    MonitoringTestCases.viewRightClickToExport()    
# NavigateToConfiguration page to select VIEW is pending due to new Configuration page.
             
def VerifyAllRightClickOptionsForTourAreVisible():     #15669	(Sanity) Monitoring: right click on tour  
    MonitoringTestCases.rightClickOptionsOfTour()

def VerifyAllRightClickOptionsForWebLinkAreVisible():     #15671	(Sanity) Monitoring: right click on weblink     
    MonitoringTestCases.rightClickOptionsOfWebLink()
# NavigateToConfiguration page to select Relay is pending due to new Configuration page. 
        
def VerifyAllRightClickOptionsForRelayAreVisible():
    MonitoringTestCases.rightClickOptionsOfRelayDevice()
# NavigateToConfiguration page to select Relay is pending due to new Configuration page. 

def VerifyAllRightClickOptionsForMapAreVisible():
    MonitoringTestCases.rightClickOptionsOfMap()

def VerifyRightClickOptionToOpenMapFormMapGallary():  
    MonitoringTestCases.rightClickOptionsOfMap()
    MonitoringTestCases.mapRightClickToViewMapGallary()
# NavigateToConfiguration page to select Map is pending due to new Configuration page.

def VerifyAllRightClickOptionsForVAXactionPlanAreVisible():
    MonitoringTestCases.rightClickOptionsOfVAXactionPlan()
# Run Action plan and NavigateToConfiguration page to select VAX action plan is pending due to new Configuration page.    
    
def VerifyAllRightClickOptionsForVAXDoorAreVisible():
    MonitoringTestCases.rightClickOptionsOfVAXDoors()
    MonitoringTestCases.rightClickOptionsOfVAXDoors_OverrideSubOptions()

#-----------------------------------------------------------------------    
  
def DoubleClickOn3x3tileToExpandvideoChannelStreamWithSingleChannel():         #11514	(Sanity) Layout changes on double click - Double click on any tile - case 2
    MonitoringTestCases.clickOn3x3tileView()
    Log.Message("3x3 tile is opened.")
    Delay(300)
    MonitoringTestCases.dragAndDropCamera1InFirstTileOf3x3OnMonitoring()
    Log.Message("Expected video channel is opened in first tile of 3x3 view on Monitoring.")
    Delay(300)
    MonitoringTestCases.doubleClickOnCameraTitle()
    Log.Message("Double click on Video channel")
    Delay(300)
    MonitoringTestCases.verify1x1tileIsOpened()
    Log.Message("1x1 tile is opened as expected")
    Delay(300)
    MonitoringTestCases.doubleClickOnCameraTitle()
    Log.Message("Double click on Video channel")
    Delay(300)
    MonitoringTestCases.verify3x3tileIsOpened()
    Log.Message("2x2 view is opened.")
    MonitoringTestCases.clickOnStopAllBtn()
    Delay(300)
    MonitoringTestCases.clickOn2x2tileView()
    Log.Message("2x2 tile is opened.")
    MonitoringTestCases.clickOn3x3tileView()
    Delay(300)
    
def DoubleClickOnVertical5x2tileToExpandvideoChannelStreamWithSingleChannel():         #11515 (Sanity) Layout changes on double click - Double click on any tile - case 3
    MonitoringTestCases.clickOnVertical5x2Tile()
    Log.Message("5x2 tile is opened.")
    Delay(300)
    MonitoringTestCases.dragAndDropCamera1InFirstTileOf3x3OnMonitoring()
    Log.Message("Expected video channel is opened in first tile of 3x3 view on Monitoring.")
    Delay(300)    
    MonitoringTestCases.doubleClickOnCameraTitle()
    Log.Message("Double click on Video channel")
    Delay(300)
    MonitoringTestCases.verify1x1tileIsOpened()
    Log.Message("1x1 tile is opened as expected")
    Delay(300)
    MonitoringTestCases.doubleClickOnCameraTitle()
    Log.Message("Double click on Video channel")
    Delay(300)
    MonitoringTestCases.verifyVertical5x2TileIsOpened()
    Log.Message("2x2 view is opened.")
    MonitoringTestCases.clickOnStopAllBtn()
    Delay(300)   
       
def DoubleClickOn2x2tileToExpandvideoChannelStreamWithSingleChannel():           #11516 - (Sanity) Layout changes on double click - Double click on a single tile - case 1   
    MonitoringTestCases.clickOn2x2tileView()
    Log.Message("2x2 tile is opened.")
    Delay(300)
    MonitoringTestCases.dragAndDropCamera1InFirstTileOf2x2OnMonitoring()
    Log.Message("Expected video channel is opened in first tile of 2x2 view on Monitoring.")
    Delay(300)
    MonitoringTestCases.doubleClickOnCameraTitle()
    Log.Message("Double click on Video channel")
    Delay(300)
    MonitoringTestCases.verify1x1tileIsOpened()
    Log.Message("1x1 tile is opened as expected")
    Delay(300)
    MonitoringTestCases.doubleClickOnCameraTitle()
    Log.Message("Double click on Video channel")
    Delay(300)
    MonitoringTestCases.verify2x2tileIsOpened()
    Log.Message("2x2 view is opened.")
    MonitoringTestCases.clickOnStopAllBtn()
    Delay(300)

def DoubleClickOn2x2tileToExpandvideoChannelStreamWith2Channels():              #11517	(Sanity) Layout changes on double click - Double click on a single tile - case 2
    MonitoringTestCases.clickOn2x2tileView()
    Log.Message("2x2 tile is opened.")
    Delay(300)
    MonitoringTestCases.dragAndDropCamera1InFirstTileOf2x2OnMonitoring()
    Log.Message("Expected video channel is opened in first tile of 2x2 view on Monitoring.")
    Delay(300)
    MonitoringTestCases.dragAndDropCamera2InSecondTileOf2x2OnMonitoring()
    Log.Message("Expected video channel is opened in second tile of 2x2 view on Monitoring.")
    Delay(300)
    MonitoringTestCases.doubleClickOnCameraTitle()
    Log.Message("Double click on Video channel")
    Delay(300)
    MonitoringTestCases.verify1x1tileIsOpened()
    Log.Message("1x1 tile is opened as expected")
    Delay(300)
    MonitoringTestCases.doubleClickOnCameraTitle()
    Log.Message("Double click on Video channel")
    Delay(300)
    MonitoringTestCases.verify2x2tileIsOpened()
    Log.Message("2x2 view is opened.")
    MonitoringTestCases.clickOnStopAllBtn()
    Delay(300)
    
    



#-----------------------------------------------------------------------
          
def VeifySingleVideoChannelDetachedWindowIn1x1tile():
    MonitoringTestCases.clickOn1x1tileView()
    Log.Message("1x1 tile is opened.")
    Delay(300)
    MonitoringTestCases.dragAndDropCamera1OnMonitoring()
    Log.Message("Camera is dragged on Monitoring screeen.")
    Delay(300)
    MonitoringTestCases.detachSingleVideoChannelOn1x1Tile()
    Log.Message("Video channel is opened in Detached screen as expected.")
    
def VeifySingleAudioChannelDetachedWindowIn1x1tile():
    MonitoringTestCases.clickOn1x1tileView()
    Log.Message("1x1 tile is opened.")
    Delay(300)
    MonitoringTestCases.dragAndDropMic1OnMonitoring()
    Log.Message("Audio Channel is dragged on Monitoring screeen.")
    Delay(300)
    MonitoringTestCases.detachSingleAudioChannelOn1x1Tile()
    Log.Message("Audio Channel is opened in Detached window as expected.")
    
def VeifySingleMapDetachedWindowIn1x1tile():
    MonitoringTestCases.clickOn1x1tileView()
    Log.Message("1x1 tile is opened.")
    Delay(300)
    MonitoringTestCases.dragAndDropMap1OnMonitoring()
    Log.Message("Map is dragged on Monitoring screeen.")  
    Delay(300)
    MonitoringTestCases.detachSingleMapOn1x1Tile()
    Log.Message("Map is opened in Detached window as expected.")  
    
def VeifySingleViewDetachedWindow():
    MonitoringTestCases.clickOn1x1tileView()
    Log.Message("1x1 tile is opened.")
    Delay(300)
    MonitoringTestCases.dragAndDropView1OnMonitoring()
    Log.Message("View is dragged on Monitoring screeen.")  
    Delay(300)
    MonitoringTestCases.detachView()
    Log.Message("View is opened in Detached window as expected.")    
    
def VeifySingleTourDetachedWindow():
    MonitoringTestCases.clickOn1x1tileView()
    Log.Message("1x1 tile is opened.")
    Delay(300)
    MonitoringTestCases.dragAndDropTour1OnMonitoring()
    Log.Message("Tour is dragged on Monitoring screeen.")  
    Delay(300)  
    MonitoringTestCases.detachTour()
    Log.Message("Tour is opened in Detached window as expected.")    

#-----------------------------------------------------------------------    
        
def VerifyOverrideNewVideoChannelOnExistingVideoChannel(): 
    MonitoringTestCases.clickOn1x1tileView()
    Log.Message("1x1 tile is opened.")
    Delay(300)
    MonitoringTestCases.dragAndDropCamera1OnMonitoring()
    Delay(500)
    MonitoringTestCases.dragAndDropCamera2OnMonitoring()
    Delay(300)    
    MonitoringTestCases.clickOnStopAllBtn()
         
def VerifyOverrideNewWebpageOnExistingWebpage(): 
    MonitoringTestCases.clickOn1x1tileView()
    Log.Message("1x1 tile is opened.")
    Delay(500)
    MonitoringTestCases.dragAndDropWebpage1OnMonitoring()
    Delay(500)  
    MonitoringTestCases.dragAndDropWebpage2OnMonitoring()
    Delay(500)    
    
def VerifyOverrideNewViewOnExistingView(): 
    MonitoringTestCases.clickOn1x1tileView()
    Log.Message("1x1 tile is opened.")
    Delay(300)
    MonitoringTestCases.dragAndDropView1OnMonitoring()
    Delay(500)  
    MonitoringTestCases.dragAndDropView2OnMonitoring()
    Delay(500)    
    
def VerifyOverrideNewTourOnExistingTour():
    MonitoringTestCases.clickOn1x1tileView()
    Log.Message("1x1 tile is opened.")
    Delay(300)
    MonitoringTestCases.dragAndDropTour1OnMonitoring()
    Delay(500)  
    MonitoringTestCases.dragAndDropTour2OnMonitoring()
    Delay(500)    
    MonitoringTestCases.clickOnStopAllBtn()
    
def VerifyOverrideNewMapOnExistingMap():
    MonitoringTestCases.clickOn1x1tileView()
    Log.Message("1x1 tile is opened.")
    Delay(300)
    MonitoringTestCases.dragAndDropMap1OnMonitoring()
    Delay(1000)  
    MonitoringTestCases.dragAndDropMap2OnMonitoring()
    Delay(500)   
    MonitoringTestCases.clickOnStopAllBtn()    

#-----------------------------------------------------------------------
        
def VerifyOverrideWebpageOnExistingVideoChannel():
    MonitoringTestCases.clickOn1x1tileView()
    Log.Message("1x1 tile is opened.")
    Delay(300)
    MonitoringTestCases.dragAndDropCamera1OnMonitoring()
    Delay(500)
    MonitoringTestCases.dragAndDropWebpage1OnMonitoring()
    Delay(300)    
    MonitoringTestCases.clickOnStopAllBtn()
    
def VerifyOverrideViewOnExistingVideoChannel():
    MonitoringTestCases.clickOn1x1tileView()
    Log.Message("1x1 tile is opened.")
    Delay(300)
    MonitoringTestCases.dragAndDropCamera1OnMonitoring()
    Delay(500)
    MonitoringTestCases.dragAndDropView1OnMonitoring()
    Delay(300)    
    MonitoringTestCases.clickOnStopAllBtn()    
    
def VerifyOverrideTourOnExistingVideoChannel():
    MonitoringTestCases.clickOn1x1tileView()
    Log.Message("1x1 tile is opened.")
    Delay(300)
    MonitoringTestCases.dragAndDropCamera1OnMonitoring()
    Delay(500)
    MonitoringTestCases.dragAndDropTour1OnMonitoring()
    Delay(300)    
    MonitoringTestCases.clickOnStopAllBtn()    
    
def VerifyOverrideMapOnExistingVideoChannel():
    MonitoringTestCases.clickOn1x1tileView()
    Log.Message("1x1 tile is opened.")
    Delay(300)
    MonitoringTestCases.dragAndDropCamera1OnMonitoring()
    Delay(500)
    MonitoringTestCases.dragAndDropMap1OnMonitoring()
    Delay(300)    
    MonitoringTestCases.clickOnStopAllBtn()    
 
def VerifyOverrideVAXDoorOnExistingVideoChannel():
    MonitoringTestCases.clickOn1x1tileView()
    Log.Message("1x1 tile is opened.")
    Delay(300)
    MonitoringTestCases.dragAndDropCamera1OnMonitoring()
    Delay(500)
    MonitoringTestCases.dragAndDropVAXdoor1OnMonitoring()
    Delay(300)    
    MonitoringTestCases.clickOnStopAllBtn()    
          
def VerifyOverrideViewOnExistingTour():    
    MonitoringTestCases.clickOn1x1tileView()
    Log.Message("1x1 tile is opened.")
    Delay(300)
    MonitoringTestCases.dragAndDropTour1OnMonitoring()
    Delay(500)
    MonitoringTestCases.dragAndDropView1OnMonitoring()
    Delay(300)    
    MonitoringTestCases.clickOnStopAllBtn()    
    
def VerifyOverrideMapOnExistingWebpage():        
    MonitoringTestCases.clickOn1x1tileView()
    Log.Message("1x1 tile is opened.")
    Delay(300)
    MonitoringTestCases.dragAndDropWebpage1OnMonitoring()
    Delay(500)
    MonitoringTestCases.dragAndDropMap1OnMonitoring()
    Delay(500)    
    MonitoringTestCases.clickOnStopAllBtn()  

#-----------------------------------------------------------------------    
    
def VerifiyNavigateToConfigurationPage():       #15683	(Sanity) Monitoring rectangle : configuration icon
    CommonUtility.openConfigurationPage()
    Delay(500)
    CommonUtility.openMonitoringPage()
    
def VerifyLastState_ClosingWithoutLogout():       #11665	(Sanity) Last State - Closing without logout
    CommonUtility.closeApplication()
    Delay(5000)    
    CommonUtility.Login()
    Delay(4000)
    MonitoringTestCases.clickOn3x3tileView()
    Delay(500)    
    CommonUtility.closeApplication()
    Delay(5000)    
    CommonUtility.LoginWithEnabledReturnTolastDisplay()
    Delay(5000)    
    MonitoringTestCases.verify3x3tileIsOpened()
    Delay(500)    
    CommonUtility.closeApplication()
    Delay(5000)    
    CommonUtility.Login()
    Delay(4000)
    CommonUtility.verifyDefaultMonitoringPageStateIsOpened()
    Delay(500)
    
def VerifyLastState_GUIfunctionalityLastState():              #11668	(Sanity) Last State - GUI functionality         
    CommonUtility.closeApplication()
    Delay(5000)    
    CommonUtility.Login()
    Delay(4000)
    MonitoringTestCases.clickOn3x3tileView()
    Delay(500)   
    MonitoringTestCases.dragAndDropCamera1InFirstTileOf3x3OnMonitoring()
    Delay(500)
    MonitoringTestCases.VerifyExpectedCamera1isDraggedOnMonitoring() 
    CommonUtility.closeApplication()
    Delay(5000)   
    CommonUtility.Login()
    Delay(4000)    
    CommonUtility.verifyDefaultMonitoringPageStateIsOpened()
    Delay(500) 
    
def VerifyLastState_ChangeLayout():               #11681 - (Sanity) Last State - Layout change
    CommonUtility.closeApplication()
    Delay(5000)    
    CommonUtility.Login()
    Delay(4000)
    MonitoringTestCases.clickOnHorizontal2Layout()
    Delay(500)
    MonitoringTestCases.addSecondViewOnMonitoringPage()
    Delay(500)
    MonitoringTestCases.clickOnVertical5Layout()
    Delay(500)
    MonitoringTestCases.addThirdViewOnMonitoringPage()
    Delay(500)
    MonitoringTestCases.clickOnMixed7Layout()
    Delay(500)
    CommonUtility.closeApplication()
    Delay(5000)    
    CommonUtility.Login()
    Delay(4000)
    MonitoringTestCases.verifyDefaultMonitoringPageStateIsOpened()
    Delay(500)
    MonitoringTestCases.clickOn1x1tileView()
    
def VerifyDifferentLayoutSelection():                #12249	(Sanity) Different display layouts - Simple test
    CommonUtility.closeApplication()
    Delay(5000)    
    CommonUtility.Login()
    Delay(4000)
    MonitoringTestCases.clickOn2x2tileView()
    MonitoringTestCases.verify2x2tileIsOpened()
    Delay(500)
    MonitoringTestCases.addSecondViewOnMonitoringPage()
    Delay(500)
    MonitoringTestCases.clickOn3x3tileView()
    MonitoringTestCases.verify3x3tileIsOpened()
    Delay(500)
    MonitoringTestCases.addThirdViewOnMonitoringPage()
    Delay(500)
    MonitoringTestCases.clickOnVertical5x2Tile()
    MonitoringTestCases.verifyVertical5x2TileIsOpened()
    CommonUtility.closeApplication()
    Delay(5000)    
    CommonUtility.Login()
    Delay(4000)
    
    
    
    
#-----------------------------------------------------------------------     

def ExportWithoutAnyResource():                 #15676	(Sanity) Monitoring : Export without cameras present in view 
    MonitoringTestCases.exportWithoutCamera()
    