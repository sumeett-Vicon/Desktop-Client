﻿##############################################################################################
import CommonUtility


def VerifyNameFeild():
    CommonUtility.GotoSearch()
    Log.Message("Verifying Name Feild")
        #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonAddNew object equals 'Add New'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonAddNew, "WPFControlText", cmpEqual, "Add New")
    #Clicks the 'ButtonAddNew' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonAddNew.ClickButton()
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox, "Enabled", cmpEqual, True)
    #Clicks the 'TextBox' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.Click(113, 17)
    #Enters the text 'Verify name feild !@#$%^&*()_+12' in the 'TextBox' text editor.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.SetText("Verify name feild !@#$%^&*()_+12")
    #Checks whether the 'wText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox object equals 'Verify name feild !@#$%^&*()_+12'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox, "wText", cmpEqual, "Verify name feild !@#$%^&*()_+12")
    
    
    
def VerifySaveQueryFunctionality():
  #Drags the 'TextBox' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.Drag(273, 20, -279, -1)
    #Enters the text 'verify save functiob' in the 'TextBox' text editor.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.SetText("verify save function")
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbEvent).BlockByText("event").Click()
    Delay(500)
    #Clicks the 'PopupRoot' object.
    Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.Click(89, 28)
    Delay(500)
    #Enters 'motion' in the 'HwndSource_shell' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.Keys("motion")
    Delay(500)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.RadTreeViewItem).BlockByText("Motion").Click()
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ExtendedCombo).BlockByText("Select").Click()
    #Clicks the 'PopupRoot' object.
    Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.Click(52, 18)
    #Enters '248' in the 'HwndSource_shell' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.Keys("248")
    #Sets the 'toggleBtn' toggle button to the cbChecked state.
    Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.toggleBtn.ClickButton(cbChecked)
    #Clicks the 'cmbDateRange' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange.Click(248, 28)
    #Selects the 3 item of the 'cmbDateRange' combo box.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange.ClickItem(3)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.UpdateQuery).BlockByText("Query").Click()
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn, "wState", cmpEqual, 0)
    Delay(500)
    #Clicks the 'ButtonDelete' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete.ClickButton()
    #Clicks the 'ButtonYesDeleteIt' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ButtonYesDeleteIt.ClickButton()
    
    
def VerifyLongEventName():
    CommonUtility.LogoutandClose()
    CommonUtility.GotoSearch() 
    #Clicks the 'ButtonAddNew' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonAddNew.ClickButton()
    #Clicks the 'TextBox' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.Click(103, 20)
    Delay(1500)
    #Enters the text 'verify long name for query with ' in the 'TextBox' text editor.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.SetText("VERIFY LONG NAME FOR QUERY WITH ")
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbEvent).BlockByText("event").Click()
    #Clicks the 'PopupRoot' object.
    Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.Click(88, 21)
    Delay(1000)
    #Enters 'motion ' in the 'HwndSource_shell' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.Keys("motion ")
    Delay(500)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.RadTreeViewItem).BlockByText("Motion").Click()
    Delay(500)
    #Clicks the 'ExtendedCombo' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ExtendedCombo.Click(145, 18)
    #Clicks the 'PopupRoot' object.
    Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.Click(113, 30)
    Delay(500)
    #Enters '142' in the 'HwndSource_shell' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.Keys("142")
    #Sets the 'toggleBtn' toggle button to the cbChecked state.
    Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.toggleBtn.ClickButton(cbChecked)
    Delay(500)
    #Selects the 1 item of the 'cmbDateRange' combo box.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange.ClickItem(1)
    #Clicks the 'UpdateQuery' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.UpdateQuery.Click(54, 11)
    Delay(2000)
    #Checks whether the 'ToolTip' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn object equals 'VERIFY LONG NAME FOR QUERY WITH '.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn, "ToolTip", cmpEqual, "VERIFY LONG NAME FOR QUERY WITH ")
    Delay(500)
    #Clicks the 'ButtonDelete' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete.ClickButton()
    Delay(500)
    #Clicks the 'ButtonYesDeleteIt' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ButtonYesDeleteIt.ClickButton()

    
def VerifySearchButtonWhenQueryNameIsNotPresent():
    CommonUtility.LogoutandClose()
    CommonUtility.GotoSearch()
    #Clicks the 'ButtonAddNew' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonAddNew.ClickButton()
    #Clicks the 'cmbEvent' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbEvent.Click(710, 22)
    Delay(1500)
    #Clicks the 'PopupRoot' object.
    Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.Click(47, 20)
    Delay(1500)
    #Enters 'book' in the 'HwndSource_shell' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.Keys("book")
    Delay(1500)
    #Sets the 'VScroll' scroll bar thumb to position 0.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ScrollViewer.VScroll.Pos = 0
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.RadTreeViewItem).BlockByText("Bookmark").Click()
    Delay(500)
    #Sets the 'VScroll' scroll bar thumb to position 0.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ScrollViewer.VScroll.Pos = 0
    Delay(1500)
    #Clicks the 'ExtendedCombo' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ExtendedCombo.Click(197, 22)
    Delay(500)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator).BlockByText("...").Click()
    #Enters '248' in the 'HwndSource_shell' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.Keys("248")
    #Sets the 'toggleBtn' toggle button to the cbChecked state.
    Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.toggleBtn.ClickButton(cbChecked)
    Delay(1500)
    #Rotates the mouse wheel to -3 over the 'ScrollViewer' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ScrollViewer.MouseWheel(-3)
    #Sets the 'VScroll' scroll bar thumb to position 105.6.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ScrollViewer.VScroll.Pos = 105.59999999999999
    #Clicks the 'cmbDateRange' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange.Click(136, 24)
    #Selects the 2 item of the 'cmbDateRange' combo box.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange.ClickItem(2)
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.FocusedbuttonSearch object equals False.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.FocusedbuttonSearch, "Enabled", cmpEqual, False)
    Log.Message("Search Button is disable")
    Delay(1500)
    #Rotates the mouse wheel to 5 over the 'ScrollViewer' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ScrollViewer.MouseWheel(5)
    #Checks whether the 'wText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox object equals ''.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox, "wText", cmpEqual, "")
    Log.Message("This Checkpoint For Blank Query Name")
    
    
    
def VerifyQuerySavingWithoutQueryName():
    CommonUtility.LogoutandClose()
    CommonUtility.GotoSearch()
    #Clicks the 'ButtonAddNew' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonAddNew.ClickButton()
    #Checks whether the 'wText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox object equals ''.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox, "wText", cmpEqual, "")
    #Clicks the 'cmbEvent' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbEvent.Click(710, 22)
    Delay(1500)
    #Clicks the 'PopupRoot' object.
    Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.Click(47, 20)
    Delay(1500)
    #Enters 'book' in the 'HwndSource_shell' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.Keys("book")
    Delay(1500)
    #Sets the 'VScroll' scroll bar thumb to position 0.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ScrollViewer.VScroll.Pos = 0
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.RadTreeViewItem).BlockByText("Bookmark").Click()
    Delay(500)
    #Sets the 'VScroll' scroll bar thumb to position 0.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ScrollViewer.VScroll.Pos = 0
    Delay(1500)
    #Clicks the 'ExtendedCombo' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ExtendedCombo.Click(197, 22)
    Delay(500)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator).BlockByText("...").Click()
    #Enters '248' in the 'HwndSource_shell' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.Keys("248")
    #Sets the 'toggleBtn' toggle button to the cbChecked state.
    Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.toggleBtn.ClickButton(cbChecked)
    Delay(1500)
    #Rotates the mouse wheel to -3 over the 'ScrollViewer' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ScrollViewer.MouseWheel(-3)
    #Sets the 'VScroll' scroll bar thumb to position 105.6.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ScrollViewer.VScroll.Pos = 105.59999999999999
    #Clicks the 'cmbDateRange' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange.Click(136, 24)
    #Selects the 2 item of the 'cmbDateRange' combo box.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange.ClickItem(2)
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.UpdateQuery object equals False.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.UpdateQuery, "Enabled", cmpEqual, False)    
    Log.Message("Save Query Button is disable")
    Delay(1500)
    #Rotates the mouse wheel to 5 over the 'ScrollViewer' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ScrollViewer.MouseWheel(5)
    #Checks whether the 'wText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox object equals ''.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox, "wText", cmpEqual, "")
    Log.Message("This Checkpoint For Blank Query Name")
    
    
    
    
def VerifyBlankEventSelection():
    #Clicks the 'ButtonAddNew' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonAddNew.ClickButton()
    #Clicks the 'TextBox' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.Click(92, 20)
    #Enters the text 'Blank event selection test case' in the 'TextBox' text editor.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.SetText("Blank event selection test case")
    #Checks whether the 'Text' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbEvent object equals 'Select an event'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbEvent, "Text", cmpEqual, "Select an event")
    Log.Message("No Event Seleted")
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ExtendedCombo object equals False.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ExtendedCombo, "Enabled", cmpEqual, False)
    Log.Message("Select Resource(s) Drop dowon is DISABLE")
    #Clicks the 'cmbDateRange' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange.Click(127, 25)
    #Selects the 1 item of the 'cmbDateRange' combo box.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange.ClickItem(1)
    #Checks whether the 'wText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange object equals 'Last 1 day'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange, "wText", cmpEqual, "Last 1 day")
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.UpdateQuery object equals False.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.UpdateQuery, "Enabled", cmpEqual, False)
    Log.Message("Save Query button is Disable")
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.FocusedbuttonSearch object equals False.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.FocusedbuttonSearch, "Enabled", cmpEqual, False)
    Log.Message(" Save Query button is Disable")   
    
    
    
def VerifyBlankResourceSelection():
    #Drags the 'TextBox' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.Drag(237, 20, -242, 0)
    #Enters the text 'Blank Resources selection test c' in the 'TextBox' text editor.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.SetText("Blank Resources selection test c")
    Delay(2000)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbEvent).BlockByText("Select an event").Click()
    Delay(2000)
    #Clicks the 'PopupRoot' object.
    Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.Click(79, 24)
    Delay(2000)
    #Enters 'motion detection' in the 'HwndSource_shell' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.Keys("motion detection")
    Delay(1500)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.RadTreeViewItem).BlockByText("Motion").Click()
    #Checks whether the 'Text' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ExtendedCombo object equals 'Select resource(s)'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ExtendedCombo, "Text", cmpEqual, "Select resource(s)")
    Log.Message("This Checkpoint for no resources selected ")
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.UpdateQuery object equals False.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.UpdateQuery, "Enabled", cmpEqual, False)
    Log.Message("Save Query button is Disable")
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.FocusedbuttonSearch object equals False.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.FocusedbuttonSearch, "Enabled", cmpEqual, False)
    Log.Message(" Save Query button is Disable")
    
    
