function validaCampo() {

    let nome = document.getElementById("campoNome").value.trim();
    let email = document.getElementById("campoEmail").value.trim();
    let erro = document.getElementById("erro");

    erro.innerHTML = "";

    if (nome === "" || email === "") {
        erro.innerHTML = "Preencha todos os campos!";
        return false;
    }

    return true;
}
