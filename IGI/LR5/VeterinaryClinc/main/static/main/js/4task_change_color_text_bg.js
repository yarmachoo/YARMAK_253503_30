// Получаем ссылки на существующие элементы из HTML
const toggleInput = document.getElementById("customization-toggle");
const panel = document.getElementById("customization-panel");
const fontSizeSlider = document.getElementById("font-size-slider");
const textColorPicker = document.getElementById("text-color-picker");
const bgColorPicker = document.getElementById("background-color-picker");

// Показать/скрыть панель при переключении чекбокса
toggleInput.addEventListener("change", function () {
  panel.style.display = this.checked ? "block" : "none";
});

// Изменение размера шрифта
fontSizeSlider.addEventListener("input", function () {
  document.body.style.fontSize = `${this.value}px`;
});

// Изменение цвета текста
textColorPicker.addEventListener("input", function () {
  document.body.style.color = this.value;
});

// Изменение цвета фона
bgColorPicker.addEventListener("input", function () {
  document.body.style.backgroundColor = this.value;
});
