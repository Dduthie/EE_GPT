# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UImainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QGridLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QSpinBox, QSplitter, QStackedWidget, QStatusBar,
    QTabWidget, QTextEdit, QToolBar, QToolButton,
    QWidget)
import Mainwindow_rc

class Ui_Mainwindow(object):
    def setupUi(self, Mainwindow):
        if not Mainwindow.objectName():
            Mainwindow.setObjectName(u"Mainwindow")
        Mainwindow.setEnabled(True)
        Mainwindow.resize(782, 750)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        Mainwindow.setPalette(palette)
        icon = QIcon()
        icon.addFile(u":/Icons/Resources/artificial-intelligence-48.png", QSize(), QIcon.Normal, QIcon.Off)
        Mainwindow.setWindowIcon(icon)
        Mainwindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        Mainwindow.setDocumentMode(False)
        Mainwindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.actionSettings = QAction(Mainwindow)
        self.actionSettings.setObjectName(u"actionSettings")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Resources/settings_FILL_24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSettings.setIcon(icon1)
        self.actionSettings.setMenuRole(QAction.NoRole)
        self.actionchat = QAction(Mainwindow)
        self.actionchat.setObjectName(u"actionchat")
        self.actionchat.setCheckable(True)
        icon2 = QIcon()
        icon2.addFile(u":/Icons/Resources/chat_FILL1_24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionchat.setIcon(icon2)
        self.actionchat.setMenuRole(QAction.NoRole)
        self.actionadd_chat = QAction(Mainwindow)
        self.actionadd_chat.setObjectName(u"actionadd_chat")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/Resources/chat_add_on_FILL1_24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionadd_chat.setIcon(icon3)
        self.actionadd_chat.setMenuRole(QAction.NoRole)
        self.actionOpen_chat = QAction(Mainwindow)
        self.actionOpen_chat.setObjectName(u"actionOpen_chat")
        icon4 = QIcon()
        icon4.addFile(u":/Icons/Resources/folder_open_FILL14.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen_chat.setIcon(icon4)
        self.actionOpen_chat.setMenuRole(QAction.NoRole)
        self.actionSave = QAction(Mainwindow)
        self.actionSave.setObjectName(u"actionSave")
        icon5 = QIcon()
        icon5.addFile(u":/Icons/Resources/save_FILL1_24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave.setIcon(icon5)
        self.actionSave.setMenuRole(QAction.NoRole)
        self.actionFont = QAction(Mainwindow)
        self.actionFont.setObjectName(u"actionFont")
        icon6 = QIcon()
        icon6.addFile(u":/Icons/Resources/font_download_FILL1_24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionFont.setIcon(icon6)
        self.actionFont.setMenuRole(QAction.NoRole)
        self.actionReset_View = QAction(Mainwindow)
        self.actionReset_View.setObjectName(u"actionReset_View")
        self.actionFullscreen = QAction(Mainwindow)
        self.actionFullscreen.setObjectName(u"actionFullscreen")
        self.actionLoad_ffile = QAction(Mainwindow)
        self.actionLoad_ffile.setObjectName(u"actionLoad_ffile")
        self.actionDelete = QAction(Mainwindow)
        self.actionDelete.setObjectName(u"actionDelete")
        icon7 = QIcon()
        icon7.addFile(u":/Icons/Resources/delete_FILL1_24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionDelete.setIcon(icon7)
        self.actionDelete.setMenuRole(QAction.NoRole)
        self.actionUndo = QAction(Mainwindow)
        self.actionUndo.setObjectName(u"actionUndo")
        self.actionRedo = QAction(Mainwindow)
        self.actionRedo.setObjectName(u"actionRedo")
        self.actionExport_as_txt = QAction(Mainwindow)
        self.actionExport_as_txt.setObjectName(u"actionExport_as_txt")
        icon8 = QIcon()
        icon8.addFile(u":/Icons/Resources/export_FILL_48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExport_as_txt.setIcon(icon8)
        self.actionExit = QAction(Mainwindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(Mainwindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(9)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet(u"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.reset_Button = QPushButton(self.page)
        self.reset_Button.setObjectName(u"reset_Button")

        self.gridLayout_2.addWidget(self.reset_Button, 1, 1, 1, 1)

        self.splitter = QSplitter(self.page)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setHandleWidth(3)
        self.Ouput = QTextEdit(self.splitter)
        self.Ouput.setObjectName(u"Ouput")
        self.Ouput.setFocusPolicy(Qt.ClickFocus)
        self.Ouput.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.Ouput.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.Ouput.setReadOnly(True)
        self.splitter.addWidget(self.Ouput)
        self.Input = QTextEdit(self.splitter)
        self.Input.setObjectName(u"Input")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Input.sizePolicy().hasHeightForWidth())
        self.Input.setSizePolicy(sizePolicy)
        self.Input.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.Input.setAutoFormatting(QTextEdit.AutoNone)
        self.Input.setReadOnly(False)
        self.splitter.addWidget(self.Input)

        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.submit_Button = QPushButton(self.page)
        self.submit_Button.setObjectName(u"submit_Button")

        self.gridLayout_2.addWidget(self.submit_Button, 1, 2, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_3 = QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(self.page_2)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_7 = QGridLayout(self.tab)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(20)
        self.gridLayout_4.setVerticalSpacing(30)
        self.modelCombo = QComboBox(self.tab)
        self.modelCombo.addItem("")
        self.modelCombo.addItem("")
        self.modelCombo.addItem("")
        self.modelCombo.addItem("")
        self.modelCombo.setObjectName(u"modelCombo")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.modelCombo.sizePolicy().hasHeightForWidth())
        self.modelCombo.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        self.modelCombo.setFont(font1)

        self.gridLayout_4.addWidget(self.modelCombo, 0, 1, 1, 1)

        self.modelLabel = QLabel(self.tab)
        self.modelLabel.setObjectName(u"modelLabel")
        sizePolicy.setHeightForWidth(self.modelLabel.sizePolicy().hasHeightForWidth())
        self.modelLabel.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(14)
        self.modelLabel.setFont(font2)
        self.modelLabel.setLayoutDirection(Qt.LeftToRight)
        self.modelLabel.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.modelLabel, 0, 0, 1, 1)

        self.tempLabel = QLabel(self.tab)
        self.tempLabel.setObjectName(u"tempLabel")
        sizePolicy.setHeightForWidth(self.tempLabel.sizePolicy().hasHeightForWidth())
        self.tempLabel.setSizePolicy(sizePolicy)
        self.tempLabel.setFont(font2)
        self.tempLabel.setStyleSheet(u"")
        self.tempLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.tempLabel, 1, 0, 1, 1)

        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.gridLayout_4.addWidget(self.label_6, 4, 0, 1, 1)

        self.comboBox = QComboBox(self.tab)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_4.addWidget(self.comboBox, 5, 1, 1, 1)

        self.horizontalSlider = QSlider(self.tab)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(20)
        self.horizontalSlider.setValue(11)
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.horizontalSlider, 2, 1, 1, 1)

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.gridLayout_4.addWidget(self.label_2, 5, 0, 1, 1)

        self.tempSlider = QSlider(self.tab)
        self.tempSlider.setObjectName(u"tempSlider")
        sizePolicy1.setHeightForWidth(self.tempSlider.sizePolicy().hasHeightForWidth())
        self.tempSlider.setSizePolicy(sizePolicy1)
        self.tempSlider.setStyleSheet(u"    QSlider::groove:horizontal {\n"
"        background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,\n"
"                                    stop: 0 #0000FF, stop: 0.25 #00CCFF,\n"
"                                    stop: 0.5 #00FF00, stop: 0.75 #FFCC00,\n"
"                                    stop: 1 #FF0000);\n"
"        height: 5px;\n"
"    }\n"
"\n"
"")
        self.tempSlider.setMinimum(0)
        self.tempSlider.setMaximum(20)
        self.tempSlider.setValue(5)
        self.tempSlider.setSliderPosition(5)
        self.tempSlider.setOrientation(Qt.Horizontal)
        self.tempSlider.setInvertedAppearance(False)
        self.tempSlider.setInvertedControls(False)
        self.tempSlider.setTickPosition(QSlider.TicksAbove)
        self.tempSlider.setTickInterval(1)

        self.gridLayout_4.addWidget(self.tempSlider, 1, 1, 1, 1)

        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.gridLayout_4.addWidget(self.label_4, 2, 0, 1, 1)

        self.spinBox = QSpinBox(self.tab)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(4096)
        self.spinBox.setValue(4096)

        self.gridLayout_4.addWidget(self.spinBox, 4, 1, 1, 1)

        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.gridLayout_4.addWidget(self.label_7, 3, 0, 1, 1)

        self.horizontalSlider_2 = QSlider(self.tab)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setMinimum(1)
        self.horizontalSlider_2.setMaximum(20)
        self.horizontalSlider_2.setValue(11)
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.horizontalSlider_2, 3, 1, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_3, 1, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_4, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_6 = QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.restoreButton = QPushButton(self.tab_2)
        self.restoreButton.setObjectName(u"restoreButton")
        self.restoreButton.setStyleSheet(u"color: rgb(170, 0, 0);")

        self.gridLayout_6.addWidget(self.restoreButton, 2, 0, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(20)
        self.gridLayout_5.setVerticalSpacing(30)
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.gridLayout_5.addWidget(self.label_5, 2, 0, 1, 1)

        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)

        self.gridLayout_5.addWidget(self.label, 1, 0, 1, 1)

        self.themeCombo = QComboBox(self.tab_2)
        self.themeCombo.addItem("")
        self.themeCombo.addItem("")
        self.themeCombo.addItem("")
        self.themeCombo.setObjectName(u"themeCombo")
        sizePolicy1.setHeightForWidth(self.themeCombo.sizePolicy().hasHeightForWidth())
        self.themeCombo.setSizePolicy(sizePolicy1)
        self.themeCombo.setMinimumSize(QSize(100, 0))

        self.gridLayout_5.addWidget(self.themeCombo, 2, 1, 1, 1)

        self.fontbutton = QToolButton(self.tab_2)
        self.fontbutton.setObjectName(u"fontbutton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.fontbutton.sizePolicy().hasHeightForWidth())
        self.fontbutton.setSizePolicy(sizePolicy2)
        self.fontbutton.setMaximumSize(QSize(32, 32))
        self.fontbutton.setIcon(icon6)
        self.fontbutton.setIconSize(QSize(48, 48))

        self.gridLayout_5.addWidget(self.fontbutton, 0, 1, 1, 1)

        self.paletteButton = QToolButton(self.tab_2)
        self.paletteButton.setObjectName(u"paletteButton")
        self.paletteButton.setMaximumSize(QSize(32, 32))
        icon9 = QIcon()
        icon9.addFile(u":/Icons/Resources/palette_FILL1_48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.paletteButton.setIcon(icon9)
        self.paletteButton.setIconSize(QSize(48, 48))

        self.gridLayout_5.addWidget(self.paletteButton, 1, 1, 1, 1)

        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_3, 2, 1, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        Mainwindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Mainwindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 782, 22))
        self.menuChat = QMenu(self.menubar)
        self.menuChat.setObjectName(u"menuChat")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        Mainwindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Mainwindow)
        self.statusbar.setObjectName(u"statusbar")
        Mainwindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(Mainwindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setAllowedAreas(Qt.AllToolBarAreas)
        self.toolBar.setOrientation(Qt.Horizontal)
        self.toolBar.setIconSize(QSize(24, 24))
        Mainwindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QToolBar(Mainwindow)
        self.toolBar_2.setObjectName(u"toolBar_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.toolBar_2.sizePolicy().hasHeightForWidth())
        self.toolBar_2.setSizePolicy(sizePolicy3)
        self.toolBar_2.setMinimumSize(QSize(0, 0))
        Mainwindow.addToolBar(Qt.LeftToolBarArea, self.toolBar_2)

        self.menubar.addAction(self.menuChat.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menuChat.addAction(self.actionSave)
        self.menuChat.addAction(self.actionOpen_chat)
        self.menuChat.addAction(self.actionExport_as_txt)
        self.menuChat.addSeparator()
        self.menuChat.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuView.addAction(self.actionFullscreen)
        self.menuView.addAction(self.actionReset_View)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionOpen_chat)
        self.toolBar_2.addAction(self.actionchat)
        self.toolBar_2.addAction(self.actionadd_chat)
        self.toolBar_2.addAction(self.actionDelete)
        self.toolBar_2.addSeparator()
        self.toolBar_2.addAction(self.actionSettings)
        self.toolBar_2.addAction(self.actionFont)

        self.retranslateUi(Mainwindow)
        self.actionExit.triggered.connect(Mainwindow.close)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Mainwindow)
    # setupUi

    def retranslateUi(self, Mainwindow):
        Mainwindow.setWindowTitle(QCoreApplication.translate("Mainwindow", u"GPT", None))
        self.actionSettings.setText(QCoreApplication.translate("Mainwindow", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.actionSettings.setToolTip(QCoreApplication.translate("Mainwindow", u"change app settings", None))
#endif // QT_CONFIG(tooltip)
        self.actionchat.setText(QCoreApplication.translate("Mainwindow", u"chat", None))
#if QT_CONFIG(tooltip)
        self.actionchat.setToolTip(QCoreApplication.translate("Mainwindow", u"current chat", None))
#endif // QT_CONFIG(tooltip)
        self.actionadd_chat.setText(QCoreApplication.translate("Mainwindow", u"add chat", None))
#if QT_CONFIG(tooltip)
        self.actionadd_chat.setToolTip(QCoreApplication.translate("Mainwindow", u"add a new chat", None))
#endif // QT_CONFIG(tooltip)
        self.actionOpen_chat.setText(QCoreApplication.translate("Mainwindow", u"Load conversation", None))
#if QT_CONFIG(tooltip)
        self.actionOpen_chat.setToolTip(QCoreApplication.translate("Mainwindow", u"Open a previous chat", None))
#endif // QT_CONFIG(tooltip)
        self.actionSave.setText(QCoreApplication.translate("Mainwindow", u"Save conversation", None))
#if QT_CONFIG(tooltip)
        self.actionSave.setToolTip(QCoreApplication.translate("Mainwindow", u"save current chat", None))
#endif // QT_CONFIG(tooltip)
        self.actionFont.setText(QCoreApplication.translate("Mainwindow", u"Font", None))
#if QT_CONFIG(tooltip)
        self.actionFont.setToolTip(QCoreApplication.translate("Mainwindow", u"Change font", None))
#endif // QT_CONFIG(tooltip)
        self.actionReset_View.setText(QCoreApplication.translate("Mainwindow", u"Reset View", None))
        self.actionFullscreen.setText(QCoreApplication.translate("Mainwindow", u"Fullscreen", None))
        self.actionLoad_ffile.setText(QCoreApplication.translate("Mainwindow", u"Load conversation", None))
        self.actionDelete.setText(QCoreApplication.translate("Mainwindow", u"Delete", None))
        self.actionUndo.setText(QCoreApplication.translate("Mainwindow", u"Undo", None))
#if QT_CONFIG(shortcut)
        self.actionUndo.setShortcut(QCoreApplication.translate("Mainwindow", u"Ctrl+Z", None))
#endif // QT_CONFIG(shortcut)
        self.actionRedo.setText(QCoreApplication.translate("Mainwindow", u"Redo", None))
#if QT_CONFIG(shortcut)
        self.actionRedo.setShortcut(QCoreApplication.translate("Mainwindow", u"Ctrl+Y", None))
#endif // QT_CONFIG(shortcut)
        self.actionExport_as_txt.setText(QCoreApplication.translate("Mainwindow", u"Export as .txt", None))
        self.actionExit.setText(QCoreApplication.translate("Mainwindow", u"Exit", None))
        self.reset_Button.setText(QCoreApplication.translate("Mainwindow", u"Reset", None))
        self.Input.setPlaceholderText(QCoreApplication.translate("Mainwindow", u"Enter text here", None))
        self.submit_Button.setText(QCoreApplication.translate("Mainwindow", u"Submit", None))
        self.modelCombo.setItemText(0, QCoreApplication.translate("Mainwindow", u"ChatGPT 3.5", None))
        self.modelCombo.setItemText(1, QCoreApplication.translate("Mainwindow", u"ChatGPT 3.5 16k", None))
        self.modelCombo.setItemText(2, QCoreApplication.translate("Mainwindow", u"ChatGPT 4", None))
        self.modelCombo.setItemText(3, QCoreApplication.translate("Mainwindow", u"ChatGPT 4 32k", None))

        self.modelLabel.setText(QCoreApplication.translate("Mainwindow", u"Model:", None))
        self.tempLabel.setText(QCoreApplication.translate("Mainwindow", u"Temperature:", None))
        self.label_6.setText(QCoreApplication.translate("Mainwindow", u"Max Tokens:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Mainwindow", u"Delete messages", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Mainwindow", u"Summarize conversation", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Mainwindow", u"Choose messages", None))

        self.label_2.setText(QCoreApplication.translate("Mainwindow", u"Token Limit Behaviour:", None))
        self.label_4.setText(QCoreApplication.translate("Mainwindow", u"Presence Penatly:", None))
        self.label_7.setText(QCoreApplication.translate("Mainwindow", u"Frequency Penalty:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Mainwindow", u"GPT Options", None))
        self.restoreButton.setText(QCoreApplication.translate("Mainwindow", u"Reset all app defaults", None))
        self.label_5.setText(QCoreApplication.translate("Mainwindow", u"Theme:", None))
        self.label.setText(QCoreApplication.translate("Mainwindow", u"Accent Colour:", None))
        self.themeCombo.setItemText(0, QCoreApplication.translate("Mainwindow", u"Auto", None))
        self.themeCombo.setItemText(1, QCoreApplication.translate("Mainwindow", u"Dark", None))
        self.themeCombo.setItemText(2, QCoreApplication.translate("Mainwindow", u"Light", None))

        self.fontbutton.setText(QCoreApplication.translate("Mainwindow", u"...", None))
        self.paletteButton.setText(QCoreApplication.translate("Mainwindow", u"...", None))
        self.label_3.setText(QCoreApplication.translate("Mainwindow", u"Change Font:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Mainwindow", u"App settings", None))
        self.menuChat.setTitle(QCoreApplication.translate("Mainwindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("Mainwindow", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("Mainwindow", u"View", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("Mainwindow", u"toolBar", None))
        self.toolBar_2.setWindowTitle(QCoreApplication.translate("Mainwindow", u"toolBar_2", None))
    # retranslateUi

