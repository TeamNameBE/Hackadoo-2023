<template>
    <div class="news-article">
        <h2>{{ title }}</h2>
        <p class="subhead justified">{{ content }}</p>
    </div>
</template>

<script>
export default {
    name: "NewsArticle",
    props: {
        title: String,
        content: String
    },
}
</script>

<style scoped>
.news-article {
    transform: scale(1);
}

.news-article:hover {
    transform: scale(1.01);
}
</style>
