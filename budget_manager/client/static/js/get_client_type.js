function loadForm(clientType) {
    var formContainer = document.getElementById("form_container");

    fetch(`/client/add/?type=${clientType}`)
        .then(response => {
            if (!response.ok) {
                throw new Error("Erro ao carregar o formulário.");
            }
            return response.text();
        })
        .then(html => {
            formContainer.innerHTML = html;
        })
        .catch(error => {
            console.error("Erro:", error);
        });
}