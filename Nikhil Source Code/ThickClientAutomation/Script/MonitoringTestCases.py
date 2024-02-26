import CommonUtility


def verifyMonitoringPageIsOpened():
    #Checks whether the 'Caption' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl object equals 'Resources'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl, "Caption", cmpEqual, "Resources")
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemUngrouped object equals 'UNGROUPED'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemUngrouped, "WPFControlText", cmpEqual, "UNGROUPED")

def addSecondViewOnMonitoringPage():
    #Clicks the 'tabView' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.Click(110, 33)
    
def addThirdViewOnMonitoringPage():    
    #Clicks the 'tabView' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.Click(200, 34)
    
def addFourthViewOnMonitoringPage():    
    #Clicks the 'tabView' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.Click(290, 35)    
    
def ClickOnFirstLayout():
    #Clicks the 'TabitemView' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.TabitemView.Click(40, 35)

def clickOnSecondLayOut():
    #Clicks the 'tabView' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.Click(130, 34)    
    
def clickOnThirdLayOut():
    #Clicks the 'tabView' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.Click(220, 34)    
    
def clickOnFourthLayOut():
    #Clicks the 'tabView' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.Click(310, 34)    
    
def clickOn1x1tileView():    
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.HeaderbuttonChangeLayout).BlockByText("Change").Click()
    #Clicks the 'control2' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ItemsControl.ItemscontrolBasic.control2.Click(50, 44)
    
def verify1x1tileIsOpened():
    Delay(1000)
    #Checks whether the 'Width' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect object equals 1598.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect, "Width", cmpGreaterOrEqual, 1580)
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect, "Width", cmpLessOrEqual, 1620)
    #Checks whether the 'Height' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect object equals 778.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect, "Height", cmpEqual, 778)    
    Delay(1000)
    
def clickOn2x2tileView():    
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.HeaderbuttonChangeLayout).BlockByText("Change Layout").Click()
    Delay(500)
    #Clicks the 'control3' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ItemsControl.ItemscontrolBasic.control3.Click(38, 44)

def verify2x2tileIsOpened():
    Delay(1000)
    #Checks whether the 'Height' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect object equals 389.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect, "Height", cmpGreaterOrEqual, 380)
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect, "Height", cmpLessOrEqual, 400)
    #Checks whether the 'Width' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect object equals 799.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect, "Width", cmpGreaterOrEqual, 790)      
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect, "Width", cmpLessOrEqual, 810) 
    Delay(1000)      
       
def clickOn3x3tileView():
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.HeaderbuttonChangeLayout).BlockByText("Change Layout").Click()
    Delay(500)
    #Clicks the 'control2' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ItemsControl.ItemscontrolBasic.control4.Click(81, 55)

def verify3x3tileIsOpened():
    #Checks whether the 'Height' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect object equals 260.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect, "Height", cmpGreaterOrEqual, 255)
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect, "Height", cmpLessOrEqual, 265)
    #Checks whether the 'Width' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect object equals 533.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect, "Width", cmpGreaterOrEqual, 528)
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect, "Width", cmpLessOrEqual, 538)  
    Delay(1000)    
    
def clickOn4x4tileView():
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.HeaderbuttonChangeLayout).BlockByText("Change Layout").Click()
    Delay(500)
    #Clicks the 'control' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ItemsControl.ItemscontrolBasic.control.Click(58, 58)
    
def clickOn5x5tileView():
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.HeaderbuttonChangeLayout).BlockByText("Change Layout").Click()
    Delay(500)    
    #Clicks the 'control5' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ItemsControl.ItemscontrolBasic.control5.Click(47, 29)             
     
def clickOnVertical5x2Tile():
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.HeaderbuttonChangeLayout).BlockByText("Change Layout").Click()
    Delay(500)   
    #Clicks the 'control' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ItemsControl.ItemscontrolVertical.control.Click(66, 39)    
  
def CloseCurrentOpenViewLayout():
    #Clicks the 'TabitemView' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.TabitemView.Click(84, 13)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.Border.TextblockClickOnTheDesiredLayout object equals 'Click on the desired layout'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.Border.TextblockClickOnTheDesiredLayout, "WPFControlText", cmpEqual, "Click on the desired layout")

def clickOnHorizontal2Layout():
    Delay(500)
    #Clicks the 'control' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.ItemsControl.ItemscontrolHorizontal.Click(89, 50)
  
def clickOnVertical5Layout():  
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.HeaderbuttonChangeLayout).BlockByText("Change Layout").Click()
    Delay(500) 
    #Clicks the 'control2' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ItemsControl.control2.Click(46, 50)
  
def clickOnMixed7Layout():    
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.HeaderbuttonChangeLayout).BlockByText("Change Layout").Click()
    Delay(500) 
    #Clicks the 'control' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ItemsControl.ItemscontrolMixed.control.Click(61, 63)    
       
def verifyVertical5x2TileIsOpened():
    #Checks whether the 'Height' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect object equals 156.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect, "Height", cmpGreaterOrEqual, 151)
    Delay(300)
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect, "Height", cmpLessOrEqual, 161)
    Delay(300)
    #Checks whether the 'Width' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect object equals 799.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect, "Width", cmpGreaterOrEqual, 794)
    Delay(300)
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect, "Width", cmpLessOrEqual, 804)  
     
def collapseResourceTree():
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemUngrouped object equals 'UNGROUPED'.
    if Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemUngrouped.Visible:
       Log.Message("Resources are Visible on Monitoring page.")  
       OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl).BlockByText("<<").Click()
       Delay(1000)
       if Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemUngrouped.Exists:
          Log.Message("Resource tree is not collapsed - Test Case failed.")  
       else :
          Log.Message("Resource tree is now collapsed ")         
    else : 
       Log.Message("Resource tree is not present on page. May be Monitoring page is not opened.")   
       
def expandResourceTree():
    #Clicks the 'SliderControl' object. TO EXPAND RESOURCE TREE WHICH IS IN COLLAPSED STATE
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(15, 29)
    if Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemUngrouped.Exists:
       Log.Message("Resource tree is expanded.")  
    else :
       Log.Error("Resource tree is NOT Expanded - test Case Failed ") 

def fullScreen():
    #Clicks the 'Button' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.Button.ClickButton()
    #Clicks the 'Button' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.Button.ClickButton()
    Delay(500)
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.TextblockFullScreen, "WPFControlText", cmpEqual, "Full Screen")
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.TextblockPressEscToExitFullScreen object equals 'Press ESC to exit full screen'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.TextblockPressEscToExitFullScreen, "WPFControlText", cmpEqual, "Press ESC to exit full screen")
    Delay(2000)
    Sys.Keys("[Esc]")
    Delay(500)
 
