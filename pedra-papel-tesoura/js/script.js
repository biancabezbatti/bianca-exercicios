const opcoes = ["pedra", "papel", "tesoura"]

let pontosJogador = 0
let pontosPc = 0

const imagens = {
    pedra: "img/pedra.png",
    papel: "img/papel.png",
    tesoura: "img/tesoura.png"
}

function jogar(escolhaJogador){

    const pos = Math.floor(Math.random() * 3)
    const escolhaPc = opcoes[pos]

    // mostrar imagens
    document.getElementById("imgJogador").src = imagens[escolhaJogador]
    document.getElementById("imgPc").src = imagens[escolhaPc]

    let mensagem = ""

    if(escolhaJogador === escolhaPc){
        mensagem = "Empate 😐"
    }
    else if(
        (escolhaJogador === "pedra" && escolhaPc === "tesoura") ||
        (escolhaJogador === "tesoura" && escolhaPc === "papel") ||
        (escolhaJogador === "papel" && escolhaPc === "pedra")
    ){
        mensagem = "Você venceu 😎"
        pontosJogador++
    }
    
    else{
        mensagem = "Computador venceu 🤖"
        pontosPc++
    }
    if(pontosJogador === 10){
        alert("🎉 Você ganhou o jogo!")
        pontosJogador = 0
        pontosPc = 0
    }
    else if(pontosPc === 10){
        alert("🤖 Computador ganhou o jogo!")
        pontosJogador = 0
        pontosPc = 0
    }
    
    // atualizar placar após reset
    document.getElementById("pontosJogador").innerText = pontosJogador
    document.getElementById("pontosPc").innerText = pontosPc

    document.getElementById("mensagem").innerText = mensagem

    // atualizar pontuação
    document.getElementById("pontosJogador").innerText = pontosJogador
    document.getElementById("pontosPc").innerText = pontosPc
}