<template>
    <div class="p-3">
        <div class="row width-90">
            <div class="col-3 news-article">
                <h2>The Time Traveler's Gazette</h2>
                <p class="justified">
                    Welcome to The Time Traveler's Gazette! Our digital journal takes you on a journey through time, providing daily news from the past on all kinds of topics, tailored to your interests. With our platform, you can discover the stories and events that shaped the world we live in today, and explore history in a new and engaging way. Every day, you'll receive a personalized selection of news stories from the particular day you're in, giving you a unique window into the past. From politics to science, culture to sports, The Time Traveler's Gazette has it all. So come join us on this journey through history, and see the world in a whole new light!<br />
                </p>
            </div>
            <div class="central-columm news-article col-6">
                <h2>How does it work ?</h2>
                <img src="https://miro.medium.com/v2/resize:fit:1240/0*cv9k-Bkd3_f1hu0z.gif" alt="The Time Traveler's Gazette" class="col-12"> 
                <p class="justified">
                    The Time Traveler's Gazette is an easy-to-use digital journal that brings the past to life. Once you've accessed our website, you can create a profile and select your areas of interest, and we'll curate a daily selection of news stories from the particular day you're in. Our platform uses advanced algorithms to sift through historical archives and provide you with the most relevant and engaging content. Whether you're a history buff, a casual reader, or simply curious about the world around you, The Time Traveler's Gazette has something for everyone. With our intuitive interface and personalized approach, you'll find it easy to navigate through the past and discover the events and stories that fascinate you. So why wait? Visit our website today and take a journey through time!<br/>
                </p>
            </div>
            <div class="col-3">
                <div v-if="notLogged" class="news-article">
                    <h2>Login</h2>
                    <div class="subhead justified">
                        By logging in you accept to give us all of your data for purely financial purposes 🤑

                        <div class="alert alert-danger" v-if="error">
                            {{ error }}
                        </div>
                        <div class="alert alert-success" v-if="success">
                            {{ success }}
                        </div>

                        <form class="form mt-5" action="javascript:void(0)" v-if="notLogged">
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
                <div v-else-if="!user_loading" class="news-article">
                    <h2>Your Interests</h2>

                    <div v-for="interest in all_interests" :key="interest.id" :class="form-check">
                        <input class="form-check-input" type="checkbox" value="" :id="interest.id" :checked="interestPicked(interest)">
                        <label class="form-check-label" for="flexCheckDefault">
                            {{ interest.name }}
                        </label>
                    </div>
                    <button type="button" class="btn btn-warning" @click="saveInterest()">Save</button>
                    <hr />
                    <button type="button" class="btn btn-danger" @click="logout()">Log out</button>
                </div>
                <div v-else class="news-article">
                    <h2>Loading...</h2>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import instance from "@/src/axios";
import { saveToken, saveRefreshToken, check_token, destroyRefreshToken, destroyToken } from "@/src/store";
import $ from "jquery";


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
        },
    },
    data(){
        return {
            username: "",
            password: "",
            error: "",
            success: "",
            all_interests: [],
            user: {
                "interests": []
            },
            user_loading: true,
            notLogged: true
        }
    },
    methods: {
        login() {
            instance.post(
                "/api/token/",
                JSON.stringify({
                    username: this.username,
                    password: this.password
                })
            )
            .then(response => {
                saveToken(response.data.access);
                saveRefreshToken(response.data.refresh);
                this.success = "You are now logged in !";
                this.notLogged = false
                setTimeout(() => {
                    this.success = "";
                }, 3000);
            })
            .catch(error => {
                console.error(error);
                this.error = "An error occured while trying to log you in.";
                setTimeout(() => {
                    this.error = "";
                }, 3000);
            });
        },
        register() {
            console.log("register");
        },
        logout(){
            destroyRefreshToken();
            destroyToken();
        },
        interestPicked(interest){
            return this.user.interests.filter(user_interest => {
                if (user_interest.id === interest.id)
                    return user_interest
            }).length > 0
        }, 
        saveInterest(){
            var check_interests = $('.form-check-input:checkbox:checked')
            var checked_interests = []
            for (const interest of check_interests) {
                checked_interests.push(parseInt(interest.id))
            }

            var new_interests = this.all_interests.filter(interest => {
                if(checked_interests.includes(interest.id))
                    return interest
            })
            this.user.interests = new_interests
            instance.put(
                "/api/users/",
                JSON.stringify(this.user)
            ).then(response =>{console.log(response)})
        }
    },
    mounted(){
        if (check_token()){
            instance.get(
                "/api/categories/"
            )
            .then(response =>{
                this.all_interests = response.data
            })

            this.notLogged = false
            instance.get(
                "/api/users/",
            )
            .then(response => {
                this.user = response.data
                this.user_loading = false
            })
        }
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

.section-title {
    font-family: "DSWalbaumfraktur", serif;
    text-transform: capitalize;
}
</style>
