# 🎨 Проект: Программа для создания изображений на основе TKinter  

**DrawingApp** — это простое приложение для рисования, позволяющее создавать рисунки, выбирать цвета, изменять размеры кисти и сохранять свои творения в формате PNG.  

![Скриншот программы](./image.png)  

## ✨ Функциональность  

- 🖌️ **Рисование на холсте:** Удобное рисование линий с использованием мыши.  
- 🎨 **Выбор цвета кисти:** Настройка цвета кисти через встроенное диалоговое окно.  
- 🔧 **Изменение размера кисти:** Выбор одного из предопределенных размеров кисти (1, 2, 5, 10).  
- 🧹 **Очистка холста:** Полная очистка холста для начала нового рисунка.  
- 💾 **Сохранение изображения:** Экспорт текущего рисунка в формат PNG через диалог выбора файла.  
- 🧽 **Ластик:** Возможность стирать части рисунка, устанавливая цвет кисти в белый. После использования ластика кисть автоматически возвращается к ранее выбранному цвету.  
- 🎯 **Пипетка:** Выбор цвета прямо с холста. Нажмите **правую кнопку мыши** на любом нарисованном элементе, и программа автоматически установит цвет под курсором в качестве нового цвета кисти.  

## 📁 Файлы проекта  

- 📌 `drawing_app.py` — основной файл, содержащий исходный код приложения.  
- 📌 `image.png` — скриншот, демонстрирующий интерфейс приложения.  

## 🚀 Как использовать  

1. Запустите `drawing_app.py`.  
2. **Рисуйте** — удерживайте левую кнопку мыши и перемещайте курсор по холсту.  
3. **Выбор цвета** — нажмите кнопку «Выбрать цвет» для открытия цветового диалогового окна.  
4. **Изменение размера кисти** — выберите размер кисти из выпадающего списка.  
5. **Использование ластика** — нажмите кнопку «Ластик», чтобы стереть часть рисунка. Для возврата к кисти нажмите «Кисть».  
6. **Очистка холста** — нажмите кнопку «Очистить», чтобы удалить всё с холста.  
7. **Выбор цвета с холста (Пипетка)** — нажмите **правую кнопку мыши** на холсте, чтобы выбрать цвет из нарисованного изображения.  
8. **Сохранение рисунка** — нажмите кнопку «Сохранить», выберите путь и имя файла для сохранения изображения в формате PNG.  

## 📦 Требования  

- Python 3.7+  
- Библиотека `Pillow`  

## 📥 Установка зависимостей  

```bash
pip install pillow  
