const btn = document.getElementById('colorModeButton');
const svgBtn = document.getElementById('svgBtn')
const title = document.getElementById('title');
const subTitle = document.getElementById('subTitle');
const text = document.getElementById('text');
const corners = document.querySelectorAll('.corner');

let isDarkMode = true;

function toggleMode() {
  if (isDarkMode) {
    // Switch to light mode
    title.style.color = 'var(--accentLight)';
    subTitle.style.color = 'var(--accentLight)';
		document.body.style.backgroundImage = 'var(--backgroundLight)';
		text.style.color = 'var(--mainDark)';
    svgBtn.setAttribute('fill', 'var(--mainDark');
		corners.forEach(corner => {
			corner.style.borderColor = 'var(--mainDark)';
		});
  } else {
    // Switch to dark mode
    title.style.color = 'var(--accentDark)';
    subTitle.style.color = 'var(--accentDark)';
		document.body.style.backgroundImage = 'var(--backgroundDark)';
		text.style.color = 'var(--mid)';
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