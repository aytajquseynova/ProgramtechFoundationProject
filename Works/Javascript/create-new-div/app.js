 var panelDiv=document.querySelector("#panel");
            var btn=document.querySelector("#elaveet");
    
            
            btn.onclick=function(){
                var etiket=document.createElement("div"); 
              
                etiket.classList="box"; 
                panelDiv.appendChild(etiket);
            }   