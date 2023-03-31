<template>
    <div class="news-article">
        <h2>{{ title }}</h2>
        <p>{{ content }}</p>
    </div>
</template>

<script>
export default {
    name: "NewsArticle",
    props: {
        title: String,
        content: String
    }
}
</script>
