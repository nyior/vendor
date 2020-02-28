import { CSRF_TOKEN } from "./csrf_token.js";
import axios from "axios";

const API_URL = "http://localhost:8000";
const endpoint = "http://localhost:8000";

export class APIService {
  constructor() {}

  getResource(endpoint) {
    return axios.get(`${API_URL}/${endpoint}`).then(response => response.data);
  }
}
