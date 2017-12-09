$(document).ready(function(){
 $("#buscador").keyup(function(){
  var i = document.getElementById("buscador").value;
  if (i.length > 2) {
   Dajaxice.tienda.busqueda(encontrados, {'texto': i});   
  } else {
   $("#quebusco").slideUp(300);
  }
 });
 $("#buscador").keypress(function(e){
  if (e.which == 13){
   var i = document.getElementById("buscador").value;
   window.location = "/buscar/" + i;
  }
 });
});
