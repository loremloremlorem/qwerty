const SECTION = [
    {
        id: 1,
        image: './images/section/section-1.png',
        title: 'Choose For Many Fabrics and Textiles materials for your production',
        subtitle: 'We classified it on the basis of material, design and by craft.',
        number: '01'
    },
    {
        id: 2,
        image: './images/section/section-2.png',
        title: 'Create Your Design Only for the Fabric Production and Natural Fabrics',
        subtitle: 'With its rapid growth over the last four decades, since 1970',
        number: '02'
    },
    {
        id: 3,
        image: './images/section/section-3.png',
        title: 'Shoose from various fabric types that are stretchy and comfortable.',
        subtitle: 'Fabiflex is a leading export textile service globally.',
        number: '03'
    }
];

// Контейнер для секций
const sectionBlok = document.getElementById('section-blok');

// Генерация HTML на основе массива SECTION
SECTION.forEach(item => {
    const sectionElement = document.createElement('div');
    sectionElement.classList.add('section-blok__section');
    sectionElement.innerHTML = `
        <div class="section-blok__section__image">
            <img src="${item.image}" alt="${item.title}">
        </div>
        <h2>${item.title}</h2>
        <div class="section-blok__section__footer">
            <p class="section-blok__section__footer__p1">${item.subtitle}</p>
            <p class="section-blok__section__footer__p2">${item.number}</p>
        </div>
    `;
    sectionBlok.appendChild(sectionElement);
});