import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export const store = new Vuex.Store({
  state: {
    isAuthenticated: JSON.parse(window.localStorage.getItem("isAuthenticated")),
    userId: JSON.parse(window.localStorage.getItem("user_id")),
    authToken: window.localStorage.getItem("token"),
    username: window.localStorage.getItem("username")
  },

  mutations: {
    modifyAuthState: (state, payload) => {
      state.isAuthenticated = payload;
    },

    modifyUserId: (state, payload) => {
      state.userId = payload;
    },

    modifyAuthToken: (state, payload) => {
      state.authToken = payload;
    },

    logout: state => {
      //change user's auth state to false
      window.localStorage.setItem("isAuthenticated", false);

      //set token to null
      window.localStorage.setItem("token", null);

      //set user id to null
      window.localStorage.setItem("user_id", null);

      window.localStorage.setItem("username", null);

      state.isAuthenticated = false;
      state.authToken = null;
      state.userId = null;
      state.username = null;
    },

    join: (state, payload) => {
      let authToken = payload["authToken"];
      let userId = payload["userId"];
      let username = payload["username"];

      //change user's auth state to true
      window.localStorage.setItem("isAuthenticated", true);

      //save user's auth token to the local store
      window.localStorage.setItem("token", authToken);

      //save user id to the local store
      window.localStorage.setItem("user_id", userId);

      window.localStorage.setItem("username", username);

      state.isAuthenticated = true;
      state.authToken = authToken;
      state.userId = userId;
      state.username = username;
    }
  },

  actions: {
    modifyAuthStateAction: (context, payload) => {
      context.commit("modifyAuthState", payload);
    },

    modifyUserIdAction: (context, payload) => {
      context.commit("modifyUserId", payload);
    },

    modifyAuthTokenAction: (context, payload) => {
      context.commit("modifyAuthToken", payload);
    },

    logoutAction: context => {
      context.commit("logout");
    },

    joinAction: (context, payload) => {
      context.commit("join", payload);
    }
  }
});
