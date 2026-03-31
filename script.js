let aberto = false;

async function carregarProjetos() {
    const lista = document.getElementById("lista-projetos");

    // Se já estiver aberto → FECHA
    if (aberto) {
        lista.innerHTML = "";
        aberto = false;
        return;
    }

    // Se estiver fechado → ABRE
    try {
        const resposta = await fetch("http://127.0.0.1:8000/projetos");
        const projetos = await resposta.json();

        lista.innerHTML = "";

        projetos.forEach(p => {
            const li = document.createElement("li");
            li.textContent = p;
            lista.appendChild(li);
        });

        aberto = true;

    } catch (erro) {
        alert("Erro ao carregar projetos 😢");
        console.log(erro);
    }
}