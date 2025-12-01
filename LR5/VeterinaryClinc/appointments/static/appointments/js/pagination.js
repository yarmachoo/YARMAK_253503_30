document.addEventListener("DOMContentLoaded", function () {
  const itemsPerPage = 3;
  const gridContainer = document.querySelector(".grid-container");
  const paginationContainer = document.getElementById("pagination");
  const gridItems = Array.from(document.querySelectorAll(".grid-item"));
  // округление вверх
  const totalPages = Math.ceil(gridItems.length / itemsPerPage);

  // Функция отображения элементов текущей страницы
  function displayPage(page) {
    gridContainer.innerHTML = "";
    const start = (page - 1) * itemsPerPage;
    const end = start + itemsPerPage;

    gridItems.slice(start, end).forEach((item) => {
      gridContainer.appendChild(item);
    });

    renderPagination(page);
  }

  // Создание кнопок навигации
  function renderPagination(currentPage) {
    paginationContainer.innerHTML = "";
    for (let i = 1; i <= totalPages; i++) {
      const button = document.createElement("button");
      button.textContent = i;
      //button.classList.add("page-button");
      if (i === currentPage) button.classList.add("active");
      button.addEventListener("click", () => displayPage(i));
      paginationContainer.appendChild(button);
    }
  }

  // Инициализация первой страницы
  displayPage(1);
});
