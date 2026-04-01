async function carregarDados() {

    const resposta = await fetch("http://127.0.0.1:8000/dados");
    const dados = await resposta.json();

    document.getElementById("nome").textContent = dados.nome;
    document.getElementById("titulo").textContent = dados.titulo;
    document.getElementById("sobre").textContent = dados.sobre;
    document.getElementById("escolaridade").textContent = dados.escolaridade;
    document.getElementById("contato").textContent = dados.contato;

    document.getElementById("foto").src = dados.foto;

    const lista = document.getElementById("lista-projetos");

    dados.projetos.forEach(projeto => {
        const li = document.createElement("li");
        li.textContent = projeto;
        lista.appendChild(li);
    });
}

window.onload = carregarDados;