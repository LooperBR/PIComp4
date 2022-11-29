autores_ids = []
function AdicionarAutor(){
    id = parseInt(document.getElementById("autores").value)
    console.log(id)
    console.log(autores_ids)
    if(!autores_ids.includes(id)){
        autores_ids.push(id)
    }
    atualizaAutores()
}

function DeletarAutor(id){
    console.log(id)
    const index = autores_ids.indexOf(id);
    console.log(index)
    if (index > -1) { // only splice array when item is found
        autores_ids.splice(index, 1); // 2nd parameter means remove one item only
        atualizaAutores()
    }
}

function atualizaAutores(){
    autores_ids.sort();
    area_autor = document.getElementById("area_autores");
    area_autor.innerHTML = ""
    for (let i = 0; i < autores_ids.length; i++) {
        id = autores_ids[i]
        const xhr = new XMLHttpRequest();
        xhr.open("GET", "/autor/"+id, true);
        xhr.onload = (e) => {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                //console.log(xhr.responseText);
                
                autor = JSON.parse(xhr.responseText)[0]
                area_autor.insertAdjacentHTML("beforeend",
                    "<br/><input type=\"hidden\" id=\"autor["+i+"]\" name=\"autor["+i+"]\" value=\""+autor[0]+"\" readonly>"+autor[1]+"<button type=\"button\" onclick=\"DeletarAutor("+autor[0]+")\">Deletar</button>");
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
}

function Editar(id){
    const xhr = new XMLHttpRequest();
    xhr.open("GET", "/livro/"+id, true);
    xhr.onload = (e) => {
    if (xhr.readyState === 4) {
        if (xhr.status === 200) {
            //console.log(xhr.responseText);
            livro = JSON.parse(xhr.responseText)[0]
            console.log(livro)
            document.getElementById("id").value = livro[0]
            document.getElementById("nome").value = livro[1]
            document.getElementById("edicao").value = livro[2]
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