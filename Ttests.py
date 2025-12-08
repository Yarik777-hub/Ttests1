#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QRadioButton, QGroupBox, QButtonGroup, QListWidget, QLineEdit, QTextEdit, QInputDialog,QFormLayout
from PyQt5.QtGui import QFont
from random import shuffle, randint, choice
import questions


# модуль для интерфейса учителя
# модуль для интерфейса ученика
# модуль главного окна
# модуль для работы со списками и json


#Создание главного окна приложения
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Ttests')
main_win.resize(900,800)

student8_win = QWidget() #######
student8_win.resize(900,800)

teacher_win = QWidget() #######
teacher_win.resize(900,800)

teacher_edit_win = QWidget() #######
teacher_edit_win.resize(900,800)

teacher_login_win = QWidget() #######
teacher_login_win.resize(900,800)

result_win = QWidget() #######
result_win.resize(900,800)

teacher_edit_q_win = QWidget() #######
teacher_edit_q_win.resize(900,800)

teacher_menu_edit_q_win = QWidget() #######
teacher_menu_edit_q_win.resize(900,800)

teacher_edit_q_win3 = QWidget() #######
teacher_edit_q_win3.resize(900,800)

#Создание первого учительского экрана
lbl_teach1 = QLabel('Добрый день!')
font = QFont('Arial', 30)
lbl_teach1.setFont(font)
field_tag = QLineEdit('')
field_tag.setPlaceholderText('Введите логин...')
field_text = QTextEdit()
field_tag2 = QLineEdit('')
field_tag2.setPlaceholderText('Введите пароль...')
btn_teach1 = QPushButton('Войти')


login = 'merculyn'
password = '7535'
# login = '1'
# password = '1'

#создание регистрационнго учительского экрана
lbl_teach3 = QLabel('Введите новый логин\n Введите новый пароль')
field_tag3 = QLineEdit('')
field_tag3.setPlaceholderText('Введите логин...')
field_text = QTextEdit()
field_tag4 = QLineEdit('')
field_tag4.setPlaceholderText('Введите пароль...')
field_text = QTextEdit()
btn_save = QPushButton('Сохранить')


#Создание второго учительского экрана
lbl_teach2 = QLabel('Добрый день!\n Наталья Владимировна')
lbl_teach2.setFont(font)
# btn_login = QPushButton('Сменить логин и пароль')
btn_edit5 = QPushButton('Редактировать 5 класс')
btn_edit6 = QPushButton('Редактировать 6 класс')
btn_edit8 = QPushButton('Редактировать 8 класс')
btn_edit10 = QPushButton('Редактировать 10 класс')
btn_edit11 = QPushButton('Редактировать 11 класс')

#создание окна где учитель юудет выбирать какие вопросы сделать
lbl_teach4 = QLabel('Выберете тип теста')
lbl_teach4.setFont(font)
btn_edit_quiz = QPushButton('Редактировать тест с вариантами ответа')
btn_edit_picture = QPushButton('Редактировать тест с картинкой')
btn_edit_textes = QPushButton('Редактировать тест с текстом')







#создание окна где учитель будет редактировать вопросы с вариантами ответа
list_q = QListWidget()
list_q_label = QLabel('Список вопросов')


button_q_create = QPushButton('Создать вопрос') #появляется окно с полем "Введите имя заметки"
button_q_del = QPushButton('Удалить вопрос')
button_q_save = QPushButton('Сохранить вопрос')
button_q_edit = QPushButton('Изменить вопрос')


field_text_r = QTextEdit()
field_text_q1 = QTextEdit()
field_text_q2 = QTextEdit()
field_text_q3 = QTextEdit()

#создание окна где учитель будет редактировать вопросы с письменным ответом
list_q3 = QListWidget()
list_q_label3 = QLabel('Список вопросов')


button_q_create3 = QPushButton('Создать вопрос') #появляется окно с полем "Введите имя заметки"
button_q_del3 = QPushButton('Удалить вопрос')
button_q_save3 = QPushButton('Сохранить вопрос')
field_text33 = QTextEdit()


main_win.score = 0
main_win.total = 0

#Попытка создания главного экрана
lbl_start = QLabel('Ttests - приложение для контрольных работ по информатике')
font1 = QFont('Arial', 24)

