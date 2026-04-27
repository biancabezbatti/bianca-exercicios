function contar() {
    let inicio = parseInt(document.getElementById("inicio").value);
    let fim = parseInt(document.getElementById("fim").value);
    let resultado = document.getElementById("resultado");
    
    if (isNaN(inicio) || isNaN(fim)) {
    resultado.innerHTML = "Digite valores válidos!";
    return;
    }
    
    if (inicio > fim) {
    resultado.innerHTML = "Erro: início maior que o fim!";
    return;
    }
    
    let i = inicio;
    let numeros = "";
    
    while (i <= fim) {
    numeros += i + " ";
    i++;
    }
    
    resultado.innerHTML = numeros;
    }