const startX = -1;
const endX = 1;
const step = 0.1;
const epsilon = 0.0001;

// Функция для разложения arccos(x) в ряд
function arccosSeries(x, nTerms) {
    let sum = Math.PI / 2;
    let term = x;
    for (let n = 1; n <= nTerms; n++) {
        sum -= term;
        term *= (x * x * (2 * n - 1)) / (2 * n + 1);
    }
    return sum;
}

let data = [];
for (let x = startX; x <= endX; x += step) {
    const nTerms = 5;
    const approx = arccosSeries(x, nTerms);
    const exact = Math.acos(x);
    data.push({
        x: x,
        n: nTerms,
        Fx: approx,
        mathFx: exact,
        eps: Math.abs(approx - exact)
    });
}

// Данные для построения графиков
const labels = data.map(d => d.x.toFixed(2));
const approxData = data.map(d => d.Fx);
const exactData = data.map(d => d.mathFx);

// Настройка графика с Chart.js
const ctx = document.getElementById('myChart').getContext('2d');
const chart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: labels,
        datasets: [
            {
                label: 'F(x) (Разложение в ряд)',
                data: approxData,
                borderColor: 'blue',
                fill: false
            },
            {
                label: 'Math F(x) (Точное значение)',
                data: exactData,
                borderColor: 'red',
                fill: false
            }
        ]
    },
    options: {
        animation: {
            duration: 2000 // Анимация при построении
        },
        scales: {
            x: {
                title: {
                    display: true,
                    text: 'x'
                }
            },
            y: {
                title: {
                    display: true,
                    text: 'F(x)'
                }
            }
        },
        plugins: {
            legend: {
                display: true,
                position: 'top'
            },
            tooltip: {
                callbacks: {
                    label: function (context) {
                        return `${context.dataset.label}: ${context.parsed.y.toFixed(4)}`;
                    }
                }
            }
        }
    }
});
