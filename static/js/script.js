// Carousel
$('#carouselCard').carousel({
    interval: 3000,
    cycle: true
})

// Openweathermap API.Do not share it publicly.
const api = 'cd9f16a1cf970e249d3a215852039f5f'; //Replace with your API

const iconImg = document.getElementById('weather-icon');
const loc = document.querySelector('#location');
const tempC = document.querySelector('.c');
const desc = document.querySelector('.desc');
const lon1 = document.getElementById('lastLon');
const lat1 = document.getElementById('lastLat')
    // const lonlat = document.getElementById('lastLat')
    // Using fetch to get dataffffffffff    
window.addEventListener('load', () => {
    const base = `https://api.openweathermap.org/data/2.5/weather?lat=-6.191832&lon=106.891515&appid=${api}&units=metric`;
    fetch(base)
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            const { temp } = data.main;
            const place = data.name;
            const { description, icon } = data.weather[0];
            const { sunrise, sunset } = data.sys;
            const { lon, lat } = data.coord;

            const iconUrl = `http://openweathermap.org/img/wn/${icon}@2x.png`;
            const fahrenheit = (temp * 9) / 5 + 32;

            // Converting Epoch(Unix) time to GMT
            const sunriseGMT = new Date(sunrise * 1000);
            const sunsetGMT = new Date(sunset * 1000);

            // Interacting with DOM to show data
            iconImg.src = iconUrl;
            loc.textContent = `${place}`;
            desc.textContent = `${description}`;
            tempC.textContent = `${temp.toFixed(2)} °C`;
            lon1.textContent = `${lon}`
            lat1.textContent = `${lat}`
        });
})

// Connection
var ifConnected = window.navigator.onLine;
if (ifConnected) {
    document.getElementById("checkOnline").innerHTML = "●Online";
    document.getElementById("checkOnline").style.color = "green";
} else {
    document.getElementById("checkOnline").innerHTML = "Offline";
    document.getElementById("checkOnline").style.color = "red";
}
setInterval(function() {
    var ifConnected = window.navigator.onLine;
    if (ifConnected) {
        document.getElementById("checkOnline").innerHTML = "●Online";
        document.getElementById("checkOnline").style.color = "green";
    } else {
        document.getElementById("checkOnline").innerHTML = "●Offline";
        document.getElementById("checkOnline").style.color = "red";
    }
}, 1000);


// Subs
const subC = document.getElementById('subCount')
const vidC = document.getElementById('vidCount')
const avgF = document.getElementById('avgViews')
window.addEventListener('load', () => {
    const url = `https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UC4DogC2xftpKFlF-XgZoRBg&key=AIzaSyARZmUksoAchDmAng0vuTJqlmYz7QEwTp8`;
    fetch(url)
        .then((response) => {
            // response.status === 403 ? alert("Error: " + response.status) : null
            // console.log(response)
            return response.json();
        })
        .then((data) => {
            const { subscriberCount } = data.items[0].statistics;
            subFormat = new Intl.NumberFormat().format(subscriberCount)
            subC.textContent = `${subFormat}`

            const { videoCount } = data.items[0].statistics;
            vidFormat = new Intl.NumberFormat().format(videoCount)
            vidC.textContent = `${vidFormat}` + " Videos";

            const { viewCount } = data.items[0].statistics;
            viewFormat = new Intl.NumberFormat().format(viewCount)

            avgLike = viewCount / videoCount;
            avgFormat = new Intl.NumberFormat().format(avgLike)
            avgF.textContent = `${avgFormat}`
                // console.log(avgFormat)

        })
})


const videoL = document.getElementById('videoLast')
const dateV = document.getElementById('dateVideo')
const imgT = document.getElementById('thumbnail');
const videoI = document.getElementById('lastVideoUpload')
    // const videoI = document.getElementById("lastVidId").getAttribute("youtubeid")
