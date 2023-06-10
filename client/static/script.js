function getMovies() {
    var username = document.getElementById("usernameInput").value;
    var url = "http://127.0.0.1:8000/recommend-movies/" + username;
    var outputArea = document.getElementById("outputArea");
  
    fetch(url)
      .then(response => response.json())
      .then(data => {
        var titles = data.titles;
        var moviesList = titles.map(title => "<li>" + title + "</li>").join("");
        outputArea.innerHTML = "<ul>" + moviesList + "</ul>";
      })
      .catch(error => {
        outputArea.innerHTML = "Error occurred while fetching movies." + error;
      });
  }
  