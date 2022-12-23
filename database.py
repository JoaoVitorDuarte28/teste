import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = '10.100.100.5' 
database = 'dbSicred_Proj' 
username = 'usr_sicred' 
password = '#Homologsicr3d#' 
# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)
conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD=password')
cursor = conn.cursor()

#Sample select query
cursor.execute("select * from PROPOSTASHISTORICO where proposta = 8557139;") 
row = cursor.fetchone() 
while row: 
    print(row[0])
    row = cursor.fetchone()

















    function fazPost(url) {
    let request = new XMLHttpRequest()
    request.open("PUT", url, true)

    request.send(url)

    request.onload = function() {
        console.log(this.responseText)
        alert(this.responseText)
    }

}


function cadastraUsuario() {
    event.preventDefault()
    let proposta = document.getElementById("proposta").value
    let situacao = document.getElementById("situacao").value
    let url = "http://localhost:8000/alterar/Status?numeroProposta=" + proposta + "&numeroSituacao=" + situacao + ""
    
   
    console.log(proposta)
    console.log(situacao)
    fazPost(url)

}