def VerifyMultipleResourceSelection():
    CommonUtility.LogoutandClose()
    CommonUtility.GotoSearch()
    #Clicks the 'ButtonAddNew' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonAddNew.ClickButton()
    #Drags the 'TextBox' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.Drag(252, 18, -238, 4)
    #Enters the text 'Multiple resource selection TC' in the 'TextBox' text editor.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.SetText("Multiple resource selection TC")
    Delay(500)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbEvent).BlockByText("Select an event").Click()
    Delay(1000)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator).BlockByText("...").Click()
    Delay(500)
    #Enters 'motion' in the 'HwndSource_shell' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.Keys("motion")
    Delay(500)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.RadTreeViewItem).BlockByText("Detection").Click()
    Delay(500)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ExtendedCombo).BlockByText("resource").Click()
    Delay(500)
    #Sets the 'toggleBtn' toggle button to the cbChecked state.
    Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.toggleBtn.ClickButton(cbChecked)
    Delay(500)
    #Sets the 'toggleBtn2' toggle button to the cbChecked state.
    Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.toggleBtn2.ClickButton(cbChecked)
    #Checks whether the 'Text' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ExtendedCombo object equals '2 Selected'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ExtendedCombo, "Text", cmpEqual, "2 Selected")
    #Clicks the 'cmbDateRange' object.
    Delay(500)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange.Click(104, 27)
    #Selects the 2 item of the 'cmbDateRange' combo box.
    Delay(500)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange.ClickItem(2)
    #Clicks the 'UpdateQuery' object.
    Delay(500)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.UpdateQuery.Click(42, 11)
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn, "wState", cmpEqual, 0)
    Log.Message("This Checkpoint for Very that Query is Save")
    #Checks whether the 'Text' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ExtendedCombo object equals '2 Selected'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ExtendedCombo, "Text", cmpEqual, "2 Selected")
    Log.Message("This Checkpoint for wether the Multiple Resources Seleted")
    #Clicks the 'ButtonDelete' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete.ClickButton()
    #Clicks the 'ButtonYesDeleteIt' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ButtonYesDeleteIt.ClickButton()
    
    
    
     
   
    ################################################################################################ADD Above this HERE################################################################################
    
    
    
    
    
    
    
    

        
 
def CreateMotionDetectionPrivateQuery(): #This test case Create  "Motion Detection" Private Query
    CommonUtility.LogoutandClose()
    CommonUtility.GotoSearch() #__________________________________________________________________________________COMMENT THIS WHILE RUNNING SUITE   
    #Clicks the 'TabitemEventAlarmSearch' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TabitemEventAlarmSearch.Click(100, 22)
    #Clicks the 'ButtonAddNew' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonAddNew.ClickButton()
     #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox, "Enabled", cmpEqual, True)
    Log.Message("This Check point for Query filed Veried")
    #Clicks the 'TextBox' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.Click(111, 15)
    #Enters the text 'motion detection' in the 'TextBox' text editor.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.SetText("motion detection")
    Delay(2000)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbEvent).BlockByText("Select an event").Click()
    Delay(2000)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator).BlockByText("Search").Click()
    #Enters 'motion detection' in the 'HwndSource_shell' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.Keys("motion detection")
    Delay(2000)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.RadTreeViewItem).BlockByText("Motion").Click()
    Delay(2000)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ExtendedCombo).BlockByText("resource").Click()
    Delay(2000)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator).BlockByText("...").Click()
    Delay(2000)
    #Enters '.250' in the 'HwndSource_shell' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.Keys(".248")
    Delay(2000)
    #Sets the 'toggleBtn' toggle button to the cbChecked state.
    Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.toggleBtn.ClickButton(cbChecked)
    Delay(2000)
    #Clicks the 'NumericSpinner' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.NumericSpinner.Click(39, 38)
    Delay(1000)
    #Clicks the 'NumricSpinner' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.NumericSpinner.Click(25, 8)
    Delay(500)
    #Clicks the 'NumericSpinner' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.NumericSpinner.Click(23, 8)
    Delay(500)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.NumericSpinner.Click(21, 62)
    Delay(500)
    #Clicks the 'NumericSpinner' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.NumericSpinner.Click(21, 62)
    Delay(500)
    #Clicks the 'NumericSpinner' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.NumericSpinner.Click(20, 35)
    #Drags the 'NumericSpinner' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.NumericSpinner.Drag(20, 35, 18, -1)
    #Enters '20' in the 'NumericSpinner' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.NumericSpinner.Keys("5")
    #Clicks the 'NumericSpinner' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.NumericSpinner.Click(28, 65)
    Delay(500)
    #Clicks the 'NumericSpinner' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.NumericSpinner.Click(25, 65)
    Delay(500)
    #Clicks the 'NumericSpinner' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.NumericSpinner.Click(22, 9)
    Delay(500)
    #Clicks the 'NumericSpinner' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.NumericSpinner.Click(22, 9)
    Delay(1000)
    #Clicks the 'cmbDateRange' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange.Click(156, 15)
    Delay(1000)
    #Clicks the 'cmbDateRange' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange.Click(705, 23)
    Delay(500)
    #Selects the 2 item of the 'cmbDateRange' combo box.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange.Click() 
    #Selects the 1 item of the 'cmbDateRange' combo box.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange.ClickItem(2)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.UpdateQuery).BlockByText("Save Query").Click()  
    #Checks whether the 'wState' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn object equals 0.
    Regions.toggleBtn.Check(Regions.CreateRegionInfo(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn, 21, 7, 115, 19, False), False, False, 1165, 136)
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.toggleBtn, "wState", cmpEqual, 0)
    Log.Message("MOTION DETECTION PRIVATE QUERY SAVED")
    
def Singleclickonprivatequery():
    Delay(2000)    
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ScrollViewer.TextblockName object equals 'Name'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ScrollViewer.TextblockName, "WPFControlText", cmpEqual, "Name")
    #Sets the state of the 'chkquery' check box to cbUnchecked.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.chkquery.ClickButton(cbUnchecked)
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ScrollViewer.Grid object equals True.
    Regions.Grid5.Check(Regions.CreateRegionInfo(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ScrollViewer.Grid, 27, 18, 1222, 724, False))
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ScrollViewer.Grid, "Enabled", cmpEqual, True)
    #Clicks the 'toggleBtn' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn.Click(76, 16)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ScrollViewer.TextblockName object equals 'Name'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ScrollViewer.TextblockName, "WPFControlText", cmpEqual, "Name")

    
      
def UpdateEventName(): #This test case update the Event Name in Provate Query 
    #CreateMotionDetection()
    #Checks whether the 'wText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox object equals 'motion detection'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox, "wText", cmpEqual, "motion detection")
    #Clicks the 'TextBox' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.Click(180, 23)
    #Drags the 'TextBox' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.Drag(180, 23, -245, 0)
    #Enters the text 'Update name motion detection' in the 'TextBox' text editor.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.SetText("Update name motion detection")
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.UpdateQuery).BlockByText("Update").Click()
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn, "wState", cmpEqual, 0)
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn, "wState", cmpEqual, 0)
    
def doubleclickOnQueryPrivate():
    Delay(2000)    
    #Double-clicks the 'toggleBtn' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn.DblClick(127, 20)
    Delay(2000)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Grid.TextblockSearchResult object equals 'Search Result'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Grid.TextblockSearchResult, "WPFControlText", cmpEqual, "Search Result")
    #Clicks the 'ButtonBackToQuery' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonBackToQuery.ClickButton()
    
   
def SearchResult():# This test case Shows the Motion Detection Results (Private Query)
    #CreateMotionDetection() #__________________________________________________________________________________COMMENT THIS WHILE RUNNING SUITE    
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.FocusedbuttonSearch object equals 'Search'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.FocusedbuttonSearch, "WPFControlText", cmpEqual, "Search")
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.FocusedbuttonSearch).BlockByText("Search").Click()
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Grid.TextblockSearchResult object equals 'Search Result'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Grid.TextblockSearchResult, "WPFControlText", cmpEqual, "Search Result")
    Log.Message("Search Results")
    #Sets the state of the 'CheckBox' check box to cbChecked.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.CheckBox.ClickButton(cbChecked)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.Textblock172200248Camera object equals '172.20.0.248_Camera'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.Textblock172200248Camera, "WPFControlText", cmpEqual, "172.20.0.248_Camera")
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.TextblockMotionDetection, "Enabled", cmpEqual, True)
    Delay(1000)
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.btnPlay object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.btnPlay, "Enabled", cmpEqual, True)
    #Clicks the 'btnPlay' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.btnPlay.ClickButton()
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Caption object equals '172.20.0.248_Camera'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Caption, "WPFControlText", cmpEqual, "172.20.0.248_Camera")
    Log.Message("This Check Point for Resource name on Player")
        #Clicks the 'ButtonBackToQuery' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonBackToQuery.ClickButton()
    Log.Message("Verify search button working correctly Also Executed")

def exportsearchvideo():# This test case Exports the search results of Motion Detection(Private Query)
    #Clicks the 'FocusedbuttonSearch' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.FocusedbuttonSearch.Click(66, 30)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.TextblockMotionDetection object equals 'Motion Detection'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.TextblockMotionDetection, "WPFControlText", cmpEqual, "Motion Detection")
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.Textblock172200248Camera object equals '172.20.0.248_Camera'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.Textblock172200248Camera, "WPFControlText", cmpEqual, "172.20.0.248_Camera")
    Delay(2000)
    #Sets the state of the 'CheckBox' check box to cbChecked.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.CheckBox.ClickButton(cbChecked)
    Delay(1000)
    #Clicks the 'btnPlay' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.btnPlay.ClickButton()
    Delay(2000)
    #Clicks the 'menuToggleButton' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.menuToggleButton.Click(9, 5)
    #Clicks the 'Export' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Export.Click(14, 5)
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Export, "Enabled", cmpEqual, True)
    Log.Message("This Check point is for the Export from the Player")
    export()
    
def CancleDeletebyDeleteButton(): # This test case Cancle the Delete query operation if user uses delete "BUTTON" to delete the query (Private Query) 
#    CommonUtility.LogoutandClose() 
    CreateMotionDetectionPrivateQuery()
    #Clicks the 'toggleBtn' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn.Click(233, 13)
    Delay(2000)
    #Clicks the 'ButtonCancel' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ButtonCancel.ClickButton()
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn, "wState", cmpEqual, 0)
    Log.Message("Cancel Delete BY Button QUERY executed")
    #CommonUtility.LogoutandClose()
        
def CancleDeletebyDeleteIcon():  # This test case Cancle the Delete query operation if user uses delete "ICON" to delete the query (Private Query)
    #CreateMotionDetection()
    #Clicks the 'toggleBtn' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn.Click(233, 13)
    Delay(2000)
    #Clicks the 'ButtonCancel' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ButtonCancel.ClickButton()
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn, "wState", cmpEqual, 0)
    Log.Message("Cancel Delete BY ICON QUERY executed")
    #CommonUtility.LogoutandClose()    
    
def DeleteSingleQueryByDeleteButton(): # This test case the Delete query operation if user uses delete "BUTTON" to delete the query (Private Query)
   #CommonUtility.GotoSearch()
   #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete object equals 'Delete'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete, "WPFControlText", cmpEqual, "Delete")
    #Clicks the 'ButtonDelete' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete.ClickButton()
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ButtonYesDeleteIt object equals 'Yes, Delete It'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ButtonYesDeleteIt, "WPFControlText", cmpEqual, "Yes, Delete It")
    #Clicks the 'ButtonYesDeleteIt' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ButtonYesDeleteIt.ClickButton()
    #CommonUtility.LogoutandClose()
     
def DeletebyDeleteIcon(): # This test case the Delete query operation if user uses delete "ICON" to delete the query (Private Query)
    #CreateMotionDetection()
    #Clicks the 'toggleBtn' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn.Click(233, 13)
    Delay(1000)
        #Clicks the 'ButtonYesDeleteIt' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ButtonYesDeleteIt.ClickButton()
