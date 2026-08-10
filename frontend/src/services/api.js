import axios from "axios";

const api = axios.create({
    baseURL: "https://ai-resume-analyzer-qjyg.onrender.com",
});

export default api;