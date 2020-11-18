import { CSRF_TOKEN } from "./csrf_token.js";
import axios from "axios";

// const API_URL = "http://meleemann.pythonanywhere.com";
const API_URL = "http://localhost:8000";

function apiService(endpoint, method, data) {
  endpoint = `${API_URL}/${endpoint}`;

  const config = {
    url: endpoint,
    method: method,
    data: data !== undefined ? data : null,
    headers: {
      "content-type": "application/json",
      "X-CSRFTOKEN": CSRF_TOKEN
    }
  };

  return axios(config).then(response => response.data);
}

export { apiService };