#    #Clicks the 'ButtonYesDeleteIt' button.
    Regions.Grid1.Check(Regions.CreateRegionInfo(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Grid2, 3, 189, 315, 531, False), False, False, 128236, 229)
    Log.Message("QUERY WAS DELETED BY ICON")
    #CommonUtility.LogoutandClose()
    
def CreatePublicQuery(): #This test case Create  "Motion Detection" Public Query
    CommonUtility.LogoutandClose()
    CommonUtility.GotoSearch()
   #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonAddNew object equals True.
       #Clicks the 'TabitemEventAlarmSearch' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TabitemEventAlarmSearch.Click(150, 34) 
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonAddNew, "Enabled", cmpEqual, True)
    #Clicks the 'ButtonAddNew' button.
    Delay(1000)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonAddNew.ClickButton()
    #Clicks the 'TextBox' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.Click(140, 20)
    #Enters the text 'motion detection public query' in the 'TextBox' text editor.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.SetText("motion detection public query")
    #Clicks the 'RadiobuttonPublic' radio button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPublic.ClickButton()
    #Checks whether the 'wChecked' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPublic object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPublic, "wChecked", cmpEqual, True)
    #Checks whether the 'wChecked' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPrivate object equals False.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPrivate, "wChecked", cmpEqual, False)
    #Clicks the 'TabitemEventAlarmSearch' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TabitemEventAlarmSearch.Click(100, 22)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.Click(111, 15)
    Delay(2000)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbEvent).BlockByText("Select an event").Click()
    Delay(2000)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator).BlockByText("Search").Click()
    #Enters 'motion detection' in the 'HwndSource_shell' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.Keys("motion detection")
    Delay(2000)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.RadTreeViewItem).BlockByText("Motion").Click()
    Delay(2000)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ExtendedCombo).BlockByText("resource").Click()
    Delay(2000)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator).BlockByText("...").Click()
    Delay(2000)
    #Clicks the 'PopupRoot' object.
    Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.Click(166, 26)
    #Enters '.142' in the 'HwndSource_shell' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.Keys(".142")
    Delay(1000)
    #Sets the 'toggleBtn' toggle button to the cbChecked state.
    Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.toggleBtn.ClickButton(cbChecked)
    #Checks whether the 'wText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange object equals 'Select days'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange, "wText", cmpEqual, "Select days")
       #Selects the 2 item of the 'cmbDateRange' combo box.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange.Click() 
    #Selects the 1 item of the 'cmbDateRange' combo box.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange.ClickItem(2)
       #Clicks the 'UpdateQuery' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.UpdateQuery.Click(90, 32)
    #Checks whether the 'wState' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.toggleBtn object equals 0.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.toggleBtn, "wState", cmpEqual, 0)
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.TreeViewItem.toggleBtn, "wState", cmpEqual, 0)
    Log.Message("Public Query Created")

def SingleClickOnPublicQuery():
    Delay(1000)
     #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ScrollViewer.TextblockName object equals 'Name'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ScrollViewer.TextblockName, "WPFControlText", cmpEqual, "Name")
    #Sets the state of the 'chkquery' check box to cbUnchecked.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.TreeViewItem.chkquery.ClickButton(cbUnchecked)
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete object equals False.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete, "Enabled", cmpEqual, False)
    #Sets the state of the 'chkquery' check box to cbChecked.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.TreeViewItem.chkquery.ClickButton(cbChecked)
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete, "Enabled", cmpEqual, True)
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.FocusedbuttonSearch object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.FocusedbuttonSearch, "Enabled", cmpEqual, True)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ScrollViewer.TextblockName object equals 'Name'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ScrollViewer.TextblockName, "WPFControlText", cmpEqual, "Name")
    
    
def DoubleClickOnPublicQuery():
    Delay(1000)
    #Double-clicks the 'toggleBtn' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.TreeViewItem.toggleBtn.DblClick(78, 14)
    Delay(2000)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Grid.TextblockSearchResult object equals 'Search Result'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Grid.TextblockSearchResult, "WPFControlText", cmpEqual, "Search Result")
    #Clicks the 'ButtonBackToQuery' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonBackToQuery.ClickButton()
  
      

def DisplaySearchResultAndPlayForPublicQuery():  # This test case Shows the Motion Detection Results (Public Query)
#  CreatePublicQuery()##########################################################Comment while running suite
        #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.FocusedbuttonSearch object equals 'Search'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.FocusedbuttonSearch, "WPFControlText", cmpEqual, "Search")
    Delay(2000)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.FocusedbuttonSearch).BlockByText("Search").Click()
    Delay(5000)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.TextblockMotionDetection object equals 'Motion Detection'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.TextblockMotionDetection, "WPFControlText", cmpEqual, "Motion Detection")
    #Clicks the 'btnPlay' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.btnPlay.ClickButton()
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Caption object equals '172.20.0.142_Camera'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Caption, "WPFControlText", cmpEqual, "172.20.0.142_Camera")
    Log.Message("This Check Point for Resource name on Player")
    #Clicks the 'ButtonBackToQuery' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonBackToQuery.ClickButton()
    
def ExportDispalyedResultVideoPublicQuery():# This test case Exports the search results of Motion Detection (Public Query)
    Delay(2000)
  #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.FocusedbuttonSearch object equals 'Search'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.FocusedbuttonSearch, "WPFControlText", cmpEqual, "Search")
    #Clicks the 'FocusedbuttonSearch' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.FocusedbuttonSearch.Click(54, 9)
    #Sets the state of the 'CheckBox' check box to cbChecked.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.CheckBox.ClickButton(cbChecked)
    #Clicks the 'btnPlay' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.btnPlay.ClickButton()
    #Clicks the 'menuToggleButton' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.menuToggleButton.Click(16, 7)
    #Clicks the 'Export' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Export.Click(11, 10)
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Export, "Enabled", cmpEqual, True)
    Log.Message("This Check point is for the Export from the Player")    
    export()
    
def UpdatePublicQuery(): #This test case update the Event Name in Public Query 
    #CreatePublicQuery()#################################################Commit Wi=hile running tour
    Log.Message("Check point for old name")
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.TreeViewItem.toggleBtn, "wState", cmpEqual, 0)
        #Drags the 'TextBox' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.Drag(231, 25, -356, 1)
    #Enters the text 'MD Public Qury Update Name' in the 'TextBox' text editor.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.SetText("MD Public Qury Update Name")
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.UpdateQuery).BlockByText("Query").Click()
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.TreeViewItem.toggleBtn, "wState", cmpEqual, 0)
    

    
    
def CancelDeleteByDeteleButtonPublicQuery():  # This test case Cancle the Delete query operation if user uses delete "BUTTON" to delete the query (Public Query) 
      #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete, "Enabled", cmpEqual, True)
    Delay(2000)
    #Clicks the 'ButtonDelete' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete.ClickButton()
    Delay(2000)
    #Clicks the 'ButtonCancel' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ButtonCancel.ClickButton()
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.TreeViewItem.toggleBtn, "wState", cmpEqual, 0)
    Log.Message("Qurey is avalable on the my query")
       
    
def CancleDeleteByDeleteIconPublicQuery(): # This test case Cancle the Delete query operation if user uses delete "ICON" to delete the query (Public Query)
  #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete, "Enabled", cmpEqual, True)
    Delay(2000)
    #Clicks the 'toggleBtn' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.TreeViewItem.toggleBtn.Click(234, 13)
    Delay(2000)
    #Clicks the 'ButtonCancel' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ButtonCancel.ClickButton()
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.TreeViewItem.toggleBtn, "wState", cmpEqual, 0)
    Log.Message("Qurey is avalable on the my query")      



def DeletePublicQueryByDeleteIcon(): # This test case the Delete query operation if user uses delete "ICON" to delete the query (Public Query)
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete, "Enabled", cmpEqual, True)
    Delay(2000)
    #Clicks the 'toggleBtn' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.TreeViewItem.toggleBtn.Click(234, 19)
    Delay(2000)
    #Clicks the 'ButtonYesDeleteIt' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ButtonYesDeleteIt.ClickButton()
    Delay(1000)
    Regions.Grid2.Check(Regions.CreateRegionInfo(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Grid2, 2, 189, 309, 564, False), False, False, 23236, 51)
    
  
  
  
        
def DeletePublicQueryByDeleteButton(): # This test case the Delete query operation if user uses delete "BUTTON" to delete the query (Private Query)
    CreatePublicQuery()
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete, "Enabled", cmpEqual, True)
    Delay(2000)
        #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete, "Enabled", cmpEqual, True)
    Delay(1000)
    #Clicks the 'ButtonDelete' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete.ClickButton()
    Delay(1000)
    #Clicks the 'ButtonYesDeleteIt' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ButtonYesDeleteIt.ClickButton()
    Delay(1000)
    Regions.Grid2.Check(Regions.CreateRegionInfo(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Grid2, 2, 189, 309, 564, False), False, False, 23236, 51)
    
      
    
def CreateAI_HumanQueryPublic(): #This test case Create  "AI HUMAN DETECTION" Public Query
    CommonUtility.LogoutandClose()
    CommonUtility.GotoSearch()
  #Clicks the 'TabitemEventAlarmSearch' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TabitemEventAlarmSearch.Click(150, 34) 
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonAddNew, "Enabled", cmpEqual, True)
    #Clicks the 'ButtonAddNew' button.
    Delay(1000)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonAddNew.ClickButton()
    #Clicks the 'TextBox' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.Click(140, 20)
    #Enters the text 'motion detection public query' in the 'TextBox' text editor.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.SetText("AI Human")
    #Clicks the 'RadiobuttonPublic' radio button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPublic.ClickButton()
    #Checks whether the 'wChecked' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPublic object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPublic, "wChecked", cmpEqual, True)
    #Checks whether the 'wChecked' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPrivate object equals False.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPrivate, "wChecked", cmpEqual, False)
        #Checks whether the 'Text' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbEvent object equals 'Select an event'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbEvent, "Text", cmpEqual, "Select an event")
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbEvent).BlockByText("event").Click()
    #Clicks the 'RadTreeViewItem2' object.
    Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.RadTreeViewItem2.Click(16, 19)
    Delay(1000)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.RadTreeViewItem2.RadTreeViewItem).BlockByText("Human Detection").Click()
    #Checks whether the 'Text' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ExtendedCombo object equals 'Select resource(s)'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ExtendedCombo, "Text", cmpEqual, "Select resource(s)")
    #Clicks the 'ExtendedCombo' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ExtendedCombo.Click(142, 32)
    Delay(1000)
    #Clicks the 'PopupRoot' object.
    Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.Click(80, 25)
    Delay(1000)
    #Enters '248' in the 'HwndSource_shell' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.Keys("248")
    Delay(1000)
    #Sets the 'toggleBtn' toggle button to the cbChecked state.
    Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.toggleBtn.ClickButton(cbChecked)
    #Clicks the 'cmbDateRange' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange.Click(155, 36)
    #Clicks the 'cmbDateRange' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange.Click(130, 30)
    Delay(500)
    #Selects the 2 item of the 'cmbDateRange' combo box.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange.ClickItem(2)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.UpdateQuery object equals 'Save Query'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.UpdateQuery, "WPFControlText", cmpEqual, "Save Query")
    #Clicks the 'UpdateQuery' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.UpdateQuery.Click(81, 28)
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.TreeViewItem.toggleBtn, "wState", cmpEqual, 0)
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.toggleBtn, "wState", cmpEqual, 0)
    
