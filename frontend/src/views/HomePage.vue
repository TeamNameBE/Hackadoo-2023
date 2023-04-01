<template>
    <div class="p-3">
        <div class="row width-90">
            <div class="col-3">
                <NewsArticle v-for="article in firstColumnArticles" :key="article.id" :title="article.title" :content="article.content" />
            </div>
            <div class="central-columm col-6">
                <img src="https://earlychurchhistory.org/wp-content/uploads/2020/04/Handshake-10.gif" alt="The Time Traveler's Gazette" class="col-12">
                <NewsArticle v-for="article in secondColumnArticles" :key="article.id" :title="article.title" :content="article.content" />
            </div>
            <div class="col-3">
                <div class="news-article">
                    <h2>Login</h2>
                    <div class="subhead justified">
                        By logging in you accept to give us all of your data for purely financial purposes
                        <form class="form mt-5">
                            <label class="form-label" for="username">Username</label>
                            <input class="form-control" type="text" id="username" name="username" placeholder="Your username..">
                            <label class="form-label" for="password">Password</label>
                            <input class="form-control" type="password" id="password" name="password" placeholder="Your password..">
                            <div class="row">
                                <div class="col-3 p-2">
                                    <button class="btn btn-primary mt-3 col-12" type="submit">Login</button>
                                </div>
                                <div class="col-3 p-2">
                                    <button class="col btn btn-success mt-3 col-12" type="submit">Register</button>
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
import NewsArticle from '@/components/NewsArticle.vue';

export default {
    name: "HomePage",
    methods: {
        select(portal) {
            document.getElementById(portal).classList.add("getToIt");
            document.getElementById(portal).style.zIndex = 1000;
            setTimeout(() => this.$router.push({ name: portal }), 500);
        }
    },
    components: {
        NewsArticle
    },
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
    data() {
        return {
            articles: [
                {
                    id: 1,
                    title: "The Time Traveler's Gazette",
                    content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Fermentum iaculis eu non diam phasellus vestibulum. Turpis egestas sed tempus urna et pharetra pharetra massa massa. Tincidunt tortor aliquam nulla facilisi cras fermentum. Elit duis tristique sollicitudin nibh sit. Consequat semper viverra nam libero. Cursus vitae congue mauris rhoncus aenean. Scelerisque mauris pellentesque pulvinar pellentesque habitant morbi. Duis ultricies lacus sed turpis tincidunt id. Vel pretium lectus quam id leo in vitae. Nibh sed pulvinar proin gravida hendrerit lectus. Faucibus ornare suspendisse sed nisi lacus sed viverra tellus in. Mauris pharetra et ultrices neque ornare aenean. Urna duis convallis convallis tellus.\
\
Commodo ullamcorper a lacus vestibulum sed arcu non odio euismod. Amet nisl suscipit adipiscing bibendum est ultricies integer quis auctor. Feugiat scelerisque varius morbi enim nunc faucibus a pellentesque sit. Pulvinar etiam non quam lacus. Suscipit tellus mauris a diam maecenas sed. Non diam phasellus vestibulum lorem sed. Adipiscing vitae proin sagittis nisl rhoncus mattis rhoncus. Non blandit massa enim nec dui nunc mattis enim ut. Scelerisque viverra mauris in aliquam sem fringilla ut morbi tincidunt. Eu lobortis elementum nibh tellus molestie nunc non blandit. Massa sed elementum tempus egestas sed sed risus pretium. Quis risus sed vulputate odio ut. Elit duis tristique sollicitudin nibh sit.\
\
Elit ut aliquam purus sit amet luctus. Magna sit amet purus gravida quis blandit. Diam donec adipiscing tristique risus nec feugiat in fermentum. Tempus urna et pharetra pharetra massa massa. Curabitur gravida arcu ac tortor dignissim convallis aenean et. Cursus risus at ultrices mi. Turpis nunc eget lorem dolor. Lectus mauris ultrices eros in cursus turpis. Sit amet mattis vulputate enim nulla aliquet porttitor lacus luctus. Lorem mollis aliquam ut porttitor leo a diam. Est ultricies integer quis auctor elit sed vulputate mi sit. Sit amet dictum sit amet justo donec enim diam. In tellus integer feugiat scelerisque varius morbi enim nunc faucibus. A diam maecenas sed enim ut sem viverra aliquet eget. Laoreet suspendisse interdum consectetur libero id faucibus. Vel eros donec ac odio tempor orci. In metus vulputate eu scelerisque felis imperdiet proin.",
                },
                {
                    id: 2,
                    title: "How does it work ?",
                    content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Fermentum iaculis eu non diam phasellus vestibulum. Turpis egestas sed tempus urna et pharetra pharetra massa massa. Tincidunt tortor aliquam nulla facilisi cras fermentum. Elit duis tristique sollicitudin nibh sit. Consequat semper viverra nam libero. Cursus vitae congue mauris rhoncus aenean. Scelerisque mauris pellentesque pulvinar pellentesque habitant morbi. Duis ultricies lacus sed turpis tincidunt id. Vel pretium lectus quam id leo in vitae. Nibh sed pulvinar proin gravida hendrerit lectus. Faucibus ornare suspendisse sed nisi lacus sed viverra tellus in. Mauris pharetra et ultrices neque ornare aenean. Urna duis convallis convallis tellus.\
\
Commodo ullamcorper a lacus vestibulum sed arcu non odio euismod. Amet nisl suscipit adipiscing bibendum est ultricies integer quis auctor. Feugiat scelerisque varius morbi enim nunc faucibus a pellentesque sit. Pulvinar etiam non quam lacus. Suscipit tellus mauris a diam maecenas sed. Non diam phasellus vestibulum lorem sed. Adipiscing vitae proin sagittis nisl rhoncus mattis rhoncus. Non blandit massa enim nec dui nunc mattis enim ut. Scelerisque viverra mauris in aliquam sem fringilla ut morbi tincidunt. Eu lobortis elementum nibh tellus molestie nunc non blandit. Massa sed elementum tempus egestas sed sed risus pretium. Quis risus sed vulputate odio ut. Elit duis tristique sollicitudin nibh sit.\
\
Elit ut aliquam purus sit amet luctus. Magna sit amet purus gravida quis blandit. Diam donec adipiscing tristique risus nec feugiat in fermentum. Tempus urna et pharetra pharetra massa massa. Curabitur gravida arcu ac tortor dignissim convallis aenean et. Cursus risus at ultrices mi. Turpis nunc eget lorem dolor. Lectus mauris ultrices eros in cursus turpis. Sit amet mattis vulputate enim nulla aliquet porttitor lacus luctus. Lorem mollis aliquam ut porttitor leo a diam. Est ultricies integer quis auctor elit sed vulputate mi sit. Sit amet dictum sit amet justo donec enim diam. In tellus integer feugiat scelerisque varius morbi enim nunc faucibus. A diam maecenas sed enim ut sem viverra aliquet eget. Laoreet suspendisse interdum consectetur libero id faucibus. Vel eros donec ac odio tempor orci. In metus vulputate eu scelerisque felis imperdiet proin.",
                },
            ]
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
