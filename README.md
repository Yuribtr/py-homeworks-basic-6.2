# Задание 6.2 + Продолжение

## Домашнее задание к лекции «Объекты и классы. Взаимодействие между ними»

Задача №2 "Аудиоколлекция"

Необходимо уметь хранить информацию по альбомам и трекам в них. Это можно сделать, используя классы Album и Track. У класса Track есть поля:

    Название;
    Длительность в минутах(используется тип данных int). И метод show, выводящий информацию по треку в виде <Название-Длительность>.
    У класса Album есть поля:
    Название альбома
    Группа
    Список треков И три метода:
    get_tracks - выводит информацию по всем трекам(используется метод show).
    add_track - добавление нового трека в список треков.
    get_duration - выводит длительность всего альбома.

Задание:

Создать 2 альбома с 3 треками. Для каждого вывести его длительность.

## Задача №2 "Аудиоколлекция". Продолжение.
Подробная информация об альбомах и треках.  

## Задание 1:
Вместо метода ```show``` использовать магический метод ```__str__``` у трека для вывода информации по треку.  
Пример использования
```python
print(track1)
Bohemian rhapsody-6min
```
У Класса Альбом также реализовать магический метод ```__str__``` для вывода информации по альбому и его треков.
Пример использования
```python
print(my_album)
Name group: Queen
Name album: Bohemian rhapsody
Tracks:
	Bohemian rhapsody-6min
	The show must go on-4min
```

## Задание 2:
Реализовать возможность сравнивать треки по длительности. Для этого нужно будет определить магические методы.
Пример
```python
track1 = Track('Bohemian rhapsody', 6)
track2 = Track('The show must go on', 4)
track1 > track2
True
```