def fullScreenRestartApp():
    cameraIPtoDragOnMonitoring = "172.20.0.238_Camera"
    #Clicks the 'Button' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.Button.ClickButton()
    #Enters '~[F4]' in the 'Button' object.
    Sys.Keys("~[F4]")
    Delay(500)
    #Runs the "Valerus" tested application.
    TestedApps.Valerus.Run(1, True)
    Delay(500)
    #Clicks the 'Password' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.Password.Click(145, 25)
    #Enters text in the 'Password' text editor.
    Delay(500)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.Password.SetText("1234")
    Sys.Keys("[Enter]")
    Delay(3000)
    #Checks whether the 'Visible' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.Border.TextblockClickOnTheDesiredLayout object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.HeaderbuttonChangeLayout, "WPFControlText", cmpEqual, "Change Layout")
    #Clicks the 'Button' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.Button.ClickButton()
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.TextblockFullScreen object equals 'Full Screen'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.TextblockFullScreen, "WPFControlText", cmpEqual, "Full Screen")
    #Enters '[Esc]' in the 'ctnt' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.ScrollViewer.ctnt.Keys("[Esc]")           
       
def dragAndDropCamera1OnMonitoring():
    #Clicks the 'SliderControl' object.
    cameraIP1 = Project.Variables.CameraIP1toDragOnMonitoring
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(120, 89)
    Delay(500)
    #Enters '172.20.0.223' in the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("^a")
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("[BS]")
    Delay(500)
    #Enters '172.20.0.238' in the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys(cameraIP1)
    Delay(2500)
    #Drags the 'RadTreeViewItem2' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadTreeViewItem2.Drag(103, 22, 282, 36)
    Delay(500)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption object equals '172.20.0.238_Camera'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption, "WPFControlText", cmpEqual, cameraIP1) 

def VerifyExpectedCamera1isDraggedOnMonitoring():
    cameraIP = Project.Variables.CameraIP1toDragOnMonitoring
    Delay(500)
#    #Checks whether the 'WPFControlText' property of the NameMapping.Sys.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption object equals '172.20.0.238_Camera'.
#    #Checks whether the 'Visibility' property of the NameMapping.Sys.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption object equals 'Visible'.
#    aqObject.CheckProperty(NameMapping.Sys.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption, "Visibility", cmpEqual, "Visible")
#    Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption object equals '172.20.0.238_Camera'.
    if  aqObject.CheckProperty(NameMapping.Sys.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption, "WPFControlText", cmpEqual, "172.20.0.238_Camera") :
       Delay(500)
       Log.Message("Expected camera is dragged on Monitoring page.")
       Delay(500)
    else :
       Log.Error("Expected camera is NOT present on Monitoring page.")
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(228, 88)
    Delay(500)

def exportFromCameraStreamOnMonitoringPage():
    cameraIP = Project.Variables.CameraIP1toDragOnMonitoring
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption object equals '172.20.0.238_Camera'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption, "WPFControlText", cmpEqual, cameraIP)
    #Clicks the 'menuToggleButton' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.GridContainer.menuToggleButton.Click(15, 11)
    #Clicks the 'HeaderButton' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.GridContainer.HeaderButton.Click(8, 14)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.TextblockExportForm object equals 'Export Form'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.TextblockExportForm, "WPFControlText", cmpEqual, "Export Form")
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.dtGrid2.Caption object equals '172.20.0.238_Camera'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.dtGrid2.Caption, "WPFControlText", cmpEqual, cameraIP)
    #Clicks the 'crossButton' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.crossButton.ClickButton()   
    
def clickOnResourceFromMonitoringTile():
    #Clicks the 'Close' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.GridContainer.Close.ClickButton()    
        
def dragAndDropCamera2OnMonitoring():
    #Clicks the 'SliderControl' object.
    cameraIP2 = Project.Variables.CameraIP2toDragOnMonitoring
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(120, 89)
    #Enters '172.20.0.223' in the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("^a")
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("[BS]")
    Delay(500)
    #Enters '172.20.0.223' in the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys(cameraIP2)
    Delay(1800)
    #Drags the 'RadTreeViewItem2' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadTreeViewItem2.Drag(83, 16, 295, 95)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption object equals '172.20.0.234_Camera'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption, "WPFControlText", cmpEqual, cameraIP2)
    Delay(500)
    #Clicks the 'VideoHeaderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.VideoHeaderControl.Click(97, 16)
    Delay(500)
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.GridContainer.Info object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.GridContainer.Info, "Enabled", cmpEqual, True)
    Log.Message("Expected camera is dragged on Monitoring page.")
    Delay(500)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(228, 88)
    Delay(500)      
 
def dragAndDropMic1OnMonitoring():
    #Clicks the 'SliderControl' object.
    MicIP = Project.Variables.MicIP1toDragOnMonitoring
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(120, 89)
    #Enters '172.20.0.223' in the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("^a")
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("[BS]")
    Delay(500)
    #Enters '172.20.0.223' in the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys(MicIP)
    Delay(1900)
    #Drags the 'RadTreeViewItem6' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadTreeViewItem2.Drag(124, 20, 458, 3)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption object equals '172.20.0.223_Camera'.
    Delay(500)
    #Clicks the 'AudioHeaderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.AudioHeaderControl.Click(76, 14)
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.GridContainer.Volume object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.GridContainer.Volume, "Enabled", cmpEqual, True)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption object equals '172.20.0.102_Mic'.
    if Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.AudioHeaderControl.Exists :
       aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect, "Height", cmpEqual, 81)
       Log.Message("Expected Mic is dragged on Monitoring page.")
    else :    
       Log.Message("Expected Mic is not dragged on Monitoring page.")
    Delay(500)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(228, 88)
    Delay(500)    

def dragAndDropMic2OnMonitoring():
    #Clicks the 'SliderControl' object.
    MicIP = Project.Variables.MicIP2toDragOnMonitoring
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(120, 89)
    #Enters '172.20.0.223' in the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("^a")
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("[BS]")
    Delay(500)
    #Enters '172.20.0.223' in the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys(MicIP)
    Delay(1900)
    #Drags the 'RadTreeViewItem6' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemUngrouped.RadTreeViewItem6.Drag(124, 20, 458, 3)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption object equals '172.20.0.223_Camera'.
    Delay(500)
    #Clicks the 'AudioHeaderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.AudioHeaderControl.Click(76, 14)
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.GridContainer.Volume object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.GridContainer.Volume, "Enabled", cmpEqual, True)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption object equals '172.20.0.102_Mic'.
    if Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.AudioHeaderControl.Exists :
       aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect, "Height", cmpEqual, 81)
       Log.Message("Expected Mic is dragged on Monitoring page.")
    else :    
       Log.Message("Expected Mic is not dragged on Monitoring page.")
    Delay(500)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(228, 88)
    Delay(500)    
        