lbl_start.setFont(font1)
btn_sts = QPushButton('Войти как ученик')
btn_stt = QPushButton('Войти как учитель')

#созданиие финального окна
lbl_stat = QLabel('Статистика:')
lbl_fin = QLabel('Ваша оценка:')
lbl_mark = QLabel('')

lbl_fin.setFont(font1)
lbl_mark.setFont(font1)



# создание меню для ученика
student_menu_win = QWidget() #######
student_menu_win.resize(900,800)
lbl_student_menu = QLabel('Выбери класс')
font2 = QFont('Arial', 18)

lbl_student_menu.setFont(font2)
btn_student_menu5 = QPushButton('5 класс')
btn_student_menu6 = QPushButton('6 класс')
btn_student_menu8 = QPushButton('8 класс')
btn_student_menu10 = QPushButton('10 класс')
btn_student_menu11 = QPushButton('11 класс')


# создание виджетов
lbl_question = QLabel('Вопрос')
lbl_question.setFont(font2)
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



# lbl_stat = QLabel('Статистика:')




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

#привязка учительских элементов к лэйаутам
layout_q = QHBoxLayout()
col_3 = QVBoxLayout()
col_3.addWidget(field_text)
col_3.addWidget(field_text_r)
col_3.addWidget(field_text_q1)
col_3.addWidget(field_text_q2)
col_3.addWidget(field_text_q3)
col_3.addWidget(button_q_edit)




col_4 = QVBoxLayout()
col_4.addWidget(list_q_label)
col_4.addWidget(list_q)
row_3 = QHBoxLayout()
row_3.addWidget(button_q_create)
row_3.addWidget(button_q_del)
row_4 = QHBoxLayout()
row_4.addWidget(button_q_save)
col_4.addLayout(row_3)
col_4.addLayout(row_4)

layout_q.addLayout(col_3, stretch = 2)
layout_q.addLayout(col_4, stretch = 1)
teacher_edit_q_win.setLayout(layout_q)


layout_q3 = QHBoxLayout()
col_33 = QVBoxLayout()
col_33.addWidget(field_text33)


col_34 = QVBoxLayout()
col_34.addWidget(list_q_label3)
col_34.addWidget(list_q3)
row_33 = QHBoxLayout()
row_33.addWidget(button_q_create3)
row_33.addWidget(button_q_del3)
row_34 = QHBoxLayout()
row_34.addWidget(button_q_save3)
col_34.addLayout(row_33)
col_34.addLayout(row_34)

layout_q3.addLayout(col_33, stretch = 2)
layout_q3.addLayout(col_34, stretch = 1)
teacher_edit_q_win3.setLayout(layout_q3)



student_Layout8= QVBoxLayout() #######
student_Layout8.setSpacing(15)
student_Layout8.addWidget(lbl_question, alignment = Qt.AlignCenter, stretch = 2)
student_Layout8.addWidget(RadioGroup, stretch = 2)
student_Layout8.addWidget(AnswerGroup, stretch = 2)
student_Layout8.addWidget(btn_ok)


start_Layout = QVBoxLayout() #######
start_Layout.addWidget(lbl_start, alignment = Qt.AlignCenter, stretch = 2)
start_Layout.addWidget(btn_sts)
start_Layout.addWidget(btn_stt)

teach1_Layout = QVBoxLayout() #######
teach1_Layout.addWidget(lbl_teach1, alignment = Qt.AlignCenter, stretch = 2)
teach1_Layout.addWidget(field_tag)
teach1_Layout.addWidget(field_tag2)
teach1_Layout.addWidget(btn_teach1)

teach2_Layout = QVBoxLayout() #######
teach2_Layout.addWidget(lbl_teach2, alignment = Qt.AlignCenter, stretch = 2)
# teach2_Layout.addWidget(btn_login)
teach2_Layout.addWidget(btn_edit5)
teach2_Layout.addWidget(btn_edit6)
teach2_Layout.addWidget(btn_edit8)
teach2_Layout.addWidget(btn_edit10)
teach2_Layout.addWidget(btn_edit11)


# teach_login_Layout = QVBoxLayout() #######
# teach_login_Layout.addWidget(lbl_teach3, alignment = Qt.AlignCenter, stretch = 2)
# teach_login_Layout.addWidget(field_tag3)
# teach_login_Layout.addWidget(field_tag4)
# teach_login_Layout.addWidget(btn_save)



