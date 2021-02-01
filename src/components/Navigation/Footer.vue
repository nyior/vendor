<template>
  <div class="text-center shadow  hide-on-desktop py-4" id="my-footer">
    <div class="row m-2 text-muted">
      <div class="col-2 text-center">
        <router-link :to="{ name: 'home' }" class="footer-tab">
          <div>
            <i class="fa fa-window-maximize footer-icon">
                <div>
                    <small>Home</small>
                </div>
            </i>
          </div>
        </router-link>
      </div>

      <div class="col-2 text-center">
        <router-link :to="{ name: 'search' }" class="footer-tab">
          <div>
            <i class="fa fa-search footer-icon">
                <div class="mt-1">
                    <small>Search</small>
                </div>
            </i>
          </div>
        </router-link>
      </div>

      <div class="col-4 text-center">
        <router-link :to="{ name: 'ads_create' }" class="footer-tab">
          <div>
            <i class="fa fa-plus-circle footer-icon">
                <div class="mt-1">
                    <small>Sell</small>
                </div>
            </i>
          </div>
        </router-link>
      </div>

      <div class="col-2 text-center">
        <router-link :to="{ name: 'wishlist' }" class="footer-tab">
          <div>
            <i class="fa fa-gratipay footer-icon">
                <div class="mt-1">
                    <small>Wishlist</small>
                </div>
            </i>
          </div>
        </router-link>
      </div>

      <div class="col-2 text-center">
        <router-link
          :to="{ name: 'user_detail', params: { id: userId } }"
          class="footer-tab"
        >
          <div>
            <i class="fa fa-user-circle footer-icon">
                <div class="mt-1">
                    <small>You</small>
                </div>
            </i>
          </div>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Footer",

  computed: {
    userId() {
      return this.$store.state.userId;
    }
  }
};
</script>

<style scoped>
#my-footer {
  font-size: 1.4rem;
  letter-spacing: 1px;
  width: 100%;

  background-color: white;
  position: fixed;
  bottom: 0px;
}

.footer-icon {
  font-size: 2rem;
}

#my-footer .router-link-exact-active {
  color: #7a09c4 !important;
  cursor: pointer;
}
</style>
