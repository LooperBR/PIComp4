autores_ids = []
editoras_ids = []
generos_ids = []
function AdicionarAutor(id=-1){
    if(id==-1){
        id = parseInt(document.getElementById("autores").value)
    }
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
                console.log("porraatualiza")
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

function AdicionarEditora(id=-1){
    if(id==-1){
        id = parseInt(document.getElementById("editoras").value)
    }
    console.log(id)
    console.log(editoras_ids)
    if(!editoras_ids.includes(id)){
        editoras_ids.push(id)
    }
    atualizaEditoras()
}

function DeletarEditora(id){
    console.log(id)
    const index = editoras_ids.indexOf(id);
    console.log(index)
    if (index > -1) { // only splice array when item is found
        editoras_ids.splice(index, 1); // 2nd parameter means remove one item only
        atualizaEditoras()
    }
}

function atualizaEditoras(){
    editoras_ids.sort();
    area_editora = document.getElementById("area_editoras");
    area_editora.innerHTML = ""
    console.log('editoras_ids wut')
    console.log(editoras_ids)
    for (let i = 0; i < editoras_ids.length; i++) {
        id = editoras_ids[i]
        console.log('id desgraca')
        console.log(id)
        const xhr = new XMLHttpRequest();
        xhr.open("GET", "/editora/"+id, true);
        xhr.onload = (e) => {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                console.log(xhr.responseText);
                console.log("porraatualiza")
                editora = JSON.parse(xhr.responseText)[0]
                console.log(editora);
                area_editora.insertAdjacentHTML("beforeend",
                    "<br/><input type=\"hidden\" id=\"editora["+i+"]\" name=\"editora["+i+"]\" value=\""+editora[0]+"\" readonly>"+editora[1]+"<button type=\"button\" onclick=\"DeletarEditora("+editora[0]+")\">Deletar</button>");
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

function AdicionarGenero(id=-1){
    if(id==-1){
        id = parseInt(document.getElementById("generos").value)
    }
    console.log(id)
    console.log(generos_ids)
    if(!generos_ids.includes(id)){
        generos_ids.push(id)
    }
    atualizaGeneros()
}

function DeletarGenero(id){
    console.log(id)
    const index = generos_ids.indexOf(id);
    console.log(index)
    if (index > -1) { // only splice array when item is found
        generos_ids.splice(index, 1); // 2nd parameter means remove one item only
        atualizaGeneros()
    }
}

function atualizaGeneros(){
    generos_ids.sort();
    area_genero = document.getElementById("area_generos");
    area_genero.innerHTML = ""
    for (let i = 0; i < generos_ids.length; i++) {
        id = generos_ids[i]
        const xhr = new XMLHttpRequest();
        xhr.open("GET", "/genero/"+id, true);
        xhr.onload = (e) => {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                //console.log(xhr.responseText);
                console.log("porraatualiza")
                genero = JSON.parse(xhr.responseText)[0]
                area_genero.insertAdjacentHTML("beforeend",
                    "<br/><input type=\"hidden\" id=\"genero["+i+"]\" name=\"genero["+i+"]\" value=\""+genero[0]+"\" readonly>"+genero[1]+"<button type=\"button\" onclick=\"DeletarGenero("+genero[0]+")\">Deletar</button>");
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
            console.log(JSON.parse(xhr.responseText))
            livro = JSON.parse(xhr.responseText)[0]
            autores = JSON.parse(xhr.responseText)[1]
            editoras = JSON.parse(xhr.responseText)[2]
            generos = JSON.parse(xhr.responseText)[3]
            console.log(livro)
            console.log(autores)
            document.getElementById("id").value = livro[0]
            document.getElementById("nome").value = livro[1]
            document.getElementById("edicao").value = livro[2]
            
            while(autores_ids.length>0){
                autores_ids.pop()
            }
            while(editoras_ids.length>0){
                editoras_ids.pop()
            }
            while(generos_ids.length>0){
                generos_ids.pop()
            }

            console.log("porra")
            console.log("autores_ids")
            console.log(autores_ids)
            for(let i=0;i<autores.length;i++){
                console.log("porra2")
                autores_ids.push(autores[i][0])
            }
            atualizaAutores()

            for(let i=0;i<editoras.length;i++){
                console.log("porra2")
                editoras_ids.push(editoras[i][0])
            }
            atualizaEditoras()

            for(let i=0;i<generos.length;i++){
                console.log("porra2")
                generos_ids.push(generos[i][0])
            }
            atualizaGeneros()

            console.log(autores_ids)
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