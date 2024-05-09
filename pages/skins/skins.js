// Função para carregar arquivo de texto
function carregarArquivo(url, callback) {
    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            callback(xhr.responseText);
        }
    };
    xhr.open("GET", url, true);
    xhr.send();
}

// Função para baixar arquivos de uma pasta
function baixarArquivosDoCampeao(nomeCampeao) {
    // Criar um link de download para o arquivo ZIP
    const link = document.createElement('a');
    link.href = `../../skins/${nomeCampeao}.zip`;
    link.download = `${nomeCampeao}.zip`;
    link.style.display = 'none';
    
    // Adicionar o link à página e simular o clique para iniciar o download
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}


// Função para criar divs com os nomes dos campeões e adicionar evento de clique
function criarDivsComNomes(nomes) {
    const container = document.querySelector('.champ-select-container');
    const nomesArray = nomes.split(','); // Divide os nomes separados por vírgula em um array

    for (let i = 0; i < nomesArray.length; i++) {
        const nome = nomesArray[i].trim();
        const div = document.createElement('div');
        div.className = 'champ';
        div.id = `champ-${i + 1}`;
        const img = document.createElement('img');
        img.src = `../../assets/champs-icons/${nome}.png`;
        img.alt = 'image';
        img.className = 'champ-icon';
        const span = document.createElement('span');
        span.textContent = nome;
        span.className = 'champ-name';
        div.appendChild(img);
        div.appendChild(span);
        container.appendChild(div);

        // Adicionar evento de clique para cada div criada
        div.addEventListener('click', function() {
            baixarArquivosDoCampeao(nome);
        });
    }
}

// Carregar arquivo champions-names.txt e chamar a função criarDivsComNomes quando estiver carregado
carregarArquivo('../../assets/champions-names.txt', criarDivsComNomes);
