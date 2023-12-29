from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QLineEdit, QComboBox,QTableWidget,QFileDialog,QDialog,QMessageBoxfrom PyQt5.QtWidgets import QFrame,QPushButton,QMenuBar,QStatusBar,QMainWindow,QVBoxLayout,QHBoxLayout,QGridLayout,QTableWidgetItemfrom PyQt5 import QtCorefrom PyQt5.QtWidgets import QLabelfrom PyQt5.QtGui import  QIconimport pandas as pdimport os,reclass Ui_MainWindow(QMainWindow):    def __init__(self):        super().__init__()        self.setupUi()    def setupUi(self):        self.resize(1000, 680) # 设置主窗口初始尺寸        # 创建一个容器用于放置其他组件，放置在主窗口的中心位置        self.centralwidget = QWidget(self)        self.setCentralWidget(self.centralwidget)        # 创建一个分组框组件        self.groupBox = QGroupBox(self.centralwidget)        layout1 = QVBoxLayout()        hlayout1 = QHBoxLayout()        layout1.addLayout(hlayout1)        self.groupBox.setLayout(layout1)        self.groupBox.setStyleSheet("QGroupBox { margin: 1px; border: 1px solid lightgrey; }") #指定了 QGroupBox 的内边距为 3 像素        self.comboBox = QComboBox(self.groupBox) # 创建一个下拉框组件        # 设置调整策略为 AdjustToContents,自使用内部名字长度        self.comboBox.setSizeAdjustPolicy(QComboBox.AdjustToContents)        hlayout1.addWidget(self.comboBox)        self.comboBox.setFixedHeight(23)#设置高度        self.comboBox.setFixedWidth(260)#设置宽度        self.lineEdit = QLineEdit(self.groupBox)  # 创建输入选择框        self.lineEdit.setFixedHeight(23)        hlayout1.addWidget(self.lineEdit)        self.lineEdit.mousePressEvent = self.on_mousePressEvent        self.pushButton = QPushButton(self.groupBox)  # 创建按钮1        self.pushButton.setFixedHeight(23)        self.pushButton.setFixedWidth(75)        self.pushButton.clicked.connect(self.on_pushButton_clicked)        hlayout1.addWidget(self.pushButton)        self.pushButton_2 = QPushButton(self.groupBox)  # 创建按钮2        self.pushButton_2.clicked.connect(self.openDialog)        self.pushButton_2.setFixedHeight(23)        self.pushButton_2.setFixedWidth(75)        hlayout1.addWidget(self.pushButton_2)        # 创建一个分组框组件，并设置位置和尺寸        self.groupBox_2 = QGroupBox(self.centralwidget)        self.line = QFrame(self.centralwidget)#加了条直线，主要是为了美观        self.line.setGeometry(10, 160, 571, 20)        self.line.setFrameShape(QFrame.HLine)        self.line.setFrameShadow(QFrame.Sunken)        self.groupBox_3 = QGroupBox(self.centralwidget)#创建第三个分组框组件        layout2 = QVBoxLayout()        hlayout2 = QHBoxLayout()        layout2.addLayout(hlayout2)        self.groupBox_3.setLayout(layout2)        self.tableWidget = QTableWidget(self.groupBox_3)  # 创建编辑表格数据的控件        self.tableWidget.setColumnCount(0)        self.tableWidget.setRowCount(0)        hlayout2.addWidget(self.tableWidget)        # 创建一个 QMenuBar 对象 self.menubar，并将其设置为当前窗口的菜单栏        self.menubar = QMenuBar(self)        # 设置 self.menubar 的位置和尺寸        self.menubar.setGeometry(0, 0, 604, 21)        # 将 self.menubar 设置为当前窗口的菜单栏        self.setMenuBar(self.menubar)        # 创建一个 QStatusBar 对象 self.statusbar，用于显示当前窗口的状态栏        self.statusbar = QStatusBar(self)        # 将 self.statusbar 设置为当前窗口的状态栏        self.setStatusBar(self.statusbar)        self.retranslateUi(self)#是一个自动生成的方法，用于更新界面上的文本内容        QtCore.QMetaObject.connectSlotsByName(self)#是一个用于将信号和槽函数连接起来的方法。在使用 Qt Designer 工具创建界面时，可以在界面中指定某个控件的槽函数。    def resizeEvent(self, event):        #设置各个控件随窗口大小而改变        window_size = self.size()        self.groupBox.setGeometry(10, 0, window_size.width() - 20, 41)        self.groupBox_2.setGeometry(10, 42, window_size.width() - 20, 121)        self.line.setGeometry(10, 160, window_size.width() - 20, 20)        self.groupBox_3.setGeometry(10, 175, window_size.width() - 20, window_size.height() - 230)    def retranslateUi(self, MainWindow):        _translate = QtCore.QCoreApplication.translate        MainWindow.setWindowTitle(_translate("MainWindow", "表格管理工具"))        ico_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'test.ico') #设置左上角的图片        MainWindow.setWindowIcon(QIcon(ico_file))        self.pushButton.setText(_translate("MainWindow", "搜索"))        self.pushButton_2.setText(_translate("MainWindow", "导出"))    def on_mousePressEvent(self, event):        if event.button() == QtCore.Qt.LeftButton:            directory = QFileDialog.getExistingDirectory(self, '选择目录')            if directory:                self.lineEdit.setText(directory)                self.setcombox(directory)    def setcombox(self,directory):        self.comboBox.blockSignals(True)#阻止comboBox触发信号        self.comboBox.clear()#在为combox添加值之前清除combox内的所有内容        self.file_dir = {}        pattern = re.compile(r"^[^~].*\.xlsx?$")        for item in os.listdir(directory):            if pattern.search(item):                self.comboBox.addItem(item)#将过滤好的文件名字加入到comboxBox                file_data = pd.read_excel(directory +'/'+item) #读取目录下的文件                self.file_dir[item] = file_data#将文件以文件名：文件内容的方式放入到file_dir自动中        if self.file_dir:            self.show_data()  # 当选择好目录后就展示        else:            msg_box = QMessageBox()            msg_box.setIcon(QMessageBox.Warning)            msg_box.setWindowTitle("警告")            msg_box.setText("所选目录内没有excel表格")            # 显示错误弹窗            msg_box.exec()        self.comboBox.blockSignals(False)#开启comboBox触发信号        #        # # 连接comboBox信号和槽函数        self.comboBox.currentIndexChanged.connect(self.show_data)    def show_data(self):        data = self.file_dir[self.comboBox.currentText()]        self.groupBox_2.setProperty("my_attribute", data) #将展示数据传入自定义属性        if 'Unnamed' in str(data.columns):            # 删除名为 "Unnamed: 6" 的列            data = data.drop('Unnamed: 6', axis=1)        titles = data.columns[:10]        # 获取 groupBox 中的布局        the_vbox = self.groupBox_2.layout()        if the_vbox:            for widget in self.groupBox_2.findChildren(QWidget):  # 清除groupBox内所有子元素                widget.deleteLater()        else:            the_vbox = QVBoxLayout()            self.groupBox_2.setLayout(the_vbox)        the_grid_layout = QGridLayout()  # 使用QGridLayout代替QHBoxLayout        the_vbox.addLayout(the_grid_layout)        num = 0        grid_row = 0        grid_column = 0        for item in titles:            label = QLabel('%s:' % item, self.groupBox)            lineedit = QLineEdit(self.groupBox)            lineedit.setProperty("my_attribute", item) # 为了区分和标记表格，添加一个自定义属性my_attribute,并将标题赋值给它            lineedit.setFixedHeight(30)            the_grid_layout.addWidget(label,grid_row,grid_column)            the_grid_layout.addWidget(lineedit,grid_row,grid_column+1)            num += 1            if num % 5 == 0:                grid_row += 1                grid_column = 0            else:                grid_column += 2 #控制列数        self.on_text_changed(data) #将所读    def on_text_changed(self, *args):        '''        作为combox触发函数内调用        :param data: dataframe类型数        :return:        '''        data = args[0]        self.tableWidget.setColumnCount(0)        self.tableWidget.setRowCount(0)        num_rows, num_cols = data.shape[0], data.shape[1]        # 设置QTableWidget的行数和列数        self.tableWidget.setRowCount(num_rows)        self.tableWidget.setColumnCount(num_cols)        extra_width = 160  # 设置额外宽度        self.tableWidget.resizeColumnsToContents()  # 自适应每列宽度        for column in range(self.tableWidget.columnCount()):            width = self.tableWidget.columnWidth(column)            self.tableWidget.setColumnWidth(column, width + extra_width)        self.tableWidget.horizontalHeader().setStretchLastSection(True)        # 设置每列的列名        column_names = data.columns[:-1]        self.tableWidget.setHorizontalHeaderLabels(column_names)        for i in range(num_rows):            for j in range(num_cols):                item = QTableWidgetItem(str(data.iloc[i, j]))                self.tableWidget.setItem(i, j, item)        self.tableWidget.setAlternatingRowColors(True)  # 开启交错颜色        # self.tableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)  # 开启右键菜单        # self.tableWidget.customContextMenuRequested.connect(self.show_context_menu)  # 自定义右键操作        # self.tableWidget.itemSelectionChanged.connect(self.handleSelectionChanged)    def search_term(self, df_data, column_name, find_key):        '''        根据条件 find_key 在指定列中查找对应的表格中的数据        :param DataFrame, column_name, find_key（条件）:        :return: 返回符合条件的行的行号        '''        filtered_df = df_data[column_name].astype(str).str.contains(find_key, case=False)        indexes = filtered_df[filtered_df].index.tolist()        return indexes    def on_pushButton_clicked(self):        line_edits = self.groupBox_2.findChildren(QLineEdit)#获取groupBox_2子属性中全部QLineEdit控件        #将所有QLineEdit列表中每个控件内的值和自定义属性my_attribute的值组成元组（obj1,obj2）并放入到列表select_list中        select_list = [(item.text().strip(), item.property('my_attribute')) for item in line_edits]        search_list = [] #定义一个空列表，用来接收所有的搜索到的值        dataframe = self.groupBox_2.property("my_attribute") #获取为self.groupBox_2 自定义的属性值，该值是上面代码放入的表格的dataframe类型数据        for item, line in select_list:#遍历self.groupBox_2控件内所有QLineEdit内的值            item_list = self.search_term(dataframe, line, item) #将表格数据df,列名line,搜索项item传入搜索函数，用来获取搜索到的行号            search_list.append(item_list)#将搜索到的行号全部追加到search_list 列表中        common_elements = set(search_list[0]).intersection(*search_list[1:])        new_df = dataframe.iloc[list(common_elements)]        return self.on_text_changed(new_df)    def openDialog(self):        rows = self.tableWidget.rowCount()#获取self.tableWidget的行数        cols = self.tableWidget.columnCount()#获取self.tableWidget的列数        if rows != 0:            data = [[] for _ in range(rows)] #设置data列表            for row in range(rows):                for col in range(cols):                    item = self.tableWidget.item(row, col) #获取self.tableWidget 中的内容                    if item is not None:                        data[row].append(item.text())                    else:                        data[row].append("")            header = [] #设置表格标题            for col in range(cols):                header.append(self.tableWidget.horizontalHeaderItem(col).text())            data = pd.DataFrame(data, columns=header)            dialog = MyDialog(data) #初始化MyDialog 方法            dialog.setWindowTitle("导出表格")  # 设置对话框的标题            dialog.setWindowFlags(dialog.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)  # 移除问号图标            dialog.textEdit.setText(dialog.dir)            dialog.exec_()#塞程序的执行，直至对话框关闭        else:            msg_box = QMessageBox()            msg_box.setIcon(QMessageBox.Information)            msg_box.setWindowTitle("警告")            msg_box.setText("未选择目录，请先选择目录")            # 显示错误弹窗            msg_box.exec()# 弹出的对话框class MyDialog(QDialog):    def __init__(self, data):        super().__init__()        self.initUI()        self.data = data        self.dir = os.getcwd()    def initUI(self):        layout = QVBoxLayout()        label = QLabel('选择导出位置')        layout.addWidget(label)        self.textEdit = QLineEdit()        layout.addWidget(self.textEdit)        self.textEdit.mousePressEvent = self.on_mousePressEvent        button = QPushButton('导出表格')        button.clicked.connect(self.selectDirectory)        layout.addWidget(button)        self.setLayout(layout)    def on_mousePressEvent(self, event):        if event.button() == QtCore.Qt.LeftButton:            directory = QFileDialog.getExistingDirectory(self, '选择目录')            if directory:                self.textEdit.setText(directory)        self.dir = directory    def selectDirectory(self):        try:            self.data.to_excel(self.dir + '/output.xlsx', index=False)        except Exception as e:            # 创建错误弹窗并设置错误消息            msg_box = QMessageBox()            msg_box.setIcon(QMessageBox.Critical)            msg_box.setWindowTitle("错误")            msg_box.setText("输出表格已打开，请关闭表格或选择其他导出位置")            # 显示错误弹窗            msg_box.exec()        self.accept()if __name__ == '__main__':    import sys# 引入 sys 模块，用于退出应用程序    app = QApplication([])# 创建一个 QApplication 实例    widget = Ui_MainWindow()# 创建一个 Ui_MainWindow 对象实例    widget.show()# 显示窗口    sys.exit(app.exec_())# 运行应用程序，直到退出