window.addEventListener('load', () => {
    const url = `https://www.googleapis.com/youtube/v3/search?order=date&part=snippet&channelId=UC4DogC2xftpKFlF-XgZoRBg&maxResults=5&key=AIzaSyARZmUksoAchDmAng0vuTJqlmYz7QEwTp8`;
    fetch(url)
        .then((response) => {
            return response.json();
        })
        .then((data) => { 
            const { videoId } = data.items[0].id;
            const { url } = data.items[0].snippet.thumbnails.high;
            const { title } = data.items[0].snippet;
            const { publishTime } = data.items[0].snippet;
            latestVideo = videoId + title + ":" + url + " | " + publishTime;
            const mySplit = publishTime.split("T")
                // console.log(mySplit[0])
            videoL.textContent = `${title}`
            dateV.textContent = `${mySplit[0]}`
            videoI.src = "//www.youtube.com/embed/" + `${videoId}`
            imgT.src = `${url}`
            console.log(videoI)
        })
})

urlData = `https://www.googleapis.com/youtube/v3/videos?part=contentDetails&chart=mostPopular&regionCode=ID&key=AIzaSyClRFMjeiOt1rvZlIzrmQ-B0OQ5BOo4kTk`
getVideoData = `https://www.googleapis.com/youtube/v3/search?order=date&part=snippet&channelId=UC4DogC2xftpKFlF-XgZoRBg&maxResults=5&key=AIzaSyClRFMjeiOt1rvZlIzrmQ-B0OQ5BOo4kTk`

/* Legacy code below: getUserMedia 
else if(navigator.getUserMedia) { // Standard
    navigator.getUserMedia({ video: true }, function(stream) {
        video.src = stream;
        video.play();
    }, errBack);
} else if(navigator.webkitGetUserMedia) { // WebKit-prefixed
    navigator.webkitGetUserMedia({ video: true }, function(stream){
        video.src = window.webkitURL.createObjectURL(stream);
        video.play();
    }, errBack);
} else if(navigator.mozGetUserMedia) { // Mozilla-prefixed
    navigator.mozGetUserMedia({ video: true }, function(stream){
        video.srcObject = stream;
        video.play();
    }, errBack);
}
*/

// var video = document.querySelector("#videoElement");

// if (navigator.mediaDevices.getUserMedia) {
//     navigator.mediaDevices.getUserMedia({ video: true })
//         .then(function(stream) {
//             video.srcObject = stream;
//         })
//         .catch(function(err0r) {
//             console.log("Something went wrong!");
//         });
// }


// Analytics
function youtubeAnalytics() {
    console.log("Youtube")
}

// Date object
var date = new Date();
const elementDate = document.getElementById("printDate");
const elementDay = document.getElementById("printDay");
const elementTime = document.getElementById("printTime");
const listOfDays = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
];

function printDate() {
    var day = date.getDate();
    var month = date.getMonth();
    var year = date.getFullYear();

    elementDate.innerHTML = day + " / " + month + " / " + year + " |";
}

function printDay() {
    date = new Date();
    var numberOfDay = date.getDay();
    var day = listOfDays[numberOfDay];
    elementDay.innerHTML = day + ",";
}

function printTime() {
    date = new Date();
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var seconds = date.getSeconds();

    if (seconds < 10) {
        seconds = "0" + seconds;
    }
    if (minutes < 10) {
        minutes = "0" + minutes;
    }
    if (hours > 12) {
        hours = hours - 12;
        elementTime.innerHTML = hours + " : " + minutes + " : " + seconds + "  PM ";
    } else if (hours < 12) {
        elementTime.innerHTML = hours + " : " + minutes + " : " + seconds + "  AM ";
    } else if (hours = 12) {
        elementTime.innerHTML = hours + " : " + minutes + " : " + seconds + "  PM ";
    }
}

setInterval(function() {
    printTime();
    printDate();
    printDay();
}, 1000);

(function(document) {
    var _bars = [].slice.call(document.querySelectorAll('.bar-inner'));
    _bars.map(function(bar, index) {
        setTimeout(function() {
            bar.style.width = bar.dataset.percent;
        }, index * 500);

    });
})(document)


