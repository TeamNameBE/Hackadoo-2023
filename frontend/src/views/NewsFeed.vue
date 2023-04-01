<template>
    <h1>The Time Traveler's Gazette</h1>
    <h1>{{ $route.meta.title }}</h1>
    <NewsArticle v-for="article in articles" :key="article.id" :title="article.title" :content="article.content" />
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
    components: { NewsArticle }
}
</script>
