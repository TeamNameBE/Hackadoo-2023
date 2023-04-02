<template>
    <p>{{ article.title }} - {{ article.year }}</p>
</template>

<script>
export default {
    name: "NecrologyAndBirthArticle",
    props: {
        article: Object,
    },
}
</script>
