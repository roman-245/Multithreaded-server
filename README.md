# Multithreaded-server
## Создание простого многопоточного сервера

### Цель работы

Познакомиться с приемами работы с многопоточностью на примере создания сокетного TCP-сервера, способного работать с несколькими клиентами одновременно

### Задания для выполнения

1. Создать простой эхо-сервер и клиент для него.
2. Модифицировать код сервера таким образом, чтобы при подключении нового клиента создавался новый поток и вся работа с клиентом выполнялась в нем.
3. Проверить возможность подключения нескольких клиентов к этому серверу одновременно. 

### Решение задач находится в файлах: serverth.py и clientth.py

### Дополнительные задания

1. Реализовать сканер TCP-портов. Программа должна запрашивать имя хоста/IP-адрес у пользователя. Затем программа должна пробовать подключиться к этому хосту ко всем портами по очереди. При успешном подключении программа должна выводить в консоль сообщение “Порт N открыт”. 
    1. Модифицировать эту программу, чтобы сканирование портов происходило параллельно. Для этого нужно распараллелить сканирование портов по нескольким потокам. 
    2. Обеспечить вывод списка открытых портов по порядку.
    3. Реализовать progress bar в командной строке, показывающий прогресс сканирования.
2. Модифицировать простой эхо-сервер таким образом, чтобы при подключении клиента создавался новый поток, в котором происходило взаимодействие с ним.

### Решение задач находится в файлах: tr_server.py и tr_client.py
Вывод программы:
![pic1.png](pic1.png)