def DoubleClickonAICamPublicQuery():
    Delay(2000)
    #Double-clicks the 'toggleBtn' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.TreeViewItem.toggleBtn.DblClick(67, 18)
    #aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.toggleBtn, "wState", cmpEqual, 0)
    Delay(2000)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Grid.TextblockSearchResult object equals 'Search Result'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Grid.TextblockSearchResult, "WPFControlText", cmpEqual, "Search Result")
    #Clicks the 'ButtonBackToQuery' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonBackToQuery.ClickButton()
    
    
def SearchResultAiCam():# This test case Shows the AI HUMAN DETECTION Results (Public Query)
    Delay(2000)
      #Clicks the 'FocusedbuttonSearch' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.FocusedbuttonSearch.Click(29, 5)
    Delay(5000)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.TextblockHumanDetectionViconCameraAi object equals 'Human Detection - Vicon Camera AI'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.TextblockHumanDetectionViconCameraAi, "WPFControlText", cmpEqual, "Human Detection - Vicon Camera AI")
    #Clicks the 'btnPlay' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.btnPlay.ClickButton()
    Delay(1000)
     #Clicks the 'ButtonBackToQuery' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonBackToQuery.ClickButton()
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextblockQueryProperties object equals 'Query Properties'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextblockQueryProperties, "WPFControlText", cmpEqual, "Query Properties")
    
def UpdateAiQuery():#This test case update the Event Name in Public Query
    Delay(1000)
      #Checks whether the 'wText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox object equals 'AI Human'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox, "wText", cmpEqual, "AI Human")
    #Clicks the 'TextBox' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.Click(114, 14)
    #Enters the text 'AI Human updated name' in the 'TextBox' text editor.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.SetText("AI Human updated name")
    #Checks whether the 'wText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox object equals 'AI Human updated name'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox, "wText", cmpEqual, "AI Human updated name")
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.UpdateQuery).BlockByText("Query").Click()
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.TreeViewItem.toggleBtn, "wState", cmpEqual, 0)
    
def AiQuerySearchVideoExport():# This test case Exports the search results of AI HUMAN DETECTION(Public Query)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.FocusedbuttonSearch).BlockByText("Search").Click()
    #Sets the state of the 'CheckBox' check box to cbChecked.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.CheckBox.ClickButton(cbChecked)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.TextblockHumanDetectionViconCameraAi object equals 'Human Detection - Vicon Camera AI'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.TextblockHumanDetectionViconCameraAi, "WPFControlText", cmpEqual, "Human Detection - Vicon Camera AI")  
    #Clicks the 'btnPlay' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.btnPlay.ClickButton()
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Caption, "Enabled", cmpEqual, True)
    Log.Message("This verify resoure name on player")
    #Clicks the 'menuToggleButton' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.menuToggleButton.Click(11, 12)
       #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Export object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Export, "Enabled", cmpEqual, True)
    Log.Message("This Check point is for the Export from the Player")
    #Clicks the 'Export' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Export.Click(10, 15)
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Export, "Enabled", cmpEqual, True)

    export()
    
def AIQueryCancleDeleteByDeleteButtonPublicQueryEXECUTED(): # This test case Cancle the Delete query operation if user uses delete "BUTTON" to delete the query (Public Query) 
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.TreeViewItem.toggleBtn, "wState", cmpEqual, 0)
    Log.Message("Verify query")
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete, "Enabled", cmpEqual, True)
    Delay(2000)
    #Clicks the 'ButtonDelete' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete.ClickButton()
    Delay(2000)
    #Clicks the 'ButtonCancel' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ButtonCancel.ClickButton()
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.TreeViewItem.toggleBtn, "wState", cmpEqual, 0)
    Log.Message("Query Delete Canceled")
    
    
    
def AIQueryCancleDeleteByDeleteIconPublicQueryEXECUTED():# This test case Cancle the Delete query operation if user uses delete "ICON" to delete the query (Public Query)
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.TreeViewItem.toggleBtn, "wState", cmpEqual, 0)
    Log.Message("Verify query")
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete, "Enabled", cmpEqual, True)
    Delay(2000)
    #Clicks the 'toggleBtn' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.TreeViewItem.toggleBtn.Click(235, 15)
    Delay(2000)
    #Clicks the 'ButtonCancel' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ButtonCancel.ClickButton()
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.TreeViewItem.toggleBtn, "wState", cmpEqual, 0)
    Log.Message("Query Delete Canceled")
  
    
    
def AIQueryDeleteSingleQueryByDeleteIconPublicQueryEXECUTED():# This test case the Delete query operation if user uses delete "ICON" to delete the query (Public Query)
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.TreeViewItem.toggleBtn, "wState", cmpEqual, 0)
    Log.Message("Verify query")
    Delay(2000)
    #Clicks the 'ButtonDelete' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete.ClickButton()
    Delay(2000)
    #Clicks the 'ButtonYesDeleteIt' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ButtonYesDeleteIt.ClickButton()
    Regions.Grid3.Check(Regions.CreateRegionInfo(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Grid2, 5, 193, 310, 599, False))
    Log.Message("Query Deleted")
    
    
def AIQueryDeleteSingleQueryByDeleteButtonPublicQueryEXECUTED():# This test case the Delete query operation if user uses delete "BUTTON" to delete the query (Public Query)
    CreateAI_HumanQueryPublic()  
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.TreeViewItem.toggleBtn, "wState", cmpEqual, 0)
    Log.Message("Verify query")
    Delay(2000)
    #Clicks the 'ButtonDelete' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete.ClickButton()
    Delay(2000)
    #Clicks the 'ButtonYesDeleteIt' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ButtonYesDeleteIt.ClickButton()
    Regions.Grid3.Check(Regions.CreateRegionInfo(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Grid2, 5, 193, 310, 599, False))
    Log.Message("Query Deleted")    
  
    

def CreateAI_HumanQueryPrivate():#This test case Create  "AI HUMAN DETECTION" Private Query
      CommonUtility.LogoutandClose()
      CommonUtility.GotoSearch()
      #Clicks the 'TabitemEventAlarmSearch' object.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TabitemEventAlarmSearch.Click(100, 22)
      #Clicks the 'ButtonAddNew' button.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonAddNew.ClickButton()
      #Clicks the 'TextBox' object.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.Click(111, 15)
      #Enters the text 'motion detection' in the 'TextBox' text editor.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.SetText("Ai Human Private")
      Delay(2000)
      OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbEvent).BlockByText("event").Click()
      Delay(2000)
      #Clicks the 'RadTreeViewItem2' object.
      Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.RadTreeViewItem2.Click(17, 13)
      Delay(2000)
      #Clicks the 'RadTreeViewItem' object.
      Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.RadTreeViewItem2.RadTreeViewItem.Click(159, 21)
      Delay(2000)
      #Clicks the 'ExtendedCombo' object.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ExtendedCombo.Click(111, 30)
      Delay(2000)
      #Clicks the 'PopupRoot' object.
      Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.Click(83, 21)
      Delay(2000)
      #Enters '.248' in the 'HwndSource_shell' object.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.Keys(".248")
      Delay(2000)
      #Sets the 'toggleBtn' toggle button to the cbChecked state.
      Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.toggleBtn.ClickButton(cbChecked)
      Delay(500)
      #Selects the 2 item of the 'cmbDateRange' combo box.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange.Click() 
      #Selects the 1 item of the 'cmbDateRange' combo box.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange.ClickItem(2)
      OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.UpdateQuery).BlockByText("Save Query").Click()  
      #Checks whether the 'wState' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn object equals 0.
      aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn, "wState", cmpEqual, 0)
      aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.toggleBtn, "wState", cmpEqual, 0)
      Log.Message("AI Cam Human Detetion PRIVATE QUERY SAVED")
      
      
def DoubleClickOnAICamPrivateQuery():
    Delay(2000)
    #Double-clicks the 'toggleBtn' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn.DblClick(71, 10)
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.toggleBtn, "wState", cmpEqual, 0)
    Delay(2000)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Grid.TextblockSearchResult object equals 'Search Result'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Grid.TextblockSearchResult, "WPFControlText", cmpEqual, "Search Result")
    #Clicks the 'ButtonBackToQuery' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonBackToQuery.ClickButton()
    
    
    
def SearchResultAiCamPrivateQuery(): # This test case Shows the AI HUMAN DETECTION Results (Private Query)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.FocusedbuttonSearch object equals 'Search'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.FocusedbuttonSearch, "WPFControlText", cmpEqual, "Search")
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.FocusedbuttonSearch).BlockByText("Search", spNearestToCenter).Click()
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.TextblockHumanDetectionViconCameraAi object equals 'Human Detection - Vicon Camera AI'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.TextblockHumanDetectionViconCameraAi, "WPFControlText", cmpEqual, "Human Detection - Vicon Camera AI")
    Delay(500)
    #Sets the state of the 'CheckBox' check box to cbChecked.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.CheckBox.ClickButton(cbChecked)
    Delay(500)
    #Clicks the 'btnPlay' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.btnPlay.ClickButton()
    Delay(500)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Caption object equals '172.20.0.248_Camera'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Caption, "WPFControlText", cmpEqual, "172.20.0.248_Camera")
    #Clicks the 'ButtonBackToQuery' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonBackToQuery.ClickButton()
  
    
    
def UpdateAiQueryPrivateQuery():#This test case update the Event Name in Provate Query
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn, "wState", cmpEqual, 0)
     #Checks whether the 'wText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox object equals 'Ai Human Private'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox, "wText", cmpEqual, "Ai Human Private")
    #Clicks the 'TextBox' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.Click(149, 18)
    #Enters the text 'Ai Human Private Update Name' in the 'TextBox' text editor.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.SetText("Ai Human Private Update Name")
    #Clicks the 'UpdateQuery' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.UpdateQuery.Click(39, 33)
    #Checks whether the 'wText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox object equals 'Ai Human Private Update Name'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox, "wText", cmpEqual, "Ai Human Private Update Name")
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn, "wState", cmpEqual, 0)
    
    
    
def ExportDispalyedResultVideoAiCamPrivateQuery():# This test case Exports the search results of AI HUMAN DETECTION(Private Query)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.FocusedbuttonSearch).BlockByText("Search").Click()
    #Sets the state of the 'CheckBox' check box to cbChecked.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.CheckBox.ClickButton(cbChecked)
    #Clicks the 'btnPlay' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.btnPlay.ClickButton()
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.TextblockHumanDetectionViconCameraAi object equals 'Human Detection - Vicon Camera AI'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.TextblockHumanDetectionViconCameraAi, "WPFControlText", cmpEqual, "Human Detection - Vicon Camera AI")
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Caption object equals '172.20.0.248_Camera'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Caption, "WPFControlText", cmpEqual, "172.20.0.248_Camera")
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.Textblock172200248Camera object equals '172.20.0.248_Camera'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.Textblock172200248Camera, "WPFControlText", cmpEqual, "172.20.0.248_Camera")
    #Clicks the 'menuToggleButton' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.menuToggleButton.Click(10, 2)
    Delay(500)
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Export, "Enabled", cmpEqual, True)
    Log.Message("This Check point is for the Export from the Player")
    #Clicks the 'Export' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Export.Click(9, 10)
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Export, "Enabled", cmpEqual, True)
    Log.Message("This Check point is for the Export from the Player")
    export()

  
  
  