student_menu_Layout = QVBoxLayout() #######
student_menu_Layout.addWidget(lbl_student_menu, alignment = Qt.AlignCenter, stretch = 2)
student_menu_Layout.addWidget(btn_student_menu5)
student_menu_Layout.addWidget(btn_student_menu6)
student_menu_Layout.addWidget(btn_student_menu8)
student_menu_Layout.addWidget(btn_student_menu10)
student_menu_Layout.addWidget(btn_student_menu11)

teach3_Layout = QVBoxLayout() #######
teach3_Layout.addWidget(lbl_teach4, alignment = Qt.AlignCenter, stretch = 2)
teach3_Layout.addWidget(btn_edit_quiz)
teach3_Layout.addWidget(btn_edit_picture)
teach3_Layout.addWidget(btn_edit_textes)





fin_Layout = QVBoxLayout() #######
fin_Layout.addWidget(lbl_fin, alignment = Qt.AlignCenter, stretch = 2)
fin_Layout.addWidget(lbl_mark, alignment = Qt.AlignCenter, stretch = 2)
fin_Layout.addWidget(lbl_stat, alignment = Qt.AlignLeft, stretch = 2)


main_win.setLayout(start_Layout)

student_menu_win.setLayout(student_menu_Layout) #######

student8_win.setLayout(student_Layout8) #######

teacher_win.setLayout(teach1_Layout) #######

teacher_edit_win.setLayout(teach2_Layout) #######

# teacher_login_win.setLayout(teach_login_Layout) #######

teacher_menu_edit_q_win.setLayout(teach3_Layout)

result_win.setLayout(fin_Layout)

def menu_studen(): #######
    main_win.hide()
    teacher_win.hide()
    student8_win.hide()
    student_menu_win.show()


def login_studen(): #######
    main_win.hide()
    teacher_win.hide()
    student_menu_win.hide()
    student8_win.show()

def login_teacher(): #######
    main_win.hide()
    student8_win.hide()
    student_menu_win.hide()
    teacher_win.show()

def teacer_edit(): #######
    main_win.hide()
    student8_win.hide()
    student_menu_win.hide()
    teacher_win.hide()
    teacher_edit_win.show()

def teacher_menu_edit_q(): #######
    main_win.hide()
    student8_win.hide()
    student_menu_win.hide()
    teacher_win.hide()
    teacher_edit_win.hide()
    teacher_menu_edit_q_win.show()

def teacher_menu_edit_q3(): #######
    main_win.hide()
    student8_win.hide()
    student_menu_win.hide()
    teacher_win.hide()
    teacher_edit_win.hide()
    teacher_menu_edit_q_win.hide()
    teacher_edit_q_win.hide()
    teacher_edit_q_win3.show()
    question_list = questions.load_questions()
    for i in range(len(question_list)):
        list_q3.addItem('Вопрос '+str(i+1))

def teacer_Login_edit(): #######
    main_win.hide()
    student8_win.hide()
    student_menu_win.hide()
    teacher_win.hide()
    teacher_edit_win.hide()
    teacher_login_win.show()

def teacer_q_edit(): #######
    
    main_win.hide()
    student8_win.hide()
    student_menu_win.hide()
    teacher_win.hide()
    teacher_edit_win.hide()
    teacher_login_win.hide()
    teacher_menu_edit_q_win.hide()
    teacher_edit_q_win3.hide()
    teacher_edit_q_win.show()
    
    for i in range(len(question_list)):
        list_q.addItem('Вопрос '+str(i+1))

#Создание нового логина и нового пароля 
# def new_login():
#     login = field_tag3.text()
#     password = field_tag4.text()
#     field_tag.clear()
#     field_tag2.clear()
#     main_win.hide()
#     student_win.hide()
#     student_menu_win.hide()
#     teacher_login_win.hide()
#     teacher_edit_win.hide()
#     teacher_win.show()

def fin(): #######
    main_win.hide()
    teacher_win.hide()
    student8_win.hide()
    student_menu_win.hide()
    teacher_edit_win.hide()
    teacher_login_win.hide()
    RadioGroup.hide()
    AnswerGroup.hide()
    result_win.show()

