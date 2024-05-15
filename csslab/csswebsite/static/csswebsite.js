function searchVideoGameGenre(){
	var genre = document.getElementById("Genre").value;
  
  var compiledLink = "/" + genre + "/" + "rand";
  
  window.location.href = compiledLink;
}