function searchVideoGameGenre(){
	var genre = document.getElementById("Genre").value;
  
  var compiledLink = "/" + genre;
  
  window.location.href = compiledLink;
}