document.getElementById("checkAgeBtn").addEventListener("click", function(event) {
  // Предотвращаем стандартное поведение, чтобы не перезагружалась страница
  event.preventDefault();

  const birthdateInput = document.getElementById("birthdate").value;

  // Проверка, если дата не выбрана
  if (!birthdateInput) {
    alert("Пожалуйста, выберите дату рождения.");
    return;
  }

  const birthdate = new Date(birthdateInput); // Преобразуем строку в объект Date
  const today = new Date(); // Текущая дата

  // Рассчитываем возраст
  let age = today.getFullYear() - birthdate.getFullYear();
  const monthDifference = today.getMonth() - birthdate.getMonth();
  if (monthDifference < 0 || (monthDifference === 0 && today.getDate() < birthdate.getDate())) {
    age--;
  }

  // Получаем день недели, в который человек родился
  const daysOfWeek = ["Воскресенье", "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"];
  const dayOfWeek = daysOfWeek[birthdate.getDay()]; // Получаем день недели (0 - Воскресенье, 1 - Понедельник и т.д.)

  const resultDiv = document.getElementById("result");
  // Проверка совершеннолетия
  if (age < 18) {
    alert("Вы несовершеннолетний. Для использования сайта необходима разрешение родителей.");
    resultDiv.innerHTML = "";
  }
  else{
    // Выводим информацию о возрасте и дне недели
    resultDiv.innerHTML = "<p>Ваш возраст:" + age + " лет</p><p>Вы родились в: " + dayOfWeek + "</p>";
  }

});