def dragAndDropView1OnMonitoring():
    #Clicks the 'SliderControl' object.
    ViewName = Project.Variables.ViewName1TodragOnMonitoring
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(120, 89)
    #Enters '172.20.0.223' in the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("^a")
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("[BS]")
    Delay(500)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys(ViewName)
    Delay(1900)
    #Drags the 'RadTreeViewItem6' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemUngrouped.RadTreeViewItem6.Drag(82, 24, 271, 1)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption object equals '172.20.0.223_Camera'.
    Delay(1000)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.TabitemView1 object equals 'view_1'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.TabitemView1, "WPFControlText", cmpEqual, ViewName)
    Log.Message("Expected View is dragged on Monitoring page.")
    Delay(500)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(228, 88)
    Delay(500)    
    
def dragAndDropView2OnMonitoring():
    #Clicks the 'SliderControl' object.
    ViewName = Project.Variables.ViewName2TodragOnMonitoring
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(120, 89)
    #Enters '172.20.0.223' in the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("^a")
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("[BS]")
    Delay(500)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys(ViewName)
    Delay(2000)
    #Drags the 'RadTreeViewItem6' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemUngrouped.RadTreeViewItem6.Drag(84, 21, 279, 3)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption object equals '172.20.0.223_Camera'.
    Delay(3000)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.TabitemView2 object equals 'view_2'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.TabitemView2, "WPFControlText", cmpEqual, "view_2")
    #Clicks the 'menuToggleButton' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.GridContainer.menuToggleButton.Click(10, 13)
    Delay(500)
    #Clicks the 'menuToggleButton' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.GridContainer.menuToggleButton.Click(10, 13)
    Delay(500)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption object equals '172.20.0.223_Camera'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption, "WPFControlText", cmpEqual, "172.20.0.223_Camera")
    Delay(800)
    #Clicks the 'menuToggleButton' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.GridContainer.menuToggleButton.Click(8, 8)
    Delay(500)
    #Clicks the 'menuToggleButton' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.GridContainer.menuToggleButton.Click(13, 7)
    Delay(500)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption object equals '172.20.0.225_Camera'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption, "WPFControlText", cmpEqual, "172.20.0.225_Camera")
    Delay(800)
    #Clicks the 'menuToggleButton' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.GridContainer.menuToggleButton.Click(14, 12)
    Delay(500)
    #Clicks the 'menuToggleButton' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.GridContainer.menuToggleButton.Click(14, 12)
    Delay(500)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption object equals '172.20.0.237_Camera'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption, "WPFControlText", cmpEqual, "172.20.0.237_Camera")
    Delay(800)
    #Clicks the 'menuToggleButton' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.GridContainer.menuToggleButton.Click(9, 9)
    Delay(500)
    #Clicks the 'menuToggleButton' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.GridContainer.menuToggleButton.Click(9, 9)
    Delay(500)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption object equals '172.20.0.238_Camera'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption, "WPFControlText", cmpEqual, "172.20.0.238_Camera")
    Delay(800)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption object equals '6_Selenium'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption, "WPFControlText", cmpEqual, "6_Selenium")
    Delay(800)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption object equals '5_Vicon'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption, "WPFControlText", cmpEqual, "5_Vicon")
    Delay(800)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption object equals '3_NDTV'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption, "WPFControlText", cmpEqual, "3_NDTV")
    Delay(800)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption object equals '4_ZeeNews'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption, "WPFControlText", cmpEqual, "4_ZeeNews")
    Delay(800)
    #Clicks the 'AudioHeaderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.AudioHeaderControl.Click(49, 14)
    Delay(500)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption object equals '172.20.0.238_Mic'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption, "WPFControlText", cmpEqual, "172.20.0.238_Mic")
    Delay(800)
    #Clicks the 'AudioHeaderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.AudioHeaderControl.Click(112, 19)
    Delay(500)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption object equals '172.20.0.234_Mic'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption, "WPFControlText", cmpEqual, "172.20.0.234_Mic")
    Delay(800)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.HeaderbuttonStopAll).BlockByText("All").Click()
    Delay(1000)
    #Clicks the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(225, 91)
    
    Log.Message("Expected View is dragged on Monitoring page.")
    Delay(500)
    
def dragAndDropView5x5OnMonitoring():
    #Clicks the 'SliderControl' object.
    ViewName = Project.Variables.ViewName5x5ToDragOnMonitoring
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(120, 89)
    #Enters '172.20.0.223' in the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("^a")
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("[BS]")
    Delay(500)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys(ViewName)
    Delay(1900)
    #Drags the 'RadTreeViewItem6' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemUngrouped.RadTreeViewItem6.Drag(82, 24, 265, 1)
    Delay(1000)       
    
def dragAndDropTour1OnMonitoring():
    #Clicks the 'SliderControl' object.
    TourName = Project.Variables.TourName1ToDragOnMonitoring
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(120, 89)
    #Enters '172.20.0.223' in the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("^a")
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("[BS]")
    Delay(500)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys(TourName)
    Delay(1900)
    #Drags the 'RadTreeViewItem6' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemUngrouped.RadTreeViewItem6.Drag(89, 23, 305, 12)
    Delay(1000)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.TabitemTour1 object equals 'tour1'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.TabitemTour1, "WPFControlText", cmpEqual, TourName)
    Log.Message("Expected Tour is dragged on Monitoring page.")
    Delay(500)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(228, 88)
    Delay(500)

def dragAndDropTour2OnMonitoring():
    #Clicks the 'SliderControl' object.
    TourName = Project.Variables.TourName2ToDragOnMonitoring
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(120, 89)
    #Enters '172.20.0.223' in the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("^a")
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("[BS]")
    Delay(500)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys(TourName)
    Delay(1900)
    #Drags the 'RadTreeViewItem6' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemUngrouped.RadTreeViewItem6.Drag(89, 23, 305, 12)
    Delay(1000)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.TabitemTour1 object equals 'tour1'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.TabitemTour1, "WPFControlText", cmpEqual, TourName)
    Log.Message("Expected Tour is dragged on Monitoring page.")
    Delay(500)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(228, 88)
    Delay(500)    
        
