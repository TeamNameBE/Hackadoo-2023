<template>
    <div class="p-3">
        <div class="row width-90">
            <div class="col-3">
                <NewsArticle v-for=" article in firstColumnArticles" :key="article.id" :article="article" :center="false" />
            </div>
            <div class="central-columm col-6">
                <div v-if="!firstColumnArticles.length">
                    <h2>No articles available</h2>
                    <img src="https://media3.giphy.com/media/6uGhT1O4sxpi8/giphy.gif?cid=ecf05e47301vdg9qy7pjxehyom4km7o0znszxqs2evxm9fy6&rid=giphy.gif&ct=g"/>
                </div>
                <NewsArticle v-for="(article, index) in secondColumnArticles" :key="article.id" :article="article" :media_position="index" :center="true" />
            </div>
            <div class="col-3">
                <h2 v-if="deaths.length" class="section-title">Necrology</h2>
                <div class="col-12 row">
                    <NecrologyAndBirthArticle v-for="article in deaths" :key="article.id" :article="article" />
                </div>
                <hr />
                <h2 v-if="births.length" class="section-title">Births</h2>
                <div class="col-12 row">
                    <NecrologyAndBirthArticle v-for="article in births" :key="article.id" :article="article" />
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import NewsArticle from '@/components/NewsArticle.vue';
import NecrologyAndBirthArticle from '@/components/NecrologyAndBirthArticle.vue';
import instance from '@/src/axios';

export default {
    name: "NewsFeed",
    data() {
        return {
            articles: [],
            deaths: [],
            births: []
        };
    },
    computed: {
        firstColumnArticles() {
            return this.articles.filter((article, index) => index % 3 === 0);
        },
        secondColumnArticles() {
            return this.articles.filter((article, index) => (index % 3 === 1) || (index % 3 === 2));
        }
    },
    components: {
        NewsArticle ,
        NecrologyAndBirthArticle,
    },
    mounted() {
        var url = "/api/articles/random/"
        if (this.$route.meta.title == "For You")
            url = "/api/articles/forme/"

        instance.get(url)
        .then(response => {
            this.articles = response.data.articles;
            this.deaths = response.data.deaths;
            this.births = response.data.births;
        })
    }
}
</script>
