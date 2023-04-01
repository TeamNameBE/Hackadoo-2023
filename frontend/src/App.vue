<template>
    <div class="row h-25">
        <div class="col col-9">
            <h1 class="text-center news-feed-title">Time Traveler's Gazette</h1>
            <h5 class="subtitle">Bringing you yesterday's news, today!</h5>
            <span class="text-center row text-black ps-5 pe-5">
                <router-link class="col link-black" to="/">Home Page</router-link>
                <p class="col">♰</p>
                <router-link  class="col link-black" to="/random">Random Page</router-link>
                <p class="col">♰</p>
                <router-link  class="col link-black" to="/foryou">For You</router-link>
                <p class="col">♰</p>
                <router-link  class="col link-black" to="/profile">Profile</router-link>
            </span>
        </div>
        <div class="col vertical-ruler"></div>
        <div class="col text-center mt-4">
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

<style scoped>
.news-feed-title {
    font-family: "Bungee", cursive;
    font-size: 7.5em;
}

.vertical-ruler {
    border-left: 1px solid black;
    margin-top: 10px;
    margin-bottom: 10px;
    max-width: 1px;
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

.date-start {
    font-family: "Bungee", cursive;
    font-size: 2.8em;
}

.data-year {
    font-family: "Bungee", cursive;
    font-size: 5em;
    margin-top: -0.75em;
}
</style>
