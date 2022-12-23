function fazPost(url) {
    let request = new XMLHttpRequest()
    request.open("PUT", url, true)
    request.send(url)

    request.onload = function() {
        console.log(this.responseText)
        alert("Proposta alterada Com suscessso!")
    }
}

function cadastraUsuario() {
    event.preventDefault()
    let proposta = document.getElementById("proposta").value
    let situacao = document.getElementById("situacao").value
    let url = "http://localhost:8000/alterar/Status?numeroProposta=" + proposta + "&numeroSituacao=" + situacao + ""
    console.log(proposta)
    fazPost(url)

}