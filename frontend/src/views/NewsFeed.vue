<template>
    <div class="p-3">
        <div class="row width-90">
            <div class="col-3">
                <NewsArticle v-for=" article in firstColumnArticles" :key="article.id" :article="article" :center="false" />
            </div>
            <div class="central-columm col-6">
                <div v-if="!firstColumnArticles.length">
                    <h2>No articles available</h2>
                    <img src="https://giphy.com/embed/6uGhT1O4sxpi8"/>
                </div>
                <NewsArticle v-for="(article, index) in secondColumnArticles" :key="article.id" :article="article" :media_position="index" :center="true" />
            </div>
            <div class="col-3">
                <h2 v-if="deaths.length">Necrology</h2>
                <NecrologyArticle v-for="article in deaths" :key="article.id" :article="article" />
                <h2 v-if="births.length">Births</h2>
                <BirthArticle v-for="article in births" :key="article.id" :article="article" />
            </div>
        </div>
    </div>
</template>

<script>
import NewsArticle from '@/components/NewsArticle.vue';
import NecrologyArticle from '@/components/NecrologyArticle.vue';
import BirthArticle from '@/components/BirthArticle.vue';
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
        NecrologyArticle,
        BirthArticle
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