def dragAndDropWebpage1OnMonitoring():
    #Clicks the 'SliderControl' object.
    WebPageName = Project.Variables.Webpage1ToDragOnMonitoring
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(120, 89)
    #Enters '172.20.0.223' in the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("^a")
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("[BS]")
    Delay(500)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys(WebPageName)
    Delay(1900)
    #Drags the 'RadTreeViewItem6' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemUngrouped.RadTreeViewItem6.Drag(109, 19, 339, 23)
    Delay(500)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption object equals 'weblink1'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption, "WPFControlText", cmpEqual, WebPageName)
    #Clicks the 'menuToggleButton' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.GridContainer.menuToggleButton.Click(10, 11)
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.GridContainer.HeaderButton object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.GridContainer.HeaderButton, "Enabled", cmpEqual, True)
    Log.Message("Expected Webpage is dragged on Monitoring page.")
    Delay(500)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(228, 88)
    Delay(500)   
    
def dragAndDropWebpage2OnMonitoring():
    #Clicks the 'SliderControl' object.
    WebPageName = Project.Variables.Webpage2ToDragOnMonitoring
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(120, 89)
    #Enters '172.20.0.223' in the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("^a")
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("[BS]")
    Delay(500)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys(WebPageName)
    Delay(1900)
    #Drags the 'RadTreeViewItem6' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemUngrouped.RadTreeViewItem6.Drag(109, 19, 339, 23)
    Delay(500)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption object equals 'weblink1'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption, "WPFControlText", cmpEqual, WebPageName)
    #Clicks the 'menuToggleButton' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.GridContainer.menuToggleButton.Click(10, 11)
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.GridContainer.HeaderButton object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.GridContainer.HeaderButton, "Enabled", cmpEqual, True)
    Log.Message("Expected Webpage is dragged on Monitoring page.")
    Delay(500)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(228, 88)
    Delay(500)    
                 
def dragAndDropMap1OnMonitoring():
    #Clicks the 'SliderControl' object.
    MapName = Project.Variables.Map1ToDragOnMonitoring
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(120, 89)
    #Enters '172.20.0.223' in the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("^a")
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("[BS]")
    Delay(500)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys(MapName)
    Delay(1900)
    #Drags the 'RadTreeViewItem6' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemUngrouped.RadTreeViewItem6.Drag(86, 16, 278, 7)
    Delay(500)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption object equals 'weblink1'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption, "WPFControlText", cmpEqual, MapName)
    Delay(500)
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.ChromiumWebBrowserConfigurationHomePage object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.ChromiumWebBrowserConfigurationHomePage, "Enabled", cmpEqual, True)
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.ChromiumWebBrowserConfigurationHomePage object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.ChromiumWebBrowserConfigurationHomePage, "Enabled", cmpEqual, True)
    #Checks whether the 'VisibleOnScreen' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.ChromiumWebBrowserConfigurationHomePage object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.ChromiumWebBrowserConfigurationHomePage, "VisibleOnScreen", cmpEqual, True)
    #Checks whether the 'VisibleOnScreen' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.ChromiumWebBrowserConfigurationHomePage object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.ChromiumWebBrowserConfigurationHomePage, "VisibleOnScreen", cmpEqual, True)
    Log.Message("Expected Map is dragged on Monitoring page.")
    Delay(500)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(228, 88)
    Delay(500)   

def dragAndDropMap2OnMonitoring():
    #Clicks the 'SliderControl' object.
    MapName = Project.Variables.Map2ToDragOnMonitoring
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(120, 89)
    #Enters '172.20.0.223' in the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("^a")
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("[BS]")
    Delay(500)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys(MapName)
    Delay(1900)
    #Drags the 'RadTreeViewItem6' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemUngrouped.RadTreeViewItem6.Drag(86, 16, 278, 7)
    Delay(500)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption object equals 'weblink1'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption, "WPFControlText", cmpEqual, MapName)
    Delay(500)
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.ChromiumWebBrowserConfigurationHomePage object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.ChromiumWebBrowserConfigurationHomePage, "Enabled", cmpEqual, True)
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.ChromiumWebBrowserConfigurationHomePage object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.ChromiumWebBrowserConfigurationHomePage, "Enabled", cmpEqual, True)
    #Checks whether the 'VisibleOnScreen' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.ChromiumWebBrowserConfigurationHomePage object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.ChromiumWebBrowserConfigurationHomePage, "VisibleOnScreen", cmpEqual, True)
    #Checks whether the 'VisibleOnScreen' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.ChromiumWebBrowserConfigurationHomePage object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.ChromiumWebBrowserConfigurationHomePage, "VisibleOnScreen", cmpEqual, True)
    Log.Message("Expected Map is dragged on Monitoring page.")
    Delay(500)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(228, 88)
    Delay(500)       
    
def dragAndDropVAXdoor1OnMonitoring():
    #Clicks the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(120, 89)
    #Enters '172.20.0.223' in the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("^a")
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("[BS]")
    Delay(300)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("Door")
    Delay(1900)
    #Drags the 'RadTreeViewItem6' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemUngrouped.RadTreeViewItem6.Drag(109, 19, 339, 23)
    Delay(500)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption object equals 'weblink1'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption, "WPFControlText", cmpContains, "Door")
    Delay(200)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.TextblockWaitingForEventData object equals 'Waiting for event data'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.TextblockWaitingForEventData, "WPFControlText", cmpEqual, "Waiting for event data")
    Log.Message("Expected VAX Door is dragged on Monitoring page.")
    Delay(200)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(228, 88)
    Delay(300)    
    
def visiblityOfRelayOutput():
    relayOutput = Project.Variables.RelayDeviceOnMonitoring
    #Clicks the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(120, 89)
    #Enters '172.20.0.223' in the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("^a")
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("[BS]")
    Delay(300)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys(relayOutput)
    Delay(2000)
    #Checks whether the 'Visibility' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadTreeViewItem2 object equals 'Visible'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadTreeViewItem2, "Visibility", cmpEqual, "Visible")
    Delay(300)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(228, 88)
    Delay(300)         
       
def clickOnStopAllBtn():
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.HeaderbuttonStopAll).BlockByText("Stop All").Click()
    #Clicks the 'SliderControl' object.
    Delay(500)    
    Log.Message("Clicked on Stop All button.")  
       
