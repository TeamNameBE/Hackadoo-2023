<template>
    <div class="news-article">
        <h2>{{ title }}</h2>
        <p class="subhead">{{ content }}</p>
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
.justified{
    text-align: justify;
}

.news-article {
    transform: scale(1);
}

.news-article:hover {
    transform: scale(1.01);
}

.subhead {
    initial-letter: 2;
}

h2 {
    font-family: "Baskervville", cursive;
    /* font-size: 1.7em; */
}

p {
    font-family: "Baskervville", serif;
    /* font-size: 1.2em; */
}
</style>