def AIQueryCancleDeleteByDeleteButtonPrivateQueryEXECUTED(): # This test case Cancle the Delete query operation if user uses delete "BUTTON" to delete the query (Private Query) 
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.toggleBtn, "wState", cmpEqual, 0)
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn, "wState", cmpEqual, 0)
    Log.Message("Verify query")
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete, "Enabled", cmpEqual, True)
    Delay(2000)
    #Clicks the 'ButtonDelete' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete.ClickButton()
    Delay(2000)
    #Clicks the 'ButtonCancel' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ButtonCancel.ClickButton()
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn, "wState", cmpEqual, 0)
    Log.Message("Query Delete Canceled")
    
    
    
def AIQueryCancleDeleteByDeleteIconPrivateQueryEXECUTED():# This test case Cancle the Delete query operation if user uses delete "ICON" to delete the query (Private Query)
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.toggleBtn, "wState", cmpEqual, 0)
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn, "wState", cmpEqual, 0)
    Log.Message("Verify query")
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete, "Enabled", cmpEqual, True)
    Delay(2000)
    #Clicks the 'toggleBtn' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn.Click(236, 18)
    Delay(2000)
    #Clicks the 'ButtonCancel' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ButtonCancel.ClickButton()
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn, "wState", cmpEqual, 0)
    Log.Message("Query Delete Canceled")
  
    
    
def AIQueryDeleteSingleQueryByDeleteIconPrivateQueryEXECUTED(): # This test case the Delete query operation if user uses delete "ICON" to delete the query (Private Query)
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.toggleBtn, "wState", cmpEqual, 0)
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn, "wState", cmpEqual, 0)
    Log.Message("Verify query")
    Delay(2000)
    #Clicks the 'ButtonDelete' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete.ClickButton()
    Delay(2000)
    #Clicks the 'ButtonYesDeleteIt' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ButtonYesDeleteIt.ClickButton()
    Regions.Grid3.Check(Regions.CreateRegionInfo(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Grid2, 5, 193, 310, 599, False))
    Log.Message("Query Deleted")
    
def AIQueryDeleteSingleQueryByDeleteButtonPrivateQueryEXECUTED():# This test case the Delete query operation if user uses delete "BUTTON" to delete the query (Private Query)
    CreateAI_HumanQueryPrivate()  
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.toggleBtn, "wState", cmpEqual, 0)
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn, "wState", cmpEqual, 0)
    Log.Message("Verify query")
    Delay(2000)
    #Clicks the 'ButtonDelete' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete.ClickButton()
    Delay(2000)
    #Clicks the 'ButtonYesDeleteIt' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ButtonYesDeleteIt.ClickButton()
    Regions.Grid3.Check(Regions.CreateRegionInfo(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Grid2, 5, 193, 310, 599, False))
    Log.Message("Query Deleted")         
    
       
def export():
#  #Clicks the 'FocusedbuttonSearch' object.
#    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.FocusedbuttonSearch.Click(66, 30)
#    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.TextblockMotionDetection object equals 'Motion Detection'.
#    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.TextblockMotionDetection, "WPFControlText", cmpEqual, "Motion Detection")
#    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.Textblock172200248Camera object equals '172.20.0.248_Camera'.
#    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.Textblock172200248Camera, "WPFControlText", cmpEqual, "172.20.0.248_Camera")
#    Delay(2000)
#    #Sets the state of the 'CheckBox' check box to cbChecked.
#    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.CheckBox.ClickButton(cbChecked)
#    Delay(1000)
#    #Clicks the 'btnPlay' button.
#    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.btnPlay.ClickButton()
#    Delay(2000)
#    #Clicks the 'menuToggleButton' object.
#    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.menuToggleButton.Click(9, 5)
#    #Clicks the 'Export' object.
#    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Export.Click(14, 5)
    if Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.btnExport.Exists :
       Delay(1500)
       Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.btnExport.ClickButton()  # Click on Export button.
       Delay(500)
         #Clicks the 'ButtonBackToQuery' button.
       Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonBackToQuery.ClickButton()
       Delay(1500)
        #Sets the 'btnExportPopUp' toggle button to the cbChecked state.
       Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.btnExportPopUp.ClickButton(cbChecked)
        #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.listDownload object equals True.
       aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.listDownload, "Enabled", cmpEqual, True)
       
    else :
      Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ButtonOk.ClickButton()
      Delay(1500)
      #Sets the 'btnExportPopUp' toggle button to the cbChecked state.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.btnExportPopUp.ClickButton(cbChecked)
      #Sets the 'VScroll' scroll bar thumb to position 0.
      Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.ScrollViewer.VScroll.Pos = 0
      Delay(1500)
      #Clicks the 'btnDelete' radio button.
      Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.listDownload.btnDelete.ClickButton()
      Delay(1500)
      #Clicks the 'ButtonYes' button.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.Border.ButtonYes.ClickButton()
      Delay(1500)
      #Clicks the 'Export' object.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Export.Click(9, 11)
      Delay(1500)
      #Clicks the 'btnExport' button.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.btnExport.ClickButton()
      Delay(1500)
      #Clicks the 'ButtonBackToQuery' button.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonBackToQuery.ClickButton()
      #Sets the 'btnExportPopUp' toggle button to the cbChecked state.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.btnExportPopUp.ClickButton(cbChecked) 
      #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.listDownload object equals True.
      aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.listDownload, "Enabled", cmpEqual, True)
       
       
      
def VerifyIfDeleteButtonIsDisabled():
    CreateAI_HumanQueryPrivate()    
    #Checks whether the 'wState' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.chkquery object equals 1.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.chkquery, "wState", cmpEqual, 1)
    #Sets the state of the 'chkquery' check box to cbUnchecked.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.chkquery.ClickButton(cbUnchecked)
    #Checks whether the 'wState' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.chkquery object equals 0.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.chkquery, "wState", cmpEqual, 0)
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete object equals False.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete, "Enabled", cmpEqual, False)
    Delay(2000)
    #Clicks the 'toggleBtn' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn.Click(89, 17)
    #Clicks the 'ButtonDelete' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete.ClickButton()
    #Clicks the 'ButtonYesDeleteIt' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ButtonYesDeleteIt.ClickButton()
    
    
    
    
    
def VerifySearchForDropdownWorkingCorrectly():
    CommonUtility.LogoutandClose()
    CommonUtility.GotoSearch() 
#Clicks the 'ButtonAddNew' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonAddNew.ClickButton()
    #Clicks the 'TextBox' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.Click(83, 25)
    #Enters the text 'verify drop down' in the 'TextBox' text editor.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.SetText("verify drop down")
    #Checks whether the 'Text' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbEvent object equals 'Select an event'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbEvent, "Text", cmpEqual, "Select an event")
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbEvent object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbEvent, "Enabled", cmpEqual, True)
    #Clicks the 'cmbEvent' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbEvent.Click(155, 18)
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator, "Enabled", cmpEqual, True)
    
  
      
      
def VerifyDefaultQuertProperties(): 
    Delay(2000)  
##Clicks the 'ButtonDelete' button.
#    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete.ClickButton()
#    #Clicks the 'ButtonYesDeleteIt' button.
#    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ButtonYesDeleteIt.ClickButton()
#    #Clicks the 'ButtonAddNew' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonAddNew.ClickButton()
    Regions.Grid4.Check(Regions.CreateRegionInfo(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Grid2, 3, 197, 310, 546, False))
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ScrollViewer.TextblockName object equals 'Name'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ScrollViewer.TextblockName, "WPFControlText", cmpEqual, "Name")
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox, "Enabled", cmpEqual, True)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ScrollViewer.txtQueryName object equals 'Query Type'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ScrollViewer.txtQueryName, "WPFControlText", cmpEqual, "Query Type")
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPrivate object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPrivate, "Enabled", cmpEqual, True)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ScrollViewer.TextblockSearchFor object equals 'Search for'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ScrollViewer.TextblockSearchFor, "WPFControlText", cmpEqual, "Search for")
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ScrollViewer.RadiobuttonEvents object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ScrollViewer.RadiobuttonEvents, "Enabled", cmpEqual, True)
    #Checks whether the 'Text' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbEvent object equals 'Select an event'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbEvent, "Text", cmpEqual, "Select an event")
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbEvent object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbEvent, "Enabled", cmpEqual, True)
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ExtendedCombo object equals False.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ExtendedCombo, "Enabled", cmpEqual, False)
    #Checks whether the 'Text' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ExtendedCombo object equals 'Select resource(s)'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ExtendedCombo, "Text", cmpEqual, "Select resource(s)")
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RBtn object equals 'OR'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RBtn, "WPFControlText", cmpEqual, "OR")
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RBtn object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RBtn, "Enabled", cmpEqual, True)
    #Checks whether the 'wText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange object equals 'Select days'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange, "wText", cmpEqual, "Select days")
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange, "Enabled", cmpEqual, True)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.UpdateQuery object equals 'Save Query'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.UpdateQuery, "WPFControlText", cmpEqual, "Save Query")
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.UpdateQuery object equals False.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.UpdateQuery, "Enabled", cmpEqual, False)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.FocusedbuttonSearch object equals 'Search'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.FocusedbuttonSearch, "WPFControlText", cmpEqual, "Search")
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.FocusedbuttonSearch object equals False.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.FocusedbuttonSearch, "Enabled", cmpEqual, False)
    
    
def VerifyPublicQueryColumn():
#    DeletePublicQueryByDeleteIcon()
    CreatePublicQuery()
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.toggleBtn, "wState", cmpEqual, 0)
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.TreeViewItem.toggleBtn, "wState", cmpEqual, 0)
    DeleteSingleQueryByDeleteButton()
    #DeleteSingleQueryByDeleteButton()
   
    
    
def VerifyPrivateQueryColumn():
    CreateMotionDetectionPrivateQuery()
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.toggleBtn, "wState", cmpEqual, 0)
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn, "wState", cmpEqual, 0)
    DeleteSingleQueryByDeleteButton()

    
def VerifyUpdateQueryWorkingCorrectly(): 
    CreatePublicQuery()
        
     #Drags the 'TextBox' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.Drag(232, 19, -220, 13)
    #Enters the text 'verify update query' in the 'TextBox' text editor.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.SetText("verify update query ")
    #Clicks the 'RadiobuttonPrivate' radio button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPrivate.ClickButton()
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.toggleBtn object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.toggleBtn, "Enabled", cmpEqual, True)
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.TreeViewItem.toggleBtn object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.TreeViewItem.toggleBtn, "Enabled", cmpEqual, True)
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.UpdateQuery object equals True.
#    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.UpdateQuery, "Enabled", cmpEqual, True)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.UpdateQuery).BlockByText("Query").Click()
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.toggleBtn object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.toggleBtn, "Enabled", cmpEqual, True)
    DeleteSingleQueryByDeleteButton()
   
  

    
    
    