def verifyCameraAndMicAreStopped() :
    if Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption.Exists :
       Log.Message("Camera stream is not stopped.")
       Delay(500)
    elif Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.AudioHeaderControl.Exists :   
       Log.Message("Camera stream is not stopped.")
       Delay(500)
    else :   
       Log.Message("All player windows are stopped.")
       Delay(500)

def ClickOnUngrouped():
    #Clicks the 'RadtreeviewitemUngrouped' object.
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemUngrouped).BlockByText("UNGROUPED", spNearestToCenter).DblClick()
    Delay(2000)
    
def verifyResourcesAreHiddenUnderUngrouped():    
    if Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemUngrouped.RadTreeViewItem6.Exists :
       Log.Message("All listed resources are Visible.")
    else :
       Log.Message("Ungrouped resource tree is not Visisble to user.")

def closeResourceFromMonitoring():
    #Clicks the 'Close' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.GridContainer.Close.ClickButton()              

def verifyResourceIsClosed():
    #Clicks the 'Close' button.
    if Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.GridContainer.Close.Exists :
       Log.Error("Resource is not closed from Monitoring page")
    else :
       Log.Message("Resource is closed from Monitoring page")  
              
def rightClickOptionsOfCamera():
    #Clicks the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(138, 87)
    #Enters '172.20.0.238_Camera' in the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("^a")
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("[BS]")
    Delay(500)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("172.20.0.238_Camera")
    Delay(1900)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemUngrouped.RadTreeViewItem6).BlockByText("172.20.0.238_Camera").ClickR()
    Delay(500)
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuItem object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuItem, "Enabled", cmpEqual, True)     
    Delay(500)
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuItem2 object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuItem2, "Enabled", cmpEqual, True)    
    Delay(500)
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuItem3 object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuItem3, "Enabled", cmpEqual, True)    
    Delay(500)
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuItem4 object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuItem4, "Enabled", cmpEqual, True)    
    Delay(500)
    
def cameraRightClickOptionsToThumbnailSearchPage():
    #Clicks the '[0]' item of the 'ContextMenu' bar.
    Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.ClickItem("[0]")
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextblockThumbnailSearch object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextblockThumbnailSearch, "Enabled", cmpEqual, True)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextblockThumbnailSearch object equals 'Thumbnail Search'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextblockThumbnailSearch, "WPFControlText", cmpEqual, "Thumbnail Search")
    Delay(500)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.TabitemMonitoring).BlockByText("MONITORING").Click()  
    Delay(300)
    #Clicks the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(226, 87)
            
def cameraRightClickOptionsToMuseumSearchPage():
    #Clicks the '[1]' item of the 'ContextMenu' bar.
    Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.ClickItem("[1]")
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextblockMuseumSearch object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextblockMuseumSearch, "Enabled", cmpEqual, True)
    Delay(300)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextblockMuseumSearch object equals 'Museum Search'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextblockMuseumSearch, "WPFControlText", cmpEqual, "Museum Search")
    Delay(300)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.TabitemMonitoring).BlockByText("MONITORING").Click()
    Delay(300)
    #Clicks the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(226, 87)              
       
def cameraRightClickToExport():    
    #Clicks the '[2]' item of the 'ContextMenu' bar.
    Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.ClickItem("[2]")
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.TextblockExportForm object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.TextblockExportForm, "Enabled", cmpEqual, True)
    Delay(200)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.TextblockExportForm object equals 'Export Form'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.TextblockExportForm, "WPFControlText", cmpEqual, "Export Form")
    Delay(200)
    #Clicks the 'crossButton' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.crossButton.ClickButton()
    Delay(300)
    
def rightClickOptionsOfMic():    
    #Clicks the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(138, 87)
    #Enters '172.20.0.238_Camera' in the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("^a")
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("[BS]")
    Delay(300)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys(Project.Variables.MicIP1toDragOnMonitoring)
    Delay(1900)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemUngrouped.RadTreeViewItem6).BlockByText("172.20.0.238_Mic").ClickR()
    Delay(500)
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuItem object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuItem, "Enabled", cmpEqual, True)
    Delay(200)
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuItem2 object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuItem2, "Enabled", cmpEqual, True)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(229, 88)

def micRightClickToExport():
      #Clicks the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(138, 87)
    #Enters '172.20.0.238_Camera' in the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("^a")
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("[BS]")
    Delay(300)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys(Project.Variables.MicIP1toDragOnMonitoring)
    Delay(1900)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemUngrouped.RadTreeViewItem6).BlockByText("172.20.0.238_Mic").ClickR()
    Delay(500)
    #Clicks the '[0]' item of the 'ContextMenu' bar.
    Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.ClickItem("[0]")
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.TextblockExportForm object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.TextblockExportForm, "Enabled", cmpEqual, True)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.TextblockExportForm object equals 'Export Form'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.TextblockExportForm, "WPFControlText", cmpEqual, "Export Form")
    #Clicks the 'crossButton' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.crossButton.ClickButton()    
       
def rightClickOptionsOfView():    
     #Clicks the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(138, 87)
    #Enters '172.20.0.238_Camera' in the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("^a")
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("[BS]")
    Delay(300)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys(Project.Variables.ViewName1ToDragOnMonitoring)
    Delay(1900)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemUngrouped.RadTreeViewItem6).BlockByText(Project.Variables.ViewName1ToDragOnMonitoring).ClickR()
    Delay(1000)
    #Checks whether the 'VisibleOnScreen' property of the Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuItem object equals False.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuItem, "VisibleOnScreen", cmpEqual, True)
    Delay(1000)
    #Checks whether the 'VisibleOnScreen' property of the Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuItem2 object equals False.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuItem2, "VisibleOnScreen", cmpEqual, True)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(229, 88)
      
def viewRightClickToExport():
    #Clicks the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(138, 87)
    #Enters '172.20.0.238_Camera' in the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("^a")
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("[BS]")
    Delay(300)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys(Project.Variables.ViewName1ToDragOnMonitoring)
    Delay(1900)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemUngrouped.RadTreeViewItem6).BlockByText(Project.Variables.ViewName1ToDragOnMonitoring).ClickR()
    Delay(500)
    #Clicks the '[0]' item of the 'ContextMenu' bar.
    Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.ClickItem("[1]")
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.TextblockExportForm object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.TextblockExportForm, "Enabled", cmpEqual, True)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.TextblockExportForm object equals 'Export Form'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.TextblockExportForm, "WPFControlText", cmpEqual, "Export Form")
    #Clicks the 'crossButton' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.crossButton.ClickButton()    
      
