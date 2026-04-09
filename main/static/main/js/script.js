// Плавная прокрутка для якорей
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Анимация появления элементов при скролле
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

document.querySelectorAll('.character-card, .hashira-card, .feature-card').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(30px)';
    el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(el);
});

// Подсветка активного пункта меню
const currentLocation = window.location.pathname;
const menuItems = document.querySelectorAll('.nav-menu a');

menuItems.forEach(item => {
    if (item.getAttribute('href') === currentLocation) {
        item.style.color = '#ff3366';
    }
});

// Консольное приветствие
console.log('Добро пожаловать в мир Demon Slayer! 🗡️');
console.log('「全集中の呼吸」 - Дзенсю но кокю: Дыхание концентрации');

// Добавим небольшой интерактив на карточки персонажей
document.querySelectorAll('.character-card').forEach(card => {
    card.addEventListener('click', function() {
        const characterName = this.dataset.character;
        console.log(`Вы выбрали персонажа: ${characterName}`);
        
        // Маленькая анимация
        this.style.transform = 'scale(0.95)';
        setTimeout(() => {
            this.style.transform = 'scale(1)';
        }, 200);
    });
});

// Создадим эффект плавающих частиц на фоне (опционально)
function createParticle() {
    const particle = document.createElement('div');
    particle.className = 'particle';
    particle.style.cssText = `
        position: fixed;
        width: 4px;
        height: 4px;
        background: rgba(255, 51, 102, 0.5);
        border-radius: 50%;
        pointer-events: none;
        z-index: 9999;
        left: ${Math.random() * 100}vw;
        top: -10px;
        animation: fall ${5 + Math.random() * 5}s linear forwards;
    `;
    
    document.body.appendChild(particle);
    
    setTimeout(() => {
        particle.remove();
    }, 10000);
}

// Добавим стили для анимации падающих частиц
const style = document.createElement('style');
style.textContent = `
    @keyframes fall {
        to {
            transform: translateY(100vh);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Запускаем создание частиц раз в 500ms
setInterval(createParticle, 500);