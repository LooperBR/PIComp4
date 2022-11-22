function Editar(id){
    const xhr = new XMLHttpRequest();
    xhr.open("GET", "/editora/"+id, true);
    xhr.onload = (e) => {
    if (xhr.readyState === 4) {
        if (xhr.status === 200) {
            //console.log(xhr.responseText);
            editora = JSON.parse(xhr.responseText)[0]
            console.log(editora)
            document.getElementById("id").value = editora[0]
            document.getElementById("nome").value = editora[1]
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
    return true;
}