﻿def Login():
    TestedApps.Valerus.Run()
    #Clicks the 'UserName' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.UserName.Click(129, 27)
    #Enters 'admin' in the 'UserName' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.UserName.Keys("admin")
    #Clicks the 'Password' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.Password.Click(121, 33)
    #Enters text in the 'Password' text editor.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.Password.SetText(Project.Variables.Password1)
    #Clicks the 'ServerName' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.ServerName.Click(102, 29)
    #Enters 'localhost' in the 'ServerName' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.ServerName.Keys("localhost")
    Delay(500)
    #Clicks the 'LoginView' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.LoginView.Click(1147, 710)
    #Sets the 'ToggleButton' toggle button to the cbUnchecked state.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.ToggleButton.ClickButton(cbUnchecked)
    #Clicks the 'LoginButton' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.LoginButton.ClickButton()
    Delay(3000)

def LoginWithEnabledReturnTolastDisplay():
    TestedApps.Valerus.Run()
    #Clicks the 'UserName' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.UserName.Click(129, 27)
    #Enters 'admin' in the 'UserName' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.UserName.Keys("admin")
    #Clicks the 'Password' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.Password.Click(121, 33)
    #Enters text in the 'Password' text editor.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.Password.SetText(Project.Variables.Password1)
    #Clicks the 'ServerName' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.ServerName.Click(102, 29)
    #Enters 'localhost' in the 'ServerName' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.ServerName.Keys("localhost")
    Delay(500)
    #Clicks the 'LoginView' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.LoginView.Click(1147, 710)
    #Clicks the 'LoginButton' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.LoginButton.ClickButton()
    Delay(3000)    
    
    
def openSearchPage():
    #Clicks the 'TabitemSearch' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.TabitemSearch.Click(64, 47)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TabitemThumbnailSearch object equals 'Thumbnail Search'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TabitemThumbnailSearch, "WPFControlText", cmpEqual, "Thumbnail Search")

def openConfigurationPage():
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.TabitemConfiguration).BlockByText("CONFIGURATION").Click()
    
def openAlarmsPage():
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.TabitemAlarms).BlockByText("ALARMS").Click()
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.dtGrid.DatagridcolumnheaderAlarmId object equals 'Alarm ID'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.dtGrid.DatagridcolumnheaderAlarmId, "WPFControlText", cmpEqual, "Alarm ID")

def openMonitoringPage():
    #Clicks the 'TabitemMonitoring' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.TabitemMonitoring.Click(71, 46)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemUngrouped object equals 'UNGROUPED'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.SliderControl.RadtreeviewitemUngrouped, "WPFControlText", cmpEqual, "UNGROUPED")

def closeApplication():
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.Click(10, 14)
    #Moves the mouse cursor to the menu item specified and then simulates a single click.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.PopupMenu.Click("Close") 
    
    
    
    
    
    
    
    
    
    
    
def LogOut():
    #Sets the 'ToggleButton' toggle button to the cbChecked state.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.ToggleButton.ClickButton(cbChecked)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.IconButton).BlockByText("[→ Logout").Click()
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.LoginView.TextblockEnterYourCredentials object equals 'Enter your credentials'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.LoginView.TextblockEnterYourCredentials, "WPFControlText", cmpEqual, "Enter your credentials")


