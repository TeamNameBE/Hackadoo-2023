<template>
    <!-- <h1>{{ $route.meta.title }}</h1> -->
    <div class="p-3">
        <div class="row width-90">
            <div class="col-3">
                <NewsArticle v-for="article in firstColumnArticles" :key="article.id" :title="article.title" :content="article.abstract" />
            </div>
            <div class="central-columm col-6">
                <img src="https://earlychurchhistory.org/wp-content/uploads/2020/04/Handshake-10.gif" alt="The Time Traveler's Gazette" class="col-12">
                <NewsArticle v-for="article in secondColumnArticles" :key="article.id" :title="article.title" :content="article.abstract" />
            </div>
            <div class="col-3">
                <NewsArticle v-for="article in thirdColumnArticles" :key="article.id" :title="article.title" :content="article.abstract" />
            </div>
        </div>
    </div>
</template>

<script>
import NewsArticle from '@/components/NewsArticle.vue';

export default {
    name: "ForYou",
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
        fetch("/api/articles/random/")
        .then(response => response.json())
        .then(data => {
            this.articles = data;
            this.articles.forEach(article => {
                article.title = article.title.replace(/_/g, " ");
            });
        })
    }
}
</script>
