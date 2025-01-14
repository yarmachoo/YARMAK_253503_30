const imageLeft = document.getElementById("image-left");
const imageRight = document.getElementById("image-right");

window.addEventListener("scroll", () => {
  const scrollValue = window.scrollY;

  // Расхождение картинок при прокрутке вниз
  imageLeft.style.transform = `translateX(-${scrollValue * 0.5}px)`;
  imageRight.style.transform = `translateX(${scrollValue * 0.5}px)`;

  // Схождение обратно при прокрутке вверх
  if (scrollValue === 0) {
    imageLeft.style.transform = "translateX(0)";
    imageRight.style.transform = "translateX(0)";
  }
});
