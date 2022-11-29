function Editar(id){
    const xhr = new XMLHttpRequest();
    xhr.open("GET", "/autor/"+id, true);
    xhr.onload = (e) => {
    if (xhr.readyState === 4) {
        if (xhr.status === 200) {
            //console.log(xhr.responseText);
            autor = JSON.parse(xhr.responseText)[0]
            console.log(autor)
            document.getElementById("id").value = autor[0]
            document.getElementById("nome").value = autor[1]
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