def CreateQuerywithCustomTimeFrame():
    CommonUtility.LogoutandClose()
    CommonUtility.GotoSearch()
    #Clicks the 'ButtonAddNew' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonAddNew.ClickButton()
    #Clicks the 'TextBox' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.Click(135, 26)
    #Enters the text 'verify timeframe' in the 'TextBox' text editor.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.SetText("Create Query Cust Time Frame")
    Delay(1000)
    #Clicks the 'cmbEvent' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbEvent.Click(128, 33)
    Delay(1000)
    #Clicks the 'PopupRoot' object.
    Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.Click(123, 24)
    Delay(1000)
    #Enters 'motion' in the 'HwndSource_shell' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.Keys("motion")
    Delay(1000)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.RadTreeViewItem).BlockByText("Motion").Click()
    Delay(1000)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ExtendedCombo).BlockByText("resource").Click()
    Delay(1000)
    #Clicks the 'PopupRoot' object.
    Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.Click(113, 28)
    Delay(1000)
    #Enters '248' in the 'HwndSource_shell' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.Keys("248")
    Delay(1000)
    #Sets the 'toggleBtn' toggle button to the cbChecked state.
    Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.toggleBtn.ClickButton(cbChecked)
    Delay(1000)
    #Selects the 0 item of the 'cmbDateRange' combo box.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange.ClickItem(0)
    Delay(1000)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.Border.Calendardaybutton202).BlockByText("20").Click()
    #Clicks the 'Calendardaybutton19' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.Border.Calendardaybutton19.Click(25, 17)
    Delay(1000)
    #Clicks the 'Calendardaybutton20' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.Border.Calendardaybutton20.Click(26, 16)
    Delay(1000)
    #Drags the 'NumericSpinner' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.Border.NumericSpinner.Drag(36, 48, -35, 3)
    Delay(1000)
    #Drags the 'NumericSpinner' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.Border.NumericSpinner.Drag(32, 46, -26, 0)
    Delay(1000)
    #Enters '10' in the 'NumericSpinner' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.Border.NumericSpinner.Keys("10")
    #Drags the 'NumericSpinner2' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.Border.NumericSpinner2.Drag(35, 46, -24, 4)
    Delay(1000)
    #Drags the 'NumericSpinner2' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.Border.NumericSpinner2.Drag(20, 46, 28, 0)
    Delay(1000)
    #Enters '10' in the 'NumericSpinner2' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.Border.NumericSpinner2.Keys("10")
    Delay(1000)
    #Drags the 'NumericSpinner3' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.Border.NumericSpinner3.Drag(20, 52, 16, 3)
    
    Delay(1000)
    #Enters '10' in the 'NumericSpinner3' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.Border.NumericSpinner3.Keys("10")
    Delay(1000)
#    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.Border.NumericSpinner4).BlockByText("02").Click()
    #Drags the 'NumericSpinner4' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.Border.NumericSpinner4.Drag(34, 46, -30, 4)
    #Drags the 'NumericSpinner4' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.Border.NumericSpinner4.Drag(18, 45, 32, 0)
    #Enters '15' in the 'NumericSpinner4' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.Border.NumericSpinner4.Keys("15")
    #Drags the 'NumericSpinner22' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.Border.NumericSpinner22.Drag(31, 47, -21, 4)
    #Enters '15' in the 'NumericSpinner22' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.Border.NumericSpinner22.Keys("15")
    #Drags the 'NumericSpinner32' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.Border.NumericSpinner32.Drag(17, 46, 32, 0)
    Delay(2000)
    #Enters '15' in the 'NumericSpinner32' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.Border.NumericSpinner32.Keys("15")
    Delay(2000)
    #Clicks the 'ButtonApplyAndClose' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.Border.ButtonApplyAndClose.ClickButton()
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.UpdateQuery).BlockByText("Save").Click()
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn, "wState", cmpEqual, 0)
    

    

    
def VerifySelectTimeFrameButtonFunctionality():  
    Delay(2000)
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange, "wText", cmpEqual, "19-09-2023 10:10:10 , 20-09-2023 15:15:15")
    #Clicks the 'FocusedbuttonSearch' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.FocusedbuttonSearch.Click(42, 21)
    Delay(1000)
    #Sets the state of the 'CheckBox' check box to cbChecked.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.CheckBox.ClickButton(cbChecked)
    #Clicks the 'btnPlay' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.btnPlay.ClickButton()
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.Textblock172200248Camera object equals '172.20.0.248_Camera'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.Textblock172200248Camera, "WPFControlText", cmpEqual, "172.20.0.248_Camera")


def VerifyStartAndEndTimeOnSearchResult ():
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.DatagridcolumnheaderStartTimeEndTime object equals ' Start Time - End Time'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.DatagridcolumnheaderStartTimeEndTime, "WPFControlText", cmpEqual, " Start Time - End Time")
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.Textblock object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.Textblock, "Enabled", cmpEqual, True)    
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonBackToQuery.ClickButton()
    #Checks whether the 'wText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange object equals '19-09-2023 10:10:10 , 20-09-2023 15:15:15'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange, "wText", cmpEqual, "19-09-2023 10:10:10 , 20-09-2023 15:15:15")
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.UpdateQuery).BlockByText("Query").Click()
    
    
def VerifyDoubleClickonCustomtimeframeQuery():
    Delay(1000)
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn, "Enabled", cmpEqual, True)
    #Double-clicks the 'toggleBtn' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn.DblClick(85, 20)
    Delay(1000)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Grid.TextblockSearchResult object equals 'Search Result'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Grid.TextblockSearchResult, "Enabled", cmpEqual, True)
    #Sets the state of the 'CheckBox' check box to cbChecked.
    Delay(1000)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.CheckBox.ClickButton(cbChecked)
    #Clicks the 'btnPlay' button.
    Delay(1000)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.btnPlay.ClickButton()
    #Clicks the 'ButtonBackToQuery' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonBackToQuery.ClickButton()
    
    
    
def VerifyUpdateofCustomtimeframequery ():
    #Drags the 'TextBox' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.Drag(244, 22, -334, -4)
    #Enters the text 'update cust time frame' in the 'TextBox' text editor.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.SetText("update cust time frame")
    #Clicks the 'cmbDateRange' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange.Click(313, 6)
    #Selects the 0 item of the 'cmbDateRange' combo box.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange.ClickItem(0)
    #Clicks the 'Calendardaybutton202' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.Border.Calendardaybutton202.Click(23, 9)
    #Clicks the 'Calendardaybutton21' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.Border.Calendardaybutton21.Click(22, 20)
    Delay(1000)
    #Drags the 'NumericSpinner' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.Border.NumericSpinner.Drag(32, 47, -43, -6)
    Delay(1000)
    #Enters '10' in the 'NumericSpinner' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.Border.NumericSpinner.Keys("10")
    Delay(1000)
    #Drags the 'NumericSpinner2' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.Border.NumericSpinner2.Drag(31, 48, -14, -4)
    Delay(1000)
    #Enters '50' in the 'NumericSpinner2' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.Border.NumericSpinner2.Keys("50")
    Delay(1000)
    #Drags the 'NumericSpinner3' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.Border.NumericSpinner3.Drag(33, 52, -21, -6)
    #Enters '20' in the 'NumericSpinner3' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.Border.NumericSpinner3.Keys("20")
    Delay(1000)
    #Drags the 'NumericSpinner4' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.Border.NumericSpinner4.Drag(30, 49, -15, 0)
    Delay(1000)
    #Enters '11' in the 'NumericSpinner4' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.Border.NumericSpinner4.Keys("11")
    Delay(1000)
    #Drags the 'NumericSpinner22' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.Border.NumericSpinner22.Drag(32, 48, -16, 0)
    Delay(1000)
    #Enters '10' in the 'NumericSpinner22' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.Border.NumericSpinner22.Keys("10")
    Delay(1000)
    #Drags the 'NumericSpinner32' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.Border.NumericSpinner32.Drag(32, 43, -18, 3)
    Delay(1000)
    #Enters '50' in the 'NumericSpinner32' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.Border.NumericSpinner32.Keys("50")
    Delay(1000)
    #Clicks the 'ButtonApplyAndClose' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.Border.ButtonApplyAndClose.ClickButton()
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.UpdateQuery).BlockByText("Update").Click()
    #Checks whether the 'wText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange object equals '20-09-2023 10:50:20 , 21-09-2023 23:10:50'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange, "wText", cmpEqual, "20-09-2023 10:50:20 , 21-09-2023 11:10:50")
    #Clicks the 'FocusedbuttonSearch' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.FocusedbuttonSearch.Click(71, 30)
    Delay(5000)
    #Sets the state of the 'CheckBox' check box to cbChecked.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.CheckBox.ClickButton(cbChecked)
    #Clicks the 'btnPlay' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.eventsResultDataGrid.btnPlay.ClickButton()
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Grid.TextblockSearchResult object equals 'Search Result'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Grid.TextblockSearchResult, "WPFControlText", cmpEqual, "Search Result")
    #Clicks the 'ButtonBackToQuery' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonBackToQuery.ClickButton()
    DeleteSingleQueryByDeleteButton()

    
    
def CreateMultiplePrivateQueries():
    CommonUtility.LogoutandClose()
    CommonUtility.GotoSearch()  
    for i in range (8):
      #Clicks the 'TabitemEventAlarmSearch' object.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TabitemEventAlarmSearch.Click(100, 22)
      #Clicks the 'ButtonAddNew' button.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonAddNew.ClickButton()
       #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox object equals True.
      aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox, "Enabled", cmpEqual, True)
      Log.Message("This Check point for Query filed Veried")
      #Clicks the 'TextBox' object.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.Click(111, 15)
      #Enters the text 'motion detection' in the 'TextBox' text editor.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.SetText("motion detection")
      Delay(1000)
      OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbEvent).BlockByText("Select an event").Click()
      Delay(1000)
      OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator).BlockByText("Search").Click()
      #Enters 'motion detection' in the 'HwndSource_shell' object.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.Keys("motion detection")
      Delay(1000)
      OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.RadTreeViewItem).BlockByText("Motion").Click()
      Delay(1000)
      OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ExtendedCombo).BlockByText("resource").Click()
      Delay(1000)
      OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator).BlockByText("...").Click()
      Delay(1000)
      #Enters '.250' in the 'HwndSource_shell' object.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.Keys(".248")
      Delay(1000)
      #Sets the 'toggleBtn' toggle button to the cbChecked state.
      Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.toggleBtn.ClickButton(cbChecked)
      #Selects the 2 item of the 'cmbDateRange' combo box.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange.Click() 
      #Selects the 1 item of the 'cmbDateRange' combo box.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange.ClickItem(2)
      OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.UpdateQuery).BlockByText("Save Query").Click()  
      #Checks whether the 'wState' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn object equals 0.
      Regions.toggleBtn.Check(Regions.CreateRegionInfo(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn, 21, 7, 115, 19, False), False, False, 1165, 136)
      aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.toggleBtn, "wState", cmpEqual, 0)
      Log.Message("MOTION DETECTION PRIVATE QUERY SAVED")
    #Verify mulple privete query
    Tables.Grid.Check()
    Log.Message("Multiple Private query Created")
  
    
def VerifyDeletemultiplePrivatequery():
    CommonUtility.LogoutandClose()
    CommonUtility.GotoSearch()
    Tables.Grid.Check()
    #Sets the state of the 'chkquery' check box to cbChecked.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.chkquery.ClickButton(cbChecked)
    Delay(1000)
    #Sets the state of the 'chkquery' check box to cbChecked.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.chkquery.ClickButton(cbChecked)
    #Clicks the 'ButtonDelete' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete.ClickButton()
    Delay(2000)
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.Border object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.Border, "Enabled", cmpEqual, True)
    #Clicks the 'ButtonYesDeleteIt' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ButtonYesDeleteIt.ClickButton()
    Tables.TreeviewitemTypePrivateQueryItemsSystemLin2.Check()
    Log.Message("Multiple Query Deleted")
    
    
    
