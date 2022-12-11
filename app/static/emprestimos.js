function Editar(id){
    const xhr = new XMLHttpRequest();
    xhr.open("GET", "/emprestimo/"+id, true);
    xhr.onload = (e) => {
    if (xhr.readyState === 4) {
        if (xhr.status === 200) {
            //console.log(xhr.responseText);
            emprestimo = JSON.parse(xhr.responseText)[0]
            console.log(emprestimo)

            data_emprestimo = new Date(emprestimo[2])
            data_devolucao = new Date(emprestimo[3])
            data_estimada_devolucao = new Date(emprestimo[4])

            document.getElementById("id").value = emprestimo[0]
            document.getElementById("devolvido").checked = emprestimo[1]
            document.getElementById("data_emprestimo").value = data_emprestimo.toISOString().substring(0,10)
            document.getElementById("data_devolucao").value = data_devolucao.toISOString().substring(0,10)
            document.getElementById("data_estimada_devolucao").value = data_estimada_devolucao.toISOString().substring(0,10)
            document.getElementById("bibliotecario").value = emprestimo[5]
            document.getElementById("cliente").value = emprestimo[6]
            document.getElementById("livro").value = emprestimo[7]
        } else {
            console.error(xhr.statusText);
        }
    }
    };
    xhr.onerror = (e) => {
    console.error(xhr.statusText);
    };
    xhr.send(null);
}

function validateForm(){
    livro = document.getElementById("livro")
    livro.options[livro.selectedIndex].disabled = false
    return true;
}