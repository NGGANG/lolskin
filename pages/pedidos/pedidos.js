// Obtém os botões e os elementos que você deseja modificar
const skinsButton = document.querySelector('.btn-mark:nth-of-type(1)');
const chromasButton = document.querySelector('.btn-mark:nth-of-type(2)');
const fixButton = document.querySelector('.btn-mark:nth-of-type(3)');
const helpButton = document.querySelector('.btn-mark:nth-of-type(4)');
const skinsSelector = document.querySelector('.skins-selector');
const chromaSelector = document.querySelector('.chroma-selector');
const fixSelector = document.querySelector('.fix-selector');
const helpSelector = document.querySelector('.help-selector');
const skinInput = document.querySelector('.skin-input');
const confirmButton = document.querySelector('.confirm-button');


// Adiciona ouvintes de eventos para os botões
skinsButton.addEventListener('click', () => {
    skinsSelector.style.display = 'flex';
    chromaSelector.style.display = 'none';
    fixSelector.style.display = 'none';
    helpSelector.style.display = 'none';
    confirmButton.style.display = 'block';
    skinInput.style.display = 'block'; // Mostra o input apenas para "Skins"
    skinInput.placeholder = 'Skins';
});

chromasButton.addEventListener('click', () => {
    skinsSelector.style.display = 'none';
    chromaSelector.style.display = 'flex';
    fixSelector.style.display = 'none';
    helpSelector.style.display = 'none';
    confirmButton.style.display = 'block';  
    skinInput.style.display = 'block'; // Esconde o input para "Chromas"
    skinInput.placeholder = 'Chromas';
});

fixButton.addEventListener('click', () => {
    skinsSelector.style.display = 'none';
    chromaSelector.style.display = 'none';
    fixSelector.style.display = 'flex';
    helpSelector.style.display = 'none';
    confirmButton.style.display = 'none';
    skinInput.style.display = 'none'; // Esconde o input para "Fix"
});

helpButton.addEventListener('click', () => {
    skinsSelector.style.display = 'none';
    chromaSelector.style.display = 'none';
    fixSelector.style.display = 'none';
    helpSelector.style.display = 'flex';
    confirmButton.style.display = 'none';
    skinInput.style.display = 'none'; // Esconde o input para "Help"
});
