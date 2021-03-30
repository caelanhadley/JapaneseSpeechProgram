from PyQt5 import QtCore, QtGui, QtWidgets
from math import log10
from time import sleep
import timeit
import threading
import AudioHandler as ah
import LanguageCheck as lc
import LanguageHandler as lh


class Ui_MainWindow(object):
    def __init__(self):
        self.highScore = 0
        self.lowScore = 100
        self.scores = []
        self.start_time = 0
        self.end_time = 0
        self.identity = 0
        self.LCDTime = 0
        self.countActive = False
        self.count_thread = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1328, 755)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setDockOptions(
            QtWidgets.QMainWindow.AllowTabbedDocks | QtWidgets.QMainWindow.AnimatedDocks)
        MainWindow.setWindowIcon(QtGui.QIcon('image_src/japan_app.ico'))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(800, 0, 531, 511))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.question_information = QtWidgets.QGroupBox(self.tab_1)
        self.question_information.setGeometry(QtCore.QRect(10, 10, 501, 241))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.question_information.setFont(font)
        self.question_information.setObjectName("question_information")
        self.text_lesson = QtWidgets.QLabel(self.question_information)
        self.text_lesson.setGeometry(QtCore.QRect(20, 30, 471, 21))
        self.text_lesson.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.text_lesson.setObjectName("text_lesson")
        self.text_reference = QtWidgets.QLabel(self.question_information)
        self.text_reference.setGeometry(QtCore.QRect(20, 60, 471, 21))
        self.text_reference.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.text_reference.setObjectName("text_reference")
        self.text_QuestionType = QtWidgets.QLabel(self.question_information)
        self.text_QuestionType.setGeometry(QtCore.QRect(20, 90, 471, 21))
        self.text_QuestionType.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.text_QuestionType.setObjectName("text_QuestionType")
        self.text_hint = QtWidgets.QLabel(self.question_information)
        self.text_hint.setGeometry(QtCore.QRect(20, 120, 471, 111))
        self.text_hint.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.text_hint.setWordWrap(True)
        self.text_hint.setObjectName("text_hint")
        self.score_information = QtWidgets.QGroupBox(self.tab_1)
        self.score_information.setGeometry(QtCore.QRect(10, 260, 501, 211))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.score_information.setFont(font)
        self.score_information.setObjectName("score_information")
        self.text_average_score = QtWidgets.QLabel(self.score_information)
        self.text_average_score.setGeometry(QtCore.QRect(20, 30, 170, 31))
        self.text_average_score.setObjectName("text_average_score")
        self.text_highscore = QtWidgets.QLabel(self.score_information)
        self.text_highscore.setGeometry(QtCore.QRect(20, 70, 170, 31))
        self.text_highscore.setObjectName("text_highscore")
        self.text_low_score = QtWidgets.QLabel(self.score_information)
        self.text_low_score.setGeometry(QtCore.QRect(20, 110, 170, 31))
        self.text_low_score.setObjectName("text_low_score")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lesson_selection = QtWidgets.QGroupBox(self.tab_2)
        self.lesson_selection.setGeometry(QtCore.QRect(10, 10, 511, 171))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lesson_selection.setFont(font)
        self.lesson_selection.setObjectName("lesson_selection")
        self.setting_lesson1 = QtWidgets.QCheckBox(self.lesson_selection)
        self.setting_lesson1.setGeometry(QtCore.QRect(20, 40, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.setting_lesson1.setFont(font)
        self.setting_lesson1.setChecked(True)
        self.setting_lesson1.setObjectName("setting_lesson1")
        self.setting_lesson2 = QtWidgets.QCheckBox(self.lesson_selection)
        self.setting_lesson2.setGeometry(QtCore.QRect(20, 60, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.setting_lesson2.setFont(font)
        self.setting_lesson2.setChecked(True)
        self.setting_lesson2.setObjectName("setting_lesson2")
        self.setting_lesson3 = QtWidgets.QCheckBox(self.lesson_selection)
        self.setting_lesson3.setGeometry(QtCore.QRect(20, 80, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.setting_lesson3.setFont(font)
        self.setting_lesson3.setChecked(True)
        self.setting_lesson3.setObjectName("setting_lesson3")
        self.setting_lesson4 = QtWidgets.QCheckBox(self.lesson_selection)
        self.setting_lesson4.setGeometry(QtCore.QRect(20, 100, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.setting_lesson4.setFont(font)
        self.setting_lesson4.setChecked(True)
        self.setting_lesson4.setObjectName("setting_lesson4")
        self.label_2 = QtWidgets.QLabel(self.lesson_selection)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 301, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.setting_lesson5 = QtWidgets.QCheckBox(self.lesson_selection)
        self.setting_lesson5.setGeometry(QtCore.QRect(20, 120, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.setting_lesson5.setFont(font)
        self.setting_lesson5.setChecked(False)
        self.setting_lesson5.setObjectName("setting_lesson5")
        self.setting_lesson6 = QtWidgets.QCheckBox(self.lesson_selection)
        self.setting_lesson6.setGeometry(QtCore.QRect(20, 140, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.setting_lesson6.setFont(font)
        self.setting_lesson6.setChecked(False)
        self.setting_lesson6.setObjectName("setting_lesson6")
        self.setting_greetings = QtWidgets.QCheckBox(self.lesson_selection)
        self.setting_greetings.setGeometry(QtCore.QRect(110, 40, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.setting_greetings.setFont(font)
        self.setting_greetings.setChecked(True)
        self.setting_greetings.setObjectName("setting_greetings")
        self.audio_settings = QtWidgets.QGroupBox(self.tab_2)
        self.audio_settings.setGeometry(QtCore.QRect(10, 350, 511, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.audio_settings.setFont(font)
        self.audio_settings.setObjectName("audio_settings")
        self.volume_slider = QtWidgets.QSlider(self.audio_settings)
        self.volume_slider.setGeometry(QtCore.QRect(150, 30, 160, 22))
        self.volume_slider.setProperty("value", 80)
        self.volume_slider.setOrientation(QtCore.Qt.Horizontal)
        self.volume_slider.setObjectName("volume_slider")
        self.text_volume = QtWidgets.QLabel(self.audio_settings)
        self.text_volume.setGeometry(QtCore.QRect(20, 30, 61, 16))
        self.text_volume.setObjectName("text_volume")
        self.additional_settings = QtWidgets.QGroupBox(self.tab_2)
        self.additional_settings.setGeometry(QtCore.QRect(10, 190, 511, 151))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.additional_settings.setFont(font)
        self.additional_settings.setObjectName("additional_settings")
        self.setting_hints = QtWidgets.QCheckBox(self.additional_settings)
        self.setting_hints.setGeometry(QtCore.QRect(20, 80, 101, 17))
        self.setting_hints.setChecked(True)
        self.setting_hints.setObjectName("setting_hints")
        self.setting_difficulty = QtWidgets.QComboBox(self.additional_settings)
        self.setting_difficulty.setGeometry(QtCore.QRect(140, 30, 91, 22))
        self.setting_difficulty.setObjectName("setting_difficulty")
        self.setting_difficulty.addItem("")
        self.setting_difficulty.addItem("")
        self.setting_difficulty.addItem("")
        self.text_scoring_mode = QtWidgets.QLabel(self.additional_settings)
        self.text_scoring_mode.setGeometry(QtCore.QRect(20, 30, 91, 21))
        self.text_scoring_mode.setObjectName("text_scoring_mode")
        self.text_score_explanation = QtWidgets.QLabel(
            self.additional_settings)
        self.text_score_explanation.setGeometry(QtCore.QRect(290, 30, 211, 81))
        self.text_score_explanation.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.text_score_explanation.setObjectName("text_score_explanation")
        self.tabWidget.addTab(self.tab_2, "")
        self.interaction_options = QtWidgets.QGroupBox(self.centralwidget)
        self.interaction_options.setGeometry(QtCore.QRect(800, 520, 531, 201))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.interaction_options.setFont(font)
        self.interaction_options.setObjectName("interaction_options")
        self.button_start = QtWidgets.QPushButton(self.interaction_options)
        self.button_start.setGeometry(QtCore.QRect(30, 30, 141, 51))
        self.button_start.setObjectName("button_start")
        self.button_next = QtWidgets.QPushButton(self.interaction_options)
        self.button_next.setGeometry(QtCore.QRect(30, 100, 141, 91))
        self.button_next.setObjectName("button_next")
        self.button_hint = QtWidgets.QPushButton(self.interaction_options)
        self.button_hint.setGeometry(QtCore.QRect(190, 30, 141, 51))
        self.button_hint.setObjectName("button_hint")
        self.button_answer = QtWidgets.QPushButton(self.interaction_options)
        self.button_answer.setGeometry(QtCore.QRect(190, 100, 301, 91))
        self.button_answer.setObjectName("button_answer")
        self.button_challenge = QtWidgets.QPushButton(self.interaction_options)
        self.button_challenge.setGeometry(QtCore.QRect(350, 30, 141, 51))
        self.button_challenge.setObjectName("button_challenge")
        self.viewer_main = QtWidgets.QGroupBox(self.centralwidget)
        self.viewer_main.setGeometry(QtCore.QRect(10, 10, 781, 501))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.viewer_main.setFont(font)
        self.viewer_main.setObjectName("viewer_main")
        self.picture_container = QtWidgets.QLabel(self.viewer_main)
        self.picture_container.setGeometry(QtCore.QRect(10, 20, 761, 471))
        self.picture_container.setText("")
        self.picture_container.setScaledContents(True)
        self.picture_container.setObjectName("picture_container")
        self.interactions_main = QtWidgets.QGroupBox(self.centralwidget)
        self.interactions_main.setGeometry(QtCore.QRect(9, 520, 781, 191))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.interactions_main.setFont(font)
        self.interactions_main.setObjectName("interactions_main")
        self.text_interaction = QtWidgets.QLabel(self.interactions_main)
        self.text_interaction.setGeometry(QtCore.QRect(10, 30, 681, 151))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.text_interaction.setFont(font)
        self.text_interaction.setScaledContents(False)
        self.text_interaction.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.text_interaction.setWordWrap(True)
        self.text_interaction.setObjectName("text_interaction")
        self.counter_countdown = QtWidgets.QLCDNumber(self.interactions_main)
        self.counter_countdown.setGeometry(QtCore.QRect(700, 20, 71, 41))
        self.counter_countdown.setSmallDecimalPoint(False)
        self.counter_countdown.setDigitCount(3)
        self.counter_countdown.setMode(QtWidgets.QLCDNumber.Dec)
        self.counter_countdown.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.counter_countdown.setProperty("intValue", 60)
        self.counter_countdown.setObjectName("counter_countdown")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1328, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)

        self.button_start.clicked.connect(self.startPressed)
        self.button_next.clicked.connect(self.nextPressed)
        self.button_hint.clicked.connect(self.hintPressed)
        self.button_challenge.clicked.connect(self.challengePressed)
        self.button_answer.clicked.connect(self.answerPressed)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    ## Load Methods ##

    def loadSplash(self):
        try:
            self.setViewerImage('splash.png')
        except:
            print("Error: Loading Splash Image!")

    ### GET METHODS ###

    # Will return String of Scoring Difficulty #
    def getScoringMode(self):
        return self.setting_difficulty.currentText()

    # Will return Array of active lessons #
    def getActiveLessons(self):
        result = []
        if self.setting_lesson1.checkState() == 2:
            result.append("LESSON_1")
        if self.setting_lesson2.checkState() == 2:
            result.append("LESSON_2")
        if self.setting_lesson3.checkState() == 2:
            result.append("LESSON_3")
        if self.setting_lesson4.checkState() == 2:
            result.append("LESSON_4")
        if self.setting_lesson5.checkState() == 2:
            result.append("LESSON_5")
        if self.setting_lesson6.checkState() == 2:
            result.append("LESSON_6")
        if self.setting_greetings.checkState() == 2:
            result.append("GREETINGS")
        return result

    # Returns boolean if hints should be active #
    def getHintActive(self):
        if self.setting_hints.checkState() == 2:
            return True
        else:
            return False

    # Returns int 1-100 to controll the output volume #
    def getVolume(self):
        return None

    ### SET METHODS ###

    # takes an int/double value; sets Countdown timer's time #
    def setLCD(self, numIn):
        self.LCDTime = numIn
        self.counter_countdown.display(numIn)

    def setInteractionsText(self, textIn):
        self.text_interaction.setText(textIn)

    def setHintText(self, textIn):
        self.text_hint.setText("Hint: " + textIn)

    def setFromLesson(self, lesson):
        self.text_lesson.setText("From: " + lesson)

    def setQuestionType(self, qType):
        self.text_QuestionType.setText("Type: " + qType)

    def setReference(self, reference):
        self.text_reference.setText("Reference: " + reference)

    def setAverageScore(self, score):
        self.text_average_score.setText("Average Score: " + str(score))

    def setHighScore(self, score):
        self.text_highscore.setText("High Score: " + str(score))

    def setLowScore(self, score):
        self.text_low_score.setText("Low Score: " + str(score))

    def setViewerImage(self, filename):
        try:
            self.picture_container.setScaledContents(False)
            self.picture_container.setAlignment(QtCore.Qt.AlignCenter)
            pixmap = QtGui.QPixmap("image_src/" + filename)
            pixmap = pixmap.scaledToHeight(471, QtCore.Qt.SmoothTransformation)
            self.picture_container.setPixmap(pixmap)
        except:
            self.setInteractionsText(f'Error: Image {filename} was not found')

    def removeViewerImage(self):
        try:
            self.picture_container.clear()
        except:
            print("Error: removeViewerImage")

    def getAnswerWithTag(self, answer, tag):
        if tag == "Conv":
            return lc.compareAnswers(answer, self.identity)
        elif tag == "Pers":
            return lc.compareContains(answer, self.identity)
        else:
            return None

    def scoreCalculation(self, deltTime):
        try:
            tempScore = -(log10(deltTime / 50) / 1.2)
            if tempScore > 1:
                tempScore = 1
            elif tempScore < 0:
                tempScore = 0
            return tempScore * 100
        except:
            print("ERROR: Score Calculation Problem!")

    def countdownTimer(self, timeAmt):
        self.setLCD(timeAmt)
        while self.LCDTime > 0 and self.countActive:
            self.countdownLCD()
            sleep(1)

    # --- >>> INPUT <<< --- #

    def startPressed(self):  # Redundant Code! MAY BE HANDY
        self.nextPressed()

    def nextPressed(self):
        try:
            if self.count_thread != None:
                self.countActive = False
                self.count_thread.join()
        except:
            print("Error: Countdown Thread")
        self.start_time = timeit.default_timer()
        audiofile, self.identity = lh.selectClipFromSet(
            lc.getQuestionSet(self.getActiveLessons()))
        self.newAudioThread(audiofile)
        self.setFromLesson(str(lc.getLesson(self.identity)))
        self.setQuestionType(str(lc.getCategory(self.identity)))
        self.countActive = True
        self.count_thread = threading.Thread(
            target=self.countdownTimer, args=(60,))
        self.count_thread.start()

        if lc.hasImage(self.identity):
            self.setViewerImage(lc.getImage(self.identity))

    def hintPressed(self):
        self.setInteractionsText("Hint!")

    def challengePressed(self):
        self.setInteractionsText("Challange!")

    def answerPressed(self):
        self.setInteractionsText("Please speak into your microphone...")
        answer = lh.getInput(self.identity)

        if self.getAnswerWithTag(answer, lc.getTag(self.identity)):
            self.end_time = timeit.default_timer()
            self.countActive = False
            self.count_thread.join()
            self.setInteractionsText(
                f'Correct! You said \"{answer}\" in {round(self.deltaTime(), 1)}')
            self.newAudioThread('buzzer.wav')
            self.removeViewerImage()
            self.addScore(self.scoreCalculation(self.deltaTime()))
        else:
            self.setInteractionsText(
                f'Incorrect! You said \"{answer}\" in {round(self.deltaTime(), 1)} seconds!')
            self.newAudioThread('buzzer_wrong.wav')

    def countdownLCD(self):
        if self.counter_countdown.value() > 0:
            self.LCDTime -= 1
            self.counter_countdown.display(self.counter_countdown.value() - 1)

    def addScore(self, score):
        if score > self.highScore:
            self.highScore = score
            self.setHighScore(str(round(score, 1)))
        elif score < self.lowScore:
            self.lowScore = score
            self.setLowScore(str(round(score, 1)))
        self.scores.append(score)
        self.setAverageScore(self.average(self.scores))

    def average(self, number_list):
        try:
            return round(sum(number_list) / len(number_list), 1)
        except:
            self.setInteractionsText("Error: Average calculation error!")

    def plotScores(self):  # WIP ##
        return None

    def newAudioThread(self, filename):
        audio_thread = threading.Thread(target=ah.play_audio, args=(filename,))
        audio_thread.start()

    def deltaTime(self):
        return self.end_time - self.start_time

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.question_information.setTitle(
            _translate("MainWindow", "Question Information"))
        self.text_lesson.setText(_translate("MainWindow", "From:"))
        self.text_reference.setText(_translate("MainWindow", "Reference:"))
        self.text_QuestionType.setText(_translate("MainWindow", "Type:"))
        self.text_hint.setText(_translate("MainWindow", "Hint:"))
        self.score_information.setTitle(
            _translate("MainWindow", "Score Information"))
        self.text_average_score.setText(
            _translate("MainWindow", "Average Score:"))
        self.text_highscore.setText(_translate("MainWindow", "High Score:"))
        self.text_low_score.setText(_translate("MainWindow", "Low Score:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_1), _translate("MainWindow", "Info"))
        self.lesson_selection.setTitle(
            _translate("MainWindow", "Lesson Selection"))
        self.setting_lesson1.setText(_translate("MainWindow", "Lesson 1"))
        self.setting_lesson2.setText(_translate("MainWindow", "Lesson 2"))
        self.setting_lesson3.setText(_translate("MainWindow", "Lesson 3"))
        self.setting_lesson4.setText(_translate("MainWindow", "Lesson 4"))
        self.label_2.setText(_translate(
            "MainWindow", "Enable to include dialogue from selected lesson(s):"))
        self.setting_lesson5.setText(_translate("MainWindow", "Lesson 5"))
        self.setting_lesson6.setText(_translate("MainWindow", "Lesson 6"))
        self.setting_greetings.setText(_translate("MainWindow", "Greetings"))
        self.audio_settings.setTitle(
            _translate("MainWindow", "Audio Settings"))
        self.text_volume.setText(_translate("MainWindow", "Volume"))
        self.additional_settings.setTitle(
            _translate("MainWindow", "Additional Settings"))
        self.setting_hints.setToolTip(_translate(
            "MainWindow", "Allows hints to be used"))
        self.setting_hints.setText(_translate("MainWindow", "Allow Hints"))
        self.setting_difficulty.setToolTip(_translate(
            "MainWindow", "Changes the difficulty of scores"))
        self.setting_difficulty.setItemText(
            0, _translate("MainWindow", "Easy"))
        self.setting_difficulty.setItemText(
            1, _translate("MainWindow", "Normal"))
        self.setting_difficulty.setItemText(
            2, _translate("MainWindow", "Realistic"))
        self.text_scoring_mode.setText(
            _translate("MainWindow", "Scoring Mode"))
        self.text_score_explanation.setText(_translate("MainWindow", "For a score of"
                                                       + " 100 answer in:\n   Easy -     15s \n   Medium - 10s \n   Realistic -   4s"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_2), _translate("MainWindow", "Options"))
        self.interaction_options.setTitle(
            _translate("MainWindow", "Interaction Options"))
        self.button_start.setText(_translate("MainWindow", "Start"))
        self.button_next.setToolTip(_translate(
            "MainWindow", "Press for next Question"))
        self.button_next.setText(_translate("MainWindow", "Next"))
        self.button_hint.setText(_translate("MainWindow", "Hint"))
        self.button_answer.setToolTip(_translate(
            "MainWindow", "Press to answer current question"))
        self.button_answer.setText(_translate("MainWindow", "Press to Answer"))
        self.button_challenge.setText(
            _translate("MainWindow", "Challenge Answer"))
        self.viewer_main.setTitle(_translate("MainWindow", "Viewer"))
        self.interactions_main.setTitle(
            _translate("MainWindow", "Interactions"))
        self.text_interaction.setText(_translate(
            "MainWindow", "<INTERACTIONS PLACEHOLDER>"))
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Japanese Speech Program"))


def onExit(app, ui):
    app.exec_()
    try:
        ui.countActive = False
        ui.count_thread.join()
    except:
        print("Thread Does Not Exist!")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.loadSplash()
    MainWindow.show()
    sys.exit(onExit(app, ui))
