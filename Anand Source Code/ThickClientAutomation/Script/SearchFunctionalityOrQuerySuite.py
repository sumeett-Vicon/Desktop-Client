#################################################################################

# Created By : Anand Zade                     Verified By:                 (Date)

# Updated By:31/08/2023                       Verified By:                 (Date)

#

# Description:
# This is Test Suite for Event Search Test cases

# VA-1	Verify Name Feild  

# VA-2	Verify Save Query Functionality

# VA-3	Verify Long Event Name

# VA-4	Verify Search Button When Query Name Is Not Present

# VA-5	Verify Query Saving Without Query Name

# VA-6	Verify Blank Event Selection

# VA-7	Verify Blank Resource Selection

# VA-8	Verify Multiple Resource Selection

# VA-9	Create Motion Detection Private Query

# VA-10	Single click on private query

# VA-11	Update EventName  in Private Query

# VA-12	double click on event query(Private Query)

# VA-13	Search Result Private Query 

# VA-14	Exports the search results of Motion Detection (Private Query)

# VA-15	Cancle the Delete query operation if user uses delete "BUTTON" to delete the query (Private Query) 

# VA-16	Cancle the Delete query operation if user uses delete "ICON" to delete the query (Private Query)

# VA-17	Delete query operation if user uses delete "BUTTON" to delete the query (Private Query)

# VA-18	the Delete query operation if user uses delete "ICON" to delete the query (Private Query)

# VA-19	Create  "Motion Detection" Public Query

# VA-20	Single Click On PublicQuery

# VA-21	Double Click On Public Query

# VA-22	Display Search Result And Play For Public Query

# VA-23	Export Dispalyed Result Video Public Query

# VA-24	Update Public Query

# VA-25	Cancel Delete By Detele Button Public Query

# VA-26	Cancel Delete By Delete Icon Public Query

# VA-27	Delete Public Query By Delete Icon

# VA-28	Delete Public Query By Delete Button

# VA-29	Create AI Human Query Public

# VA-30	Double Click on AI Cam Public Query

# VA-31	The AI HUMAN DETECTION Results (Public Query)

# VA-32	Update the Event Name in Public Query

# VA-33	Export the search results of AI HUMAN DETECTION (Public Query)

# VA-34	AI Query Cancel Delete By Delete Button Public Query EXECUTED

# VA-35	AI Query Cancel Delete By Delete Icon Public Query EXECUTED

# VA-36	AI Query Delete Single Query By Delete Icon Public Query EXECUTED

# VA-37	AI Query Delete Single Query By Delete Button Public Query EXECUTED

# VA-38	Create AI Human Query Private

# VA-39	Double Click On AI Cam Private Query

# VA-40	Search Result Ai Cam Private Query

# VA-41	Update Ai Query Private Query

# VA-42	AI Query Cancel Delete By Delete Button Private Query EXECUTED

# VA-43	AI Query Cancel Delete By Delete Icon Private Query EXECUTED

# VA-44	AI Query Delete Single Query By Delete Icon Private Query EXECUTED

# VA-45	AI Query Delete Single Query By Delete Button Private Query EXECUTED

# VA-46	Verify If Delete Button Is Disabled

# VA-47	Verify Search For Dropdown Working Correctly

# VA-48	Verify Default Query Properties

# VA-49	Verify Private Query Column

# VA-50	Verify Public Query Column

# VA-51	Verify Update Query Working Correctly

# VA-52	Create Query with Custom Time Frame

# VA-53	Verify Select Time Frame Button Functionality

# VA-54	Verify Start And End Time On Search Result 

#VA-55 Verify double click on Custom timeframe query

#VA-56 Verify Update of Custom timeframe query

#VA-57	Create Multiple Private Queries

#VA-58	Verify Delete multiple Private query
 
#VA-59	Verify Delete all Private query
 
#VA-60	Verify Maximum number of Private queries displayed per page
 
#VA-61	Verify functionality of scroll bar in private Query column

#VA-62	Create Multiple Public Queries

#VA-63	Verify Delete multiple public query 

#VA-64	Verify Delete All public query

#VA-65	Verify Maximum number of Public queries displayed per page
 
#VA-66	Verify scrollbar for Public Query

#VA-67	Verify select multiple public query functionality

#VA-68	Verify Click or select on other query after deletion of the query 

#VA-69	Verify when user move to other tab after deletion of all the query



 
 

#################################################################################


# Pre-requisite :-  
# 1) Rquired Cameras: 172.20.0.238, 172.20.0.250, 172.20.0.248
# 2) Events: The required event should have already been triggered in the application.
# 3) All Queries should have been deleted from application.



