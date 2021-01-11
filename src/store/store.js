import Vue from 'vue';
import Vuex from 'vuex'

Vue.use(Vuex);


export const store = new Vuex.Store(
    {
        state: {
            isAuthenticated: false,
            userId: null,
            authToken: null
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
            modifyAuthState: (context, newState) => {
                context.commit("modifyAuthState", newState);
            },

            modifyUserId: (context, userId) => {
                context.commit("modifyUserId", userId);
            },

            modifyAuthToken: (context, authToken) => {
                context.commit(" modifyAuthToken", authToken);
            },

            logout: context => {
                context.commit("logout");
            }
        }
    }
);