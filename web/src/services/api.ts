import axios from 'axios';


const api = axios.create({
  baseURL: 'http://localhost:5000'
});

api.interceptors.request.use(config => {
  config.headers.authorization = `Bearer ${localStorage.getItem('@eletronicx:auth_token')}`
  config.headers.user_id = `${JSON.parse(localStorage.getItem('@eletronicx:user'))}`
  return config;
});

export default api;