import CommonUtility
import SearchFunctionality

def SearchSuite():
  SearchFunctionality.VerifyNameFeild()
  Log.Message("Name Feild Has been Verifed")
  
  SearchFunctionality.VerifySaveQueryFunctionality()
  Log.Message("Verify save query functionality")
  
  
  SearchFunctionality.VerifyLongEventName()
  Log.Message("Long Name Query verified with tool tip Has been Verifed")
  
  SearchFunctionality.VerifySearchButtonWhenQueryNameIsNotPresent()
  Log.Message("Search Button Is Disable When Query Name Is Not Present test case Executed")
     
  SearchFunctionality.VerifyQuerySavingWithoutQueryName()
  Log.Message(" Query Saving Without Query Name test case Executed")
  
  SearchFunctionality.VerifyBlankEventSelection()
  Log.Message("Verify Blank Event Selection Test Case Executed")
  
  SearchFunctionality.VerifyBlankResourceSelection()
  Log.Message("Verify Blank Resource Selection Test Case Executed")
  
  SearchFunctionality.VerifyMultipleResourceSelection()
  Log.Message("Verify Multiple Resource Selection Test Case Executed")
    
  SearchFunctionality.CreateMotionDetectionPrivateQuery() #This test case Create  "Motion Detection" Private Query
  Log.Message("Create Motion Detection Private Query EXECUTED")#1
  
  SearchFunctionality.Singleclickonprivatequery()
  Log.Message("Single click on private query EXECUTED")
  
  
  SearchFunctionality.UpdateEventName() #This test case update the Event Name in PrIvate Query
  Log.Message("Update Event Name Private Query EXECUTED")#2
  
  SearchFunctionality.doubleclickOnQueryPrivate()# This test case is to double click on event query(Private Query)
  Log.Message("Double click on private query Executed")
  
  SearchFunctionality.SearchResult() # This test case Shows the Motion Detection Results (Private Query)
  Log.Message("Search Result Private Query EXECUTED")#3
  
  SearchFunctionality.exportsearchvideo() # This test case Exports the search results of Motion Detection (Private Query)
  Log.Message("Export Search Video Private Query EXECUTED")#4
  
  SearchFunctionality.CancleDeletebyDeleteButton()# This test case Cancle the Delete query operation if user uses delete "BUTTON" to delete the query (Private Query) 
  Log.Message("Cancle Delete By Delete Button Private Query EXECUTED")#5
  
  SearchFunctionality.CancleDeletebyDeleteIcon() # This test case Cancle the Delete query operation if user uses delete "ICON" to delete the query (Private Query)
  Log.Message("Cancle Delete By Delete Icon Private Query EXECUTED")#6
  
  SearchFunctionality.DeleteSingleQueryByDeleteButton()# This test case the Delete query operation if user uses delete "BUTTON" to delete the query (Private Query)
  Log.Message(" Delete Single Query By Delete Button Private Query EXECUTED")#7
  
  SearchFunctionality.DeletebyDeleteIcon() # This test case the Delete query operation if user uses delete "ICON" to delete the query (Private Query)
  Log.Message("Delete By Delete Icon Private Query EXECUTED")#8
  
  SearchFunctionality.CreatePublicQuery()#This test case Create  "Motion Detection" Public Query
  Log.Message("Create Public Query EXECUTED")#9
  
  SearchFunctionality.SingleClickOnPublicQuery()
  Log.Message("Single click on public query Executed")
  
  SearchFunctionality.DoubleClickOnPublicQuery() # This test case is to double click on event query(Public Query)
  Log.Message("Double click on public query Executed")
  
  SearchFunctionality.DisplaySearchResultAndPlayForPublicQuery()# This test case Shows the Motion Detection Results (Public Query)
  Log.Message("Display Search Result And Play For Public Query")#10
  
  SearchFunctionality.ExportDispalyedResultVideoPublicQuery()# This test case Exports the search results of Motion Detection (Public Query)
  Log.Message("Export Dispalyed Result Video Public Query Executed")#11
  
  SearchFunctionality.UpdatePublicQuery()#This test case update the Event Name in Public Query 
  Log.Message("Update Event Name Public Query Executed")
  
  SearchFunctionality.CancelDeleteByDeteleButtonPublicQuery() # This test case Cancle the Delete query operation if user uses delete "BUTTON" to delete the query (Public Query) 
  Log.Message("Cancle Delete By Delete Button Public Query EXECUTED")#12
  
  SearchFunctionality.CancleDeleteByDeleteIconPublicQuery()# This test case Cancle the Delete query operation if user uses delete "ICON" to delete the query (Public Query)
  Log.Message("Cancle Delete By Delete Icon Public Query EXECUTED")#13
  
  SearchFunctionality.DeletePublicQueryByDeleteIcon()# This test case the Delete query operation if user uses delete "ICON" to delete the query (Public Query)
  Log.Message("Delete Single Query By Delete Icon Public Query EXECUTED")#14
  
  SearchFunctionality.DeletePublicQueryByDeleteButton() # This test case the Delete query operation if user uses delete "BUTTON" to delete the query (Private Query)
  Log.Message("Delete Single Query By Delete Button Public Query EXECUTED")#15
  
  SearchFunctionality.CreateAI_HumanQueryPublic()#This test case Create  "AI HUMAN DETECTION" Public Query
  Log.Message("Create AI_Human Query Public Exeuted")#16
  
  SearchFunctionality.DoubleClickonAICamPublicQuery()# This test case is to double click on AI CAM event query(Public Query)
  Log.Message("Double click on AI CAM Public query Executed")
  
  SearchFunctionality.SearchResultAiCam()# This test case Shows the AI HUMAN DETECTION Results (Public Query)
  Log.Message("Search Result Ai Cam  Public Query Executed")#17
  
  SearchFunctionality.UpdateAiQuery()#This test case update the Event Name in Public Query
  Log.Message("Update Ai  Public  Query Executed")#18
  
  SearchFunctionality.AiQuerySearchVideoExport()# This test case Exports the search results of AI HUMAN DETECTION(Public Query)
  Log.Message("Ai Search Video Export  Public Query Executed ")#19
  
  SearchFunctionality.AIQueryCancleDeleteByDeleteButtonPublicQueryEXECUTED() # This test case Cancle the Delete query operation if user uses delete "BUTTON" to delete the query (Public Query) 
  Log.Message("AI Query Cancle Delete By Delete Button Public Query EXECUTED")#20
  
  SearchFunctionality.AIQueryCancleDeleteByDeleteIconPublicQueryEXECUTED()# This test case Cancle the Delete query operation if user uses delete "ICON" to delete the query (Public Query)
  Log.Message("AI Query Cancle Delete By Delete Icon Public Query EXECUTED")#21
  
  SearchFunctionality.AIQueryDeleteSingleQueryByDeleteIconPublicQueryEXECUTED()# This test case the Delete query operation if user uses delete "ICON" to delete the query (Public Query)
  Log.Message("AI Query Delete Single Query By Delete Icon Public Query EXECUTED")#22
  
  SearchFunctionality.AIQueryDeleteSingleQueryByDeleteButtonPublicQueryEXECUTED()# This test case the Delete query operation if user uses delete "BUTTON" to delete the query (Public Query)
  Log.Message("AI Query Delete Single Query By Delete Button Public Query EXECUTED")#23
  
  SearchFunctionality.CreateAI_HumanQueryPrivate()#This test case Create  "AI HUMAN DETECTION" Private Query
  Log.Message("Create AI_Human Query Private Query Exeuted")#24
  
  SearchFunctionality.DoubleClickOnAICamPrivateQuery()# This test case is to double click on AI CAM event query(Private Query)
  Log.Message("Double click on AI CAM private query Executed")
  
  SearchFunctionality.SearchResultAiCamPrivateQuery()# This test case Shows the AI HUMAN DETECTION Results (Private Query)
  Log.Message("Search Result Ai Cam Private Query Exeuted")#25
  
  SearchFunctionality.UpdateAiQueryPrivateQuery()#This test case update the Event Name in Private Query
  Log.Message("UpdateAiQueryPrivate Query Exeuted")#25  
  
  SearchFunctionality.AIQueryCancleDeleteByDeleteButtonPrivateQueryEXECUTED() # This test case Cancle the Delete query operation if user uses delete "BUTTON" to delete the query (Private Query) 
  Log.Message("AI Query Cancle Delete By Delete Button Private Query EXECUTED")#26
  
  SearchFunctionality.AIQueryCancleDeleteByDeleteIconPrivateQueryEXECUTED()# This test case Cancle the Delete query operation if user uses delete "ICON" to delete the query (Private Query)
  Log.Message("AI Query Cancle Delete By Delete Icon Private Query EXECUTED")#27
  
  SearchFunctionality.AIQueryDeleteSingleQueryByDeleteIconPrivateQueryEXECUTED()# This test case the Delete query operation if user uses delete "ICON" to delete the query (Private Query)
  Log.Message("AI Query Delete Single Query By Delete Icon Private Query EXECUTED")#28
  
  SearchFunctionality.AIQueryDeleteSingleQueryByDeleteButtonPrivateQueryEXECUTED()# This test case the Delete query operation if user uses delete "BUTTON" to delete the query (Private Query)
  Log.Message("AI Query Delete Single Query By Delete Button Private Query EXECUTED")#29
  
  SearchFunctionality.VerifyIfDeleteButtonIsDisabled()
  Log.Message("Verify if delete button is disabled Executed")
  
  SearchFunctionality.VerifySearchForDropdownWorkingCorrectly()
  Log.Message("Verify Search For Dropdown Working Correctly Query is Executed")
  
  SearchFunctionality.VerifyDefaultQuertProperties()
  Log.Message("Verify Default Query Properties Executed")
  
  SearchFunctionality.VerifyPrivateQueryColumn()
  Log.Message("Verify Private Query Column Executed")
  
  
  SearchFunctionality.VerifyPublicQueryColumn()
  Log.Message("Verify Public Query Column Executed")
  
  
  SearchFunctionality.VerifyUpdateQueryWorkingCorrectly()
  Log.Message("Verify Update Query Working Correctly Executed")
  
  
  SearchFunctionality.CreateQuerywithCustomTimeFrame()
  Log.Message("Create Query with Custom Time Frame Executed")
  
  
  SearchFunctionality.VerifySelectTimeFrameButtonFunctionality()
  Log.Message("Verify Select Time Frame Button Functionality EXECTUTED")
  
  
  SearchFunctionality.VerifyStartAndEndTimeOnSearchResult ()
  Log.Message("Verify Start And End Time On Search Result EXECTUTED")
  
  SearchFunctionality.VerifyDoubleClickonCustomtimeframeQuery()
  Log.Message("Verify double click on Custom timeframe query Executed")
  
  SearchFunctionality.VerifyUpdateofCustomtimeframequery ()
  Log.Message("Verify Update of Custom timeframe query  EXECUTED")
  
  
  SearchFunctionality.CreateMultiplePrivateQueries()
  Log.Message("Create Multiple Private Queries Executed")
  
  SearchFunctionality.VerifyDeletemultiplePrivatequery()
  Log.Message("Verify Delete multiple Private query Executed")
  
  SearchFunctionality.VerifyDeleteallPrivatequery()
  Log.Message("Verify Delete all Private query Executed")
  
  
  SearchFunctionality.VerifyMaximumnumberofPrivatequeriesdisplayedperpage ()
  Log.Message("Verify Maximum number of Private queries displayed per page Executed")
  
  
  SearchFunctionality.VerifyfunctionalityofscrollbarinprivateQuerycolumn()
  Log.Message("Verify functionality of scroll bar in private Query column Executed")
  
  
  SearchFunctionality.CreateMultiplePublicQueries()
  Log.Message("Create Multiple Public Queries Executed")
  
  
  SearchFunctionality.VerifyDeleteMultiplePublicQuery ()
  Log.Message("Verify Delete Multiple Public Query Executed")
  
  
  SearchFunctionality.VerifyClickOrSelectOnOtherQueryAfterDeletionOfTheQuery ()
  Log.Message("Verify Click Or Select On Other Query After Deletion Of The Query Executed")
  
  
  SearchFunctionality.VerifyDeleteAllPublicQuery()
  Log.Message("Search Functionality Verify Delete All Public Query Executed")
  
  
  SearchFunctionality.VerifyMaximumNumberOfPublicQuerieDisplayedPerPage ()
  Log.Message("Verify Maximum Number Of Public Queries Displayed Per Page Executed")
  
  
  SearchFunctionality.VerifyScrollbarForPublicQuery()
  Log.Message("Verify Scrollbar For Public Query Executed")
  
  
  SearchFunctionality.VerifySelectMultiplePublicQueryFunctionality()
  Log.Message("Verify Select Multiple Public Query Functionality Executed")
  
  
  SearchFunctionality.VerifyWhenUserMoveToOtherTabAfterDeletionOfAllTheQuery ()
  Log.Message("Verify When User Move To Other Tab After Deletion Of All The Query Executed")
  
  
  SearchFunctionality.VerifyNewQueryCreationAfterDeletionOfAllAueryAtATime()
  Log.Message("Verify New query creation after deletion of all query at a time Executed")
  
  
  SearchFunctionality.UpdatePrivateQueryToPublic()
  
  
  SearchFunctionality.UpdatePublicQueryToPrivate()
  
  
  
  
  
##########################################################################  In Process#####################################################################

#SearchFunctionality.PlayMultipleResultVideo() 