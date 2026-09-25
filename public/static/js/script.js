/* ===========================
   Mobile Menu
=========================== */

const menuBtn = document.getElementById("menu-btn");
const mobileMenu = document.getElementById("mobile-menu");

if (menuBtn) {
  menuBtn.addEventListener("click", () => {
    mobileMenu.classList.toggle("hidden");
  });
}

/* ===========================
   Typing Animation
=========================== */

const words = [
  "Python Developer",
  "Django Developer",
  "AI Enthusiast",
  "Full Stack Learner",
];

const typing = document.getElementById("typing-text");

let index = 0;

if (typing) {
  setInterval(() => {
    typing.style.opacity = "0";

    setTimeout(() => {
      index = (index + 1) % words.length;
      typing.textContent = words[index];
      typing.style.opacity = "1";
    }, 250);
  }, 2300);
}

/* ===========================
   Navbar Scroll Effect
=========================== */

const navbar = document.getElementById("navbar");

window.addEventListener("scroll", () => {
  if (!navbar) return;

  if (window.scrollY > 30) {
    navbar.classList.add("shadow-2xl");
    navbar.classList.remove("border-slate-700");
    navbar.classList.add("border-cyan-500/30");
  } else {
    navbar.classList.remove("shadow-2xl");
    navbar.classList.add("border-slate-700");
    navbar.classList.remove("border-cyan-500/30");
  }
});

/* ===========================
   Scroll Reveal Animation
=========================== */

const revealElements = document.querySelectorAll(".reveal");

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.remove("opacity-0", "translate-y-10");
        entry.target.classList.add("opacity-100", "translate-y-0");
      }
    });
  },
  {
    threshold: 0.15,
  },
);

revealElements.forEach((el) => {
  el.classList.add("opacity-0", "translate-y-10", "transition", "duration-700");

  observer.observe(el);
});

const carousel = document.getElementById("projectCarousel");
const prev = document.getElementById("prevProject");
const next = document.getElementById("nextProject");

if (carousel) {
  const cards = [...carousel.querySelectorAll(".project-card")];
  let current = 2;

  function updateCards() {
    cards.forEach((c) => c.classList.remove("active-card"));
    cards[current].classList.add("active-card");

    const activeCard = cards[current];
    const viewport = carousel.parentElement;

    const translate =
      viewport.clientWidth / 2 -
      (activeCard.offsetLeft + activeCard.offsetWidth / 2);

    carousel.style.transform = `translateX(${translate}px)`;
  }

  next.onclick = () => {
    current = (current + 1) % cards.length;
    updateCards();
  };

  prev.onclick = () => {
    current = (current - 1 + cards.length) % cards.length;
    updateCards();
  };

  window.addEventListener("resize", updateCards);
  updateCards();
}

updateCards();
