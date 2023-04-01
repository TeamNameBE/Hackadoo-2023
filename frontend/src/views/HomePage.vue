<template>
    <div class="p-3">


    <div id="flipbook">
        <div class="hard"> Turn.js </div>
        <div class="hard"></div>
        <div> Page 1 </div>
        <div> Page 2 </div>
        <div> Page 3 </div>
        <div> Page 4 </div>
        <div class="hard"></div>
        <div class="hard"></div>
    </div>

        <div class="row width-90">
            <div class="col-3 news-article">
                <h2>The Time Traveler's Gazette</h2>
                <p class="justified">
                    Welcome to The Time Traveler's Gazette! Our digital journal takes you on a journey through time, providing daily news from the past on all kinds of topics, tailored to your interests. With our platform, you can discover the stories and events that shaped the world we live in today, and explore history in a new and engaging way. Every day, you'll receive a personalized selection of news stories from the particular day you're in, giving you a unique window into the past. From politics to science, culture to sports, The Time Traveler's Gazette has it all. So come join us on this journey through history, and see the world in a whole new light!<br />
                </p>
            </div>
            <div class="central-columm news-article col-6">
                <h2>How does it work ?</h2>
                <img src="https://earlychurchhistory.org/wp-content/uploads/2020/04/Handshake-10.gif" alt="The Time Traveler's Gazette" class="col-12">
                <p class="justified">
                    The Time Traveler's Gazette is an easy-to-use digital journal that brings the past to life. Once you've accessed our website, you can create a profile and select your areas of interest, and we'll curate a daily selection of news stories from the particular day you're in. Our platform uses advanced algorithms to sift through historical archives and provide you with the most relevant and engaging content. Whether you're a history buff, a casual reader, or simply curious about the world around you, The Time Traveler's Gazette has something for everyone. With our intuitive interface and personalized approach, you'll find it easy to navigate through the past and discover the events and stories that fascinate you. So why wait? Visit our website today and take a journey through time!<br/>
                </p>
            </div>
            <div class="col-3">
                <div class="news-article">
                    <h2>Login</h2>
                    <div class="subhead justified">
                        By logging in you accept to give us all of your data for purely financial purposes 🤑
                        <form class="form mt-5" action="javascript:void(0)">
                            <label class="form-label" for="username">Username</label>
                            <input v-model="username" class="form-control" type="text" id="username" name="username" placeholder="Your username.." />
                            <label class="form-label" for="password">Password</label>
                            <input v-model="password" class="form-control" type="password" id="password" name="password" placeholder="Your password.." />
                            <div class="row">
                                <div class="col-3 p-2">
                                    <button class="btn btn-primary mt-3 col-12" @click="() => login()" type="submit">Login</button>
                                </div>
                                <div class="col-3 p-2">
                                    <button class="col btn btn-success mt-3 col-12" @click="() => register()" type="submit">Register</button>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import $ from 'jquery';
import 'turn.js';

export default {
    name: "HomePage",
    computed: {
        firstColumnArticles() {
            return this.articles.filter((article, index) => index % 3 === 0);
        },
        secondColumnArticles() {
            return this.articles.filter((article, index) => index % 3 === 1);
        },
        thirdColumnArticles() {
            return this.articles.filter((article, index) => index % 3 === 2);
        }
    },
    data(){
        return {
            username: "",
            password: ""
        }
    },
    methods: {
        login() {
            console.log(this.username);
            console.log(this.password);
        },
        register() {
            console.log("register");
        }
    },
    mounted(){
        $("#flipbook").turn({
            width: 400,
            height: 300,
            autoCenter: true
        });
    }
    
}
</script>


<style>
.central-columm {
    border-left: 2px solid black;
    border-right: 2px solid black;
}

.justified{
    text-align: justify;
}

.width-90{
    width: 90%;
    margin-left: 5%;
}

.news-article h2 {
    font-family: "BaskervvilleItalic", serif;
    text-transform: capitalize;
}

.news-article p {
    font-family: "Baskervville", serif;
}
.justified::first-letter{
    padding-top:0.2em;
    padding-right:0.2em;
    font-size: 300%;
    float:left;
    font-family: "DSWalbaumfraktur", cursive; 
}
</style>
