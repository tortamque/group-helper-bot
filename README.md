🇺🇦

<a href="https://github.com/pyrogram/pyrogram"><img src="https://docs.pyrogram.org/_static/pyrogram.png" align="right" width="10%"></a>

# Груповий бот-помічник
#### Це Telegram бот, який допоможе автоматизувати навчальну рутину
<i>Повністю настроюваний, модульний, простий в обслуговуванні, простий у масштабуванні 🐸</i>

-  [Необхідні пакети](#Необхідні-пакети)
-  [Можливості](#Можливості)
-  [Авторизація та встановлення](#Авторизація-та-встановлення)
-  [Модулі](#Модулі)
-  [Команди](#Команди)

<a name="Необхідні-пакети"/></a>
## Необхідні пакети
| Пакет | Посилання |
| ------ | ------ |
| APScheduler | https://pypi.org/project/APScheduler/ |
| Requests | https://pypi.org/project/requests/ |
| Pyrogram  | https://pypi.org/project/Pyrogram/ |
| TgCrypto | https://pypi.org/project/TgCrypto/ |

<a name="Можливості"/></a>
## Можливості
* Формування та управління чергою
* Відправка розкладу (Розклад береться із сайту schedule.kpi.ua)
* Нагадування про початок пари (За наявності, відправляється посилання на пару)
* Управління локальною базою даних із інтерфейсу бота

<a name="Авторизація-та-встановлення"/></a>
## Авторизація та встановлення
### 1. Авторизація
1. Для початку тобі потрібно створити власного бота. Для цього напиши офіційному боту (https://t.me/BotFather), за допомогою команди <code>/newbot</code> і наявних інструкцій ти створиш власного.
2. Запиши унікальний токен (Має вигляд <i>1234567:AAABBBCCCDDDEEEFFF</i>)
3. Створи унікальний <code>.session</code> файл твого бота (<a href="https://docs.pyrogram.org/start/auth">Детальніше</a>)
### 2. Встановлення
4. Тепер потрібно налаштувати основні параметри бота. Для цього, в папці <code>config/app.py</code> зміни ім'я сесії на своє.
5. В папці <code>config/config.py</code> зміни усі параметри
<br/><i>Примітка:</i>
<br/>admin_user_id - ID користувача з підвищеними правами (Зможе видаляти чергу, навіть якщо він її не створив, управляти базою даних і т.п.)
<br/>chat_id - ID чату, в якому буде працювати бот
<br/>bot_username - Username бота (без символу @)
<br/>group_name - Назва групи (Наприклад: XX-11)
6. Завантаж усі файли собі на сервер
7. Встанови <a href="#Необхідні-пакети">необхідні пакети</a>
8. Запусти бота: <code>python3 main.py</code>

<a name="Модулі"/></a>
## Модулі
1. Queue - Формування черги
2. Reminder - Нагадування про початок пари
3. Database - Управління базою даних
4. Timetable - Відправка розкладу
5. Tools - Інструменти

<a name="Команди"/></a>
## Команди

<b>Черги</b>
1. <code>/create <назва черги></code> - створити чергу
2. <code>/delete <назва черги></code> - видалити чергу
3. <code>/join <назва черги></code> - записатись у чергу
4. <code>/leave <назва черги></code> - вийти з черги
5. <code>/check</code> - перевірити наявні черги
6. <code>/pass <кількість людей> <назва черги></code> - пропустити людей в черзі
7. <code>/reset</code>

<b>Розклад</b>
1. <code>/week</code> - Розклад на цей тиждень
2. <code>/nextweek</code> - Розклад на наступний тиждень
3. <code>/today</code> - Розклад на сьогодні
4. <code>/tomorrow</code> - Розклад на завтра

<b>Управління базою даних</b>
1. <code>/setup_db</code> - Налаштувати базу даних
2. <code>/reset_db</code> - Очистити базу даних
3. <code>/show_db</code> - Показати вміст бази даних
4. <code>/editlink <ID пари> <нове посилання></code> - Змінити посилання на пару
5. <code>/ids</code> - Отримати ID всіх пар
  
<b>Інструменти</b>
1. <code>/ping</code> - Пінг
2. <code>/chat_id</code> - Отримати ID чату
3. <code>/user_id</code> - Показати ID користувача, який відправив цю команду
4. <code>/user_id у відповідь на повідомлення</code>- Показати ID користувача, на якого відповіли
-----

🇺🇸

# Group Helper Bot
#### This is the Telegram bot that will simplify the studying routine
<i>Fully customizable, Modular, Easy-to-maintain, Easy-to-scale 🐸</i>

-  [Required packages](#Required-packages)
-  [Сapabilities](#Сapabilities)
-  [Authorization and Setup](#Authorization-and-Setup)
-  [Modules](#Modules)
-  [Commands](#Commands)

<a name="Required-packages"/></a>
## Required packages
| Package | Link |
| ------ | ------ |
| APScheduler | https://pypi.org/project/APScheduler/ |
| Requests | https://pypi.org/project/requests/ |
| Pyrogram  | https://pypi.org/project/Pyrogram/ |
| TgCrypto | https://pypi.org/project/TgCrypto/ |

<a name="Сapabilities"/></a>
## Сapabilities
* Queue formation and management
* Sending the schedule (The schedule is taken from the website schedule.kpi.ua)
* Reminder about the start of the lesson (If available, a link to the lesson is sent)
* Local database management from the bot interface

<a name="Authorization-and-Setup"/></a>
## Authorization and Setup
### 1. Authorization
1. Firstly you need to create your own bot. To do this, write to the official bot (https://t.me/BotFather), using the command <code>/newbot</code> and the available instructions, you will create your own.
2. Write down the unique token (It looks like <i>1234567:AAABBBCCCDDDEEEFFF</i>)
3. Create a unique <code>.session</code> file of your bot (<a href="https://docs.pyrogram.org/start/auth">Details</a>)
### 2. Setup
4. Now you need to configure the basic parameters of the bot. To do this, change the session name to your own in the <code>config/app.py</code> folder.
5. Change all parameters in the <code>config/config.py</code> folder
<br/><i>Note:</i>
<br/>admin_user_id - ID of a user with elevated rights (Can delete a queue even if he did not create it, manage the database, etc.)
<br/>chat_id - ID of the chat in which the bot will work
<br/>bot_username - Username of the bot (without the @ symbol)
<br/>group_name - Group name (For example: XX-11)
6. Upload all files to your server
7. Install <a href="#Required-packages">required packages</a>
8. Run the bot: <code>python3 main.py</code>

<a name="Modules"/></a>
## Modules
1. Queue - Queue formation
2. Reminder - Reminder about the start of the lesson
3. Database - Database management
4. Timetable - Sending the schedule
5. Tools - Tools

<a name="Commands"/></a>
## Commands

<b>Queue</b>
1. <code>/create \<queue name></code> - create a queue
2. <code>/delete \<queue name></code> - delete the queue
3. <code>/join \<queue name></code> - join the queue
4. <code>/leave \<queue name></code> - leave the queue
5. <code>/check</code> - check available queues
6. <code>/pass \<number of people> \<queue name></code> - skip people in the queue
7. <code>/reset</code>

<b>Schedule</b>
1. <code>/week</code> - Schedule for this week
2. <code>/nextweek</code> - Schedule for the next week
3. <code>/today</code> - Schedule for today
4. <code>/tomorrow</code> - Schedule for tomorrow

<b>Database Management</b>
1. <code>/setup_db</code> - Set up the database
2. <code>/reset_db</code> - Clear the database
3. <code>/show_db</code> - Show the content of the database
4. <code>/editlink \<lesson ID> \<new link></code> - Change the lesson link
5. <code>/ids</code> - Get IDs of all lessons
  
<b>Tools</b>
1. <code>/ping</code> - Ping
2. <code>/chat_id</code> - Get chat ID
3. <code>/user_id</code> - Show the ID of the user who sent this command
4. <code>/user_id in response to the message</code> - Show the ID of the user who was answered
