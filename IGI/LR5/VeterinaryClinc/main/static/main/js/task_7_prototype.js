// Базовый класс "Employee"
function Employee(firstName, lastName, patronymic, gender, experience) {
  this.firstName = firstName;
  this.lastName = lastName;
  this.patronymic = patronymic || '';
  this.gender = gender;
  this.experience = experience;
}

Employee.prototype.getFirstName = function() {
  return this.firstName;
};

Employee.prototype.setFirstName = function(firstName) {
  this.firstName = firstName;
};

Employee.prototype.getLastName = function() {
  return this.lastName;
};

Employee.prototype.setLastName = function(lastName) {
  this.lastName = lastName;
};

Employee.prototype.getExperience = function() {
  return this.experience;
};

Employee.prototype.setExperience = function(experience) {
  this.experience = experience;
};

// Класс "EmployeeList" для работы с массивом сотрудников
function EmployeeList() {
  this.employees = [];
}

EmployeeList.prototype.addEmployee = function(employee) {
  this.employees.push(employee);
};

EmployeeList.prototype.getMostCommonNames = function() {
  let maleNames = {};
  let femaleNames = {};

  this.employees.forEach((employee) => {
    const firstName = employee.getFirstName();
    if (employee.gender === 'male') {
      maleNames[firstName] = (maleNames[firstName] || 0) + 1;
    } else {
      femaleNames[firstName] = (femaleNames[firstName] || 0) + 1;
    }
  });

    const mostCommonMaleName = Object.keys(maleNames).length
    ? Object.keys(maleNames).reduce((a, b) => maleNames[a] > maleNames[b] ? a : b)
    : 'нет данных';

  const mostCommonFemaleName = Object.keys(femaleNames).length
    ? Object.keys(femaleNames).reduce((a, b) => femaleNames[a] > femaleNames[b] ? a : b)
    : 'нет данных';


  return { mostCommonMaleName, mostCommonFemaleName };
};

EmployeeList.prototype.renderEmployees = function() {
  const employeeListElement = document.getElementById("employeeList");
  employeeListElement.innerHTML = '';

  this.employees.forEach((employee) => {
    const li = document.createElement("li");
    li.textContent = `${employee.firstName} ${employee.lastName}, Стаж: ${employee.experience}`;
    employeeListElement.appendChild(li);
  });
};

const employeeList = new EmployeeList();

document.getElementById("employeeForm").addEventListener("submit", function(event) {
  event.preventDefault();

  const firstName = document.getElementById("firstName").value;
  const lastName = document.getElementById("lastName").value;
  const patronymic = document.getElementById("patronymic").value;
  const gender = document.getElementById("gender").value;
  const experience = document.getElementById("experience").value;

  const employee = new Employee(firstName, lastName, patronymic, gender, experience);
  employeeList.addEmployee(employee);
  employeeList.renderEmployees();

  const mostCommonNames = employeeList.getMostCommonNames();
  document.getElementById("mostCommonMaleName").textContent = `Мужские имена: ${mostCommonNames.mostCommonMaleName}`;
  document.getElementById("mostCommonFemaleName").textContent = `Женские имена: ${mostCommonNames.mostCommonFemaleName}`;
});
