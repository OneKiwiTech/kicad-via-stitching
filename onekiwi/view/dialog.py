# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class ViaStitchingDialog
###########################################################################

class ViaStitchingDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Via Stitching", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"label" ), wx.VERTICAL )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		self.textLayer = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Layer:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textLayer.Wrap( -1 )

		bSizer11.Add( self.textLayer, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choiceLayerChoices = []
		self.choiceLayer = wx.Choice( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceLayerChoices, 0 )
		self.choiceLayer.SetSelection( 0 )
		bSizer11.Add( self.choiceLayer, 0, wx.ALL, 5 )


		sbSizer2.Add( bSizer11, 0, wx.EXPAND, 5 )

		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

		self.textArea = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Area:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textArea.Wrap( -1 )

		bSizer13.Add( self.textArea, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choiceAreaChoices = []
		self.choiceArea = wx.Choice( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceAreaChoices, 0 )
		self.choiceArea.SetSelection( 0 )
		bSizer13.Add( self.choiceArea, 0, wx.ALL, 5 )


		sbSizer2.Add( bSizer13, 0, wx.EXPAND, 5 )

		self.textNet = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Net:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textNet.Wrap( -1 )

		sbSizer2.Add( self.textNet, 0, wx.ALL, 5 )


		bSizer10.Add( sbSizer2, 1, wx.ALL|wx.EXPAND, 5 )

		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"label" ), wx.VERTICAL )

		self.textUnit = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Unit:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textUnit.Wrap( -1 )

		sbSizer3.Add( self.textUnit, 0, wx.ALL, 5 )

		bSizer111 = wx.BoxSizer( wx.HORIZONTAL )

		self.textVia = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Via:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textVia.Wrap( -1 )

		bSizer111.Add( self.textVia, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choiceViaChoices = []
		self.choiceVia = wx.Choice( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceViaChoices, 0 )
		self.choiceVia.SetSelection( 0 )
		bSizer111.Add( self.choiceVia, 0, wx.ALL, 5 )


		sbSizer3.Add( bSizer111, 0, wx.EXPAND, 5 )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		self.textSpace = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Via spacing:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textSpace.Wrap( -1 )

		bSizer14.Add( self.textSpace, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.editSpace = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.editSpace, 0, wx.ALL, 5 )


		sbSizer3.Add( bSizer14, 0, wx.EXPAND, 5 )

		bSizer141 = wx.BoxSizer( wx.HORIZONTAL )

		self.textClearance = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Clearance:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textClearance.Wrap( -1 )

		bSizer141.Add( self.textClearance, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.editClearance = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer141.Add( self.editClearance, 0, wx.ALL, 5 )


		sbSizer3.Add( bSizer141, 0, wx.EXPAND, 5 )


		bSizer10.Add( sbSizer3, 1, wx.ALL|wx.EXPAND, 5 )

		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Via Patterns" ), wx.VERTICAL )

		self.radioFillAligned = wx.RadioButton( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Fill Aligned", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.radioFillAligned, 0, wx.ALL, 5 )

		self.radioFillStaggered = wx.RadioButton( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Fill Staggered", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.radioFillStaggered, 0, wx.ALL, 5 )

		self.radioPerimeter = wx.RadioButton( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Perimeter", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.radioPerimeter, 0, wx.ALL, 5 )

		self.radioShield = wx.RadioButton( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Shield", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.radioShield, 0, wx.ALL, 5 )


		bSizer10.Add( sbSizer4, 1, wx.ALL|wx.EXPAND, 5 )

		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Preview" ), wx.VERTICAL )

		self.m_bitmap1 = wx.StaticBitmap( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer5.Add( self.m_bitmap1, 0, wx.ALL, 5 )


		bSizer10.Add( sbSizer5, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer9.Add( bSizer10, 1, wx.EXPAND, 5 )

		bSizer23 = wx.BoxSizer( wx.HORIZONTAL )

		self.buttonApply = wx.Button( self, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.buttonApply, 0, wx.ALL, 5 )

		self.buttonUndo = wx.Button( self, wx.ID_ANY, u"Undo", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.buttonUndo, 0, wx.ALL, 5 )

		self.buttonClear = wx.Button( self, wx.ID_ANY, u"Clear log", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.buttonClear, 0, wx.ALL, 5 )

		self.buttonClose = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.buttonClose, 0, wx.ALL, 5 )


		bSizer9.Add( bSizer23, 0, wx.EXPAND, 5 )


		bSizer1.Add( bSizer9, 1, wx.EXPAND, 5 )

		self.staticline = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.staticline, 0, wx.EXPAND |wx.ALL, 5 )

		self.textLog = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,100 ), wx.HSCROLL|wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer1.Add( self.textLog, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		bSizer1.Fit( self )

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