def VerifyDeleteallPrivatequery ():
    #Sets the 'toggleBtn' toggle button to the cbChecked state.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.toggleBtn.ClickButton(cbChecked)
    Delay(1000)
    #Sets the state of the 'chkquery' check box to cbChecked.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.chkquery.ClickButton(cbChecked)
    #Clicks the 'ButtonDelete' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete.ClickButton()
    #Clicks the 'ButtonYesDeleteIt' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ButtonYesDeleteIt.ClickButton()
    #Clicks the 'ButtonDelete' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete.ClickButton()
    #Clicks the 'ButtonYesDeleteIt' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ButtonYesDeleteIt.ClickButton()
    #Compares the Grid6 Stores item with the image of the Regions.CreateRegionInfo(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Grid2, 5, 190, 310, 647, False) object.
    Regions.Grid6.Check(Regions.CreateRegionInfo(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.Grid2, 5, 190, 310, 647, False))
    Log.Message("All Queries are Deteled")
    
    
    
    
    
    
def VerifyMaximumnumberofPrivatequeriesdisplayedperpage ():
      CommonUtility.LogoutandClose()
      CommonUtility.GotoSearch()
      Delay(1000)     
      for i in range (21):
        #Clicks the 'TabitemEventAlarmSearch' object.
        Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TabitemEventAlarmSearch.Click(100, 22)
        #Clicks the 'ButtonAddNew' button.
        Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonAddNew.ClickButton()
         #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox object equals True.
        aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox, "Enabled", cmpEqual, True)
        Log.Message("This Check point for Query filed Veried")
        #Clicks the 'TextBox' object.
        Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.Click(111, 15)
        #Enters the text 'motion detection' in the 'TextBox' text editor.
        Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.SetText("motion detection" +str(i))
        Delay(1000)
        OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbEvent).BlockByText("Select an event").Click()
        Delay(1000)
        OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator).BlockByText("Search").Click()
        #Enters 'motion detection' in the 'HwndSource_shell' object.
        Aliases.Valerus_Bootstrapper.HwndSource_shell.Keys("motion detection")
        Delay(1000)
        OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.RadTreeViewItem).BlockByText("Motion").Click()
        Delay(1000)
        OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ExtendedCombo).BlockByText("resource").Click()
        Delay(1000)
        OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator).BlockByText("...").Click()
        Delay(1000)
        #Enters '.250' in the 'HwndSource_shell' object.
        Aliases.Valerus_Bootstrapper.HwndSource_shell.Keys(".248")
        Delay(1000)
        #Sets the 'toggleBtn' toggle button to the cbChecked state.
        Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.toggleBtn.ClickButton(cbChecked)
        #Selects the 2 item of the 'cmbDateRange' combo box.
        Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange.Click() 
        #Selects the 1 item of the 'cmbDateRange' combo box.
        Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange.ClickItem(2)
        OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.UpdateQuery).BlockByText("Save Query").Click()  
        #Checks whether the 'wState' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn object equals 0.
        Regions.toggleBtn.Check(Regions.CreateRegionInfo(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn, 21, 7, 115, 19, False), False, False, 1165, 136)
        aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.toggleBtn, "wState", cmpEqual, 0)
        
        
def VerifyfunctionalityofscrollbarinprivateQuerycolumn():
      Delay(1000)     
      for i in range (10):
        #Clicks the 'TabitemEventAlarmSearch' object.
        Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TabitemEventAlarmSearch.Click(100, 22)
        #Clicks the 'ButtonAddNew' button.
        Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonAddNew.ClickButton()
         #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox object equals True.
        aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox, "Enabled", cmpEqual, True)
        Log.Message("This Check point for Query filed Veried")
        #Clicks the 'TextBox' object.
        Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.Click(111, 15)
        #Enters the text 'motion detection' in the 'TextBox' text editor.
        Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.SetText("motion detection" +str(i))
        Delay(1000)
        OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbEvent).BlockByText("Select an event").Click()
        Delay(1000)
        OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator).BlockByText("Search").Click()
        #Enters 'motion detection' in the 'HwndSource_shell' object.
        Aliases.Valerus_Bootstrapper.HwndSource_shell.Keys("motion detection")
        Delay(1000)
        OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.RadTreeViewItem).BlockByText("Motion").Click()
        Delay(1000)
        OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ExtendedCombo).BlockByText("resource").Click()
        Delay(1000)
        OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator).BlockByText("...").Click()
        Delay(1000)
        #Enters '.250' in the 'HwndSource_shell' object.
        Aliases.Valerus_Bootstrapper.HwndSource_shell.Keys(".248")
        Delay(1000)
        #Sets the 'toggleBtn' toggle button to the cbChecked state.
        Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.toggleBtn.ClickButton(cbChecked)
        #Selects the 2 item of the 'cmbDateRange' combo box.
        Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange.Click() 
        #Selects the 1 item of the 'cmbDateRange' combo box.
        Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange.ClickItem(2)
        OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.UpdateQuery).BlockByText("Save Query").Click()  
        #Checks whether the 'wState' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn object equals 0.
        Regions.toggleBtn.Check(Regions.CreateRegionInfo(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn, 21, 7, 115, 19, False), False, False, 1165, 136)
        aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.toggleBtn, "wState", cmpEqual, 0)
      #Checks whether the 'ScrollViewer_HorizontalScrollBarVisibility' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView object equals 'Auto'.
      aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView, "ScrollViewer_HorizontalScrollBarVisibility", cmpEqual, "Auto")
      Delay(2000)
      #Sets the 'toggleBtn' toggle button to the cbChecked state.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.toggleBtn.ClickButton(cbChecked)
      #Clicks the 'ButtonDelete' button.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete.ClickButton()
      Delay(1000)
      #Clicks the 'ButtonYesDeleteIt' button.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ButtonYesDeleteIt.ClickButton()
      #Clicks the 'ButtonDelete' button.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete.ClickButton()
      Delay(1000)
      #Clicks the 'ButtonYesDeleteIt' button.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ButtonYesDeleteIt.ClickButton()
      
      
def CreateMultiplePublicQueries():
    CommonUtility.LogoutandClose()
    CommonUtility.GotoSearch()
    for i in range(8):
      #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonAddNew object equals True.
         #Clicks the 'TabitemEventAlarmSearch' object.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TabitemEventAlarmSearch.Click(150, 34) 
      aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonAddNew, "Enabled", cmpEqual, True)
      #Clicks the 'ButtonAddNew' button.
      Delay(1000)
      Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonAddNew.ClickButton()
      #Clicks the 'TextBox' object.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.Click(140, 20)
      #Enters the text 'motion detection public query' in the 'TextBox' text editor.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.SetText("motion detection public query" +str(i))
      #Clicks the 'RadiobuttonPublic' radio button.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPublic.ClickButton()
      #Checks whether the 'wChecked' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPublic object equals True.
      aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPublic, "wChecked", cmpEqual, True)
      #Checks whether the 'wChecked' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPrivate object equals False.
      aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPrivate, "wChecked", cmpEqual, False)
      #Clicks the 'TabitemEventAlarmSearch' object.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TabitemEventAlarmSearch.Click(100, 22)
      Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.Click(111, 15)
      Delay(1000)
      OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbEvent).BlockByText("Select an event").Click()
      Delay(1000)
      OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator).BlockByText("Search").Click()
      #Enters 'motion detection' in the 'HwndSource_shell' object.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.Keys("motion detection")
      Delay(1000)
      OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.RadTreeViewItem).BlockByText("Motion").Click()
      Delay(1000)
      OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ExtendedCombo).BlockByText("resource").Click()
      Delay(1000)
      OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator).BlockByText("...").Click()
      Delay(1000)
      #Clicks the 'PopupRoot' object.
      Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.Click(166, 26)
      #Enters '.142' in the 'HwndSource_shell' object.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.Keys(".142")
      Delay(1000)
      #Sets the 'toggleBtn' toggle button to the cbChecked state.
      Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.toggleBtn.ClickButton(cbChecked)
      #Checks whether the 'wText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange object equals 'Select days'.
      aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange, "wText", cmpEqual, "Select days")
         #Selects the 2 item of the 'cmbDateRange' combo box.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange.Click() 
      #Selects the 1 item of the 'cmbDateRange' combo box.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange.ClickItem(2)
         #Clicks the 'UpdateQuery' object.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.UpdateQuery.Click(90, 32)
      #Checks whether the 'wState' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.toggleBtn object equals 0.
      aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.toggleBtn, "wState", cmpEqual, 0)
      aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.TreeViewItem.toggleBtn, "wState", cmpEqual, 0)
    Log.Message("Multiple Public Query Created")

    
    
def VerifyDeleteMultiplePublicQuery ():
    CommonUtility.LogoutandClose()
    CommonUtility.GotoSearch()
    Delay(1000)
    #Sets the state of the 'chkquery' check box to cbChecked.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.TreeViewItem.chkquery.ClickButton(cbChecked)
    Delay(1000)
    #Clicks the 'ButtonDelete' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete.ClickButton()
    Delay(1000)
    #Clicks the 'ButtonYesDeleteIt' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ButtonYesDeleteIt.ClickButton()
    
    
    
def VerifyClickOrSelectOnOtherQueryAfterDeletionOfTheQuery ():
    #Clicks the 'toggleBtn' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.TreeViewItem.toggleBtn.Click(115, 21)
    #Checks whether the 'wText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox object equals 'motion detection public query3'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.TreeViewItem.toggleBtn, "wState", cmpEqual, 0)
  
    
    
def VerifyDeleteAllPublicQuery():
    #Sets the 'toggleBtn' toggle button to the cbChecked state.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.toggleBtn.ClickButton(cbChecked)
    Delay(1000)
    #Clicks the 'ButtonDelete' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete.ClickButton()
    Delay(1000)
    #Clicks the 'ButtonYesDeleteIt' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ButtonYesDeleteIt.ClickButton()
    Delay(1000)
    #Clicks the 'ButtonDelete' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete.ClickButton()
    #Clicks the 'ButtonYesDeleteIt' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ButtonYesDeleteIt.ClickButton()
   
    
    
    
def VerifyMaximumNumberOfPublicQuerieDisplayedPerPage ():
    for i in range(20):
      #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonAddNew object equals True.
         #Clicks the 'TabitemEventAlarmSearch' object.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TabitemEventAlarmSearch.Click(150, 34) 
      aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonAddNew, "Enabled", cmpEqual, True)
      #Clicks the 'ButtonAddNew' button.
      Delay(1000)
      Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonAddNew.ClickButton()
      #Clicks the 'TextBox' object.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.Click(140, 20)
      #Enters the text 'motion detection public query' in the 'TextBox' text editor.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.SetText("motion detection public query" +str(i))
      #Clicks the 'RadiobuttonPublic' radio button.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPublic.ClickButton()
      #Checks whether the 'wChecked' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPublic object equals True.
      aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPublic, "wChecked", cmpEqual, True)
      #Checks whether the 'wChecked' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPrivate object equals False.
      aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPrivate, "wChecked", cmpEqual, False)
      #Clicks the 'TabitemEventAlarmSearch' object.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TabitemEventAlarmSearch.Click(100, 22)
      Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.Click(111, 15)
      Delay(1000)
      OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbEvent).BlockByText("Select an event").Click()
      Delay(1000)
      OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator).BlockByText("Search").Click()
      #Enters 'motion detection' in the 'HwndSource_shell' object.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.Keys("motion detection")
      Delay(1000)
      OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.RadTreeViewItem).BlockByText("Motion").Click()
      Delay(1000)
      OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ExtendedCombo).BlockByText("resource").Click()
      Delay(1000)
      OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator).BlockByText("...").Click()
      Delay(1000)
      #Clicks the 'PopupRoot' object.
      Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.Click(166, 26)
      #Enters '.142' in the 'HwndSource_shell' object.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.Keys(".142")
      Delay(1000)
      #Sets the 'toggleBtn' toggle button to the cbChecked state.
      Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.toggleBtn.ClickButton(cbChecked)
      #Checks whether the 'wText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange object equals 'Select days'.
      aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange, "wText", cmpEqual, "Select days")
         #Selects the 2 item of the 'cmbDateRange' combo box.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange.Click() 
      #Selects the 1 item of the 'cmbDateRange' combo box.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange.ClickItem(2)
         #Clicks the 'UpdateQuery' object.
      Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.UpdateQuery.Click(90, 32)
      #Checks whether the 'wState' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.toggleBtn object equals 0.
      aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.toggleBtn, "wState", cmpEqual, 0)
      aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.TreeViewItem.toggleBtn, "wState", cmpEqual, 0)
    Log.Message("Multiple Public Query Created")
    
    
    