// Main APi
const todayN = document.getElementById('todayNews')
window.addEventListener('load', () => {
    const url = `https://cbn360-api.herokuapp.com/api/announcements/`;
    fetch(url)
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            const { today_news } = data.data[data.data.length - 1].attributes;
            todayN.textContent = "📢: " + `${today_news}`
            console.log(today_news)
        })
})

// Writer Api
const keywordP = document.getElementById('keywordP')
const keywordPr = document.getElementById('keywordPr')
const keyD = document.getElementById('keywordDate')

window.addEventListener('load', () => {
    const url = `https://cbn360-api.herokuapp.com/api/writers/`;
    fetch(url)
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            // Keyword
            const { keyword_proposion } = data.data[data.data.length - 1].attributes;
            keyFormat = new Intl.NumberFormat().format(keyword_proposion)
            keywordP.textContent = `${keyFormat}`
                // console.log(keyFormat)

            // Keyword Date
            const { updatedAt } = data.data[data.data.length - 1].attributes;
            const mySplit = updatedAt.split("T")
            keyD.textContent = "Last Update: " + `${mySplit[0]}`
                // console.log(mySplit)

            // WebVisitor
            const { website_visitor } = data.data[data.data.length - 1].attributes;
            visitFormat = new Intl.NumberFormat().format(website_visitor)
            keywordPr.textContent = `${visitFormat}`
        })
})


const negativeF = document.getElementById('negative')
const neutralF = document.getElementById('neutral')
const positiveF = document.getElementById('positive')
window.addEventListener('load', () => {
    const url = `http://50.50.50.229:1337/api/sentiments`;
    fetch(url)
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            // Keyword
            const { negative } = data.data[data.data.length - 1].attributes;
            negativeFormat = new Intl.NumberFormat().format(negative)
            negativeF.textContent = `${negativeFormat}`
                // console.log(negativeFormat)
                // Keyword
            const { neutral } = data.data[data.data.length - 1].attributes;
            neutralFormat = new Intl.NumberFormat().format(neutral)
            neutralF.textContent = `${neutralFormat}`
            const { positive } = data.data[data.data.length - 1].attributes;
            positiveFormat = new Intl.NumberFormat().format(positive)
            positiveF.textContent = `${positiveFormat}`
        })
})

var text = [
    "How's Your Day",
    "Cie Baru Gajian Tapi Duit Udah Abis",
    "Udah Minum KSK Belum Brok???",
];

var randomItem = text[Math.floor(Math.random() * text.length)]
console.log(randomItem)

function getDays(){
    var myDate = new Date();
var hrs = myDate.getHours();

var greet;

if (hrs < 12)
    greet = 'Good Morning';
else if (hrs >= 12 && hrs <= 17)
    greet = 'Good Afternoon';
else if (hrs >= 17 && hrs <= 24)
    greet = 'Good Evening';

document.getElementById('greetings').innerHTML =
    '<b>' + greet + '</b>, Hows your day??';
}

setInterval(function(){
    getDays();
},3000)


// $(document).ready(function() {
//     // Gets the video src from the data-src on each button
//     var $videoSrc;
//     $('.video-btn').click(function() {
//         $videoSrc = $(this).data("src");
//     });
//     // console.log($videoSrc);
//     // when the modal is opened autoplay it  
//     $('#myModal').on('shown.bs.modal', function(e) {
//             // set the video src to autoplay and not to show related video. Youtube related video is like a box of chocolates... you never know what you're gonna get
//             $("#video").attr('src', $videoSrc + "?autoplay=1&amp;modestbranding=1&amp;showinfo=0");
//         })
//         // stop playing the youtube video when I close the modal
//     $('#myModal').on('hide.bs.modal', function(e) {
//         // a poor man's stop video
//         $("#video").attr('src', $videoSrc);
//     })

//     // document ready  
// });