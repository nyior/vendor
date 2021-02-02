import { CSRF_TOKEN } from "./csrf_token.js";
import axios from "axios";

//uncomment the line below before pushing to heroku
const API_URL = "https://vendor-aun.herokuapp.com";
// const API_URL = "http://localhost:8000";
const TKN = JSON.parse(window.localStorage.getItem("token"));
const TOKEN = `Token ${TKN}`;

function apiService(endpoint, method, data) {
  endpoint = `${API_URL}/${endpoint}`;

  const config = {
    url: endpoint,
    method: method,
    data: data !== undefined ? data : null,
    headers: {
      "content-type": "application/json",
      "X-CSRFTOKEN": CSRF_TOKEN,
      Authorization: TKN !== undefined && TKN !== null ? TOKEN : null
    }
  };

  return axios(config).then(response => response.data);
}

export { apiService };
