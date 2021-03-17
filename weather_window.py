from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Main window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(892, 640)
        MainWindow.setMinimumSize(QtCore.QSize(892, 640))
        MainWindow.setMaximumSize(QtCore.QSize(892, 640))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Tabs hub 
        self.tabHub = QtWidgets.QTabWidget(self.centralwidget)
        self.tabHub.setEnabled(True)
        self.tabHub.setGeometry(QtCore.QRect(10, 80, 871, 481))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.tabHub.setFont(font)
        self.tabHub.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabHub.setObjectName("tabHub")


        # - - - - - - - -  TAB LOCATION - - - - - - - - #
        self.tab_location = QtWidgets.QWidget()
        self.tab_location.setObjectName("tab_location")

        # LineEdit location
        self.loc_lineEdit = QtWidgets.QLineEdit(self.tab_location)
        self.loc_lineEdit.setGeometry(QtCore.QRect(120, 60, 301, 51))
        self.loc_lineEdit.setText("Lyon")
        self.loc_lineEdit.setObjectName("loc_lineEdit")

        # Button search
        self.loc_button_search = QtWidgets.QPushButton(self.tab_location)
        self.loc_button_search.setGeometry(QtCore.QRect(540, 60, 191, 51))
        self.loc_button_search.setObjectName("loc_button_search")

        # Label searching...
        self.loc_label_searching = QtWidgets.QLabel(self.tab_location)
        self.loc_label_searching.setGeometry(QtCore.QRect(760, 74, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.loc_label_searching.setFont(font)
        self.loc_label_searching.setObjectName("loc_label_searching")

        # Label Enter location
        self.loc_label_enter_location = QtWidgets.QLabel(self.tab_location)
        self.loc_label_enter_location.setGeometry(QtCore.QRect(120, 30, 301, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.loc_label_enter_location.setFont(font)
        self.loc_label_enter_location.setAlignment(QtCore.Qt.AlignCenter)
        self.loc_label_enter_location.setObjectName("loc_label_enter_location")

        # Frame choose location
        self.loc_frame_choose = QtWidgets.QFrame(self.tab_location)
        self.loc_frame_choose.setGeometry(QtCore.QRect(110, 210, 631, 181))
        self.loc_frame_choose.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.loc_frame_choose.setFrameShadow(QtWidgets.QFrame.Raised)
        self.loc_frame_choose.setObjectName("loc_frame_choose")

        # Combobox location
        self.loc_combo = QtWidgets.QComboBox(self.loc_frame_choose)
        self.loc_combo.setGeometry(QtCore.QRect(10, 60, 301, 51))
        self.loc_combo.setObjectName("loc_combo")
        font = QtGui.QFont()
        font.setPointSize(13)
        self.loc_combo.setFont(font)

        # Button OK
        self.loc_button_OK = QtWidgets.QPushButton(self.loc_frame_choose)
        self.loc_button_OK.setGeometry(QtCore.QRect(430, 60, 191, 51))
        self.loc_button_OK.setObjectName("loc_button_OK")

        # Label choose location
        self.loc_label_choose_location = QtWidgets.QLabel(self.loc_frame_choose)
        self.loc_label_choose_location.setGeometry(QtCore.QRect(10, 30, 301, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.loc_label_choose_location.setFont(font)
        self.loc_label_choose_location.setAlignment(QtCore.Qt.AlignCenter)
        self.loc_label_choose_location.setObjectName("loc_label_choose_location")

        # Label getting...
        self.loc_label_getting = QtWidgets.QLabel(self.loc_frame_choose)
        self.loc_label_getting.setGeometry(QtCore.QRect(280, 150, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.loc_label_getting.setFont(font)
        self.loc_label_getting.setAlignment(QtCore.Qt.AlignCenter)
        self.loc_label_getting.setObjectName("loc_label_getting")

        # Horizontal line
        self.loc_line = QtWidgets.QFrame(self.tab_location)
        self.loc_line.setGeometry(QtCore.QRect(-10, 150, 891, 20))
        self.loc_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.loc_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.loc_line.setObjectName("loc_line")


        # - - - - - - - -  TAB CURRENT WEATHER - - - - - - - - #
        self.tabHub.addTab(self.tab_location, "")
        self.tab_current = QtWidgets.QWidget()
        self.tab_current.setEnabled(True)
        self.tab_current.setObjectName("tab_current")

        # - - - - Frame temperature
        self.curr_frame_temp = QtWidgets.QFrame(self.tab_current)
        self.curr_frame_temp.setGeometry(QtCore.QRect(10, 50, 381, 181))
        self.curr_frame_temp.setFrameShape(QtWidgets.QFrame.Box)
        self.curr_frame_temp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.curr_frame_temp.setObjectName("curr_frame_temp")

        # Label temperature
        self.curr_label_temp = QtWidgets.QLabel(self.curr_frame_temp)
        self.curr_label_temp.setGeometry(QtCore.QRect(0, 30, 211, 81))
        font = QtGui.QFont()
        font.setPointSize(61)
        self.curr_label_temp.setFont(font)
        self.curr_label_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.curr_label_temp.setObjectName("curr_label_temp")

        # Label temperature title frame
        self.curr_label_temp_title = QtWidgets.QLabel(self.curr_frame_temp)
        self.curr_label_temp_title.setGeometry(QtCore.QRect(10, 10, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.curr_label_temp_title.setFont(font)
        self.curr_label_temp_title.setObjectName("curr_label_temp_title")

        # Label temperature more info
        self.curr_label_temp_more = QtWidgets.QLabel(self.curr_frame_temp)
        self.curr_label_temp_more.setGeometry(QtCore.QRect(240, 120, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.curr_label_temp_more.setFont(font)
        self.curr_label_temp_more.setScaledContents(False)
        self.curr_label_temp_more.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.curr_label_temp_more.setWordWrap(False)
        self.curr_label_temp_more.setObjectName("curr_label_temp_more")

        # Label temperature description
        self.curr_label_temp_description = QtWidgets.QLabel(self.curr_frame_temp)
        self.curr_label_temp_description.setGeometry(QtCore.QRect(30, 120, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.curr_label_temp_description.setFont(font)
        self.curr_label_temp_description.setAlignment(QtCore.Qt.AlignCenter)
        self.curr_label_temp_description.setObjectName("curr_label_temp_description")

        # Icon current weather
        self.curr_icon_temp = QtWidgets.QLabel(self.curr_frame_temp)
        self.curr_icon_temp.setGeometry(QtCore.QRect(250, 10, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.curr_icon_temp.setFont(font)
        self.curr_icon_temp.setText("")
        self.curr_icon_temp.setPixmap(QtGui.QPixmap("10d@4x.png"))
        self.curr_icon_temp.setScaledContents(True)
        self.curr_icon_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.curr_icon_temp.setObjectName("curr_icon_temp")

        # - - - - Frame wind
        self.curr_frame_wind = QtWidgets.QFrame(self.tab_current)
        self.curr_frame_wind.setGeometry(QtCore.QRect(470, 50, 381, 181))
        self.curr_frame_wind.setFrameShape(QtWidgets.QFrame.Box)
        self.curr_frame_wind.setFrameShadow(QtWidgets.QFrame.Raised)
        self.curr_frame_wind.setObjectName("curr_frame_wind")

        # Label wind speed
        self.curr_label_wind_speed = QtWidgets.QLabel(self.curr_frame_wind)
        self.curr_label_wind_speed.setGeometry(QtCore.QRect(20, 50, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.curr_label_wind_speed.setFont(font)
        self.curr_label_wind_speed.setAlignment(QtCore.Qt.AlignCenter)
        self.curr_label_wind_speed.setObjectName("curr_label_wind_speed")

        # Label wind title
        self.curr_label_wind_title = QtWidgets.QLabel(self.curr_frame_wind)
        self.curr_label_wind_title.setGeometry(QtCore.QRect(10, 10, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.curr_label_wind_title.setFont(font)
        self.curr_label_wind_title.setObjectName("curr_label_wind_title")

        # Label wind direction
        self.curr_label_wind_dir = QtWidgets.QLabel(self.curr_frame_wind)
        self.curr_label_wind_dir.setGeometry(QtCore.QRect(260, 50, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.curr_label_wind_dir.setFont(font)
        self.curr_label_wind_dir.setAlignment(QtCore.Qt.AlignCenter)
        self.curr_label_wind_dir.setObjectName("curr_label_wind_dir")

        # Label wind more info
        self.curr_label_wind_more = QtWidgets.QLabel(self.curr_frame_wind)
        self.curr_label_wind_more.setGeometry(QtCore.QRect(20, 114, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.curr_label_wind_more.setFont(font)
        self.curr_label_wind_more.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.curr_label_wind_more.setObjectName("curr_label_wind_more")

        # Label wind cardinal point
        self.curr_label_wind_cardinal = QtWidgets.QLabel(self.curr_frame_wind)
        self.curr_label_wind_cardinal.setGeometry(QtCore.QRect(248, 120, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.curr_label_wind_cardinal.setFont(font)
        self.curr_label_wind_cardinal.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.curr_label_wind_cardinal.setObjectName("curr_label_wind_cardinal")
        
        # - - - - Frame more info
        self.curr_frame_more_info = QtWidgets.QFrame(self.tab_current)
        self.curr_frame_more_info.setGeometry(QtCore.QRect(10, 240, 381, 181))
        self.curr_frame_more_info.setFrameShape(QtWidgets.QFrame.Box)
        self.curr_frame_more_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.curr_frame_more_info.setObjectName("curr_frame_more_info")
        
        # Label more info title
        self.curr_label_more_title = QtWidgets.QLabel(self.curr_frame_more_info)
        self.curr_label_more_title.setGeometry(QtCore.QRect(10, 10, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.curr_label_more_title.setFont(font)
        self.curr_label_more_title.setObjectName("curr_label_more_title")
        
        # Label more : pressure ...
        self.curr_label_more_info_press = QtWidgets.QLabel(self.curr_frame_more_info)
        self.curr_label_more_info_press.setGeometry(QtCore.QRect(30, 50, 141, 101))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.curr_label_more_info_press.setFont(font)
        self.curr_label_more_info_press.setScaledContents(False)
        self.curr_label_more_info_press.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.curr_label_more_info_press.setWordWrap(False)
        self.curr_label_more_info_press.setObjectName("curr_label_more_info_press")
        
        # Vertical line
        self.curr_line_more_info = QtWidgets.QFrame(self.curr_frame_more_info)
        self.curr_line_more_info.setGeometry(QtCore.QRect(180, 54, 20, 81))
        self.curr_line_more_info.setFrameShape(QtWidgets.QFrame.VLine)
        self.curr_line_more_info.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.curr_line_more_info.setObjectName("curr_line_more_info")
        
        # Label sunrise/sunset
        self.curr_label_sun = QtWidgets.QLabel(self.curr_frame_more_info)
        self.curr_label_sun.setGeometry(QtCore.QRect(230, 60, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.curr_label_sun.setFont(font)
        self.curr_label_sun.setScaledContents(False)
        self.curr_label_sun.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.curr_label_sun.setWordWrap(False)
        self.curr_label_sun.setObjectName("curr_label_sun")

        # - - - - Frame next hours
        self.curr_frame_next_hours = QtWidgets.QFrame(self.tab_current)
        self.curr_frame_next_hours.setGeometry(QtCore.QRect(470, 240, 381, 181))
        self.curr_frame_next_hours.setFrameShape(QtWidgets.QFrame.Box)
        self.curr_frame_next_hours.setFrameShadow(QtWidgets.QFrame.Raised)
        self.curr_frame_next_hours.setObjectName("curr_frame_next_hours")
        
        # Label next hours title
        self.label_next_hours_title = QtWidgets.QLabel(self.curr_frame_next_hours)
        self.label_next_hours_title.setGeometry(QtCore.QRect(10, 10, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_next_hours_title.setFont(font)
        self.label_next_hours_title.setObjectName("label_next_hours_title")
        
        # Icon H1
        self.curr_icon_h1 = QtWidgets.QLabel(self.curr_frame_next_hours)
        self.curr_icon_h1.setGeometry(QtCore.QRect(12, 70, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.curr_icon_h1.setFont(font)
        self.curr_icon_h1.setFrameShape(QtWidgets.QFrame.Box)
        self.curr_icon_h1.setText("")
        self.curr_icon_h1.setPixmap(QtGui.QPixmap("10d@4x.png"))
        self.curr_icon_h1.setScaledContents(True)
        self.curr_icon_h1.setAlignment(QtCore.Qt.AlignCenter)
        self.curr_icon_h1.setObjectName("curr_icon_h1")

        # Icon H2
        self.curr_icon_h2 = QtWidgets.QLabel(self.curr_frame_next_hours)
        self.curr_icon_h2.setGeometry(QtCore.QRect(75, 70, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.curr_icon_h2.setFont(font)
        self.curr_icon_h2.setFrameShape(QtWidgets.QFrame.Box)
        self.curr_icon_h2.setText("")
        self.curr_icon_h2.setPixmap(QtGui.QPixmap("10d@4x.png"))
        self.curr_icon_h2.setScaledContents(True)
        self.curr_icon_h2.setAlignment(QtCore.Qt.AlignCenter)
        self.curr_icon_h2.setObjectName("curr_icon_h2")

        # Icon H3
        self.curr_icon_h3 = QtWidgets.QLabel(self.curr_frame_next_hours)
        self.curr_icon_h3.setGeometry(QtCore.QRect(136, 70, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.curr_icon_h3.setFont(font)
        self.curr_icon_h3.setFrameShape(QtWidgets.QFrame.Box)
        self.curr_icon_h3.setText("")
        self.curr_icon_h3.setPixmap(QtGui.QPixmap("10d@4x.png"))
        self.curr_icon_h3.setScaledContents(True)
        self.curr_icon_h3.setAlignment(QtCore.Qt.AlignCenter)
        self.curr_icon_h3.setObjectName("curr_icon_h3")

        # Icon H4
        self.curr_icon_h4 = QtWidgets.QLabel(self.curr_frame_next_hours)
        self.curr_icon_h4.setGeometry(QtCore.QRect(197, 70, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.curr_icon_h4.setFont(font)
        self.curr_icon_h4.setFrameShape(QtWidgets.QFrame.Box)
        self.curr_icon_h4.setText("")
        self.curr_icon_h4.setPixmap(QtGui.QPixmap("10d@4x.png"))
        self.curr_icon_h4.setScaledContents(True)
        self.curr_icon_h4.setAlignment(QtCore.Qt.AlignCenter)
        self.curr_icon_h4.setObjectName("curr_icon_h4")

        # Icon H5
        self.curr_icon_h5 = QtWidgets.QLabel(self.curr_frame_next_hours)
        self.curr_icon_h5.setGeometry(QtCore.QRect(257, 70, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.curr_icon_h5.setFont(font)
        self.curr_icon_h5.setFrameShape(QtWidgets.QFrame.Box)
        self.curr_icon_h5.setText("")
        self.curr_icon_h5.setPixmap(QtGui.QPixmap("10d@4x.png"))
        self.curr_icon_h5.setScaledContents(True)
        self.curr_icon_h5.setAlignment(QtCore.Qt.AlignCenter)
        self.curr_icon_h5.setObjectName("curr_icon_h5")

        # Icon H6
        self.curr_icon_h6 = QtWidgets.QLabel(self.curr_frame_next_hours)
        self.curr_icon_h6.setGeometry(QtCore.QRect(317, 70, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.curr_icon_h6.setFont(font)
        self.curr_icon_h6.setFrameShape(QtWidgets.QFrame.Box)
        self.curr_icon_h6.setText("")
        self.curr_icon_h6.setPixmap(QtGui.QPixmap("10d@4x.png"))
        self.curr_icon_h6.setScaledContents(True)
        self.curr_icon_h6.setAlignment(QtCore.Qt.AlignCenter)
        self.curr_icon_h6.setObjectName("curr_icon_h6")

        # Label H1
        self.curr_label_h1 = QtWidgets.QLabel(self.curr_frame_next_hours)
        self.curr_label_h1.setGeometry(QtCore.QRect(14, 50, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.curr_label_h1.setFont(font)
        self.curr_label_h1.setAlignment(QtCore.Qt.AlignCenter)
        self.curr_label_h1.setObjectName("curr_label_h1")
        
        # Label H2
        self.curr_label_h2 = QtWidgets.QLabel(self.curr_frame_next_hours)
        self.curr_label_h2.setGeometry(QtCore.QRect(76, 50, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.curr_label_h2.setFont(font)
        self.curr_label_h2.setAlignment(QtCore.Qt.AlignCenter)
        self.curr_label_h2.setObjectName("curr_label_h2")

        # Label H3
        self.curr_label_h3 = QtWidgets.QLabel(self.curr_frame_next_hours)
        self.curr_label_h3.setGeometry(QtCore.QRect(138, 50, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.curr_label_h3.setFont(font)
        self.curr_label_h3.setAlignment(QtCore.Qt.AlignCenter)
        self.curr_label_h3.setObjectName("curr_label_h3")

        # Label H4
        self.curr_label_h4 = QtWidgets.QLabel(self.curr_frame_next_hours)
        self.curr_label_h4.setGeometry(QtCore.QRect(200, 50, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.curr_label_h4.setFont(font)
        self.curr_label_h4.setAlignment(QtCore.Qt.AlignCenter)
        self.curr_label_h4.setObjectName("curr_label_h4")

        # Label H5
        self.curr_label_h5 = QtWidgets.QLabel(self.curr_frame_next_hours)
        self.curr_label_h5.setGeometry(QtCore.QRect(260, 50, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.curr_label_h5.setFont(font)
        self.curr_label_h5.setAlignment(QtCore.Qt.AlignCenter)
        self.curr_label_h5.setObjectName("curr_label_h5")

        # Label H6
        self.curr_label_h6 = QtWidgets.QLabel(self.curr_frame_next_hours)
        self.curr_label_h6.setGeometry(QtCore.QRect(320, 50, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.curr_label_h6.setFont(font)
        self.curr_label_h6.setAlignment(QtCore.Qt.AlignCenter)
        self.curr_label_h6.setObjectName("curr_label_h6")

        # Label H1 weather
        self.curr_label_h1_info = QtWidgets.QLabel(self.curr_frame_next_hours)
        self.curr_label_h1_info.setGeometry(QtCore.QRect(15, 125, 47, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.curr_label_h1_info.setFont(font)
        self.curr_label_h1_info.setAlignment(QtCore.Qt.AlignCenter)
        self.curr_label_h1_info.setObjectName("curr_label_h1_info")
        
        # Label H2 weather
        self.curr_label_h2_info = QtWidgets.QLabel(self.curr_frame_next_hours)
        self.curr_label_h2_info.setGeometry(QtCore.QRect(77, 125, 47, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.curr_label_h2_info.setFont(font)
        self.curr_label_h2_info.setAlignment(QtCore.Qt.AlignCenter)
        self.curr_label_h2_info.setObjectName("curr_label_h2_info")
        
        # Label H3 weather
        self.curr_label_h3_info = QtWidgets.QLabel(self.curr_frame_next_hours)
        self.curr_label_h3_info.setGeometry(QtCore.QRect(140, 125, 47, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.curr_label_h3_info.setFont(font)
        self.curr_label_h3_info.setAlignment(QtCore.Qt.AlignCenter)
        self.curr_label_h3_info.setObjectName("curr_label_h3_info")
        
        # Label H4 weather
        self.curr_label_h4_info = QtWidgets.QLabel(self.curr_frame_next_hours)
        self.curr_label_h4_info.setGeometry(QtCore.QRect(200, 125, 47, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.curr_label_h4_info.setFont(font)
        self.curr_label_h4_info.setAlignment(QtCore.Qt.AlignCenter)
        self.curr_label_h4_info.setObjectName("curr_label_h4_info")
        
        # Label H5 weather
        self.curr_label_h5_info = QtWidgets.QLabel(self.curr_frame_next_hours)
        self.curr_label_h5_info.setGeometry(QtCore.QRect(262, 125, 47, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.curr_label_h5_info.setFont(font)
        self.curr_label_h5_info.setAlignment(QtCore.Qt.AlignCenter)
        self.curr_label_h5_info.setObjectName("curr_label_h5_info")
        
        # Label H6 weather
        self.curr_label_h6_info = QtWidgets.QLabel(self.curr_frame_next_hours)
        self.curr_label_h6_info.setGeometry(QtCore.QRect(322, 125, 47, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.curr_label_h6_info.setFont(font)
        self.curr_label_h6_info.setAlignment(QtCore.Qt.AlignCenter)
        self.curr_label_h6_info.setObjectName("curr_label_h6_info")
        
        # Label recap (on main tab)
        self.curr_label_recap = QtWidgets.QLabel(self.tab_current)
        self.curr_label_recap.setGeometry(QtCore.QRect(10, 10, 680, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.curr_label_recap.setFont(font)
        self.curr_label_recap.setObjectName("curr_label_recap")


        # - - - - - - - -  TAB FORECAST - - - - - - - - #
        self.tabHub.addTab(self.tab_current, "")
        self.tab_forecast = QtWidgets.QWidget()
        self.tab_forecast.setObjectName("tab_forecast")

        # - - - - FRAME TODAY - - - -
        self.for_frame_today = QtWidgets.QFrame(self.tab_forecast)
        self.for_frame_today.setGeometry(QtCore.QRect(20, 10, 401, 91))
        self.for_frame_today.setFrameShape(QtWidgets.QFrame.Box)
        self.for_frame_today.setFrameShadow(QtWidgets.QFrame.Raised)
        self.for_frame_today.setObjectName("for_frame_today")

        # Label today title
        self.for_label_today = QtWidgets.QLabel(self.for_frame_today)
        self.for_label_today.setGeometry(QtCore.QRect(10, 10, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.for_label_today.setFont(font)
        self.for_label_today.setObjectName("for_label_today")

        # Label min
        self.for_label_today_min = QtWidgets.QLabel(self.for_frame_today)
        self.for_label_today_min.setGeometry(QtCore.QRect(20, 61, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.for_label_today_min.setFont(font)
        self.for_label_today_min.setObjectName("for_label_today_min")
        
        # Label minimum temperature today
        self.for_label_today_minTemp = QtWidgets.QLabel(self.for_frame_today)
        self.for_label_today_minTemp.setGeometry(QtCore.QRect(60, 49, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.for_label_today_minTemp.setFont(font)
        self.for_label_today_minTemp.setObjectName("for_label_today_minTemp")
        
        # Label max
        self.for_label_today_max = QtWidgets.QLabel(self.for_frame_today)
        self.for_label_today_max.setGeometry(QtCore.QRect(120, 61, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.for_label_today_max.setFont(font)
        self.for_label_today_max.setObjectName("for_label_today_max")
        
        # Label maximum temperature today
        self.for_label_today_maxTemp = QtWidgets.QLabel(self.for_frame_today)
        self.for_label_today_maxTemp.setGeometry(QtCore.QRect(160, 49, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.for_label_today_maxTemp.setFont(font)
        self.for_label_today_maxTemp.setObjectName("for_label_today_maxTemp")
        
        # Label description weather
        self.for_label_today_descr = QtWidgets.QLabel(self.for_frame_today)
        self.for_label_today_descr.setGeometry(QtCore.QRect(223, 61, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.for_label_today_descr.setFont(font)
        self.for_label_today_descr.setObjectName("for_label_today_descr")
        
        # Label icon today
        self.for_icon_today = QtWidgets.QLabel(self.for_frame_today)
        self.for_icon_today.setGeometry(QtCore.QRect(315, 5, 81, 81))
        self.for_icon_today.setFrameShape(QtWidgets.QFrame.Box)
        self.for_icon_today.setText("")
        self.for_icon_today.setPixmap(QtGui.QPixmap("10d@4x.png"))
        self.for_icon_today.setScaledContents(True)
        self.for_icon_today.setAlignment(QtCore.Qt.AlignCenter)
        self.for_icon_today.setObjectName("for_icon_today")

        # - - - - FRAME DAY+1 - - - -
        self.for_frame_d1 = QtWidgets.QFrame(self.tab_forecast)
        self.for_frame_d1.setGeometry(QtCore.QRect(440, 10, 401, 91))
        self.for_frame_d1.setFrameShape(QtWidgets.QFrame.Box)
        self.for_frame_d1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.for_frame_d1.setObjectName("for_frame_d1")

        # Label day+1 title
        self.for_label_d1 = QtWidgets.QLabel(self.for_frame_d1)
        self.for_label_d1.setGeometry(QtCore.QRect(10, 10, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.for_label_d1.setFont(font)
        self.for_label_d1.setObjectName("for_label_d1")

        # Label min
        self.for_label_d1_min = QtWidgets.QLabel(self.for_frame_d1)
        self.for_label_d1_min.setGeometry(QtCore.QRect(20, 61, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.for_label_d1_min.setFont(font)
        self.for_label_d1_min.setObjectName("for_label_d1_min")

        # Label minimum temperature D+1
        self.for_label_d1_minTemp = QtWidgets.QLabel(self.for_frame_d1)
        self.for_label_d1_minTemp.setGeometry(QtCore.QRect(60, 49, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.for_label_d1_minTemp.setFont(font)
        self.for_label_d1_minTemp.setObjectName("for_label_d1_minTemp")
        
        # Label max
        self.for_label_d1_max = QtWidgets.QLabel(self.for_frame_d1)
        self.for_label_d1_max.setGeometry(QtCore.QRect(120, 61, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.for_label_d1_max.setFont(font)
        self.for_label_d1_max.setObjectName("for_label_d1_max")

        # Label maximum temperature D+1
        self.for_label_d1_maxTemp = QtWidgets.QLabel(self.for_frame_d1)
        self.for_label_d1_maxTemp.setGeometry(QtCore.QRect(160, 49, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.for_label_d1_maxTemp.setFont(font)
        self.for_label_d1_maxTemp.setObjectName("for_label_d1_maxTemp")
        
        # Label D+1 description
        self.for_label_d1_descr = QtWidgets.QLabel(self.for_frame_d1)
        self.for_label_d1_descr.setGeometry(QtCore.QRect(223, 61, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.for_label_d1_descr.setFont(font)
        self.for_label_d1_descr.setObjectName("for_label_d1_descr")
        
        # Icon D+1
        self.for_icon_d1 = QtWidgets.QLabel(self.for_frame_d1)
        self.for_icon_d1.setGeometry(QtCore.QRect(315, 5, 81, 81))
        self.for_icon_d1.setFrameShape(QtWidgets.QFrame.Box)
        self.for_icon_d1.setText("")
        self.for_icon_d1.setPixmap(QtGui.QPixmap("10d@4x.png"))
        self.for_icon_d1.setScaledContents(True)
        self.for_icon_d1.setAlignment(QtCore.Qt.AlignCenter)
        self.for_icon_d1.setObjectName("for_icon_d1")

        # - - - - FRAME D+2 - - - -
        self.for_frame_d2 = QtWidgets.QFrame(self.tab_forecast)
        self.for_frame_d2.setGeometry(QtCore.QRect(20, 120, 401, 91))
        self.for_frame_d2.setFrameShape(QtWidgets.QFrame.Box)
        self.for_frame_d2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.for_frame_d2.setObjectName("for_frame_d2")

        # Label day+2 title
        self.for_label_d2 = QtWidgets.QLabel(self.for_frame_d2)
        self.for_label_d2.setGeometry(QtCore.QRect(10, 10, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.for_label_d2.setFont(font)
        self.for_label_d2.setObjectName("for_label_d2")

        # Label min
        self.for_label_d2_min = QtWidgets.QLabel(self.for_frame_d2)
        self.for_label_d2_min.setGeometry(QtCore.QRect(20, 61, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.for_label_d2_min.setFont(font)
        self.for_label_d2_min.setObjectName("for_label_d2_min")

        # Label minimum temperature
        self.for_label_d2_minTemp = QtWidgets.QLabel(self.for_frame_d2)
        self.for_label_d2_minTemp.setGeometry(QtCore.QRect(60, 49, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.for_label_d2_minTemp.setFont(font)
        self.for_label_d2_minTemp.setObjectName("for_label_d2_minTemp")
        
        # Label max
        self.for_label_d2_max = QtWidgets.QLabel(self.for_frame_d2)
        self.for_label_d2_max.setGeometry(QtCore.QRect(120, 61, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.for_label_d2_max.setFont(font)
        self.for_label_d2_max.setObjectName("for_label_d2_max")
        
        # Label maximum temperature D+2
        self.for_label_d2_maxTemp = QtWidgets.QLabel(self.for_frame_d2)
        self.for_label_d2_maxTemp.setGeometry(QtCore.QRect(160, 49, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.for_label_d2_maxTemp.setFont(font)
        self.for_label_d2_maxTemp.setObjectName("for_label_d2_maxTemp")
        
        # Label description D+2
        self.for_label_d2_descr = QtWidgets.QLabel(self.for_frame_d2)
        self.for_label_d2_descr.setGeometry(QtCore.QRect(223, 61, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.for_label_d2_descr.setFont(font)
        self.for_label_d2_descr.setObjectName("for_label_d2_descr")
        
        # Icon D+2
        self.for_icon_d2 = QtWidgets.QLabel(self.for_frame_d2)
        self.for_icon_d2.setGeometry(QtCore.QRect(315, 5, 81, 81))
        self.for_icon_d2.setFrameShape(QtWidgets.QFrame.Box)
        self.for_icon_d2.setText("")
        self.for_icon_d2.setPixmap(QtGui.QPixmap("10d@4x.png"))
        self.for_icon_d2.setScaledContents(True)
        self.for_icon_d2.setAlignment(QtCore.Qt.AlignCenter)
        self.for_icon_d2.setObjectName("for_icon_d2")

        # - - - - FRAME D+3 - - - -
        self.for_frame_d3 = QtWidgets.QFrame(self.tab_forecast)
        self.for_frame_d3.setGeometry(QtCore.QRect(440, 120, 401, 91))
        self.for_frame_d3.setFrameShape(QtWidgets.QFrame.Box)
        self.for_frame_d3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.for_frame_d3.setObjectName("for_frame_d3")
        
        # Label D+3 title
        self.for_label_d3 = QtWidgets.QLabel(self.for_frame_d3)
        self.for_label_d3.setGeometry(QtCore.QRect(10, 10, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.for_label_d3.setFont(font)
        self.for_label_d3.setObjectName("for_label_d3")

        # Label min
        self.for_label_d3_min = QtWidgets.QLabel(self.for_frame_d3)
        self.for_label_d3_min.setGeometry(QtCore.QRect(20, 61, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.for_label_d3_min.setFont(font)
        self.for_label_d3_min.setObjectName("for_label_d3_min")

        # Label minimum temperature D+3
        self.for_label_d3_minTemp = QtWidgets.QLabel(self.for_frame_d3)
        self.for_label_d3_minTemp.setGeometry(QtCore.QRect(60, 49, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.for_label_d3_minTemp.setFont(font)
        self.for_label_d3_minTemp.setObjectName("for_label_d3_minTemp")
        
        # Label max
        self.for_label_d3_max = QtWidgets.QLabel(self.for_frame_d3)
        self.for_label_d3_max.setGeometry(QtCore.QRect(120, 61, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.for_label_d3_max.setFont(font)
        self.for_label_d3_max.setObjectName("for_label_d3_max")
        
        # Label maximum temperature D+3
        self.for_label_d3_maxTemp = QtWidgets.QLabel(self.for_frame_d3)
        self.for_label_d3_maxTemp.setGeometry(QtCore.QRect(160, 49, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.for_label_d3_maxTemp.setFont(font)
        self.for_label_d3_maxTemp.setObjectName("for_label_d3_maxTemp")
        
        # Label description D+3
        self.for_label_d3_descr = QtWidgets.QLabel(self.for_frame_d3)
        self.for_label_d3_descr.setGeometry(QtCore.QRect(223, 61, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.for_label_d3_descr.setFont(font)
        self.for_label_d3_descr.setObjectName("for_label_d3_descr")
        
        # Icon D+3
        self.for_icon_d3 = QtWidgets.QLabel(self.for_frame_d3)
        self.for_icon_d3.setGeometry(QtCore.QRect(315, 5, 81, 81))
        self.for_icon_d3.setFrameShape(QtWidgets.QFrame.Box)
        self.for_icon_d3.setText("")
        self.for_icon_d3.setPixmap(QtGui.QPixmap("10d@4x.png"))
        self.for_icon_d3.setScaledContents(True)
        self.for_icon_d3.setAlignment(QtCore.Qt.AlignCenter)
        self.for_icon_d3.setObjectName("for_icon_d3")

        # - - - - FRAME D+4 - - - -
        self.for_frame_d4 = QtWidgets.QFrame(self.tab_forecast)
        self.for_frame_d4.setGeometry(QtCore.QRect(20, 230, 401, 91))
        self.for_frame_d4.setFrameShape(QtWidgets.QFrame.Box)
        self.for_frame_d4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.for_frame_d4.setObjectName("for_frame_d4")

        # Label D+4 title
        self.for_label_d4 = QtWidgets.QLabel(self.for_frame_d4)
        self.for_label_d4.setGeometry(QtCore.QRect(10, 10, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.for_label_d4.setFont(font)
        self.for_label_d4.setObjectName("for_label_d4")

        # Label min
        self.for_label_d4_min = QtWidgets.QLabel(self.for_frame_d4)
        self.for_label_d4_min.setGeometry(QtCore.QRect(20, 61, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.for_label_d4_min.setFont(font)
        self.for_label_d4_min.setObjectName("for_label_d4_min")

        # Label minimum temperature D+4
        self.for_label_d4_minTemp = QtWidgets.QLabel(self.for_frame_d4)
        self.for_label_d4_minTemp.setGeometry(QtCore.QRect(60, 49, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.for_label_d4_minTemp.setFont(font)
        self.for_label_d4_minTemp.setObjectName("for_label_d4_minTemp")
        
        # Label max
        self.for_label_d4_max = QtWidgets.QLabel(self.for_frame_d4)
        self.for_label_d4_max.setGeometry(QtCore.QRect(120, 61, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.for_label_d4_max.setFont(font)
        self.for_label_d4_max.setObjectName("for_label_d4_max")

        # Label maximum temperature D+4
        self.for_label_d4_maxMin = QtWidgets.QLabel(self.for_frame_d4)
        self.for_label_d4_maxMin.setGeometry(QtCore.QRect(160, 49, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.for_label_d4_maxMin.setFont(font)
        self.for_label_d4_maxMin.setObjectName("for_label_d4_maxMin")
        
        # Label D+4 description
        self.for_label_d4_descr = QtWidgets.QLabel(self.for_frame_d4)
        self.for_label_d4_descr.setGeometry(QtCore.QRect(223, 61, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.for_label_d4_descr.setFont(font)
        self.for_label_d4_descr.setObjectName("for_label_d4_descr")
        
        # Icon D+4
        self.for_icon_d4 = QtWidgets.QLabel(self.for_frame_d4)
        self.for_icon_d4.setGeometry(QtCore.QRect(315, 5, 81, 81))
        self.for_icon_d4.setFrameShape(QtWidgets.QFrame.Box)
        self.for_icon_d4.setText("")
        self.for_icon_d4.setPixmap(QtGui.QPixmap("10d@4x.png"))
        self.for_icon_d4.setScaledContents(True)
        self.for_icon_d4.setAlignment(QtCore.Qt.AlignCenter)
        self.for_icon_d4.setObjectName("for_icon_d4")

        # - - - - FRAME D+5 - - - -
        self.for_frame_d5 = QtWidgets.QFrame(self.tab_forecast)
        self.for_frame_d5.setGeometry(QtCore.QRect(440, 230, 401, 91))
        self.for_frame_d5.setFrameShape(QtWidgets.QFrame.Box)
        self.for_frame_d5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.for_frame_d5.setObjectName("for_frame_d5")

        # Label D+5 title
        self.for_label_d5 = QtWidgets.QLabel(self.for_frame_d5)
        self.for_label_d5.setGeometry(QtCore.QRect(10, 10, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.for_label_d5.setFont(font)
        self.for_label_d5.setObjectName("for_label_d5")

        # Label min
        self.for_label_d5_min = QtWidgets.QLabel(self.for_frame_d5)
        self.for_label_d5_min.setGeometry(QtCore.QRect(20, 61, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.for_label_d5_min.setFont(font)
        self.for_label_d5_min.setObjectName("for_label_d5_min")

        # Label minimum temperature D+5
        self.for_label_d5_minTemp = QtWidgets.QLabel(self.for_frame_d5)
        self.for_label_d5_minTemp.setGeometry(QtCore.QRect(60, 49, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.for_label_d5_minTemp.setFont(font)
        self.for_label_d5_minTemp.setObjectName("for_label_d5_minTemp")
        
        # Label max
        self.for_label_d5_max = QtWidgets.QLabel(self.for_frame_d5)
        self.for_label_d5_max.setGeometry(QtCore.QRect(120, 61, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.for_label_d5_max.setFont(font)
        self.for_label_d5_max.setObjectName("for_label_d5_max")
        
        # Label maximum temperature D+5
        self.for_label_d5_maxTemp = QtWidgets.QLabel(self.for_frame_d5)
        self.for_label_d5_maxTemp.setGeometry(QtCore.QRect(160, 49, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.for_label_d5_maxTemp.setFont(font)
        self.for_label_d5_maxTemp.setObjectName("for_label_d5_maxTemp")
        
        # Label D+5 description
        self.for_label_d5_descr = QtWidgets.QLabel(self.for_frame_d5)
        self.for_label_d5_descr.setGeometry(QtCore.QRect(223, 61, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.for_label_d5_descr.setFont(font)
        self.for_label_d5_descr.setObjectName("for_label_d5_descr")
        
        # Icon D+5
        self.for_icon_d5 = QtWidgets.QLabel(self.for_frame_d5)
        self.for_icon_d5.setGeometry(QtCore.QRect(315, 5, 81, 81))
        self.for_icon_d5.setFrameShape(QtWidgets.QFrame.Box)
        self.for_icon_d5.setText("")
        self.for_icon_d5.setPixmap(QtGui.QPixmap("10d@4x.png"))
        self.for_icon_d5.setScaledContents(True)
        self.for_icon_d5.setAlignment(QtCore.Qt.AlignCenter)
        self.for_icon_d5.setObjectName("for_icon_d5")

        # - - - - FRAME D+6 - - - -
        self.for_frame_d6 = QtWidgets.QFrame(self.tab_forecast)
        self.for_frame_d6.setGeometry(QtCore.QRect(20, 340, 401, 91))
        self.for_frame_d6.setFrameShape(QtWidgets.QFrame.Box)
        self.for_frame_d6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.for_frame_d6.setObjectName("for_frame_d6")

        # Label D+6 title
        self.for_label_d6 = QtWidgets.QLabel(self.for_frame_d6)
        self.for_label_d6.setGeometry(QtCore.QRect(10, 10, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.for_label_d6.setFont(font)
        self.for_label_d6.setObjectName("for_label_d6")

        # Label min
        self.for_label_d6_min = QtWidgets.QLabel(self.for_frame_d6)
        self.for_label_d6_min.setGeometry(QtCore.QRect(20, 61, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.for_label_d6_min.setFont(font)
        self.for_label_d6_min.setObjectName("for_label_d6_min")

        # Label minimum temperature D+6
        self.for_label_d6_minTemp = QtWidgets.QLabel(self.for_frame_d6)
        self.for_label_d6_minTemp.setGeometry(QtCore.QRect(60, 49, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.for_label_d6_minTemp.setFont(font)
        self.for_label_d6_minTemp.setObjectName("for_label_d6_minTemp")
        
        # Label max
        self.for_label_d6_max = QtWidgets.QLabel(self.for_frame_d6)
        self.for_label_d6_max.setGeometry(QtCore.QRect(120, 61, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.for_label_d6_max.setFont(font)
        self.for_label_d6_max.setObjectName("for_label_d6_max")

        # Label maximum temperature D+6
        self.for_label_d6_maxTemp = QtWidgets.QLabel(self.for_frame_d6)
        self.for_label_d6_maxTemp.setGeometry(QtCore.QRect(160, 49, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.for_label_d6_maxTemp.setFont(font)
        self.for_label_d6_maxTemp.setObjectName("for_label_d6_maxTemp")
        
        # Label D+6 description
        self.for_label_d6_descr = QtWidgets.QLabel(self.for_frame_d6)
        self.for_label_d6_descr.setGeometry(QtCore.QRect(223, 61, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.for_label_d6_descr.setFont(font)
        self.for_label_d6_descr.setObjectName("for_label_d6_descr")
        
        # Icon D+6
        self.for_icon_d6 = QtWidgets.QLabel(self.for_frame_d6)
        self.for_icon_d6.setGeometry(QtCore.QRect(315, 5, 81, 81))
        self.for_icon_d6.setFrameShape(QtWidgets.QFrame.Box)
        self.for_icon_d6.setText("")
        self.for_icon_d6.setPixmap(QtGui.QPixmap("10d@4x.png"))
        self.for_icon_d6.setScaledContents(True)
        self.for_icon_d6.setAlignment(QtCore.Qt.AlignCenter)
        self.for_icon_d6.setObjectName("for_icon_d6")

        # - - - - FRAME D+7 - - - -
        self.for_frame_d7 = QtWidgets.QFrame(self.tab_forecast)
        self.for_frame_d7.setGeometry(QtCore.QRect(440, 340, 401, 91))
        self.for_frame_d7.setFrameShape(QtWidgets.QFrame.Box)
        self.for_frame_d7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.for_frame_d7.setObjectName("for_frame_d7")

        # Label D+7 title
        self.for_label_d7 = QtWidgets.QLabel(self.for_frame_d7)
        self.for_label_d7.setGeometry(QtCore.QRect(10, 10, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.for_label_d7.setFont(font)
        self.for_label_d7.setObjectName("for_label_d7")

        # Label min
        self.for_label_d7_min = QtWidgets.QLabel(self.for_frame_d7)
        self.for_label_d7_min.setGeometry(QtCore.QRect(20, 61, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.for_label_d7_min.setFont(font)
        self.for_label_d7_min.setObjectName("for_label_d7_min")

        # Label minimum temperature D+7
        self.for_label_d7_minTemp = QtWidgets.QLabel(self.for_frame_d7)
        self.for_label_d7_minTemp.setGeometry(QtCore.QRect(60, 49, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.for_label_d7_minTemp.setFont(font)
        self.for_label_d7_minTemp.setObjectName("for_label_d7_minTemp")
        
        # Label max
        self.for_label_d7_max = QtWidgets.QLabel(self.for_frame_d7)
        self.for_label_d7_max.setGeometry(QtCore.QRect(120, 61, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.for_label_d7_max.setFont(font)
        self.for_label_d7_max.setObjectName("for_label_d7_max")

        # Label maximum temperature D+7
        self.for_label_d7_maxTemp = QtWidgets.QLabel(self.for_frame_d7)
        self.for_label_d7_maxTemp.setGeometry(QtCore.QRect(160, 49, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.for_label_d7_maxTemp.setFont(font)
        self.for_label_d7_maxTemp.setObjectName("for_label_d7_maxTemp")
        
        # Label D+7 description
        self.for_label_d7_descr = QtWidgets.QLabel(self.for_frame_d7)
        self.for_label_d7_descr.setGeometry(QtCore.QRect(223, 61, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.for_label_d7_descr.setFont(font)
        self.for_label_d7_descr.setObjectName("for_label_d7_descr")
        
        # Icon D+7
        self.for_icon_d7 = QtWidgets.QLabel(self.for_frame_d7)
        self.for_icon_d7.setGeometry(QtCore.QRect(315, 5, 81, 81))
        self.for_icon_d7.setFrameShape(QtWidgets.QFrame.Box)
        self.for_icon_d7.setText("")
        self.for_icon_d7.setPixmap(QtGui.QPixmap("10d@4x.png"))
        self.for_icon_d7.setScaledContents(True)
        self.for_icon_d7.setAlignment(QtCore.Qt.AlignCenter)
        self.for_icon_d7.setObjectName("for_icon_d7")


        # - - - - - - - -  TAB OPTION - - - - - - - - #
        self.tabHub.addTab(self.tab_forecast, "")
        self.tab_option = QtWidgets.QWidget()
        self.tab_option.setObjectName("tab_option")

        # LineEdit API
        self.opt_lineEdit_api = QtWidgets.QLineEdit(self.tab_option)
        self.opt_lineEdit_api.setGeometry(QtCore.QRect(230, 20, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.opt_lineEdit_api.setFont(font)
        self.opt_lineEdit_api.setObjectName("opt_lineEdit_api")

        # Label API title
        self.opt_label_apiTitle = QtWidgets.QLabel(self.tab_option)
        self.opt_label_apiTitle.setGeometry(QtCore.QRect(140, 14, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.opt_label_apiTitle.setFont(font)
        self.opt_label_apiTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.opt_label_apiTitle.setObjectName("opt_label_apiTitle")
        
        # Button verify
        self.opt_button_verify = QtWidgets.QPushButton(self.tab_option)
        self.opt_button_verify.setGeometry(QtCore.QRect(590, 20, 121, 41))
        self.opt_button_verify.setObjectName("opt_button_verify")
        
        # GroupBox temperature unit
        self.opt_groupBox_tempUnit = QtWidgets.QGroupBox(self.tab_option)
        self.opt_groupBox_tempUnit.setGeometry(QtCore.QRect(140, 80, 571, 91))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.opt_groupBox_tempUnit.setFont(font)
        self.opt_groupBox_tempUnit.setObjectName("opt_groupBox_tempUnit")
        
        # Radio Celcius
        self.opt_radio_celcius = QtWidgets.QRadioButton(self.opt_groupBox_tempUnit)
        self.opt_radio_celcius.setGeometry(QtCore.QRect(30, 50, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.opt_radio_celcius.setFont(font)
        self.opt_radio_celcius.setChecked(True)
        self.opt_radio_celcius.setObjectName("opt_radio_celcius")

        # Radio Kelvin
        self.opt_radio_kelvin = QtWidgets.QRadioButton(self.opt_groupBox_tempUnit)
        self.opt_radio_kelvin.setGeometry(QtCore.QRect(450, 50, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.opt_radio_kelvin.setFont(font)
        self.opt_radio_kelvin.setObjectName("opt_radio_kelvin")

        # Radio Farhenheit
        self.opt_radio_farh = QtWidgets.QRadioButton(self.opt_groupBox_tempUnit)
        self.opt_radio_farh.setGeometry(QtCore.QRect(210, 50, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.opt_radio_farh.setFont(font)
        self.opt_radio_farh.setObjectName("opt_radio_farh")

        # GroupBox wind unit
        self.opt_groupBox_windUnit = QtWidgets.QGroupBox(self.tab_option)
        self.opt_groupBox_windUnit.setGeometry(QtCore.QRect(140, 190, 571, 91))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.opt_groupBox_windUnit.setFont(font)
        self.opt_groupBox_windUnit.setObjectName("opt_groupBox_windUnit")
        
        # Radio km/h
        self.opt_radio_kmh = QtWidgets.QRadioButton(self.opt_groupBox_windUnit)
        self.opt_radio_kmh.setGeometry(QtCore.QRect(30, 50, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.opt_radio_kmh.setFont(font)
        self.opt_radio_kmh.setChecked(True)
        self.opt_radio_kmh.setObjectName("opt_radio_kmh")

        # Radio mph
        self.opt_radio_mph = QtWidgets.QRadioButton(self.opt_groupBox_windUnit)
        self.opt_radio_mph.setGeometry(QtCore.QRect(450, 50, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.opt_radio_mph.setFont(font)
        self.opt_radio_mph.setObjectName("opt_radio_mph")

        # Radio m/s
        self.opt_radio_ms = QtWidgets.QRadioButton(self.opt_groupBox_windUnit)
        self.opt_radio_ms.setGeometry(QtCore.QRect(260, 50, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.opt_radio_ms.setFont(font)
        self.opt_radio_ms.setObjectName("opt_radio_ms")

        # GroupBox refresh
        self.opt_groupBox_refresh = QtWidgets.QGroupBox(self.tab_option)
        self.opt_groupBox_refresh.setGeometry(QtCore.QRect(140, 300, 571, 91))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.opt_groupBox_refresh.setFont(font)
        self.opt_groupBox_refresh.setObjectName("opt_groupBox_refresh")
        
        # SpinBox refresh
        self.opt_spinBox_refresh = QtWidgets.QSpinBox(self.opt_groupBox_refresh)
        self.opt_spinBox_refresh.setGeometry(QtCore.QRect(113, 30, 61, 41))
        self.opt_spinBox_refresh.setAlignment(QtCore.Qt.AlignCenter)
        self.opt_spinBox_refresh.setMinimum(20)
        self.opt_spinBox_refresh.setMaximum(300)
        self.opt_spinBox_refresh.setProperty("value", 20)
        self.opt_spinBox_refresh.setObjectName("opt_spinBox_refresh")
        
        # Label every
        self.opt_label_every = QtWidgets.QLabel(self.opt_groupBox_refresh)
        self.opt_label_every.setGeometry(QtCore.QRect(40, 38, 61, 20))
        self.opt_label_every.setObjectName("opt_label_every")
        
        # Label minutes
        self.opt_label_minutes = QtWidgets.QLabel(self.opt_groupBox_refresh)
        self.opt_label_minutes.setGeometry(QtCore.QRect(190, 40, 81, 20))
        self.opt_label_minutes.setObjectName("opt_label_minutes")
        
        # Vertical line
        self.opt_lineVert = QtWidgets.QFrame(self.opt_groupBox_refresh)
        self.opt_lineVert.setGeometry(QtCore.QRect(280, 10, 20, 80))
        self.opt_lineVert.setFrameShape(QtWidgets.QFrame.VLine)
        self.opt_lineVert.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.opt_lineVert.setObjectName("opt_lineVert")
        
        # Label countdown
        self.opt_label_countDown = QtWidgets.QLabel(self.opt_groupBox_refresh)
        self.opt_label_countDown.setGeometry(QtCore.QRect(330, 40, 191, 20))
        self.opt_label_countDown.setAlignment(QtCore.Qt.AlignCenter)
        self.opt_label_countDown.setObjectName("opt_label_countDown")
        
        # Button Save all
        self.opt_button_saveAll = QtWidgets.QPushButton(self.tab_option)
        self.opt_button_saveAll.setGeometry(QtCore.QRect(376, 400, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.opt_button_saveAll.setFont(font)
        self.opt_button_saveAll.setObjectName("opt_button_saveAll")
        
        self.tabHub.addTab(self.tab_option, "")

        # - - - - - - - -  MAIN WINDOW - - - - - - - - #
        # Label status
        self.main_label_status = QtWidgets.QLabel(self.centralwidget)
        self.main_label_status.setGeometry(QtCore.QRect(10, 580, 861, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.main_label_status.setFont(font)
        self.main_label_status.setFrameShape(QtWidgets.QFrame.Box)
        self.main_label_status.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_label_status.setAlignment(QtCore.Qt.AlignCenter)
        self.main_label_status.setObjectName("main_label_status")
        
        # Label app title
        self.main_label_title = QtWidgets.QLabel(self.centralwidget)
        self.main_label_title.setGeometry(QtCore.QRect(10, 9, 871, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.main_label_title.setFont(font)
        self.main_label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.main_label_title.setObjectName("main_label_title")
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabHub.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Weather App"))
        self.loc_button_search.setText(_translate("MainWindow", "Search"))
        self.loc_label_searching.setText(_translate("MainWindow", "Searching..."))
        self.loc_label_enter_location.setText(_translate("MainWindow", "Enter a location"))
        self.loc_button_OK.setText(_translate("MainWindow", "OK"))
        self.loc_label_choose_location.setText(_translate("MainWindow", "Choose a location"))
        self.loc_label_getting.setText(_translate("MainWindow", "Getting..."))
        self.tabHub.setTabText(self.tabHub.indexOf(self.tab_location), _translate("MainWindow", "Location"))
        self.curr_label_temp.setText(_translate("MainWindow", "13°C"))
        self.curr_label_temp_title.setText(_translate("MainWindow", "Temperature"))
        self.curr_label_temp_more.setText(_translate("MainWindow", "Max temp : 14°C\n"
"Min temp : 4°C\n"
"Feels : 11°C"))
        self.curr_label_temp_description.setText(_translate("MainWindow", "Clear sky"))
        self.curr_label_wind_speed.setText(_translate("MainWindow", "14 km/h"))
        self.curr_label_wind_title.setText(_translate("MainWindow", "Wind"))
        self.curr_label_wind_dir.setText(_translate("MainWindow", "340°"))
        self.curr_label_wind_more.setText(_translate("MainWindow", "Beaufort scale : 3/12\n"
"Light breeze"))
        self.curr_label_wind_cardinal.setText(_translate("MainWindow", "North"))
        self.curr_label_more_title.setText(_translate("MainWindow", "More info"))
        self.curr_label_more_info_press.setText(_translate("MainWindow", "Pressure : 1013 hP\n"
"\n"
"Visibility : 3000 km\n"
"\n"
"Humidity : 69%"))
        self.curr_label_sun.setText(_translate("MainWindow", "Sunrise : 05:48\n"
"\n"
"Sunset : 19:45"))
        self.label_next_hours_title.setText(_translate("MainWindow", "Next hours"))
        self.curr_label_h1.setText(_translate("MainWindow", "15:00"))
        self.curr_label_h2.setText(_translate("MainWindow", "16:00"))
        self.curr_label_h3.setText(_translate("MainWindow", "17:00"))
        self.curr_label_h4.setText(_translate("MainWindow", "18:00"))
        self.curr_label_h5.setText(_translate("MainWindow", "19:00"))
        self.curr_label_h6.setText(_translate("MainWindow", "19:00"))
        self.curr_label_h1_info.setText(_translate("MainWindow", "8°C\n"
"12 km/h"))
        self.curr_label_h2_info.setText(_translate("MainWindow", "9°C\n"
"11 km/h"))
        self.curr_label_h3_info.setText(_translate("MainWindow", "10°C\n"
"13 km/h"))
        self.curr_label_h4_info.setText(_translate("MainWindow", "9°C\n"
"12 km/h"))
        self.curr_label_h5_info.setText(_translate("MainWindow", "7°C\n"
"12 km/h"))
        self.curr_label_h6_info.setText(_translate("MainWindow", "6°C\n"
"11 km/h"))
        self.curr_label_recap.setText(_translate("MainWindow", "Lyon, FR - 08/03/2021 14:12"))
        self.tabHub.setTabText(self.tabHub.indexOf(self.tab_current), _translate("MainWindow", "Current weather"))
        self.for_label_today.setText(_translate("MainWindow", "Today"))
        self.for_label_today_min.setText(_translate("MainWindow", "Min :"))
        self.for_label_today_minTemp.setText(_translate("MainWindow", "3°C"))
        self.for_label_today_max.setText(_translate("MainWindow", "Max :"))
        self.for_label_today_maxTemp.setText(_translate("MainWindow", "11°C"))
        self.for_label_today_descr.setText(_translate("MainWindow", "Rain"))
        self.for_label_d1.setText(_translate("MainWindow", "Day +1"))
        self.for_label_d1_min.setText(_translate("MainWindow", "Min :"))
        self.for_label_d1_minTemp.setText(_translate("MainWindow", "3°C"))
        self.for_label_d1_max.setText(_translate("MainWindow", "Max :"))
        self.for_label_d1_maxTemp.setText(_translate("MainWindow", "11°C"))
        self.for_label_d1_descr.setText(_translate("MainWindow", "Rain"))
        self.for_label_d2.setText(_translate("MainWindow", "Day +2"))
        self.for_label_d2_min.setText(_translate("MainWindow", "Min :"))
        self.for_label_d2_minTemp.setText(_translate("MainWindow", "3°C"))
        self.for_label_d2_max.setText(_translate("MainWindow", "Max :"))
        self.for_label_d2_maxTemp.setText(_translate("MainWindow", "11°C"))
        self.for_label_d2_descr.setText(_translate("MainWindow", "Rain"))
        self.for_label_d3.setText(_translate("MainWindow", "Day +3"))
        self.for_label_d3_min.setText(_translate("MainWindow", "Min :"))
        self.for_label_d3_minTemp.setText(_translate("MainWindow", "3°C"))
        self.for_label_d3_max.setText(_translate("MainWindow", "Max :"))
        self.for_label_d3_maxTemp.setText(_translate("MainWindow", "11°C"))
        self.for_label_d3_descr.setText(_translate("MainWindow", "Rain"))
        self.for_label_d4.setText(_translate("MainWindow", "Day +4"))
        self.for_label_d4_min.setText(_translate("MainWindow", "Min :"))
        self.for_label_d4_minTemp.setText(_translate("MainWindow", "3°C"))
        self.for_label_d4_max.setText(_translate("MainWindow", "Max :"))
        self.for_label_d4_maxMin.setText(_translate("MainWindow", "11°C"))
        self.for_label_d4_descr.setText(_translate("MainWindow", "Rain"))
        self.for_label_d5.setText(_translate("MainWindow", "Day +5"))
        self.for_label_d5_min.setText(_translate("MainWindow", "Min :"))
        self.for_label_d5_minTemp.setText(_translate("MainWindow", "3°C"))
        self.for_label_d5_max.setText(_translate("MainWindow", "Max :"))
        self.for_label_d5_maxTemp.setText(_translate("MainWindow", "11°C"))
        self.for_label_d5_descr.setText(_translate("MainWindow", "Rain"))
        self.for_label_d6.setText(_translate("MainWindow", "Day +6"))
        self.for_label_d6_min.setText(_translate("MainWindow", "Min :"))
        self.for_label_d6_minTemp.setText(_translate("MainWindow", "3°C"))
        self.for_label_d6_max.setText(_translate("MainWindow", "Max :"))
        self.for_label_d6_maxTemp.setText(_translate("MainWindow", "11°C"))
        self.for_label_d6_descr.setText(_translate("MainWindow", "Rain"))
        self.for_label_d7.setText(_translate("MainWindow", "Day +7"))
        self.for_label_d7_min.setText(_translate("MainWindow", "Min :"))
        self.for_label_d7_minTemp.setText(_translate("MainWindow", "3°C"))
        self.for_label_d7_max.setText(_translate("MainWindow", "Max :"))
        self.for_label_d7_maxTemp.setText(_translate("MainWindow", "11°C"))
        self.for_label_d7_descr.setText(_translate("MainWindow", "Rain"))
        self.tabHub.setTabText(self.tabHub.indexOf(self.tab_forecast), _translate("MainWindow", "Forecast"))
        self.opt_lineEdit_api.setText(_translate("MainWindow", "1def0c78689f22035176fc71c68b106c"))
        self.opt_label_apiTitle.setText(_translate("MainWindow", "OpenWeatherMap\n"
"API key :"))
        self.opt_button_verify.setText(_translate("MainWindow", "Verify"))
        self.opt_groupBox_tempUnit.setTitle(_translate("MainWindow", "Temperature unit"))
        self.opt_radio_celcius.setText(_translate("MainWindow", "Celcius"))
        self.opt_radio_kelvin.setText(_translate("MainWindow", "Kelvin"))
        self.opt_radio_farh.setText(_translate("MainWindow", "Fahrenheit"))
        self.opt_groupBox_windUnit.setTitle(_translate("MainWindow", "Wind unit"))
        self.opt_radio_kmh.setText(_translate("MainWindow", "km/h"))
        self.opt_radio_mph.setText(_translate("MainWindow", "mph"))
        self.opt_radio_ms.setText(_translate("MainWindow", "m/s"))
        self.opt_groupBox_refresh.setTitle(_translate("MainWindow", "Refresh"))
        self.opt_label_every.setText(_translate("MainWindow", "Every :"))
        self.opt_label_minutes.setText(_translate("MainWindow", "minutes"))
        self.opt_label_countDown.setText(_translate("MainWindow", "Next refresh in : 00:00"))
        self.opt_button_saveAll.setText(_translate("MainWindow", "Save all"))
        self.tabHub.setTabText(self.tabHub.indexOf(self.tab_option), _translate("MainWindow", "Option"))
        self.main_label_status.setText(_translate("MainWindow", "Status massage"))
        self.main_label_title.setText(_translate("MainWindow", "Weather App"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())