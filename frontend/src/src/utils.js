import axios from "axios";
import instance from "@/src/axios";
import { destroyToken, saveToken, getRefreshToken } from "./store";


/**
 * Wrap the interceptor in a function, so that i can be re-instantiated
 */
function createAxiosResponseInterceptor() {
    const interceptor = instance.interceptors.response.use(
        (response) => response,
        (error) => {
            // Reject promise if usual error
            if (error.response.status !== 401) {
                return Promise.reject(error);
            }
            instance.interceptors.response.eject(interceptor);
            return instance
                .post("/api/token/refresh/", {
                    refresh: getRefreshToken(),
                })
                .then((response) => {
                    saveToken();
                    error.response.config.headers["Authorization"] = `Bearer ${response.data.access}`;

                    return axios(error.response.config);
                })
                .catch((error2) => {
                    destroyToken();
                    this.router.push("/");
                    return Promise.reject(error2);
                })
                .finally(createAxiosResponseInterceptor);
        }
    );
}

export default createAxiosResponseInterceptor;
