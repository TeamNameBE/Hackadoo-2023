<template>
    <div class="row h-25">
        <div class="col col-9">
            <h1 class="text-center news-feed-title">Time Traveler's Gazette</h1>
            <h5 class="subtitle">Bringing you yesterday's news, today!</h5>
            <span class="nav-span text-center row text-black">
                <p class="nav-item col">✹</p>
                <router-link class="nav-item col link-black" to="/">Home Page</router-link>
                <p class="nav-item col">✹</p>
                <router-link  class="nav-item col link-black" to="/random">Random Page</router-link>
                <p class="nav-item col">✹</p>
                <router-link  class="nav-item col link-black" to="/foryou">For You</router-link>
                <p class="nav-item col">✹</p>
                <router-link  class="nav-item col link-black" to="/profile">Profile</router-link>
                <p class="nav-item col">✹</p>
            </span>
        </div>
        <div class="col vertical-ruler"></div>
        <div class="col mt-4">
            <p class="text-center date-weekday">{{ dateDay }},</p>
            <p class="text-center date-start">{{ dateStart }}</p>
            <p class="text-center data-year">{{ dateYear }}</p>
        </div>
    </div>
    <div class="double-ruler"></div>
    <router-view></router-view>
</template>

<script>
export default {
    name: "App",
    computed: {
        dateDay(){
            // Returns the day of the week
            return new Date().toLocaleDateString("en-UK", { weekday: "long" });
        },
        dateStart() {
            // Returns the day of the month plus the month name
            return new Date().toLocaleDateString("en-UK", { day: "numeric", month: "long" });
        },
        dateYear() {
            // Returns the year
            return new Date().toLocaleDateString("en-UK", { year: "numeric" });
        }
    },
}
</script>

<style>
@font-face {
    font-family: DSWalbaumfraktur;
    src: url("../../hackadoo/assets/fonts/DSWalbaumfraktur.ttf");
}

@font-face {
    font-family: Baskervville;
    src: url("../../hackadoo/assets/fonts/Baskervville-Regular.ttf");
}


@font-face {
    font-family: BaskervvilleItalic;
    src: url("../../hackadoo/assets/fonts/Baskervville-Italic.ttf");
}

.news-feed-title {
    font-family: "DSWalbaumfraktur", cursive;
    font-size: 7.5em;
}

.vertical-ruler {
    border-left: 1px solid black;
    margin-top: 10px;
    margin-bottom: 10px;
    max-width: 1px;
    padding-left: 0%;
    padding-right: 0%;
}

.double-ruler{
    border-top: 3px solid black;
    border-bottom: 1px solid black;
    height: 10px;
    min-width: 90%;
    max-width: 90%;
    margin-left: 5%;
}

.subtitle {
    font-family: "Bungee", cursive;
    font-size: 2em;
    margin-top: -1em;
    padding-left: 25%;
    color: #6c757d;
}

.link-black {
    color: black;
}

.link-black:hover {
    color: #6c757d;
    text-decoration: none;
}

.date-weekday {
    font-family: "DSWalbaumfraktur", cursive;
    font-size: 2em;
}

.date-start {
    font-family: "DSWalbaumfraktur", cursive;
    font-size: 2.8em;
    margin-top: -0.75em;
}

.data-year {
    font-family: "DSWalbaumfraktur", cursive;
    font-size: 5em;
    margin-top: -0.75em;
}

.nav-item {
    text-transform: uppercase;
    max-width: fit-content;
    font-weight: 900;
    padding: 0;
    font-size: 1.5em;
    margin-left: 2px;
    margin-right: 2px;
}

.nav-span {
    padding-right: 15%;
    padding-left: 15%;
    justify-content: space-around;
}
</style>
