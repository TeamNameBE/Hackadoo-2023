import { createWebHashHistory, createRouter } from "vue-router";

import HomePage from "@/views/HomePage.vue";
import NewsFeed from "@/views/NewsFeed.vue";

const routes = [
    {
        path: "/",
        name: "HomePage",
        component: HomePage,
        meta: {
            title:"Home"
        }
    },
    {
        path: "/foryou",
        name: "ForYou",
        component: NewsFeed,
        meta: {
            title: "For You"
        }
    },
    {
        path: "/random",
        name: "Random",
        component: NewsFeed,
        meta: {
            title: "Random"
        }
    }
];

const router = createRouter({
    history: createWebHashHistory(),
    routes,
});

export default router;
