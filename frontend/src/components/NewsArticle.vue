<template>
    <div class="news-article reveal">
        <h5>{{ article.subject }}</h5>
        <h2>{{ article.title }} - {{ article.year }} </h2>
        <img :src="article.media_url" alt="" :class="position_class">

        <p class="subhead justified">{{ article.abstract }}</p>
    </div>
    <hr />
</template>

<script>
export default {
    name: "NewsArticle",
    props: {
        article: Object,
        media_position: Number,
        center: Boolean,
    },
    computed: {
        position_class() {
            if (this.center !== true) {
                return "media-grayscale col-12 img-fluid";
            } else if (this.media_position % 2 === 0) {
                return "media-grayscale col-12 media-left";
            } else {
                return "media-grayscale col-12 media-right";
            }
        }
    },
    methods: {
        reveal() {
            var reveals = document.querySelectorAll(".reveal");
            for (var i = 0; i < reveals.length; i++) {
                var windowHeight = window.innerHeight;
                var elementTop = reveals[i].getBoundingClientRect().top;
                var elementVisible = 150;
                
                if (elementTop < windowHeight - elementVisible) {
                    reveals[i].classList.add("active");
                } else if (i < 1) {
                    reveals[i].classList.remove("reveal");
                } else {
                    reveals[i].classList.remove("active");
                }
            }
        }
    },
    mounted() {
        this.reveal();
        window.addEventListener("scroll", this.reveal);
    },
}

</script>

<style scoped>
.news-q {
    transform: scale(1);
    transition-duration: 0.5s;
}

.media-grayscale {
    -webkit-filter: grayscale(1.0) brightness(0.8);
}

.media-left {
    width: auto;
    float: left;
    margin-right: 10px;
    max-height: 300px;
}

.media-right {
    width: auto;
    float: right;
    margin-left: 10px;
    max-height: 300px;
}

.news-article {
    min-height: 400px;
}

.reveal {
    position: relative;
    transform: translateY(150px);
    opacity: 0;
    transition: 1s all ease;
}

.reveal.active {
    transform: translateY(0);
    opacity: 1;
}

.active.fade-bottom {
    animation: fade-bottom 0.5s ease-in;
}

@keyframes fade-bottom {
    0% {
        transform: translateY(50px);
        opacity: 0;
    }

    100% {
        transform: translateY(0);
        opacity: 1;
    }
}</style>
