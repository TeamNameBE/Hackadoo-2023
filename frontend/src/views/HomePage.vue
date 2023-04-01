<template>
    <div class="p-3">
        <div class="row width-90">
            <div class="col-3 news-article">
                <h2>The Time Traveler's Gazette</h2>
                <p class="justified">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Fermentum iaculis eu non diam phasellus vestibulum. Turpis egestas sed tempus urna et pharetra pharetra massa massa. Tincidunt tortor aliquam nulla facilisi cras fermentum. Elit duis tristique sollicitudin nibh sit. Consequat semper viverra nam libero. Cursus vitae congue mauris rhoncus aenean. Scelerisque mauris pellentesque pulvinar pellentesque habitant morbi. Duis ultricies lacus sed turpis tincidunt id. Vel pretium lectus quam id leo in vitae. Nibh sed pulvinar proin gravida hendrerit lectus. Faucibus ornare suspendisse sed nisi lacus sed viverra tellus in. Mauris pharetra et ultrices neque ornare aenean. Urna duis convallis convallis tellus.<br />
                </p>
            </div>
            <div class="central-columm news-article col-6">
                <h2>How does it work ?</h2>
                <img src="https://earlychurchhistory.org/wp-content/uploads/2020/04/Handshake-10.gif" alt="The Time Traveler's Gazette" class="col-12">
                <p class="justified">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Fermentum iaculis eu non diam phasellus vestibulum. Turpis egestas sed tempus urna et pharetra pharetra massa massa. Tincidunt tortor aliquam nulla facilisi cras fermentum. Elit duis tristique sollicitudin nibh sit. Consequat semper viverra nam libero. Cursus vitae congue mauris rhoncus aenean. Scelerisque mauris pellentesque pulvinar pellentesque habitant morbi. Duis ultricies lacus sed turpis tincidunt id. Vel pretium lectus quam id leo in vitae. Nibh sed pulvinar proin gravida hendrerit lectus. Faucibus ornare suspendisse sed nisi lacus sed viverra tellus in. Mauris pharetra et ultrices neque ornare aenean. Urna duis convallis convallis tellus.<br/>
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
</style>
