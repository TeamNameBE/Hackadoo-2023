<template>
    <div class="mt-3 col-6">
        <img :src="get_media_url" class="img-fluid zoomOnHover grayscale aligned" />
        <h5 class="guy-name">{{ article.title }} - {{ article.year }}</h5>
    </div>
</template>

<script>
export default {
    name: "NecrologyAndBirthArticle",
    props: {
        article: Object,
    },
    computed: {
        get_media_url() {
            if(this.article.media_url !== null){
                return this.article.media_url;
            } else {
                return "/static/img/placeholder.jpg";
            }
        }
    },
}
</script>

<style>
.zoomOnHover {
    transition: transform .3s;
    transform: scale(1);
}

.zoomOnHover:hover {
    transition: transform .3s;
    transform: scale(1.05);
}

.grayscale {
    filter: grayscale(100%);
}

.aligned {
    height: 200px;
    object-fit: cover;
}

.guy-name {
    font-family: "BaskervvilleItalic", cursive;
    font-size: 1.2rem;
    font-weight: 700;
    color: #000;
}
</style>
