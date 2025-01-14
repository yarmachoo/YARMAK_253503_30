document.addEventListener('DOMContentLoaded', () => {
    const addDoctorButton = document.getElementById('add-doctor-btn');
    const addDoctorForm = document.getElementById('add-doctor-form');
    const doctorForm = document.getElementById('doctor-form');
    const submitButton = document.getElementById('submit-btn');
    const validationMessage = document.getElementById('validation-message');

    const phonePattern = /^(80|\+375)\s?\(?\d{2,3}\)?\s?\d{3}[-\s]?\d{2}[-\s]?\d{2}$|^(8)\s?\(?\d{3}\)?\s?\d{3}[-\s]?\d{2}[-\s]?\d{2}$|^(80|\+375)\s?\(?\d{2,3}\)?\s?\d{7}$/;
    const urlPattern =  /.+/;

    // Массив для хранения данных о докторах
    let doctors = [];

    // Функция для проверки телефона
    const validatePhone = (phone) => {
        return phonePattern.test(phone);
    };

    // Функция для проверки URL
    const validateURL = (url) => {
        return urlPattern.test(url);
    };

    // Показать форму для добавления сотрудника
    addDoctorButton.addEventListener('click', () => {
        addDoctorForm.style.display = 'block';
    });

    // Валидация при изменении данных в форме
    doctorForm.addEventListener('input', () => {
        const firstName = document.getElementById('first-name').value;
        const lastName = document.getElementById('last-name').value;
        const phone = document.getElementById('phone').value;
        const email = document.getElementById('email').value;
        const url = document.getElementById('url').value;

        let validPhone = validatePhone(phone);
        let validURL = validateURL(url);

        // Проверка на валидацию
        if (firstName && lastName && phone && email && validPhone && validURL) {
            submitButton.disabled = false;
            validationMessage.textContent = '';
        } else {
            submitButton.disabled = true;

            let errorMessages = [];

            if (!validPhone) {
                errorMessages.push("Неверный формат телефона.");
                document.getElementById('phone').style.border = '2px solid red';
                document.getElementById('phone').style.backgroundColor = '#f7c0c0';
            } else {
                document.getElementById('phone').style.border = '';
                document.getElementById('phone').style.backgroundColor = '';
            }

            if (!validURL) {
                errorMessages.push("Неверный формат URL.");
                document.getElementById('url').style.border = '2px solid red';
                document.getElementById('url').style.backgroundColor = '#f7c0c0';
            } else {
                document.getElementById('url').style.border = '';
                document.getElementById('url').style.backgroundColor = '';
            }

            validationMessage.textContent = errorMessages.join(' ');
        }
    });

    // Обработка отправки формы
    doctorForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const firstName = document.getElementById('first-name').value;
        const lastName = document.getElementById('last-name').value;
        const photoInput = document.getElementById('photo');
        const photo = photoInput.files[0];  // Получаем файл из инпута
        const description = document.getElementById('description').value;
        const phone = document.getElementById('phone').value;
        const email = document.getElementById('email').value;
        const url = document.getElementById('url').value;

        // Проверяем, был ли выбран файл
        let photoUrl = '';
        if (photo) {
            // Генерируем URL объекта только если файл выбран
            photoUrl = URL.createObjectURL(photo);
        } else {
            // Если файл не выбран, можем использовать какой-то URL по умолчанию
            photoUrl = 'default-photo.jpg';  // Замените на ваш URL по умолчанию
        }

        // Добавление данных в массив doctors
        const newDoctor = {
            username: `${firstName} ${lastName}`,
            photo: photoUrl,
            phone_number: phone,
            email: email,
            department: 'Не указано',
            specializations: description,
            url: url,
        };

        doctors.push(newDoctor);  // Добавляем нового доктора в массив
        renderTable();  // Обновляем таблицу с новым доктором
        addDoctorForm.style.display = 'none';  // Скрываем форму
    });

    // Функция для отображения таблицы (предполагается, что она уже существует)
    const renderTable = () => {
        // Код для рендеринга таблицы, основанный на данных из массива doctors
    };
});
