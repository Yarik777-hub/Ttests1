#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle, randint




#Создание главного окна приложения
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(900,800)

student_win = QWidget() #######

main_win.score = 0
main_win.total = 0

#Попытка создания главного экрана
lbl_start = QLabel('Ttests \n приложение для контрольных работ по информатике')
btn_sts = QPushButton('Войти как ученик')
btn_stt = QPushButton('Войти как учитель')

# создание виджетов
lbl_question = QLabel('Вопрос')
RadioGroup = QGroupBox('Варианты ответов:')
rbtn_1 = QRadioButton('Ответ 1')
rbtn_2 = QRadioButton('Ответ 2')
rbtn_3 = QRadioButton('Ответ 3')
rbtn_4 = QRadioButton('Ответ 4')

btn_ok = QPushButton('Ответить')

AnswerGroup = QGroupBox('Результат')
lbl_result = QLabel('Верно/ Не верно')
lbl_correct = QLabel('Правильный ответ')

BtnGroup = QButtonGroup()
BtnGroup.addButton(rbtn_1)
BtnGroup.addButton(rbtn_2)
BtnGroup.addButton(rbtn_3)
BtnGroup.addButton(rbtn_4)

answ =[rbtn_1, rbtn_2, rbtn_3, rbtn_4]



lbl_stat = QLabel('Статистика:')




#привязка элементов к лэйаутам

row1 = QHBoxLayout()
row1.addWidget(rbtn_1)
row1.addWidget(rbtn_2)
row2 = QHBoxLayout()
row2.addWidget(rbtn_3)
row2.addWidget(rbtn_4)

col = QVBoxLayout()
col.addLayout(row1)
col.addLayout(row2)
RadioGroup.setLayout(col)

col1 = QVBoxLayout()
col1. addWidget(lbl_result, alignment = Qt.AlignLeft)
col1. addWidget(lbl_correct, alignment = Qt.AlignCenter)
AnswerGroup.setLayout(col1)
AnswerGroup.hide()

student_Layout= QVBoxLayout() #######
student_Layout.setSpacing(15)
student_Layout.addWidget(lbl_question, alignment = Qt.AlignCenter, stretch = 2)
student_Layout.addWidget(RadioGroup, stretch = 2)
student_Layout.addWidget(AnswerGroup, stretch = 2)
student_Layout.addWidget(btn_ok)
student_Layout.addWidget(lbl_stat, alignment = Qt.AlignLeft, stretch = 2)

start_Layout = QVBoxLayout() #######
start_Layout.addWidget(lbl_start, alignment = Qt.AlignCenter, stretch = 2)
start_Layout.addWidget(btn_sts)
start_Layout.addWidget(btn_stt)


main_win.setLayout(start_Layout)

student_win.setLayout(student_Layout) #######




class Question():
    def __init__(self, q, r, W1, W2, W3):
        self.question = q
        self.r_answer = r
        self.wrong1 = W1
        self.wrong2 = W2
        self.wrong3 = W3




question_list = []
q = Question('Каких типов данных нет в Pyton?', 'tin', 'str', 'int', 'float')
question_list.append(q)
q = Question('В каком  из условных операторов используется elif?', 'с_ветвлениями', 'неполный', 'полный', 'вложенный')
question_list.append(q)
q = Question('Максимально сколько переменных может быть в скобках в цикле for?', '3', '4', '2', '1')
question_list.append(q)
q = Question('С чего начинается условный оператор?', 'if', 'for', 'while', 'elif')
question_list.append(q)
q = Question('С чего начинается цикл со счетчиком?', 'for', 'if', 'while', 'elif')
question_list.append(q)
q = Question('Укажите где правильно написан условие для условного оператора', 'if a>b:', 'ifa>b:', 'if a>b', 'If a>b')
question_list.append(q)
q = Question('Какой командой добавить переменную в Python?', 'input', 'print', 'len', 'max')
question_list.append(q)
q = Question('Сколько прообелов нужно отступать внутри цикла?', '4', '0', '1', '10')
question_list.append(q)
q = Question('По какой формуле вычисляется сумма', 'S+=a', 'K+=a', 'S+=1', 'K+=1')
question_list.append(q)
q = Question('По какой формуле вычисляется количество', 'K+=1', 'K+=a', 'S+=1', 'S+=a')
question_list.append(q)

def login_studen(): #######
    main_win.hide()
    student_win.show()

#реакция на нажатие на кнопку отвееить

def ShowResult():
    RadioGroup.hide()
    AnswerGroup.show()
    btn_ok.setText('Следующий вопрос')

def ShoQuestion():
    num = randint(0, len(question_list)-1)
    ask(question_list[num])
    RadioGroup.show()
    AnswerGroup.hide()
    btn_ok.setText('Ответить')
    BtnGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    BtnGroup.setExclusive(True)




def ask(q):
    shuffle(answ)
    lbl_question.setText(q.question)
    lbl_correct.setText(q.r_answer)
    answ[0].setText(q.r_answer)
    answ[1].setText(q.wrong1)
    answ[2].setText(q.wrong2)
    answ[3].setText(q.wrong3)
    main_win.total+=1

def Check_answer():
    if btn_ok.text() == 'Ответить':
        if answ[0].isChecked():
            lbl_result.setText('Совершенно Верно!!!!!!!!!!! :)')
            main_win.score+=1
        else:
            lbl_result.setText('Вы ошиблись! :(')
        ShowResult()
        lbl_stat.setText('Статистика:\nВсего вопросов:'+str(main_win.total)+'\nПравильных ответов'+str(main_win.score)+'\nРейтинг:'+str(main_win.score/main_win.total*100)+'%')
    else:
        ShoQuestion()



num = randint(0, len(question_list)-1)
ask(question_list[num])




btn_ok.clicked.connect(Check_answer)
btn_sts.clicked.connect(login_studen)


main_win.show()
app.exec_()