<template>
    <div class="p-3">
        <div class="row width-90">
            <div class="col-3">
                <NewsArticle v-for=" article in firstColumnArticles" :key="article.id" :article="article" />
            </div>
            <div class="central-columm col-6">
                <NewsArticle v-for="(article, index) in secondColumnArticles" :key="article.id" :article="article" :media_position="index"/>
            </div>
            <div class="col-3">
                <NewsArticle v-for="article in thirdColumnArticles" :key="article.id" :article="article" />
            </div>
        </div>
    </div>
</template>

<script>
import NewsArticle from '@/components/NewsArticle.vue';
import instance from '@/src/axios';

export default {
    name: "NewsFeed",
    data() {
        return {
            articles: []
        };
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
    components: { NewsArticle },
    mounted() {
        var url = "/api/articles/random/"
        if (this.$route.meta.title == "For You")
            url = "/api/articles/forme/"

        instance.get(url)
        .then(response => response.json())
        .then(data => {
            this.articles = data;
        })
    }
}
</script>
