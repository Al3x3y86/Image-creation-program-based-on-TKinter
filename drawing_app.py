import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox
from PIL import Image, ImageDraw


class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Рисовалка с сохранением в PNG")

        # Создаем изображение и объект для рисования
        self.image = Image.new("RGB", (600, 400), "white")
        self.draw = ImageDraw.Draw(self.image)

        # Создаем холст для отображения
        self.canvas = tk.Canvas(root, width=600, height=400, bg='white')
        self.canvas.pack()

        # Настраиваем интерфейс
        self.sizes = [1, 2, 5, 10]  # Предопределенные размеры кисти
        self.brush_size = tk.IntVar(value=self.sizes[0])
        self.setup_ui()

        # Переменные для отслеживания движения мыши
        self.last_x, self.last_y = None, None
        self.pen_color = 'black'
        self.previous_color = self.pen_color

        # Привязываем события к холсту
        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)
        self.canvas.bind('<Button-3>', self.pick_color)  # Пипетка (правая кнопка мыши)

    def setup_ui(self):
        control_frame = tk.Frame(self.root)
        control_frame.pack(fill=tk.X)

        # Кнопка "Очистить"
        clear_button = tk.Button(control_frame, text="Очистить", command=self.clear_canvas)
        clear_button.pack(side=tk.LEFT)

        # Кнопка "Выбрать цвет"
        color_button = tk.Button(control_frame, text="Выбрать цвет", command=self.choose_color)
        color_button.pack(side=tk.LEFT)

        # Кнопка "Сохранить"
        save_button = tk.Button(control_frame, text="Сохранить", command=self.save_image)
        save_button.pack(side=tk.LEFT)

        # Кнопка "Ластик"
        eraser_button = tk.Button(control_frame, text="Ластик", command=self.use_eraser)
        eraser_button.pack(side=tk.LEFT)

        # Кнопка "Кисть"
        brush_button = tk.Button(control_frame, text="Кисть", command=self.use_brush)
        brush_button.pack(side=tk.LEFT)

        # Выпадающий список для выбора размера кисти
        size_menu = tk.OptionMenu(control_frame, self.brush_size, *self.sizes)
        size_menu.pack(side=tk.LEFT)

    def paint(self, event):
        # Рисование линии между предыдущей и текущей координатами мыши
        if self.last_x and self.last_y:
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y,
                                    width=self.brush_size.get(), fill=self.pen_color,
                                    capstyle=tk.ROUND, smooth=tk.TRUE)
            self.draw.line([self.last_x, self.last_y, event.x, event.y], fill=self.pen_color,
                           width=self.brush_size.get())

        # Обновление координат мыши
        self.last_x = event.x
        self.last_y = event.y

    def reset(self, event):
        # Сброс координат после отпускания кнопки мыши
        self.last_x, self.last_y = None, None

    def clear_canvas(self):
        # Очистка холста и создание нового изображения
        self.canvas.delete("all")
        self.image = Image.new("RGB", (600, 400), "white")
        self.draw = ImageDraw.Draw(self.image)

    def choose_color(self):
        # Открытие диалогового окна для выбора цвета
        color = colorchooser.askcolor(color=self.pen_color)[1]
        if color:
            self.pen_color = color
            self.previous_color = self.pen_color

    def use_eraser(self):
        # Активируем ластик (устанавливаем цвет кисти в белый)
        self.previous_color = self.pen_color
        self.pen_color = "white"

    def use_brush(self):
        # Возвращаемся к предыдущему цвету кисти
        self.pen_color = self.previous_color

    def pick_color(self, event):
        # Определяем цвет пикселя на изображении и устанавливаем его как цвет кисти
        x, y = event.x, event.y

        # Проверяем, что координаты в пределах изображения
        if 0 <= x < self.image.width and 0 <= y < self.image.height:
            color = '#%02x%02x%02x' % self.image.getpixel((x, y))
            self.pen_color = color
            self.previous_color = color

    def save_image(self):
        # Сохранение изображения в формате PNG
        file_path = filedialog.asksaveasfilename(filetypes=[('PNG files', '*.png')])
        if file_path:
            if not file_path.endswith('.png'):
                file_path += '.png'
            self.image.save(file_path)
            messagebox.showinfo("Информация", "Изображение успешно сохранено!")


def main():
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
