function calcular(){
    let nome = (document.getElementById("nome").value);
    let nota1 = (document.getElementById("nota1").value);
    let nota2 = (document.getElementById("nota2").value);
    let nota3 = (document.getElementById("nota3").value);
    let resultado = document.getElementById("resultado");
    
    if (nome =="" || nota1 ==="" || nota2 ==="" || nota3 ===""){
    resultado.innerHTML = "Por favor preencha todos os campos!";
    return;
    }
    
    nota1 = parseFloat(nota1)
    nota2 = parseFloat(nota2)
    nota3 = parseFloat(nota3)

    let media = (nota1 + nota2 + nota3 /3)
    resultado.innerHTML = nome + ", sua media é: " + media.toFixed(3);
    }