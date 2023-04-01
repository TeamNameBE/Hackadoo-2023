<template>
    <div class="news-article">
        <h2>{{ article.title }}</h2>
        <img :src="article.media_url" alt="" class="col-12 media-left" v-if="media_position % 2 === 0">
        <img :src="article.media_url" alt="" class="col-12 media-right" v-else>

        <p class="subhead justified">{{ article.abstract }}</p>

    </div>
</template>

<script>
export default {
    name: "NewsArticle",
    props: {
        article: Object,
        media_position: Number
    },
}
</script>

<style scoped>
.news-q {
    transform: scale(1);
    transition-duration: 0.5s;
}

.news-article:hover{
    transform: scale(1.2);
    transition-duration: 0.5s;
    padding:1em;
}
.news-article:hover >body {
    background: rgb(1, 1, 1);
}

.media-left {
    -webkit-filter: grayscale(1.0) brightness(0.8);
    max-width: 400px;
    float:left;
    margin-right: 10px;
}
.media-right {
    -webkit-filter: grayscale(1.0) brightness(0.8);
    max-width: 400px;
    float:right;
    margin-left: 10px;
}
</style>
