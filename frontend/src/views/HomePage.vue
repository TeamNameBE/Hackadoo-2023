<template>
    <div class="position-absolute portal-centered-1">
        <h2>For You</h2>
        <button @click="select('ForYou')" class="btn btn-success" to="/foryou">For you Portal</button>
    </div>
    <div class="position-absolute portal-centered-2">
        <h2>Random</h2>
        <button @click="select('Random')" class="btn btn-success" to="/random">Random Portal</button>
    </div>
    <div class="row">
        <img class="col-6 portal" id="ForYou" src="/static/img/portal.png" />
        <img class="col-6 portal" id="Random" src="/static/img/portal.png" />
    </div>
</template>

<script>
export default {
    name: "HomePage",
    methods: {
        select(portal) {
            console.log("portal: ", portal);
            document.getElementById(portal).classList.add("getToIt");
            document.getElementById(portal).style.zIndex = 1000;
            setTimeout(() => this.$router.push({ name: portal }), 500);
        }
    }
}
</script>


<style scoped>
.portal {
    animation: rotation 5s;
    animation-timing-function: linear;
    animation-iteration-count: infinite;
    height: 100vh;
}

.portal-centered-1 {
    z-index: 100;
    width: 100vw;
    height: 100vh;
    transform: translate(25%, 50%);
}

.portal-centered-2 {
    z-index: 100;
    width: 100vw;
    height: 100vh;
    transform: translate(75%, 50%);
}

.getToIt {
    animation: getToIt 3s;
    animation-timing-function: linear;
}

@keyframes rotation {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(359deg);
  }
}

@keyframes getToIt {
    0% {
        transform: scale(1);
    }
    100% {
        transform: translateX(-25%);
        transform: scale(50) rotate(1800deg);
    }
}

</style>
