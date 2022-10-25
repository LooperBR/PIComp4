document.onkeydown = checkKey;
let pegouKonami=false
let konamiArray = []
let konamiCertoArray = ["up","up","down","down","left","right","left","right","b","a"]
function checkKey(e) {

    konami = document.getElementById("konami");
    
    e = e || window.event;
    console.log(e.keyCode)
    if (e.keyCode == '38') {
        // up arrow
        konamiArray.push("up");
    }else if (e.keyCode == '40') {
        // down arrow
        konamiArray.push("down");
    }else if (e.keyCode == '37') {
       // left arrow
       konamiArray.push("left");
    }else if (e.keyCode == '39') {
       // right arrow
       konamiArray.push("right");
    }else if (e.keyCode == '65') {
        // right arrow
        konamiArray.push("a");
    }else if (e.keyCode == '66') {
        // right arrow
        konamiArray.push("b");
    }
    if(konamiArray.length>10){
        konamiArray.shift()
    }
    if(konamiArray.length === konamiCertoArray.length && konamiArray.every((value, index) => value === konamiCertoArray[index])){
        pegouKonami = true
    }

    if(pegouKonami){
        konami.innerHTML = "tu é o bixão memo"
    }else{
        konami.innerHTML = konamiArray
    }

}