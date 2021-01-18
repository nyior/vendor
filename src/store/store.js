import Vue from 'vue';
import Vuex from 'vuex'

Vue.use(Vuex);


export const store = new Vuex.Store(
    {
        state: {
            isAuthenticated: window.localStorage.getItem("isAuthenticated"),
            userId: window.localStorage.getItem("user_id"),
            authToken: window.localStorage.getItem("token")
        },

        mutations: {
            modifyAuthState: (state, newState) => {
                state.isAuthenticated = newState;
            },

            modifyUserId: (state, userId) => {
                state.userId = userId;
            },

            modifyAuthToken: (state, authToken) => {
                state.authToken = authToken;
            },

            logout: state => {
                state.isAuthenticated = false;
                state.authToken = null;
                state.userId = null;
            }
        },

        actions: {
            modifyAuthStateAction: (context, newState) => {
                context.commit("modifyAuthState", newState);
            },

            modifyUserIdAction: (context, userId) => {
                context.commit("modifyUserId", userId);
            },

            modifyAuthTokenAction: (context, authToken) => {
                context.commit("modifyAuthToken", authToken);
            },

            logoutAction: context => {
                context.commit("logout");
            }
        }
    }
);