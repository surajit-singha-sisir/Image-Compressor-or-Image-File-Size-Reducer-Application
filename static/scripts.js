
const fileUpload = document.querySelector('#file-upload');
const fileName = document.querySelector('.file-name');

fileUpload.addEventListener('change', (e) => {
  const file = e.target.files[0];
  if (file) {
    fileName.textContent = file.name;
    fileName.style.display = 'block';
    fileUpload.style.display = 'none';
  }
});

const rangeInput = document.querySelector('input[type="range"]');
const rangeValue = document.querySelector('.range-value');

rangeInput.addEventListener('input', () => {
  rangeValue.textContent = rangeInput.value + '%';
});
