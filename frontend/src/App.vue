<template>
    <h1>The Time Traveler's Gazette</h1>
    <NewsArticle v-for="article in articles" :key="article.id" :title="article.title" :content="article.content" />
</template>

<script>
import NewsArticle from './components/NewsArticle.vue';

export default {
    name: "App",
    data() {
        return {
            articles: [
                {
                    id: 1,
                    title: "The Time Traveler's Gazette",
                    content: "The Time Traveler's Gazette is a weekly newspaper published in the United States. It is the only newspaper in the world that is published in the future, and is delivered to subscribers in the present. The newspaper is published by the Time Traveler's Association, a non-profit organization that was founded in 1950 by a group of time travelers. The newspaper's motto is \"The future is now.\""
                },
            ]
        };
    },
    components: { NewsArticle }
}
</script>
