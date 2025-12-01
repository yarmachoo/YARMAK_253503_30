document.addEventListener('DOMContentLoaded', () => {
    const doctorTableBody = document.querySelector('#doctor-table tbody');
    const preloader = document.getElementById('preloader');
    let currentPage = 1;
    let doctors = [];
    let sortDirection = 'asc';
    let sortColumn = '';
    const awardText = document.getElementById('award-text');
    const awardButton = document.getElementById('award-btn');

    let selectedDoctorsList = []; // Массив для хранения выбранных докторов

    const phoneRegex = /^(8|(\+375))\s?(\(\d{2}\)|\d{2})\s?\d{3}[- ]?\d{2}[- ]?\d{2}$/;
    const urlRegex = /^(http:\/\/|https:\/\/).*\.(php|html)$/;

    const validatePhoneNumber = (phoneNumber) => phoneRegex.test(phoneNumber);
    const validateUrl = (url) => urlRegex.test(url);

    const loadDoctors = async () => {
        preloader.style.display = 'block';
        try {
            const response = await fetch('/users/api/doctors/');
            doctors = await response.json();
            renderTable();
        } catch (error) {
            console.error('Ошибка при загрузке данных:', error);
        } finally {
            preloader.style.display = 'none';
        }
    };

    const renderTable = () => {
    doctorTableBody.innerHTML = '';
    const filteredDoctors = doctors.filter(doctor => {
        const filterValue = document.getElementById('filter-input').value.toLowerCase();
        return doctor.username.toLowerCase().includes(filterValue);
    });

    const sortedDoctors = sortDoctors(filteredDoctors);
    const total = sortedDoctors.length;
    const pageSize = 3;
    const startIndex = (currentPage - 1) * pageSize;
    const doctorsPage = sortedDoctors.slice(startIndex, startIndex + pageSize);

    doctorsPage.forEach(doctor => {
        const isChecked = selectedDoctorsList.some(selected => selected.id === doctor.id);
        const row = document.createElement('tr');
        row.classList.add('doctor-row');
        row.dataset.id = doctor.id;

        row.innerHTML = `
            <td>${doctor.username}</td>
            <td><img src="${doctor.photo || 'default.jpg'}" alt="Фото" width="50"></td>
            <td>${doctor.phone_number}</td>
            <td>${doctor.email}</td>
            <td>${doctor.department}</td>
            <td>
                <input type="checkbox" class="doctor-checkbox" data-id="${doctor.id}" data-name="${doctor.username}" ${isChecked ? 'checked' : ''}>
            </td>
        `;
        doctorTableBody.appendChild(row);
    });

    attachRowListeners(); // Привязываем обработчики событий к строкам
    attachCheckboxListeners(); // Привязываем обработчики к чекбоксам

    document.getElementById('current-page').textContent = currentPage;
    document.getElementById('total-pages').textContent = Math.ceil(total / pageSize);
};

const attachRowListeners = () => {
    const rows = document.querySelectorAll('.doctor-row');
    rows.forEach(row => {
        row.addEventListener('click', () => {
            const doctorId = parseInt(row.dataset.id);
            const doctor = doctors.find(doc => doc.id === doctorId);

            if (doctor) {
                const doctorInfoDiv = document.getElementById('doctor-info');
                doctorInfoDiv.innerHTML = `
                    <h3>Информация о докторе</h3>
                    <p><strong>Имя:</strong> ${doctor.username}</p>
                    <p><strong>Телефон:</strong> ${doctor.phone_number}</p>
                    <p><strong>Email:</strong> ${doctor.email}</p>
                    <p><strong>Отделение:</strong> ${doctor.department}</p>
                    <img src="${doctor.photo || 'default.jpg'}" alt="Фото" width="100">
                `;
            }
        });
    });
};



    const attachCheckboxListeners = () => {
        const checkboxes = document.querySelectorAll('.doctor-checkbox');
        checkboxes.forEach(checkbox => {
            checkbox.addEventListener('change', event => {
                const doctorId = parseInt(event.target.dataset.id);
                const doctorName = event.target.dataset.name;
                if (event.target.checked) {
                    if (!selectedDoctorsList.some(doc => doc.id === doctorId)) {
                        selectedDoctorsList.push({ id: doctorId, name: doctorName });
                    }
                } else {
                    selectedDoctorsList = selectedDoctorsList.filter(doc => doc.id !== doctorId);
                }
            });
        });
    };

    awardButton.addEventListener('click', () => {
        if (selectedDoctorsList.length > 0) {
            const names = selectedDoctorsList.map(doc => doc.name);
            const awardMessage = `Премируются сотрудники: ${names.join(', ')}.`;
            awardText.textContent = awardMessage;
        } else {
            awardText.textContent = "Выберите хотя бы одного сотрудника для премирования.";
        }
    });

    const sortDoctors = (doctors) => {
        if (!sortColumn) return doctors;

        return doctors.sort((a, b) => {
            const valueA = a[sortColumn];
            const valueB = b[sortColumn];

            if (sortDirection === 'asc') {
                if (valueA < valueB) return -1;
                if (valueA > valueB) return 1;
                return 0;
            } else {
                if (valueA < valueB) return 1;
                if (valueA > valueB) return -1;
                return 0;
            }
        });
    };

    const handleColumnClick = (column) => {
        if (sortColumn === column) {
            sortDirection = sortDirection === 'asc' ? 'desc' : 'asc';
        } else {
            sortColumn = column;
            sortDirection = 'asc';
        }
        renderTable();
    };

    document.querySelectorAll('#doctor-table th').forEach((header, index) => {
        const columns = ['username', 'photo', 'phone_number', 'email', 'department'];
        header.addEventListener('click', () => {
            handleColumnClick(columns[index]);
            updateSortIcons();
        });
    });

    const updateSortIcons = () => {
        const headers = document.querySelectorAll('#doctor-table th');
        headers.forEach((header, index) => {
            const arrow = header.querySelector('.sort-arrow');
            if (arrow) arrow.remove();

            const columns = ['username', 'photo', 'phone_number', 'email', 'department'];
            if (columns[index] === sortColumn) {
                const arrowElement = document.createElement('span');
                arrowElement.classList.add('sort-arrow');
                arrowElement.textContent = sortDirection === 'asc' ? '↑' : '↓';
                header.appendChild(arrowElement);
            }
        });
    };

    // Добавление нового доктора
    const addDoctorButton = document.getElementById('add-doctor-btn');
    const addDoctorForm = document.getElementById('add-doctor-form');

    addDoctorButton.addEventListener('click', () => {
        const username = document.getElementById('new-doctor-username').value;
        const photo = document.getElementById('new-doctor-photo').value;
        const phoneNumber = document.getElementById('new-doctor-phone').value;
        const email = document.getElementById('new-doctor-email').value;
        const department = document.getElementById('new-doctor-department').value;

        if (!validatePhoneNumber(phoneNumber)) {
            alert('Некорректный номер телефона. Проверьте формат.');
            return;
        }

        if (!validateUrl(photo)) {
            alert('Некорректный URL. Убедитесь, что он начинается с http:// или https:// и заканчивается на .php или .html.');
            return;
        }

        const newDoctor = {
            id: doctors.length + 1, // Генерируем ID
            username,
            photo,
            phone_number: phoneNumber,
            email,
            department
        };

        doctors.push(newDoctor); // Добавляем доктора в массив
        renderTable(); // Обновляем таблицу
        addDoctorForm.reset(); // Сбрасываем форму
    });

    document.getElementById('filter-btn').addEventListener('click', renderTable);

    document.getElementById('next-page').addEventListener('click', () => {
        if (currentPage * 3 < doctors.length) {
            currentPage++;
            renderTable();
        }
    });

    document.getElementById('prev-page').addEventListener('click', () => {
        if (currentPage > 1) {
            currentPage--;
            renderTable();
        }
    });

    loadDoctors();
});
