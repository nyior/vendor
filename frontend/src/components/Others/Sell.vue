<template>
  <div>
    <router-link class="sell hide-on-mobile" :to="{ name: 'ads_create' }">
      <i class="fa fa-plus-circle footer-icon"></i>
    </router-link>
  </div>
</template>

<script>
export default {
  name: "sell"
};
</script>

<style scoped>
.footer-icon {
  font-size: 5rem;
  color: #7a09c4 !important;
}

.sell {
  position: fixed;
  bottom: 50px;
  right: 50px;
  z-index: 10;
}

.sell button {
  background: #f0f0f0 !important;
  opacity: 0.7;
  font-size: 1.5rem;
  padding: 1rem 1.2rem;
}

@media only screen and (max-width: 600px) {
  .sell {
    position: fixed;
    bottom: 30px;
    right: 20px;
  }
}
</style>
