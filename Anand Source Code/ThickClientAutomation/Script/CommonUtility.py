﻿def Login():
    TestedApps.Valerus.Run()
    #Opens the 'UserName' drop-down window.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.UserName.DropDown()
    #Enters '[Caps]ADMIN' in the 'UserName' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.UserName.Keys("[Caps]ADMIN")
    #Clicks the 'LoginView' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.LoginView.Click(1175, 506)
    #Clicks the 'Password' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.LoginView.Password.Click(192, 18)
    #Enters text in the 'Password' text editor.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.LoginView.Password.SetText(Project.Variables.Password1)
    #Opens the 'ServerName' drop-down window.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.LoginView.ServerName.DropDown()
    #Enters '172.20.1.80' in the 'ServerName' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.LoginView.ServerName.Keys("172.20.1.81")
    #Clicks the 'LoginView' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.LoginView.Click(1170, 673)
    #Sets the 'ToggleButton' toggle button to the cbUnchecked state.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.LoginView.ToggleButton.ClickButton(cbUnchecked)
    #Clicks the 'LoginButton' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.LoginView.LoginButton.ClickButton()

    
def GotoSearch():
    Login()
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.TabitemSearch).BlockByText("Q SEARCH").Click()
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextblockThumbnailSearch object equals 'Thumbnail Search'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextblockThumbnailSearch, "WPFControlText", cmpEqual, "Thumbnail Search")
     #Clicks the 'TabitemEventAlarmSearch' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TabitemEventAlarmSearch.Click(123, 19)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextblockMyQuery object equals 'My Query'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextblockMyQuery, "WPFControlText", cmpEqual, "My Query")
    

def LogoutandClose():
    Delay(1000)
    #Sets the 'btnUserDropdown' toggle button to the cbChecked state.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.btnUserDropdown.ClickButton(cbChecked)
    #Clicks the 'IconButton' object.
    Delay(1000)
    Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.IconButton.Click(82, 24)
    #Clicks the 'WindowButtonCommands' object.
    Delay(5000)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.WindowButtonCommands.Click(117, 4)
    Delay(5000)

def Test1():
    Var1 = ""
   