def rightClickOptionsOfTour():    
     #Clicks the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(138, 87)
    #Enters '172.20.0.238_Camera' in the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("^a")
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("[BS]")
    Delay(300)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys(Project.Variables.TourName1ToDragOnMonitoring)
    Delay(1900)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemUngrouped.RadTreeViewItem6).BlockByText(Project.Variables.TourName1ToDragOnMonitoring).ClickR()
    Delay(1000)
    #Checks whether the 'IsVisible' property of the Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuItem object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuItem, "IsVisible", cmpEqual, True)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(229, 88)       
    
def rightClickOptionsOfWebLink():    
     #Clicks the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(138, 87)
    #Enters '172.20.0.238_Camera' in the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("^a")
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("[BS]")
    Delay(300)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys(Project.Variables.Webpage1ToDragOnMonitoring)
    Delay(1900)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemUngrouped.RadTreeViewItem6).BlockByText(Project.Variables.Webpage1ToDragOnMonitoring).ClickR()
    Delay(1000)
    #Checks whether the 'IsVisible' property of the Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuItem object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuItem, "IsVisible", cmpEqual, True)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(229, 88)    
      
def rightClickOptionsOfRelayDevice():    
    #Clicks the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(138, 87)
    #Enters '172.20.0.238_Camera' in the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("^a")
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("[BS]")
    Delay(300)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys(Project.Variables.RelayDeviceOnMonitoring)
    Delay(1900)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemUngrouped.RadTreeViewItem6).BlockByText("172.20.0.238_Relay").ClickR()
    Delay(300)
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuItem object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuItem, "Enabled", cmpEqual, True)
    Delay(500)
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuItem2 object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuItem2, "Enabled", cmpEqual, True)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(229, 88)
    
def rightClickOptionsOfMap():
    #Clicks the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(138, 87)
    #Enters '172.20.0.238_Camera' in the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("^a")
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("[BS]")
    Delay(300)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys(Project.Variables.Map1ToDragOnMonitoring)
    Delay(1000)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemUngrouped.RadTreeViewItem6).BlockByText("Map1").ClickR()
    Delay(300)
    #Checks whether the 'IsVisible' property of the Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuItem object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuItem, "IsVisible", cmpEqual, True)
    Delay(300)
    #Checks whether the 'IsVisible' property of the Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuItem2 object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuItem2, "IsVisible", cmpEqual, True)
    #Clicks the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(224, 84)
    
def mapRightClickToViewMapGallary():
    #Clicks the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(138, 87)
    #Enters '172.20.0.238_Camera' in the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("^a")
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("[BS]")
    Delay(300)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys(Project.Variables.Map1ToDragOnMonitoring)
    Delay(1000)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemUngrouped.RadTreeViewItem6).BlockByText("Map1").ClickR()
    Delay(300)
    #Checks whether the 'IsVisible' property of the Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuItem object equals True.
    Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuItem.Click()
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.TextblockMapGallery object equals 'Map Gallery'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.TextblockMapGallery, "WPFControlText", cmpEqual, "Map Gallery")
    Delay(500)
    #Sets the 'VScroll' scroll bar thumb to position 0.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ScrollViewer.VScroll.Pos = 0
    Delay(500)
    #Clicks the 'ChromiumWebBrowser' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ItemsControl.ChromiumWebBrowser.Click(196, 94)
    Delay(500)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ItemsControl.IconButton).BlockByText("this").Click()
    Delay(300)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption object equals 'Map1'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption, "WPFControlText", cmpEqual, "Map1")
    Delay(300)
    #Checks whether the 'IsVisible' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.ChromiumWebBrowserConfigurationHomePage object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.ChromiumWebBrowserConfigurationHomePage, "IsVisible", cmpEqual, True)
    Delay(300)
    #Checks whether the 'IsVisible' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.ChromiumWebBrowserConfigurationHomePage object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.ChromiumWebBrowserConfigurationHomePage, "IsVisible", cmpEqual, True)
    Delay(300)
    #Checks whether the 'IsVisible' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.ChromiumWebBrowserConfigurationHomePage object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.ChromiumWebBrowserConfigurationHomePage, "IsVisible", cmpEqual, True)
    Delay(300)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(229, 88)
    
def rightClickOptionsOfVAXactionPlan():
    #Clicks the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(138, 87)
    #Enters '172.20.0.238_Camera' in the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("^a")
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("[BS]")
    Delay(300)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys(Project.Variables.VAXActionPlanFromMonitoring)
    Delay(1900)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemUngrouped.RadTreeViewItem6).BlockByText("VAX_QA_Action").ClickR()
    Delay(500)
    #Checks whether the 'IsVisible' property of the Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuItem object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuItem, "IsVisible", cmpEqual, True)
    Delay(300)
    #Checks whether the 'IsVisible' property of the Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuItem2 object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuItem2, "IsVisible", cmpEqual, True)
    Delay(300)
    #Clicks the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(226, 86) 
    
def rightClickOptionsOfVAXDoors():
    #Clicks the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(138, 87)
    #Enters '172.20.0.238_Camera' in the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("^a")
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("[BS]")
    Delay(300)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys(Project.Variables.VAXdoorToDragOnMonitoring)
    Delay(1000)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemUngrouped.RadTreeViewItem6).BlockByText("Demo").ClickR()
    Delay(500)
    #Checks whether the 'IsVisible' property of the Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuItem object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuItem, "IsVisible", cmpEqual, True)
    #Clicks the 'RadTreeViewItem' object with the right mouse button.
    Delay(300)
    #Checks whether the 'IsVisible' property of the Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuItem2 object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuItem2, "IsVisible", cmpEqual, True)
    Delay(300)
    #Checks whether the 'IsVisible' property of the Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuItem3 object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.MenuItem3, "IsVisible", cmpEqual, True)
    Delay(300)
    
def rightClickOptionsOfVAXDoors_OverrideSubOptions():   
    #Clicks the '[2]' item of the 'ContextMenu' bar.
    Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.ContextMenu.ClickItem("[2]")
    #Checks whether the 'IsVisible' property of the Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.MenuItem object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.MenuItem, "IsVisible", cmpEqual, True)
    Delay(300)
    #Checks whether the 'IsVisible' property of the Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.MenuItem2 object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.MenuItem2, "IsVisible", cmpEqual, True)
    Delay(300)
    #Checks whether the 'IsVisible' property of the Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.MenuItem3 object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.MenuItem3, "IsVisible", cmpEqual, True)
    Delay(300)
    #Checks whether the 'IsVisible' property of the Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.MenuItem4 object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.MenuItem4, "IsVisible", cmpEqual, True)
    Delay(300)
    #Checks whether the 'IsVisible' property of the Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.MenuItem5 object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.MenuItem5, "IsVisible", cmpEqual, True)
    Delay(300)
    #Checks whether the 'IsVisible' property of the Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.MenuItem6 object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.MenuItem6, "IsVisible", cmpEqual, True)
    Delay(300)
    #Checks whether the 'IsVisible' property of the Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.MenuItem7 object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.MenuItem7, "IsVisible", cmpEqual, True)
    Delay(300)
    #Checks whether the 'IsVisible' property of the Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.MenuItem8 object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.MenuItem8, "IsVisible", cmpEqual, True)
    
