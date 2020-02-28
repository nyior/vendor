<template>
  <nav class="navbar navbar-expand-lg  shadow my-navbar fixed-top">
    <router-link :to="{ name: 'home' }" class="navbar-brand">
      Marche`
    </router-link>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <form class="form-group has-search my-0 ml-auto mr-auto">
        <input
          class="form-control mr-sm-2"
          type="search"
          placeholder="search and discover products/services on marche"
        />
      </form>

      <ul class="navbar-nav ">
        <li class="nav-item mr-3">
          <a class="btn btn-lg " href="#">Advertise With Us</a>
        </li>

        <li class="nav-item mr-3 mt-2">
          <a class="link " href="/accounts/login/">Login</a>
        </li>
        <li class="nav-item mt-2">
          <a class="link " href="/accounts/signup/">Register</a>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavbarComponent"
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Pacifico&display=swap");

.my-navbar {
  font-size: 1.4rem;
  background-color: #7a09c4;
  font-weight: bold;
}
.btn {
  background-color: white !important;
  color: #200135 !important;
  font-weight: bold;
}

.navbar-brand {
  font-weight: bold;
  font-size: 2rem;
  font-family: "Pacifico";
  color: white !important;
}

input[type="search"] {
  width: 50rem;
  height: 3rem;
  border-radius: 20px;
}
</style>
