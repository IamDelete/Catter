const btn = document.getElementById('colorModeButton');
const svgBtn = document.getElementById('svgBtn')
const title = document.getElementById('title');
const subTitle = document.getElementById('subTitle');
const texts = document.querySelectorAll('.text');
const corners = document.querySelectorAll('.corner');
const header = document.querySelector('header');

let isDarkMode = true;

function toggleMode() {
  if (isDarkMode) {
    // Switch to light mode
    title.style.color = 'var(--accentLight)';
    subTitle.style.color = 'var(--accentLight)';
		header.style.backgroundImage = 'var(--backgroundLight)';
		texts.forEach(text => {
      text.style.color = 'var(--mid)';
    });
    svgBtn.setAttribute('fill', 'var(--mainDark');
		corners.forEach(corner => {
			corner.style.borderColor = 'var(--mainDark)';
		});
  } else {
    // Switch to dark mode
    title.style.color = 'var(--accentDark)';
    subTitle.style.color = 'var(--accentDark)';
		header.style.backgroundImage = 'var(--backgroundDark)';
		texts.forEach(text => {
      text.style.color = 'var(--mid)';
    });
    svgBtn.setAttribute('fill', 'var(--mainLight');
		corners.forEach(corner => {
			corner.style.borderColor = 'var(--mainLight)';
		});
  }
  isDarkMode = !isDarkMode; // Toggle the mode
}

btn.addEventListener('click', toggleMode);

function colorAnimation() {
  svgBtn.classList.add = 'colorAnimation';
}