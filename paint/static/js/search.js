function view (data){   
    var canvas = document.getElementById("paint");    
    var ctx = canvas.getContext("2d");    
    var newImg = document.createElement("img");
    newImg.src = data;
    document.body.appendChild(newImg);    
}
