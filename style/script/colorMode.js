const btn = document.getElementById('colorModeButton');
const title = document.getElementById('title');
const subTitle = document.getElementById('subTitle');
const text = document.getElementById('text');
const corners = document.querySelectorAll('.corner');

let isDarkMode = false;

function toggleMode() {
  if (isDarkMode) {
    // Switch to light mode
    title.style.color = 'var(--accentLight)';
    subTitle.style.color = 'var(--accentLight)';
		document.body.style.backgroundImage = 'var(--backgroundLight)';
		text.style.color = 'var(--mainDark)';
		corners.forEach(corner => {
			corner.style.borderColor = 'var(--mainDark)';
		});
  } else {
    // Switch to dark mode
    title.style.color = 'var(--accentDark)';
    subTitle.style.color = 'var(--accentDark)';
		document.body.style.backgroundImage = 'var(--backgroundDark)';
		text.style.color = 'var(--mid)';
		corners.forEach(corner => {
			corner.style.borderColor = 'var(--mainLight)';
		});
  }
  isDarkMode = !isDarkMode; // Toggle the mode
}

btn.addEventListener('click', toggleMode);
