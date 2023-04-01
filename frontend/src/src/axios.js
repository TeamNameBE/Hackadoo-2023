import axios from "axios";
import { getToken } from "./store";

const instance = axios.create({
    headers: {
        "Content-Type": "application/json"
    },
});

instance.interceptors.request.use(
    function (config) {
        const token = getToken();
        if (token) {
            config.headers["Authorization"] = `Bearer ${token}`;
        }
        return config;
    },
    function (error) {
        return Promise.reject(error);
    }
);

export default instance;
