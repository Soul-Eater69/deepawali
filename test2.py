<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Deepawali SEO- Website Backlinks Checker</title>
    
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.2/font/bootstrap-icons.css">
    <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.6.1/css/bootstrap-datepicker3.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/purecss@2.1.0/build/pure-min.css" integrity="sha384-yHIFVG6ClnONEA5yB5DJXfW2/KC173DIQrYoZMEtBvGzmf0PKiGyNEqe9N6BNDBH" crossorigin="anonymous">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
</head>
<style>
    @import url('https://fonts.googleapis.com/css2?family=Palanquin+Dark:wght@700&family=Poppins&display=swap');
    
    *{
        font-family: 'Poppins', sans-serif;
    }
    .accordion-item{
        box-shadow: 0 1px 11px 0 rgb(181, 181, 181);
        margin-bottom: 8px;
        padding: 5px;
    }
    .main-wrapper{
        background-color: white;
        display: flex;
        justify-content: center;
        flex-direction: column;
        box-shadow: 0 1px 11px 0 rgb(181, 181, 181);
        overflow: auto;
    }
    .container{
        margin-top: 20px !important ;
        width: 65%;
    }
    .main-wrapper input {
        border: none !important;
        overflow: auto !important;
        outline: none;
        padding: 14px !important;
        -webkit-box-shadow: none;
        -moz-box-shadow: none;
        box-shadow: none;

    }
    .btn-primary{
        background-color: #3b8ffc;
        border: 1px solid #3b8ffc;
    }
    .btn-primary:hover{
        background-color: #4294ff;
        border: 1px solid #4294ff;
    }

    a{
        text-decoration: none;
    }
    .meta-data-container{
        display: flex;
        flex-direction: row;
        flex: 1;
    }
    .meta-data-span{
        padding: 6px;
        margin-right: 5px;
        border: 1px solid white;
        border-radius: 4px;
        box-shadow: 0 1px 11px 0 rgb(181, 181, 181);
    }
    #divToDisplay{
        display: none ;
    }
    .card {
          box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
          transition: 0.3s;
          border-radius: 5px;
          background-color: white;
          position: absolute;
          z-index: 1000;
        }

</style>
<body>

    <div class="main-wrapper" style="overflow: hidden;">
    </div>
    
</body>

<script>
    let flag = false;
    let data;

    const toggleButton = document.getElementsByClassName('toggle-button')[0]
    const navbarLinks = document.getElementsByClassName('navbar-links')[0]
        toggleButton.addEventListener('click', () => {
        navbarLinks.classList.toggle('active')
    })

    function displayCard(element) {
        
          var x = document.getElementById("cardToDisplay");
          console.log(x)
          if (x.style.display === "none") {
            console.log("none")
            x.style.display = "block";
            x.style.top = element.offsetTop + element.offsetHeight + "px";
            x.style.left = element.offsetLeft + "px";
          } else {
            console.log("none gg")
            x.style.display = "none";
          }
        }

    const get_data = async ()=>{
        const url = document.getElementById('url').value;
        
        document.getElementById('load-btn').disabled = true;
        document.getElementById('load-btn').innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>Loading...'
        await fetch("https://deepawali-api-test.up.railway.app/getBrokenlinks", {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                "url":url
            }),
        })
        .then(
            response => response.json()
        )
        .then(response_data=>{
            document.getElementById('load-btn').disabled = false;
            document.getElementById('load-btn').innerHTML = 'Generate'
            data = response_data
            document.getElementById('total_links').innerHTML = 'Total Links : '+data['total_cnt']
            document.getElementById('internal_links').innerHTML = 'Total Links : '+data['internalLinks']
            document.getElementById('external_links').innerHTML = 'Total Links : '+data['externalLinks']
            document.getElementById('dofollow_links').innerHTML = 'Total Links : '+data['do_follow']
            document.getElementById('nofollow_links').innerHTML = 'Total Links : '+data['no_follow']
            set_data(data['urls'])

        }
        )

    }

    const get_response = async (url, status_id, response_id, id) => {

        document.getElementById(status_id).style.display = 'block';
        document.getElementById(id).style.display = 'block';

        const response = fetch("https://plankton-app-5xteo.ondigitalocean.app/getResponseCode",{
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                "url":url
            })})
        .then(
            response => response.json()
        )
         .then(response_data=>{
            if(response_data['response_code']==200){
                document.getElementById(status_id).innerHTML = '<i class="bi bi-check-circle text-success"></i>';
            }
            else{
                document.getElementById(status_id).innerHTML = '<i class="bi bi-x-circle text-warning"></i>';
            }
            //document.getElementById(response_id).innerHTML = response_data['response_code'];
        })

    }


    const set_data = urls => {
        var items_1 = urls.map((ele,idx)=>{
            
            return (`<tr class="d-flex">
                <td class="col-1">${idx+1}</td>
                <td class="col-4" style="overflow-wrap: break-word;"><a href=${ele.url}>${ele.url}</a></td>
                <td class="col-4" style="overflow-wrap: break-word;">${ele.text}</td>
                <td id="${'spinner-status-'+idx+1}" class="col-1">
                    <div class="spinner-border" id="${'spinner-'+idx+1}" role="status">
                        <span class="visually-hidden">Loading...</span>
                    </div>
                </td>
                
                <td class="col-2"><button class="btn" onclick="displayCard(this)">+</button></td>
            </tr>`)
            }).join('')

        document.getElementById('tableExample1').innerHTML = `<tbody>
                <tr class="d-flex">
                    <th scope="col" class="col-1">No.</th>
                    <th scope="col" class="col-4" >URL</th>
                    <th scope='col' class="col-4">Link Text</th>
                    <th scope="col" class="col-1">Status</th>
                    <th scope='col' class="col-2">More</th>
                </tr>
                ${items_1}
            </tbody>`;
        
        set_status(urls)
    }

    const set_status = urls => {
        urls.map((url, idx) => {
            get_response(url['url'],'spinner-status-'+idx+1,'spinner-response-'+idx+1, 'spinner-'+idx+1)
        })
    }

</script>
</html>