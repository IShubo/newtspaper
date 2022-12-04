// Variables
const business = document.getElementById("business");
const general = document.getElementById("general");
const science = document.getElementById("general");
const sports = document.getElementById("general");
const technology = document.getElementById("general");
const search = document.getElementById("search");

const newsQuery = document.getElementById("newsQuery");
const newsType = document.getElementById("newsType");
const newsDetails = document.getElementById("newsDetails");

// Arrays
var newsArray = [];


// API
// API KEY: c467c532f88e46ddb2e6b2d6d4545cf5
const API_KEY = "c467c532f88e46ddb2e6b2d6d4545cf5";

// CORS Proxy
const corsAnywhereURL = 'https://cors-anywhere.herokuapp.com/';

const BUSINESS_NEWS = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=";
const HEADLINES_NEWS = "https://newsapi.org/v2/top-headlines?country=us&apiKey="
const GENERAL_NEWS = "https://newsapi.org/v2/top-headlines?country=us&category=general&apiKey=";
const SCIENCE_NEWS = "https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey=";
const SPORTS_NEWS = "https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=";
const TECHNOLOGY_NEWS = "https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=";
const SEARCH_NEWS = "https://newsapi.org/v2/everything?q=";

window.onload = function () {
    newsType.innerHTML = "<h4>Headlines</h4>";
    fetchHeadlines();
};


business.addEventListener("click", function() {
    newsType.innerHTML = "<h4>Business</h4>";
    fetchBusinessNews();
});
general.addEventListener("click", function() {
    newsType.innerHTML = "<h4>General News</h4>";
    fetchGeneralNews();
});
science.addEventListener("click", function() {
    newsType.innerHTML = "<h4>Science</h4>";
    fetchScienceNews();
});
sports.addEventListener("click", function() {
    newsType.innerHTML = "<h4>Sports</h4>";
    fetchSportsNews();
});
technology.addEventListener("click", function() {
    newsType.innerHTML = "<h4>Technology</h4>";
    fetchTechnologyNews();
});
search.addEventListener("click", function() {
    newsType.innerHTML = "<h4>Search :" + newsQuery.value + "</h4>";
    fetchQueryNews();
});


const fetchBusinessNews = async () => {
    const response = await fetch(corsAnywhereURL + BUSINESS_NEWS+API_KEY, {
        headers: {
            'Origin' : 'localhost',
        }
    });
    newsArray = [];
    if (response.status >= 200 && response.status < 300) {
        const genJson = await response.json();
        console.log(genJson);
        newsArray = genJson.articles;
    } else {
        // Handle errors
        console.log(response.status + response.statusText);
    }
    displayNews();
}

const fetchGeneralNews = async () => {
    const response = await fetch(corsAnywhereURL + GENERAL_NEWS+API_KEY);
    newsArray = [];
    if (response.status >= 200 && response.status < 300) {
        const genJson = await response.json();
        newsArray = genJson.articles;
    } else {
        // Handle errors
        console.log(response.status + response.statusText);
    }
    displayNews();
}

const fetchHeadlines = async () => {
    const response = await fetch(corsAnywhereURL + HEADLINES_NEWS+API_KEY);
    newsArray = [];
    if (response.status >= 200 && response.status < 300) {
        const genJson = await response.json();
        newsArray = genJson.articles;
    } else {
        // Handle errors
        console.log(response.status + response.statusText + "Hello, World");
    }
    displayNews();
}

const fetchScienceNews = async () => {
    const response = await fetch(corsAnywhereURL + SCIENCE_NEWS+API_KEY);
    newsArray = [];
    if (response.status >= 200 && response.status < 300) {
        const genJson = await response.json();
        newsArray = genJson.articles;
    } else {
        // Handle errors
        console.log(response.status + response.statusText);
    }
    displayNews();
}

const fetchSportsNews = async () => {
    const response = await fetch(corsAnywhereURL + SPORTS_NEWS+API_KEY);
    newsArray = [];
    if (response.status >= 200 && response.status < 300) {
        const genJson = await response.json();
        newsArray = genJson.articles;
    } else {
        // Handle errors
        console.log(response.status + response.statusText);
    }
    displayNews();
}

const fetchTechnologyNews = async () => {
    const response = await fetch(corsAnywhereURL + TECHNOLOGY_NEWS+API_KEY);
    newsArray = [];
    if (response.status >= 200 && response.status < 300) {
        const genJson = await response.json();
        newsArray = genJson.articles;
    } else {
        // Handle errors
        console.log(response.status + response.statusText);
    }
    displayNews();
}

const fetchQueryNews = async () => {
    if (newsQuery.value == null)
        return;

    const response = await fetch(corsAnywhereURL + SEARCH_NEWS + encodeURIComponent(newsQuery.value) + "&apiKey=" + API_KEY);
    newsArray = [];
    if (response.status >= 200 && response.status < 300) {
        const genJson = await response.json();
        newsArray = genJson.articles;
    } else {
        // Handle errors
        console.log(response.status + response.statusText);
    }
    displayNews();
}

function displayNews() {
    newsDetails.innerHTML = "";

    if (newsArray.length === 0) {
        newsDetails.innerHTML = "<h5>No data found.</h5>";
        return;
    }

    newsArray.forEach(news => {

        var date = news.publishedAt.split("T");

        var col = document.createElement('div');
        col.className = "card col-sm-12 col-md-4 col-lg-3 p-2";

        var card = document.createElement('div');
        card.className = "p-2"

        var image = document.createElement('img');
        image.setAttribute("height", "matchparent");
        image.setAttribute("width", "100%");
        image.src = news.urlToImage;

        var cardBody = document.createElement('div');

        var newsHeading = document.createElement('h5');
        newsHeading.className = "card-title";
        newsHeading.innerHTML = news.title;

        var dateHeading = document.createElement('h6');
        dateHeading.className = "text-primary";
        dateHeading.innerHTML = date[0];

        var description = document.createElement('p');
        description.className = "text-muted";
        description.innerHTML = news.description;

        var link = document.createElement('a');
        link.className = "btn btn-dark";
        link.setAttribute("target", "_blank");
        link.href = news.url;
        link.innerHTML = "Read more";

        cardBody.appendChild(newsHeading);
        cardBody.appendChild(dateHeading);
        cardBody.appendChild(description);
        cardBody.appendChild(link);

        card.appendChild(image);
        card.appendChild(cardBody);

        col.appendChild(card);

        newsDetails.appendChild(col);
    });
}