<template>
    <div class="p-3">
        <div class="row">
            <div class="col-12">
                <h1 class="news-feed-title">News Feed</h1>
                <p class="subtitle">What's happening in the world?</p>
            </div>
        </div>
        <div class="row">
            <div class="col-12">
                <NewsArticle v-for="article in articles" :key="article.id" :title="article.title" :content="article.content" />
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "HomePage",
    methods: {
        select(portal) {
            document.getElementById(portal).classList.add("getToIt");
            document.getElementById(portal).style.zIndex = 1000;
            setTimeout(() => this.$router.push({ name: portal }), 500);
        }
    }
}
</script>


<style scoped>

</style>