def dragAndDropCamera1InFirstTileOf2x2OnMonitoring():
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(120, 89)
    #Enters '172.20.0.223' in the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("^a")
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("[BS]")
    Delay(500)
    #Enters '172.20.0.223' in the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys(Project.Variables.CameraIP1toDragOnMonitoring)
    Delay(2000)
    #Drags the 'RadTreeViewItem6' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadTreeViewItem.Drag(76, 18, 384, 19)
    Delay(500)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption object equals '172.20.0.238_Camera'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption, "WPFControlText", cmpEqual, "172.20.0.238_Camera") 

def dragAndDropCamera1InFirstTileOf3x3OnMonitoring():
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(120, 89)
    #Enters '172.20.0.223' in the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("^a")
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("[BS]")
    Delay(500)
    #Enters '172.20.0.223' in the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys(Project.Variables.CameraIP1toDragOnMonitoring)
    Delay(2000)
    #Drags the 'RadTreeViewItem6' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadTreeViewItem.Drag(76, 18, 384, 19)
    Delay(500)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption object equals '172.20.0.238_Camera'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption, "WPFControlText", cmpEqual, "172.20.0.238_Camera")    
         
def dragAndDropCamera2InSecondTileOf2x2OnMonitoring():
    CameraIP2 = Project.Variables.CameraIP2toDragOnMonitoring
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(120, 89)
    #Enters '172.20.0.223' in the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("^a")
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("[BS]")
    Delay(500)
    #Enters '172.20.0.223' in the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys(CameraIP2)
    Delay(2000)
    #Drags the 'RadTreeViewItem' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadTreeViewItem.Drag(127, 24, 1167, 93)
    Delay(500)
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.GridContainer object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.GridContainer, "Enabled", cmpEqual, True)
        
def doubleClickOnCameraTitle():    
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.brdSelect.Caption.DblClick()

def detachSingleVideoChannelOn1x1Tile():
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.TxtMonitorId object equals '1'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.TxtMonitorId, "WPFControlText", cmpEqual, "1")
    #Clicks the 'TabitemView' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.TabitemView.Click(65, 33)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.tabView.Caption object equals '172.20.0.238_Camera'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.tabView.Caption, "WPFControlText", cmpEqual, Project.Variables.CameraIP1toDragOnMonitoring)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.TxtMonitorId object equals '2'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.TxtMonitorId, "WPFControlText", cmpEqual, "2")
    #Clicks the 'WindowButtonCommands' object.
    Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.WindowButtonCommands.Click(120, 19)    
    
def detachSingleAudioChannelOn1x1Tile():
    #Clicks the 'TabitemView' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.TabitemView.Click(66, 32)
    #Double-clicks the 'parent' object.
    Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.DblClick(349, 16)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.tabView.Caption object equals '172.20.0.238_Mic'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.tabView.Caption, "WPFControlText", cmpEqual, "172.20.0.238_Mic")
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.TxtMonitorId object equals '2'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.TxtMonitorId, "WPFControlText", cmpEqual, "2")
    #Clicks the 'WindowButtonCommands' object.
    Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.WindowButtonCommands.Click(104, 16)    
    
def detachSingleMapOn1x1Tile():
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.TxtMonitorId object equals '1'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.TxtMonitorId, "WPFControlText", cmpEqual, "1")
    #Clicks the 'TabitemView' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.TabitemView.Click(63, 31)
    #Double-clicks the 'parent' object.
    Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.DblClick(225, 13)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.TxtMonitorId object equals '2'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.TxtMonitorId, "WPFControlText", cmpEqual, "2")
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.tabView.Caption object equals 'Map1'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.tabView.Caption, "WPFControlText", cmpEqual, "Map1")
    #Checks whether the 'IsVisible' property of the Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.tabView.ChromiumWebBrowser object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.tabView.ChromiumWebBrowser, "IsVisible", cmpEqual, True)
    #Checks whether the 'IsVisible' property of the Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.tabView.ChromiumWebBrowser object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.tabView.ChromiumWebBrowser, "IsVisible", cmpEqual, True)
    #Checks whether the 'IsVisible' property of the Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.tabView.ChromiumWebBrowser object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.tabView.ChromiumWebBrowser, "IsVisible", cmpEqual, True)
    #Clicks the 'WindowButtonCommands' object.
    Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.WindowButtonCommands.Click(113, 20)    
    
def detachView():
    cameraIPtoDragOnMonitoring = "172.20.0.238_Camera"
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.TxtMonitorId object equals '1'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.TxtMonitorId, "WPFControlText", cmpEqual, "1")
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.TabitemView1 object equals 'view_1'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.TabitemView1, "WPFControlText", cmpEqual, "view_1")
    #Clicks the 'TabitemView1' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.TabitemView1.Click(88, 31)
    #Double-clicks the 'parent' object.
    Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.DblClick(436, 20)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.TxtMonitorId object equals '2'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.TxtMonitorId, "WPFControlText", cmpEqual, "2")
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.HeaderbuttonChangeLayout object equals 'Change Layout'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.HeaderbuttonChangeLayout, "WPFControlText", cmpEqual, "Change Layout")
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.HeaderbuttonStopAll object equals 'Stop All'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.HeaderbuttonStopAll, "WPFControlText", cmpEqual, "Stop All")
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.HeaderbuttonExport object equals 'Export'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.HeaderbuttonExport, "WPFControlText", cmpEqual, "Export")
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.tabView.TabitemView1 object equals 'view_1'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.tabView.TabitemView1, "WPFControlText", cmpEqual, "view_1")
    #Clicks the 'WindowButtonCommands' object.
    Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.WindowButtonCommands.Click(111, 7)    
        
