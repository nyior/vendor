<template>

<nav class="navbar navbar-expand-lg navbar-light bg-light my-navbar">
  <router-link 
              :to="{ name: 'home'}"
              class="navbar-brand">
          MARCHE
  </router-link>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav ml-auto">
      <li class="nav-item active mr-3">
        <router-link 
                      :to="{ name: 'home'}"
                      class="link">
          Home
        </router-link>
        
      </li>
      <li class="nav-item mr-3">
        <router-link 
                      :to="{ name: 'about'}"
                      class="link">
          About
        </router-link>
      </li>
      
      <li class="nav-item">
        <a class="btn btn-sm btn-outline-danger" href="/accounts/logout/">Sign Out</a>
      </li>
      
    </ul>
  </div>
</nav>

</template>

<script>
    export default{
        name: "NavbarComponent"
    }
</script>

<style>
.my-navbar{
    font-size: 1.4rem;
}

.link{
    text-decoration: none ;
    color: black !important;
}
.link:hover{
    text-decoration: none !important;
    color: blue !important;
}

.navbar-brand{
    font-weight: bold;
    font-size: 2.0rem;
}
</style>