def check():
    tag = field_tag.text()
    tag2 = field_tag2.text()
    if btn_teach1.text() == "Войти" and (tag == login or tag == 'merculyn') and (tag2 == password or tag2 == '7535'):
        teacer_edit()
    else:
        pass



#реакция на нажатие на кнопку отвееить

def ShowResult():
    RadioGroup.hide()
    AnswerGroup.show()
    btn_ok.setText('Следующий вопрос')
    if main_win.total>=10:
        btn_ok.setText('Завершить тестирование')

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

def show_q():
    #получаем текст из заметки с выделенным названием и отображаем его в поле редактирования
    key = list_q.selectedItems()[0].text()
    # print(key)
    key = key[(len('Вопрос ')):]
    # print(key)

    field_text.setText(question_list[int(key)-1][0])
    field_text_r.setText(question_list[int(key)-1][1])
    field_text_q1.setText(question_list[int(key)-1][2])
    field_text_q2.setText(question_list[int(key)-1][3])
    field_text_q3.setText(question_list[int(key)-1][4])


def edit_q():
    key = list_q.selectedItems()[0].text()
    key = key[(len('Вопрос ')):]
    question_list[int(key)-1][0] = field_text.toPlainText()
    question_list[int(key)-1][1] = field_text_r.toPlainText()
    question_list[int(key)-1][2] = field_text_q1.toPlainText()
    question_list[int(key)-1][3] = field_text_q2.toPlainText()
    question_list[int(key)-1][4] = field_text_q3.toPlainText()

    questions.save_questions(question_list)
    print(question_list)

def add_q():
    # notes[note_name] = {"текст" : "", "теги" : []}
    #     list_notes.addItem(note_name)
    #     list_tags.addItems(notes[note_name]["теги"])
    question_list.append(['Новый воспро', 'верный ответ', 'неверный ответ 1', 'неверный ответ 2', 'неверный ответ 3'])
    list_q.addItem('Вопрос '+str(len(question_list)))



    

def show_q3():
    #получаем текст из заметки с выделенным названием и отображаем его в поле редактирования
    key3 = list_q3.selectedItems()[0].text()
    # print(key)
    key3 = key3[(len('Вопрос ')):]
    # print(key)

    field_text33.setText(question_list[int(key)-1][0])
    # field_text_r.setText(question_list[int(key)-1][1])
    # field_text_q1.setText(question_list[int(key)-1][2])
    # field_text_q2.setText(question_list[int(key)-1][3])
    # field_text_q3.setText(question_list[int(key)-1][4])

def ask(q):
    shuffle(answ)
    lbl_question.setText(q[0])
    lbl_correct.setText(q[1])
    answ[0].setText(q[1])
    answ[1].setText(q[2])
    answ[2].setText(q[3])
    answ[3].setText(q[4])
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
        if main_win.score/main_win.total*100 >= 90:
            lbl_mark.setText('5')
        if main_win.score/main_win.total*100>= 70 and main_win.score/main_win.total*100< 90:
            lbl_mark.setText('4')
        if main_win.score/main_win.total*100>= 50 and main_win.score/main_win.total*100< 70:
            lbl_mark.setText('3')
        if main_win.score/main_win.total*100< 50:
            lbl_mark.setText('2')
    elif btn_ok.text() == 'Завершить тестирование':
            fin()
    else:
        ShoQuestion()
    


btn_ok.clicked.connect(Check_answer)
btn_sts.clicked.connect(menu_studen)
btn_stt.clicked.connect(login_teacher)
btn_student_menu8.clicked.connect(login_studen)
btn_teach1.clicked.connect(check)
# btn_login.clicked.connect(teacer_Login_edit)
# btn_save.clicked.connect(new_login)
btn_edit8.clicked.connect(teacher_menu_edit_q)
btn_edit_quiz.clicked.connect(teacer_q_edit)
btn_edit_textes.clicked.connect(teacher_menu_edit_q3)
button_q_create.clicked.connect(add_q)
list_q.itemClicked.connect(show_q)
button_q_edit.clicked.connect(edit_q)
# list_q3.itemClicked.connect(show_q3)

main_win.show()
# teacher.teacher_win.show()

question_list = questions.load_questions()
num = randint(0, len(question_list)-1)
ask(question_list[num])

app.exec_()