def detachTour():
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.TxtMonitorId object equals '1'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.TxtMonitorId, "WPFControlText", cmpEqual, "1")
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.TabitemTour1 object equals 'tour1'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.TabitemTour1, "WPFControlText", cmpEqual, "tour1")
    #Clicks the 'TabitemTour1' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.TabitemTour1.Click(69, 31)
    #Double-clicks the 'parent' object.
    Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.DblClick(326, 15)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.TxtMonitorId object equals '2'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.TxtMonitorId, "WPFControlText", cmpEqual, "2")
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.HeaderbuttonChangeLayout object equals 'Change Layout'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.HeaderbuttonChangeLayout, "WPFControlText", cmpEqual, "Change Layout")
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.HeaderbuttonStopAll object equals 'Stop All'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.HeaderbuttonStopAll, "WPFControlText", cmpEqual, "Stop All")
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.HeaderbuttonPauseTour object equals 'Pause Tour'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.HeaderbuttonPauseTour, "WPFControlText", cmpEqual, "Pause Tour")
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.tabView.TabitemTour1 object equals 'tour1'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.tabView.TabitemTour1, "WPFControlText", cmpEqual, "tour1")
    #Clicks the 'WindowButtonCommands' object.
    Aliases.Valerus_Bootstrapper.HwndSource_parent.parent.WindowButtonCommands.Click(114, 6)       
    
def clickOnExportTab():
    #Clicks the 'HeaderbuttonExport' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.HeaderbuttonExport.Click()
    Delay(500)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.TextblockExportForm object equals 'Export Form'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.TextblockExportForm, "WPFControlText", cmpEqual, "Export Form")   
    
def ExportTabFeature():
    #Clicks the 'ButtonAddResource' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ButtonAddResource.ClickButton()
    #Clicks the 'TextBox' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.TextBox.Click(149, 21)
    #Enters the text '172.20.0.238_Camera' in the 'TextBox' text editor.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.TextBox.SetText("172.20.0.238_Camera")
    #Checks whether the 'wText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.TextBox object equals '172.20.0.238_Camera'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.TextBox, "wText", cmpEqual, "172.20.0.238_Camera")
    #Sets the state of the 'CheckBox' check box to cbChecked.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.dtGrid.CheckBox.ClickButton(cbChecked)
    #Clicks the 'ButtonAddAndClose' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ButtonAddAndClose.ClickButton()
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.Caption object equals '172.20.0.238_Camera'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.Caption, "WPFControlText", cmpEqual, "172.20.0.238_Camera")
    #Clicks the 'btnExport' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.btnExport.ClickButton()
    #Sets the 'ToggleButton' toggle button to the cbChecked state.
    Sys.keys("~[F4]")
    Delay(3000)
    #Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.ToggleButton.ClickButton(cbChecked)
    commonUtility.Login()
    Delay(9000)
    Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.listDownload.btnDownload.WaitAliasChild(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.listDownload.btnDownload, [60])
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.listDownload.btnDownload, "WPFControlText", cmpEqual, "Download")

def exportWithoutCamera():
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.HeaderbuttonStopAll).BlockByText("Stop").Click()
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.HeaderbuttonExport).BlockByText("Export").Click()
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.TextblockExportForm object equals 'Export Form'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.TextblockExportForm, "WPFControlText", cmpEqual, "Export Form")
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.btnExport object equals False.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.btnExport, "Enabled", cmpEqual, False)
    #Clicks the 'crossButton' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.crossButton.ClickButton()


def Filter():
        #Clicks the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Click(120, 89)
    #Enters '172.20.0.223' in the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("^a")
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("[BS]")
    Delay(300)
    #Enters '172.20.0.238' in the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("172.20.0.238")
    #Checks whether the 'Visibility' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadTreeViewItem object equals 'Visible'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadTreeViewItem, "Visibility", cmpEqual, "Visible")
    #Checks whether the 'Visibility' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadTreeViewItem2 object equals 'Visible'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadTreeViewItem2, "Visibility", cmpEqual, "Visible")
    #Checks whether the 'Visibility' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadTreeViewItem3 object equals 'Visible'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadTreeViewItem3, "Visibility", cmpEqual, "Visible")
    #Enters '_Camera' in the 'SliderControl' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.Keys("_Camera")
    #Checks whether the 'Visibility' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadTreeViewItem object equals 'Visible'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadTreeViewItem, "Visibility", cmpEqual, "Visible")    
  
      
def verifyDefaultMonitoringPageStateIsOpened():
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.Border.TextblockClickOnTheDesiredLayout object equals 'Click on the desired layout'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.Border.TextblockClickOnTheDesiredLayout, "WPFControlText", cmpEqual, "Click on the desired layout")

def Test1__SortOrder():
    cameraIPtoDragOnMonitoring = "172.20.0.238_Camera"
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl).BlockByText("!!!", spRightMost).Click()
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemAudioChannels object equals 'Audio Channels'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemAudioChannels, "WPFControlText", cmpEqual, "Audio Channels")
    #Clicks the 'RadtreeviewitemAudioChannels' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemAudioChannels.Click(17, 28)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemMap object equals 'Map'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemMap, "WPFControlText", cmpEqual, "Map")
    #Clicks the 'RadtreeviewitemMap' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemMap.Click(18, 27)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemRelayOutput object equals 'Relay Output'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemRelayOutput, "WPFControlText", cmpEqual, "Relay Output")
    #Clicks the 'RadtreeviewitemRelayOutput' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemRelayOutput.Click(19, 28)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemTour object equals 'Tour'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemTour, "WPFControlText", cmpEqual, "Tour")
    #Clicks the 'RadtreeviewitemTour' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemTour.Click(20, 27)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemVaxActionPlan object equals 'VAX Action Plan'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemVaxActionPlan, "WPFControlText", cmpEqual, "VAX Action Plan")
    #Clicks the 'RadtreeviewitemVaxActionPlan' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemVaxActionPlan.Click(20, 27)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemVaxDoorResource object equals 'VAX Door Resource'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemVaxDoorResource, "WPFControlText", cmpEqual, "VAX Door Resource")
    #Clicks the 'RadtreeviewitemVaxDoorResource' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemVaxDoorResource.Click(19, 25)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemVideoChannels2 object equals 'Video Channels'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemVideoChannels2, "WPFControlText", cmpEqual, "Video Channels")
    #Clicks the 'RadtreeviewitemVideoChannels2' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemVideoChannels2.Click(19, 28)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemView object equals 'View'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemView, "WPFControlText", cmpEqual, "View")
    #Clicks the 'RadtreeviewitemView' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemView.Click(19, 27)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemWebPages object equals 'Web Pages'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemWebPages, "WPFControlText", cmpEqual, "Web Pages")
    #Clicks the 'RadtreeviewitemWebPages' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemWebPages.Click(19, 29)
