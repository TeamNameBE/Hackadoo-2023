<template>
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
    components: { NewsArticle },
    mounted() {
        this.articles = [
            {
                id: 1,
                title: "Article 1",
                content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, nisl vitae ultricies lacinia, nisl nisl aliquet nisl, eget aliquam nunc nisl eget nisl. Nullam euismod, nisl vitae ultricies lacinia, nisl nisl aliquet nisl, eget aliquam nunc nisl eget nisl. Nullam euismod, nisl vitae ultricies lacinia, nisl nisl aliquet nisl, eget aliquam nunc nisl eget nisl. Nullam euismod, nisl vitae ultricies lacinia, nisl nisl aliquet nisl, eget aliquam nunc nisl eget nisl. Nullam euismod, nisl vitae ultricies lacinia, nisl nisl aliquet nisl, eget aliquam nunc nisl eget nisl. Nullam euismod, nisl vitae ultricies lacinia, nisl nisl aliquet nisl, eget aliquam nunc nisl eget nisl. Nullam euismod, nisl vitae ultricies lacinia, nisl nisl aliquet nisl, eget aliquam nunc nisl eget nisl. Nullam euismod, nisl vitae ultricies lacinia, nisl nisl aliquet nisl, eget aliquam nunc nisl eget nisl. Nullam euismod, nisl vitae ultricies lacinia, nisl nisl aliquet nisl, eget aliquam nunc nisl eget nisl. Nullam euismod, nisl vitae ultricies lacinia, nisl nisl aliquet nisl, eget aliquam nunc nisl eget nisl. Nullam euismod, nisl vitae ultricies lacinia, nisl nisl aliquet nisl, eget aliquam nunc nisl eget nisl. Nullam euismod, nisl vitae ultricies lacinia, nisl nisl aliquet nisl, eget aliquam nunc nisl eget nisl. Nullam euismod, nisl vitae ultricies lacinia, nisl nisl aliquet nisl, eget aliquam nunc nisl eget nisl. Nullam euismod, nisl vitae"
            }
        ];
    }
}
</script>