def VerifyScrollbarForPublicQuery():
    for i in range(5):
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonAddNew object equals True.
           #Clicks the 'TabitemEventAlarmSearch' object.
        Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TabitemEventAlarmSearch.Click(150, 34) 
        aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonAddNew, "Enabled", cmpEqual, True)
        #Clicks the 'ButtonAddNew' button.
        Delay(1000)
        Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonAddNew.ClickButton()
        #Clicks the 'TextBox' object.
        Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.Click(140, 20)
        #Enters the text 'motion detection public query' in the 'TextBox' text editor.
        Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.SetText("motion detection public query" +str(i))
        #Clicks the 'RadiobuttonPublic' radio button.
        Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPublic.ClickButton()
        #Checks whether the 'wChecked' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPublic object equals True.
        aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPublic, "wChecked", cmpEqual, True)
        #Checks whether the 'wChecked' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPrivate object equals False.
        aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPrivate, "wChecked", cmpEqual, False)
        #Clicks the 'TabitemEventAlarmSearch' object.
        Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TabitemEventAlarmSearch.Click(100, 22)
        Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.Click(111, 15)
        Delay(1000)
        OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbEvent).BlockByText("Select an event").Click()
        Delay(1000)
        OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator).BlockByText("Search").Click()
        #Enters 'motion detection' in the 'HwndSource_shell' object.
        Aliases.Valerus_Bootstrapper.HwndSource_shell.Keys("motion detection")
        Delay(1000)
        OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.RadTreeViewItem).BlockByText("Motion").Click()
        Delay(1000)
        OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ExtendedCombo).BlockByText("resource").Click()
        Delay(1000)
        OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator).BlockByText("...").Click()
        Delay(1000)
        #Clicks the 'PopupRoot' object.
        Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.Click(166, 26)
        #Enters '.142' in the 'HwndSource_shell' object.
        Aliases.Valerus_Bootstrapper.HwndSource_shell.Keys(".142")
        Delay(1000)
        #Sets the 'toggleBtn' toggle button to the cbChecked state.
        Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.toggleBtn.ClickButton(cbChecked)
        #Checks whether the 'wText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange object equals 'Select days'.
        aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange, "wText", cmpEqual, "Select days")
           #Selects the 2 item of the 'cmbDateRange' combo box.
        Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange.Click() 
        #Selects the 1 item of the 'cmbDateRange' combo box.
        Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange.ClickItem(2)
           #Clicks the 'UpdateQuery' object.
        Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.UpdateQuery.Click(90, 32)
    #Checks whether the 'ScrollViewer_HorizontalScrollBarVisibility' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView object equals 'Auto'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView, "ScrollViewer_HorizontalScrollBarVisibility", cmpEqual, "Auto")

    
    
    
def VerifySelectMultiplePublicQueryFunctionality():
  CommonUtility.LogoutandClose()
  CommonUtility.GotoSearch()
  if aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.TreeViewItem.chkquery, "wState", cmpEqual, 0):
    #Sets the state of the 'chkquery' check box to cbChecked.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.TreeViewItem.chkquery.ClickButton(cbChecked)
    #Sets the state of the 'chkquery' check box to cbChecked.
  else:
    Log.Message("Alredy checked")
  #Rotates the mouse wheel to -1 over the 'toggleBtn' object.
  Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.TreeViewItem.toggleBtn.MouseWheel(-1)
  #Rotates the mouse wheel to -8 over the 'toggleBtn' object.
  Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.TreeViewItem.toggleBtn.MouseWheel(-8)
  #Checks whether the 'wState' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.TreeViewItem.chkquery object equals 1.
  aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.TreeViewItem.chkquery, "wState", cmpEqual, 1)

  
  
  
  
def VerifyWhenUserMoveToOtherTabAfterDeletionOfAllTheQuery (): 
    VerifyDeleteAllPublicQuery()
    #Clicks the 'ButtonDelete' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonDelete.ClickButton()
    #Clicks the 'ButtonYesDeleteIt' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.HwndSource_OverlayWindow.OverlayWindow.ButtonYesDeleteIt.ClickButton()
    Delay(2000)
    #Clicks the 'TabitemMonitoring' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.TabitemMonitoring.Click(64, 53)  
    Delay(2000)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.TextblockClickOnTheDesiredLayout object equals 'Click on the desired layout'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabView.TextblockClickOnTheDesiredLayout, "WPFControlText", cmpEqual, "Click on the desired layout")
    Delay(2000)
    #Clicks the 'TabitemSearch' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.TabitemSearch.Click(38, 54)
    Delay(2000)
    #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView, "Enabled", cmpEqual, True)
    #Checks whether the 'WPFControlText' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonAddNew object equals 'Add New'.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonAddNew, "WPFControlText", cmpEqual, "Add New")

    
    
def VerifyNewQueryCreationAfterDeletionOfAllAueryAtATime():
    #Clicks the 'TabitemEventAlarmSearch' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TabitemEventAlarmSearch.Click(100, 22)
    #Clicks the 'ButtonAddNew' button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ButtonAddNew.ClickButton()
     #Checks whether the 'Enabled' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox, "Enabled", cmpEqual, True)
    Log.Message("This Check point for Query filed Veried")
    #Clicks the 'TextBox' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.Click(111, 15)
    #Enters the text 'motion detection' in the 'TextBox' text editor.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.SetText("create query after del all query")
    Delay(2000)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbEvent).BlockByText("Select an event").Click()
    Delay(2000)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator).BlockByText("Search").Click()
    #Enters 'motion detection' in the 'HwndSource_shell' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.Keys("motion detection")
    Delay(2000)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.RadTreeViewItem).BlockByText("Motion").Click()
    Delay(2000)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ExtendedCombo).BlockByText("resource").Click()
    Delay(2000)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator).BlockByText("...").Click()
    Delay(2000)
    #Enters '.250' in the 'HwndSource_shell' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.Keys(".248")
    Delay(2000)
    #Sets the 'toggleBtn' toggle button to the cbChecked state.
    Aliases.Valerus_Bootstrapper.HwndSource_PopupRoot.PopupRoot.NonLogicalAdornerDecorator.toggleBtn.ClickButton(cbChecked)
    Delay(2000)
    #Clicks the 'NumericSpinner' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.NumericSpinner.Click(39, 38)
    Delay(1000)
    #Clicks the 'NumricSpinner' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.NumericSpinner.Click(25, 8)
    Delay(500)
    #Clicks the 'NumericSpinner' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.NumericSpinner.Click(23, 8)
    Delay(500)
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.NumericSpinner.Click(21, 62)
    Delay(500)
    #Clicks the 'NumericSpinner' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.NumericSpinner.Click(21, 62)
    Delay(500)
    #Clicks the 'NumericSpinner' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.NumericSpinner.Click(20, 35)
    #Drags the 'NumericSpinner' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.NumericSpinner.Drag(20, 35, 18, -1)
    #Enters '20' in the 'NumericSpinner' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.NumericSpinner.Keys("5")
    #Clicks the 'NumericSpinner' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.NumericSpinner.Click(28, 65)
    Delay(500)
    #Clicks the 'NumericSpinner' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.NumericSpinner.Click(25, 65)
    Delay(500)
    #Clicks the 'NumericSpinner' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.NumericSpinner.Click(22, 9)
    Delay(500)
    #Clicks the 'NumericSpinner' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.NumericSpinner.Click(22, 9)
    Delay(1000)
    #Clicks the 'cmbDateRange' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange.Click(156, 15)
    Delay(1000)
    #Clicks the 'cmbDateRange' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange.Click(705, 23)
    Delay(500)
    #Selects the 2 item of the 'cmbDateRange' combo box.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange.Click() 
    #Selects the 1 item of the 'cmbDateRange' combo box.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.cmbDateRange.ClickItem(2)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.UpdateQuery).BlockByText("Save Query").Click()  
    #Checks whether the 'wState' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn object equals 0.
    Regions.toggleBtn.Check(Regions.CreateRegionInfo(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn, 21, 7, 115, 19, False), False, False, 1165, 136)
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.TreeViewItem.toggleBtn, "wState", cmpEqual, 0)
    
    
    
    
def UpdatePrivateQueryToPublic():
    #Drags the 'TextBox' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.Drag(234, 15, -223, -4)
    #Enters the text 'update prive to public' in the 'TextBox' text editor.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.SetText("update private to public")
    #Checks whether the 'wChecked' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPrivate object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPrivate, "wChecked", cmpEqual, True)
    #Checks whether the 'wChecked' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPublic object equals False.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPublic, "wChecked", cmpEqual, False)
    #Clicks the 'RadiobuttonPublic' radio button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPublic.ClickButton()
    #Checks whether the 'wChecked' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPublic object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPublic, "wChecked", cmpEqual, True)
    OCR.Recognize(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.UpdateQuery).BlockByText("Query").Click()
    #Checks whether the 'wChecked' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPrivate object equals False.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPrivate, "wChecked", cmpEqual, False)
    Regions.Grid8.Check(Regions.CreateRegionInfo(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.ScrollViewer.Grid, 291, 99, 196, 47, False), False, False, 1842, 51)
    
    
    
def UpdatePublicQueryToPrivate():
    CommonUtility.LogoutandClose()
    Delay(1000)
    #Drags the 'TextBox' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.Drag(204, 23, -254, 8)
    #Enters the text 'update public to private' in the 'TextBox' text editor.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TextBox.SetText("update public to private")
    #Checks whether the 'wChecked' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPublic object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPublic, "wChecked", cmpEqual, True)
    #Checks whether the 'wChecked' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPrivate object equals False.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPrivate, "wChecked", cmpEqual, False)
    #Clicks the 'RadiobuttonPrivate' radio button.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPrivate.ClickButton()
    #Checks whether the 'wChecked' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPublic object equals False.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPublic, "wChecked", cmpEqual, False)
    Delay(1000)
    #Checks whether the 'wState' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.toggleBtn object equals 0.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePublicQueryItemsSystemLinq.toggleBtn, "wState", cmpEqual, 0)
    #Clicks the 'UpdateQuery' object.
    Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.UpdateQuery.Click(21, 17)
    #Checks whether the 'wState' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.toggleBtn object equals 0.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.TreeView.TreeviewitemTypePrivateQueryItemsSystemLin.toggleBtn, "wState", cmpEqual, 0)
    #Checks whether the 'wChecked' property of the Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPrivate object equals True.
    aqObject.CheckProperty(Aliases.Valerus_Bootstrapper.HwndSource_shell.shell.tabCtrl.tabCtrl.RadiobuttonPrivate, "wChecked", cmpEqual, True)
