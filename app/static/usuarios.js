function Editar(id){
    const xhr = new XMLHttpRequest();
    xhr.open("GET", "/usuario/"+id, true);
    xhr.onload = (e) => {
    if (xhr.readyState === 4) {
        if (xhr.status === 200) {
            //console.log(xhr.responseText);
            usuario = JSON.parse(xhr.responseText)[0]
            //console.log(usuario)
            document.getElementById("id").value = usuario[0]
            document.getElementById("login").value = usuario[1]
            document.getElementById("senha").value = usuario[2]
            document.getElementById("nome").value = usuario[3]
            document.getElementById("cpf").value = usuario[4]
            document.getElementById("bairro").value = usuario[5]
            document.getElementById("rua").value = usuario[6]
            document.getElementById("numero").value = usuario[7]
            document.getElementById("cidade").value = usuario[8]
            document.getElementById("estado").value = usuario[9]
            document.getElementById("data_nascimento").value = usuario[10]
            console.log(usuario[11]==1?true:false)
            console.log(usuario[11])
            document.getElementById("bibliotecario").checked = usuario[11]
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