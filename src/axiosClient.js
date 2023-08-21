import axios from 'axios'


const axiosClient = axios.create({
    baseURL: 'http://127.0.0.1:8000/',
});

//use Interceptors when you are working with something that requires autorization


export default axiosClient;